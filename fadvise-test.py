#!/usr/bin/env python

import ftools
import sys

def main():
    if len(sys.argv) < 2:
        print 'Usage: %s <filename>' % sys.argv[0]
        return

    fd = file(sys.argv[1], 'r')


    ftools.fadvise(fd.fileno(),mode="POSIX_FADV_DONTNEED")

    fd.close()


if __name__ == '__main__':
    main()
