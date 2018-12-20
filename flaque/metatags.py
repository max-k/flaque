# coding: utf-8

from mutagen import File as MutagenFile

from .filesystem import File


class AudioFile(MutagenFile):
    def __init__(self, _file: File):
        super.__init__(_file.full_path)

    def sanitize(self) -> None:
        if self.tags:
            for element in self:
                if isinstance(list, element):
                    self['element'] = ' '.join(self['element'])
            self.save()
