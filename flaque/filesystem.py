# coding: utf-8

from os import getcwd, listdir
from os.path import basename, getsize, join, realpath, splitext
from typing import Dict, List

from .formats import checker

DANGEROUS_CHARS = ['"', '$']


class FileSystemObject():
    def __init__(self, path: str):
        for char in DANGEROUS_CHARS:
            path = path.replace(char, '\\{}'.format(char))
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


class File(FileSystemObject):
    def __init__(self, path: str):
        super().__init__(path)
        self.__ext: str = splitext(self.basename)[1]
        self.__size: int = int(getsize(self.full_path) / 1048576)
        self.__format: Dict = checker(self.ext)

    @property
    def ext(self) -> str:
        return self.__ext

    @property
    def size(self) -> int:
        return self.__size

    @property
    def format(self) -> Dict:
        return self.__format


class Directory(FileSystemObject):
    def __init__(self, path: str):
        super().__init__(path)
        self.__files: List[File] = [File(join(path, filename))
                                    for filename in listdir(path)]

    @property
    def files(self) -> List[File]:
        return self.__files
