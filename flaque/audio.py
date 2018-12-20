# coding: utf-8

from typing import Dict


class Album():
    def __init__(self, name: str, tags: Dict):
        self.__name: str = name
        self.__tags: Dict = tags

    @property
    def name(self) -> str:
        return self.__name

    @property
    def tags(self) -> Dict:
        return self.__tags

    @tags.setter
    def tags(self, tags: Dict) -> None:
        self.tags = tags

    def decode(self) -> None:
        pass

    def split(self) -> None:
        pass

    def encode(self, mp3: bool) -> None:
        pass
