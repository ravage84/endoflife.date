---
title: nginx
permalink: /nginx
iconSlug: nginx
releasePolicyLink: https://www.nginx.com/blog/nginx-1-18-1-19-released/#NGINX-Versioning-Explained
category: server-app
activeSupportColumn: false
versionCommand: nginx -v
releaseColumn: true
releaseDateColumn: true
changelogTemplate: https://nginx.org/en/CHANGES-__RELEASE_CYCLE__
# https://rubular.com/r/bVKLuLKLLrHCTI
auto:
-   git: https://github.com/nginx/nginx.git
    regex: ^release-(?<major>0|[1-9]\d*)\.(?<minor>0|[1-9]\d*)\.(?<patch>0|[1-9]\d*)$
-   hg: https://hg.nginx.org/nginx
releases:
-   releaseCycle: "1.23"
    eol: false
    latest: "1.23.1"
    link: https://nginx.org/en/CHANGES
    latestReleaseDate: 2022-07-19
    releaseDate: 2022-06-21
-   releaseCycle: "1.22"
    eol: false
    latest: "1.22.0"
    latestReleaseDate: 2022-05-24
    releaseDate: 2022-05-24
-   releaseCycle: "1.21"
    eol: 2022-05-24
    latest: "1.21.6"
    link: https://nginx.org/en/CHANGES
    latestReleaseDate: 2022-01-25
    releaseDate: 2021-05-25
-   releaseCycle: "1.20"
    eol: 2022-05-24
    latest: "1.20.2"
    latestReleaseDate: 2021-11-16
    releaseDate: 2021-04-20
-   releaseCycle: "1.18"
    eol: 2021-04-20
    latest: "1.18.0"
    latestReleaseDate: 2020-04-21
    releaseDate: 2020-04-21
-   releaseCycle: "1.16"
    eol: 2020-04-20
    latest: "1.16.1"
    latestReleaseDate: 2019-08-13
    releaseDate: 2019-04-23
-   releaseCycle: "1.14"
    eol: 2019-04-23
    latest: "1.14.2"
    latestReleaseDate: 2018-12-04
    releaseDate: 2018-04-17
-   releaseCycle: "1.12"
    eol: 2018-04-17
    latest: "1.12.2"
    latestReleaseDate: 2017-10-17
    releaseDate: 2017-04-12
-   releaseCycle: "1.10"
    eol: 2017-04-12
    latest: "1.10.3"
    latestReleaseDate: 2017-01-31
    releaseDate: 2016-04-26
-   releaseCycle: "1.8"
    eol: 2016-04-26
    latest: "1.8.1"
    latestReleaseDate: 2016-01-26
    releaseDate: 2015-04-21
-   releaseCycle: "1.6"
    eol: 2015-04-21
    latest: "1.6.3"
    latestReleaseDate: 2015-04-07
    releaseDate: 2014-04-24
-   releaseCycle: "1.4"
    eol: 2014-04-24
    latest: "1.4.7"
    latestReleaseDate: 2014-03-18
    releaseDate: 2013-04-24
-   releaseCycle: "1.2"
    eol: 2013-04-24
    latest: "1.2.9"
    latestReleaseDate: 2013-05-13
    releaseDate: 2012-04-23
-   releaseCycle: "1.0"
    eol: 2012-04-23
    latest: "1.0.15"
    latestReleaseDate: 2012-04-12
    releaseDate: 2011-04-12

---

> [NGINX](https://nginx.org/) is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server.

## Versioning Scheme

The open-source NGINX project maintains two branches: mainline and stable.

- **mainline**: 
    Mainline is the active development branch where the latest features and bug fixes get added. It is denoted by an odd number in the second part of the version number, for example 1.21.0.
- **stable**:
    Stable receives fixes for high‑severity bugs, but is not updated with new features. It is denoted by an even number in the second part of the version number, for example 1.22.0. The stable branch never receives new functionality during its lifecycle and typically receives just one or two updates, for critical bug fixes.
   
Every April, the current stable branch is retired, after which no further bug fixes are made. The current mainline branch is forked, to create the next stable branch.
