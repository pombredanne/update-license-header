# update-header

[![Build Status](http://img.shields.io/travis/lvillani/update-header.svg?style=flat)](https://travis-ci.org/lvillani/update-header)
[![Coverage Status](http://img.shields.io/coveralls/lvillani/update-header.svg?style=flat)](https://coveralls.io/r/lvillani/update-header)
[![License](http://img.shields.io/badge/license-GPL%20v3.0-blue.svg?style=flat)](http://choosealicense.com/licenses/gpl-3.0/)

--------------------------------------------------------------------------------

Easily replace the copyright header comment in source files. The typical use case is to make header
comments consistent across files (possibly with different existing headers, where using `sed` would
be boring) and/or applying the same copyright header to source files in different languages (with
each one having a different "start comment" character).


## Usage

Call this program by passing the file to use as header boilerplate as first argument. All subsequent
arguments can be either directories or files.

If `path` refers to a directory, each file below that directory is processed recursively,
automatically using the right comment string depending on which extension the file has. Unrecognized
files are ignored.

If `path` refers to a file, it is processed using the specified header and either the default
comment string (`"#"`) or whichever one has been specified on the command line.

    usage: update-header [-h] [-c COMMENT_STRING] header path [path ...]
    positional arguments:
      header
      path
    optional arguments:
      -h, --help            show this help message and exit
      -c COMMENT_STRING, --comment-string COMMENT_STRING
