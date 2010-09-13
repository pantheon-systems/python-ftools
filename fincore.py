#!/usr/bin/env python

import ftools
import resource
import optparse
import sys
import os
import stat

def main():
    parser = optparse.OptionParser(description="Determine how much of a file is in filesystem page-cache.")

    parser.add_option('-d', '--directory', dest='directory', default=None,
                      help="Recursively descend into a directory")

    options, args = parser.parse_args()

    if len(args) == 0 and options.directory == None:
        parser.print_help()
        return 1

    page_size = resource.getpagesize()
    print "filename\tfile size\ttotal pages\tpages cached\tcached size\tpercentage cached"

    for f in args:
        fd = file(f, 'r')
        pages_cached, pages_total = ftools.fincore_ratio(fd.fileno())
        file_size = os.fstat(fd.fileno())[stat.ST_SIZE]
        fd.close()
        print "%s\t%s\t%s\t%s\t%s\t%s" % (f, file_size, pages_total, pages_cached, (pages_cached * page_size), ((float(pages_cached) / float(pages_total)) * 100.0))


if __name__ == '__main__':
    main()
