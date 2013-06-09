RegexLink
=========

About
-----
This is a simple script I use to automatically create a bunch of symbolic links according to regular expression based rules.

It's intended use is for providing a clean web-server indexable directory structure for large collections of media files.
Instead of the actual structure on disk with quirky filenames I can add a pattern to the pattern file and I get a nice directory of links with clean and consistent file names.

Usage
-----

    RegexLink.py [-q --quiet] [-h] [-v --version] /path/to/search /output/path input_pattern output_pattern


Examples
--------

    RegexLink.py ~/Videos /var/www/media ".*/ts.S(\d\d)E(\d\d).mkv$" "TV Show/Season \1/Episode \2.mkv"

Edit the source to choose your input/output directories, then edit the patterns.txt file to define your patterns.

The format of patterns.txt is csv, like so:

    ".*/(\d+)/(.+)\.txt$","/txt/\2.\1.txt"

Column 0 represents the search pattern, column 1 is the replacement pattern, like sed -e "s/col0/col1/"


Improvements
------------
This could do with some command line argument support, for specifying target directories and pattern files.

