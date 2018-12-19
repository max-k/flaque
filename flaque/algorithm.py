# coding: utf-8

from time import sleep
from typing import List

from .filesystem import Directory
from .metatags import Tags


def main(debug: bool, wait: int, force_type: str,
         mp3: bool, paths: List[str]) -> None:
    for path in paths:
        directory: Directory = Directory(path, force_type)
        if debug:
            print(directory.full_path)
        for album in directory.albums:
            tags: Tags = album.tags
            album.decode()
            album.split()
            album.encode(mp3)
            album.tags = tags
    sleep(wait)
