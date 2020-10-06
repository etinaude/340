'''
    Name:   Etienne Naude
    UPI :   enau831
    ID  :   768485633
'''
from __future__ import print_function, absolute_import, division

import logging

import os
import sys
import errno
from collections import defaultdict
from errno import ENOENT
from stat import S_IFDIR, S_IFLNK, S_IFREG
from sys import argv, exit
from time import time

from fuse import FUSE, FuseOSError, Operations, LoggingMixIn
from passthrough import Passthrough
from memory import Memory


class FuseAlt(Memory):
    def __init__(self):
        self.files = {}
        self.data = {}
        self.fd = 0
        now = time()
        self.files['/'] = dict(st_mode=(S_IFDIR | 0o755), st_ctime=now,
                               st_mtime=now, st_atime=now, st_nlink=2)

    def getattr(self, path, fh=None):
        if path not in self.files:
            raise FuseOSError(ENOENT)

        return self.files[path]

    def readdir(self, path, fh):
        return ['.', '..'] + [x[1:] for x in self.files if x != '/']

    def read(self, path, size, offset, fh):
        return self.data[path][offset:offset + size]

    def open(self, path, flags):
        self.fd += 1
        return self.fd

    def unlink(self, path):
        self.files.pop(path)

    def create(self, path, mode):
        self.files[path] = dict(st_mode=(S_IFREG | mode), st_nlink=1,
                                st_size=0, st_ctime=time(), st_mtime=time(),
                                st_atime=time())
        self.fd += 1
        return self.fd

    def write(self, path, data, offset, fh):
        print("****************",
              data, "***********************")
        self.data[path] = self.data[path][:offset] + data
        self.files[path]['st_size'] = len(self.data[path])
        return len(data)


class Fuse2(LoggingMixIn, Passthrough):
    def __init__(self, root1, root2, mnt):
        self.root1 = root1
        self.root2 = root2
        self.second = FuseAlt()

    def _full_path(self, partial, sauce=0):
        if partial.startswith("/"):
            partial = partial[1:]
        path1 = os.path.join(self.root1, partial)
        path2 = os.path.join(self.root2, partial)
        if sauce == 1:
            return path2
        if os.path.exists(path1):
            return path1
        if os.path.exists(path2):
            return path2
        return path1

    def readdir(self, path, fh):
        full_path = self._full_path(path)
        full_path2 = self._full_path(path, 1)
        dirents = [".", ".."]
        if os.path.isdir(full_path):
            dirents.extend(os.listdir(full_path))
        if os.path.isdir(full_path2):
            dirents.extend(os.listdir(full_path2))
        for r in dirents:
            yield r

    def create(self, path, mode, fi=None):
        full_path = self._full_path(path)
        return self.second.create(path, mode)

    def getattr(self, path, fh=None):
        full_path = self._full_path(path)
        try:
            st = os.lstat(full_path)
            return dict((key, getattr(st, key)) for key in ('st_atime', 'st_ctime',
                                                            'st_gid', 'st_mode', 'st_mtime', 'st_nlink', 'st_size', 'st_uid'))
        except:
            return second.getattr(full_path)
    #    return os.open(full_path, os.O_WRONLY | os.O_CREAT, mode)


def main(mountpoint, root1, root2):
    FUSE(Fuse2(root1, root2, mountpoint),
         mountpoint, nothreads=True, foreground=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main(sys.argv[3], sys.argv[1], sys.argv[2])
