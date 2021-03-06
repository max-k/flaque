# coding: utf-8

from time import sleep
from typing import Dict, List

from .analyze import analyzer
from .audio import Album
from .filesystem import Directory
from .metatags import Tags


def main(debug: bool, wait: int, force_type: str,
         mp3: bool, paths: List[str]) -> None:
    for path in paths:
        directory: Directory = Directory(path)
        if debug:
            print(directory.full_path)
        albums: Dict[str, Album] = analyzer(directory, force_type)
        for album in albums:
            tags: Tags = albums[album].tags
            album.decode()
            album.split()
            album.encode(mp3)
            album.tags = tags
    sleep(wait)
