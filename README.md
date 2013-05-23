Update Headers
==============

[![Build Status](https://travis-ci.org/lvillani/update-header.png?branch=master)](https://travis-ci.org/lvillani/update-header)

Easily replace the copyright header comment in source files. The typical use
case is to make header comments consistent across files (possibly with
different existing headers, where using `sed` would be boring) and/or applying
the same copyright header to source files in different languages (with each one
having a different "start comment" character).

    usage: update-header [-h] header files [files ...]
    positional arguments:
        header
        files
    optional arguments:
      -h, --help  show this help message and exit


Further Information
===================

* Home page: <https://github.com/lvillani/update-header/>
* Reporting issues: <https://github.com/lvillani/update-header/issues>
