# coding: utf-8

from .metatags import Tags


class Album():
    def __init__(self, name):
        self.name: str = name

    def save_tags(self) -> Tags:
        tags: Tags = Tags('title')
        return tags

    def decode(self) -> None:
        pass

    def split(self) -> None:
        pass

    def encode(self) -> None:
        pass

    def tags(self) -> None:
        pass
