#!/usr/bin/env python

import ftools
import sys

def main():
    if len(sys.argv) < 2:
        print 'Usage: %s <filename>' % sys.argv[0]
        return

    cached = 0
    total = 0

    fd = file(sys.argv[1], 'r')
    ftools.fadvise(fd.fileno(),mode="POSIX_FADV_WILLNEED")
    fd.close()
    print "fadvise POSIX_FADV_WILLNEED"

    fd = file(sys.argv[1], 'r')
    cached, total = ftools.fincore_ratio(fd.fileno())
    fd.close()
    print "fincore_ratio: %i of %i pages cached (%.00f%%)" % (cached, total, (float(cached) / float(total)) * 100.0)

    fd = file(sys.argv[1], 'r')
    ftools.fadvise(fd.fileno(),mode="POSIX_FADV_DONTNEED")
    fd.close()
    print "fadvise POSIX_FADV_DONTNEED"

    fd = file(sys.argv[1], 'r')
    cached, total = ftools.fincore_ratio(fd.fileno())
    fd.close()
    print "fincore_ratio: %i of %i pages cached (%.00f%%)" % (cached, total, (float(cached) / float(total)) * 100.0)

    fd = file(sys.argv[1], 'r')
    ftools.fadvise(fd.fileno(),mode="POSIX_FADV_WILLNEED")
    fd.close()
    print "fadvise POSIX_FADV_WILLNEED"

    fd = file(sys.argv[1], 'r')
    cached, total = ftools.fincore_ratio(fd.fileno())
    fd.close()
    print "fincore_ratio: %i of %i pages cached (%.00f%%)" % (cached, total, (float(cached) / float(total)) * 100.0)


if __name__ == '__main__':
    main()
