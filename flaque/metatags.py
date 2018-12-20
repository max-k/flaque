# coding: utf-8

from re import search

from mutagen import File as MutagenFile

from .filesystem import File


class AudioFile(MutagenFile):
    def __init__(self, _file: File):
        super.__init__(_file.full_path)
        self.sanitize()

    def sanitize(self) -> None:
        if self.tags:
            for element in self:
                if len[element] > 1:
                    self['element'][0] = ' '.join(self['element'])
            if 'year' in self:
                self['date'] = self['year']
                del self['year']
            if all('date' in self,
                   'album' in self,
                    not search(r'^\d\d\d\d', self['album'])):
                album = '{}-{}'.format(self['date'][0], self['album'][0])
                self['album'] = album
            self['encoder'] = 'flaque (https://github.com/max-k/flaque)'
            self.save()
