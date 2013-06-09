Update Headers
==============

[![Build Status](https://travis-ci.org/lvillani/update-header.png?branch=master)](https://travis-ci.org/lvillani/update-header)

Easily replace the copyright header comment in source files. The typical use
case is to make header comments consistent across files (possibly with
different existing headers, where using `sed` would be boring) and/or applying
the same copyright header to source files in different languages (with each one
having a different "start comment" character).




Usage
=====

Call this program by passing the file to use as header boilerplate as first
argument. All subsequent arguments can be either directories or files.

If `path` refers to a directory, each file below that directory is processed
recursively, automatically using the right comment string depending on which
extension the file has. Unrecognized files are ignored.

If `path` refers to a file, it is processed using the specified header and
either the default comment string (`"#"`) or whichever one has been specified
on the command line.

    usage: update-header [-h] [-c COMMENT_STRING] header path [path ...]
    positional arguments:
      header
      path
    optional arguments:
      -h, --help            show this help message and exit
      -c COMMENT_STRING, --comment-string COMMENT_STRING




Further Information
===================

* Home page: <https://github.com/lvillani/update-header/>
* Reporting issues: <https://github.com/lvillani/update-header/issues>
