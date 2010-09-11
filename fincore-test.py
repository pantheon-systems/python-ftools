#!/usr/bin/env python

import ftools
import sys

def main():
    if len(sys.argv) < 2:
        print 'Usage: %s <filename>' % sys.argv[0]
        return

    fd = file(sys.argv[1], 'r')
    
    cached, total = ftools.fincore_ratio(fd.fileno())
    print "fincore_ratio: %i of %i pages cached (%.00f%%)" % (cached, total, (float(cached) / float(total)) * 100.0)
    fd.close()

if __name__ == '__main__':
    main()
