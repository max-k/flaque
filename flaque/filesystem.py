# coding: utf-8

from os import getcwd
from os.path import join, realpath


class Directory(object):
    def __init__(self, path: str):
        self.path: str = path

    @property
    def full_path(self) -> str:
        full_path: str = ""
        if self.path.startswith("/"):
            full_path = self.path
        else:
            full_path = join(getcwd(), self.path)
        return realpath(full_path)

    def scan(self) -> None:
        pass
