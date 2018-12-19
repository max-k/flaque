# coding: utf-8

from os import getcwd
from os.path import basename, getsize, join, realpath, splitext
from typing import List

from .audio import Album


class FileSystemObject():
    def __init__(self, path: str):
        self._path: str = path
        self._fullpath: str = ""
        self._basename: str = basename(path)

    @property
    def basename(self) -> str:
        return self._basename

    @property
    def full_path(self) -> str:
        if not self._fullpath:
            full_path: str = ""
            if self._path.startswith("/"):
                full_path = self._path
            else:
                full_path = join(getcwd(), self._path)
            self._fullpath = realpath(full_path)
        return self._fullpath


class Directory(FileSystemObject):
    def __init__(self, path: str):
        super().__init__(path)
        self._scanned: bool = False
        self._albums: List[Album] = []

    @property
    def albums(self) -> List[Album]:
        if not self._scanned:
            self._albums = self._scan()
        return self._albums

    def _scan(self) -> List[Album]:
        self._scanned = True
        return self._albums


class File(FileSystemObject):
    def __init__(self, path: str, directory: Directory):
        super().__init__(path)
        self._directory = directory
        self._ext = splitext(self.basename)[1]
        self._size = getsize(self.full_path) / 1048576
