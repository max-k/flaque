# coding: utf-8

from .metatags import Tags


class Album():
    def __init__(self, name: str):
        self.name: str = name
        self.tags: Tags = self._save_tags()

    @property.setter('tags')
    def _store_tags(self, tags: Tags) -> None:
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
