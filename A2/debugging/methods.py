def __init__(self):
        self.files = {}
        self.data = defaultdict(bytes)
        self.fd = 0
        now = time()
        self.files['/'] = dict(st_mode=(S_IFDIR | 0o755), st_ctime=now,
                               st_mtime=now, st_atime=now, st_nlink=2)
'''.
        Initializes the object and makes a blank dictionary to hold the files which holds a dictionary as the value while the file path as the key.
        init also creates a dictionary named data which also uses pathname as the key but uses the files data as the value.
        It also initializes the file descriptor to 0.
        Lastly the init creates the root directory by adding the key "/" in files with a dictionary value and the current time for all time variables.
'''

def create(self, path, mode):
    self.files[path] = dict(st_mode=(S_IFREG | mode), st_nlink=1,
                            st_size=0, st_ctime=time(), st_mtime=time(),
                            st_atime=time())
    self.fd += 1
    return self.fd
'''.
        This creates a new file by adding it to the files dictionary with the specified path for the key and sets the mode to the mode passed to the method and the current time for all the time variables.
'''

def getattr(self, path, fh=None):
    if path not in self.files:
        raise FuseOSError(ENOENT)
    return self.files[path]
'''.
    This returns an item from the files dictionary if it exists else it raises an error. (the file dictionary holds the attributes for the file)
'''

def open(self, path, flags):
    self.fd += 1
    return self.fd
'''.
    open simply increases the unique file descriptor and returns it.
'''

def read(self, path, size, offset, fh):
    return self.data[path][offset:offset + size]
'''.
    This reads data from a file starting at the offset and ending at offset+length.
    It does this by using the file path as a key for the data dictionary and using the offset as indices
'''

def readdir(self, path, fh):
    return ['.', '..'] + [x[1:] for x in self.files if x != '/']
'''.
    this reads the contents of a directory 
'''

def unlink(self, path):
    self.files.pop(path)
'''.
    this simply removes an item from the files dictionary but not the data dictionary so it the data is still able to be read but there is no record of it or it's attributes.
'''

def write(self, path, data, offset, fh):
    self.data[path] = self.data[path][:offset] + data
    self.files[path]['st_size'] = len(self.data[path])
    return len(data)
'''.
    This appends a the value of the file in the data dictionary, it then also updates the length of the file in the files dictionary and returns the length of the new data.
'''