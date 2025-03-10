import sys
import frontmatter
import json
import re
import datetime
from glob import glob
from pathlib import Path
from distutils.version import StrictVersion
from ruamel.yaml import YAML
from ruamel.yaml.resolver import Resolver
from deepdiff import DeepDiff
from io import StringIO
from os.path import exists

"""
Updates the `release`, `latest` and `latestReleaseDate` property in automatically updated pages
As per data from _data/release-data. This script runs on dependabot upgrade PRs via GitHub Actions for
_data/release-data and commits back the updated data.
This is written in Python because the only package that supports writing back YAML with comments is ruamel
"""

DEFAULT_POST_TEMPLATE = """\
---
{metadata}
---

{content}
"""

# https://stackoverflow.com/a/63092850/368328
def sort_versions(data):
    def key(n):
        a = re.split(r'(\d+)', n)
        a[1::2] = map(int, a[1::2])
        return a
    return sorted(data, key=lambda n: key(n))

# https://stackoverflow.com/a/71329221/368328
# Force encoding version numbers as strings
Resolver.add_implicit_resolver(
    'tag:yaml.org,2002:string',
    re.compile(r'\d+\.\d+\.\d+', re.X),
    list('.0123456789'))
Resolver.add_implicit_resolver(
    'tag:yaml.org,2002:string',
    re.compile(r'\d+\.\d+', re.X),
    list('.0123456789'))


"""
matches releases that are exact (such as 4.1 being the first release for the 4.1 release cycle)
or releases that include a dot just after the release cycle (4.1.*)
This is important to avoid edge cases like a 4.10.x release being marked under the 4.1 release cycle.
"""
def releases_matches(r, prefix):
  return (r.startswith(prefix) and (r == prefix or r.startswith(prefix + '.') or r.startswith(prefix + '-')))

def find_first(releases, prefix):
  return next(filter(lambda r: releases_matches(r, prefix), releases), None)

def find_last(releases, prefix):
  return next(filter(lambda r: releases_matches(r, prefix), reversed(releases)), None)

def find_all(releases, prefix):
  return set(filter(lambda r: releases_matches(r, prefix), releases))

def yaml_to_str(obj):
  yaml = YAML()
  yaml.indent(sequence=4)
  string_stream = StringIO()
  yaml.dump(obj, string_stream)
  output_str = string_stream.getvalue()
  string_stream.close()
  return output_str

def update_product(name):
  fn = 'products/%s.md' % name
  with open(fn, 'r+') as f:
    yaml = YAML()
    yaml.preserve_quotes = True
    data = next(yaml.load_all(f))

    f.seek(0)
    _, content = frontmatter.parse(f.read())

    fn = '_data/release-data/releases/%s.json' % (name)
    if exists(fn):
      with open(fn) as releases_file:
        # Entire releases data as a dict
        R1 = json.loads(releases_file.read())
        # Just the list of versions
        R2 = sort_versions(R1.keys())
        R3 = set(R2)

      updated = False

      for release in data['releases']:
        old = release.copy()

        prefix = release['releaseCycle']
        first_version = find_first(R2, prefix)
        latest_version = find_last(R2, prefix)

        R3 = R3 - find_all(R3, prefix)

        if first_version:
          release['releaseDate'] = datetime.date.fromisoformat(R1[first_version])
          release['latestReleaseDate'] = datetime.date.fromisoformat(R1[latest_version])
          release['latest'] = latest_version
          diff = DeepDiff(old, release, ignore_order=True)

          # We write back to the file
          if(diff!={}):
            updated = True

      if updated:
        print("Updating %s" % fn)
        final_contents = DEFAULT_POST_TEMPLATE.format(
          metadata=yaml_to_str(data),
          content=content)

        f.seek(0)
        f.truncate()
        f.write(final_contents)

      if len(R3) != 0:
        for x in R3:
          date = datetime.date.fromisoformat(R1[x])
          days_since_release = (datetime.date.today() - date).days
          if days_since_release < 30:
            print("[WARN] %s:%s (%s) not included" % (name, x, R1[x]))

if __name__ == '__main__':
  if len(sys.argv) > 1:
    update_product(sys.argv[1])
  else:
    for x in glob('products/*.md'):
      update_product(Path(x).stem)
