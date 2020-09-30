
#!/usr/bin/env python

from __future__ import print_function, absolute_import, division

import logging

import os
import sys
import errno

from fuse import FUSE, FuseOSError, Operations, LoggingMixIn
from passthrough import Passthrough
from memory import Memory

class Fuse2(LoggingMixIn, Passthrough):
    def __init__(self, root1,root2):
        self.root = [root1,root2]



    def getattr(self, path, fh=None):
        full_path = self._full_path(path)
        st = os.lstat(full_path[0])
        return dict((key, getattr(st, key)) for key in ('st_atime', 'st_ctime',
                     'st_gid', 'st_mode', 'st_mtime', 'st_nlink', 'st_size', 'st_uid'))
        st = os.lstat(full_path[1])
        return dict((key, getattr(st, key)) for key in ('st_atime', 'st_ctime',
                     'st_gid', 'st_mode', 'st_mtime', 'st_nlink', 'st_size', 'st_uid'))



    def _full_path(self, partial):
        if partial.startswith("/"):
            partial = partial[1:]
        path = [os.path.join(self.root[0], partial),os.path.join(self.root[1], partial)]
        print(path)
        return path

    def readdir(self, path, fh):
        full_path = self._full_path(path)

        dirents = ['.', '..']
        if os.path.isdir(full_path[0]):
            dirents.extend(os.listdir(full_path[0]))
        for r in dirents:
            yield r

        if os.path.isdir(full_path[1]):
            dirents.extend(os.listdir(full_path[1]))
        for r in dirents:
            yield r


def main(mountpoint, root1, root2):
    FUSE(Fuse2(root1,root2), mountpoint, nothreads=True, foreground=True)
    #FUSE(Fuse2(root2), mountpoint, nothreads=True, foreground=True)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main(sys.argv[3], sys.argv[1], sys.argv[2])
