# coding: utf-8

from typing import List

from .filesystem import Directory


def main(paths: List[str]) -> None:
    for path in paths:
        directory: Directory = Directory(path)
        directory.scan()
        print(directory.full_path)
