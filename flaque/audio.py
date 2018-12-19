# coding: utf-8

from .metatags import Tags


class Album():
    def __init__(self, name: str):
        self.__name: str = name
        self.__tags: Tags = self._save_tags()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def tags(self) -> Tags:
        return self.__tags

    @tags.setter
    def tags(self, tags: Tags) -> None:
        self.tags = tags

    def _save_tags(self) -> Tags:
        tags: Tags = Tags(self.name)
        return tags

    def decode(self) -> None:
        pass

    def split(self) -> None:
        pass

    def encode(self, mp3: bool) -> None:
        pass
