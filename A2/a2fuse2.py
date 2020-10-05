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
    def __init__(self, root1, root2):
        self.root1 = root1
        self.root2 = root2

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

        """
        try:
            full_path = self._full_path(path)
        except:
            full_path = self._full_path(path,1)"""
        # if(self.root2 in full_path):
        #    full_path = self._full_path(path,1)
        print("~~~~~~~~~~~~~~~~full~~~~~~~~~~~~~~~~~~", full_path)
        dirents = [".", ".."]
        if os.path.isdir(full_path):
            dirents.extend(os.listdir(full_path))
        if os.path.isdir(full_path2):
            dirents.extend(os.listdir(full_path2))
        for r in dirents:
            yield r


def main(mountpoint, root1, root2):
    FUSE(Fuse2(root1, root2), mountpoint, nothreads=True, foreground=True)
    # FUSE(Fuse2(root2), mountpoint, nothreads=True, foreground=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main(sys.argv[3], sys.argv[1], sys.argv[2])


"""
    def getattr(self, path, fh=None):
        full_path = self._full_path(path)
        try:
            st = os.lstat(full_path[0])
            val = dict((key, getattr(st, key)) for key in ('st_atime', 'st_ctime',
                     'st_gid', 'st_mode', 'st_mtime', 'st_nlink', 'st_size', 'st_uid'))
            return val
        except:
            st = os.lstat(full_path[1])
            val =  dict((key, getattr(st, key)) for key in ('st_atime', 'st_ctime',
                     'st_gid', 'st_mode', 'st_mtime', 'st_nlink', 'st_size', 'st_uid'))
            return val



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

    def access(self, path, mode):
        full_path = self._full_path(path)
        if not os.access(full_path[0], mode):
            raise FuseOSError(errno.EACCES)
        if not os.access(full_path[1], mode):
            raise FuseOSError(errno.EACCES)
    def open(self, path, flags):
        full_path = self._full_path(path)
        os.open(full_path[0], flags)
        return os.open(full_path[1], flags)
"""
