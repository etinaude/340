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
