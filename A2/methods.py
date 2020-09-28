def __init__(self):
        self.files = {}
        self.data = defaultdict(bytes)
        self.fd = 0
        now = time()
        self.files['/'] = dict(st_mode=(S_IFDIR | 0o755), st_ctime=now,
                               st_mtime=now, st_atime=now, st_nlink=2)


def chmod(self, path, mode):
    self.files[path]['st_mode'] &= 0o770000
    self.files[path]['st_mode'] |= mode
    return 0

    ~~this changes the mode of the file by using the and operation with the octal number 770000 then the or operation with the mode~

def chown(self, path, uid, gid):
    self.files[path]['st_uid'] = uid
    self.files[path]['st_gid'] = gid
?
    ~~this changes the owner of a file by setting the uid and gid~

def create(self, path, mode):
    self.files[path] = dict(st_mode=(S_IFREG | mode), st_nlink=1,
                            st_size=0, st_ctime=time(), st_mtime=time(),
                            st_atime=time())
    self.fd += 1
    return self.fd

    ~~this creates a new file by adding it to the dictionary with the specific path and setting its attributes~

def getattr(self, path, fh=None):
    if path not in self.files:
        raise FuseOSError(ENOENT)
    return self.files[path]

    ~~this returns an item from the files dictionary if it exists else it raises an error~ 

def getxattr(self, path, name, position=0):
    attrs = self.files[path].get('attrs', {})
    try:
        return attrs[name]
    except KeyError:
        return ''       # Should return ENOATTR
?
    ~~this returns a specific attribute of a file in the dictionary rather than all attributes~

def listxattr(self, path):
    attrs = self.files[path].get('attrs', {})
    return attrs.keys()

    ~~this returns the names of all the attributes of a file in the dictionary~

def mkdir(self, path, mode):
    self.files[path] = dict(st_mode=(S_IFDIR | mode), st_nlink=2,
                            st_size=0, st_ctime=time(), st_mtime=time(),
                            st_atime=time())
    self.files['/']['st_nlink'] += 1

    ~~this creates a new directory at a specific path by adding it to the dictionary~

def open(self, path, flags):
    self.fd += 1
    return self.fd

    ~~ ~

def read(self, path, size, offset, fh):
    return self.data[path][offset:offset + size]

    ~~this reads data from a file starting at the offset and ending at offset+length~

def readdir(self, path, fh):
    return ['.', '..'] + [x[1:] for x in self.files if x != '/']
?
    ~~this reads the contents of a directory ~

def readlink(self, path):
    return self.data[path]
?
    ~~returns the class stored at the path in the dictionary~

def removexattr(self, path, name):
    attrs = self.files[path].get('attrs', {})
    try:
        del attrs[name]
    except KeyError:
        pass        # Should return ENOATTR

    ~~this removes and attribute from a file by deleting the attribute name from the file in the dictionary~

def rename(self, old, new):
    self.files[new] = self.files.pop(old)

    ~~this renames a file by remapping the item from the dictionary to a new name and removing it from the old location~

def rmdir(self, path):
    self.files.pop(path)
    self.files['/']['st_nlink'] -= 1
?
    ~~this deletes a directory by first removing it from the dictionary and the reducing the the st_nlink count by 1~

def setxattr(self, path, name, value, options, position=0):
    # Ignore options
    attrs = self.files[path].setdefault('attrs', {})
    attrs[name] = value

    ~~ this sets an attribute of a specific file by retreiving the file attributes form the dictionary and adding the specified value to the attribute~

def statfs(self, path):
    return dict(f_bsize=512, f_blocks=4096, f_bavail=2048)


def symlink(self, target, source):
    self.files[target] = dict(st_mode=(S_IFLNK | 0o777), st_nlink=1,
                              st_size=len(source))
    self.data[target] = source

    ~~this creates a link between a target and a source by copying the data from the source to the target~

def truncate(self, path, length, fh=None):
    self.data[path] = self.data[path][:length]
    self.files[path]['st_size'] = length

    ~~this shortens a file by deleting all content after the specified length and sets the length of the file to be shorter~

def unlink(self, path):
    self.files.pop(path)

    ~~this simply removes an item from the dictionary~

def utimens(self, path, times=None):
    now = time()
    atime, mtime = times if times else (now, now)
    self.files[path]['st_atime'] = atime
    self.files[path]['st_mtime'] = mtime

    ~~this sets the a and m time attributes of the file to the current time if the parameter times was not set ~

def write(self, path, data, offset, fh):
    self.data[path] = self.data[path][:offset] + data
    self.files[path]['st_size'] = len(self.data[path])
    return len(data)

    ~~ this appends a file by writing extra data to it, it then also updates the length of the file and returns the length of the new data~