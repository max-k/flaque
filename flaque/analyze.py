# coding: utf-8

from typing import List

from .audio import Album
from .filesystem import Directory


def analyzer(directory: Directory, force_type: str) -> List[Album]:
    albums: List[Album] = []
    for _file in directory.files:
        pass
    return albums
