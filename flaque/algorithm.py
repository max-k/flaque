# coding: utf-8

from typing import List

from .filesystem import Directory
from .metatags import Tags


def main(debug: bool, wait: int, type_: str,
         mp3: bool, paths: List[str]) -> None:
    for path in paths:
        directory: Directory = Directory(path)
        for album in directory.albums:
            tags: Tags = album.save_tags()
            album.decode()
            album.split()
            album.encode()
            album.tags = tags
