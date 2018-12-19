# coding: utf-8

from os import getcwd
from os.path import basename, getsize, join, realpath, splitext
from typing import List

from .audio import Album


class FileSystemObject():
    def __init__(self, path: str):
        self.__path: str = path
        self.__fullpath: str = ""
        self.__basename: str = basename(path)

    @property
    def path(self) -> str:
        return self.__path

    @property
    def basename(self) -> str:
        return self.__basename

    @property
    def full_path(self) -> str:
        if not self.__fullpath:
            full_path: str = ""
            if self.__path.startswith("/"):
                full_path = self.__path
            else:
                full_path = join(getcwd(), self.__path)
            self.__fullpath = realpath(full_path)
        return self.__fullpath


class Directory(FileSystemObject):
    def __init__(self, path: str, force_type: str):
        super().__init__(path)
        self.__type: str = force_type
        self.__scanned: bool = False
        self.__albums: List[Album] = []

    @property
    def albums(self) -> List[Album]:
        if not self.__scanned:
            self.__albums = self._scan()
        return self.__albums

    def _scan(self) -> List[Album]:
        self.__scanned = True
        return self.__albums


class File(FileSystemObject):
    def __init__(self, path: str, directory: Directory):
        super().__init__(path)
        self.__directory: Directory = directory
        self.__ext: str = splitext(self.basename)[1]
        self.__size: int = getsize(self.full_path) / 1048576

    @property
    def ext(self) -> str:
        return self.__ext

    @property
    def size(self) -> int:
        return self.__size
