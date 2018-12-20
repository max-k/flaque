# coding: utf-8

from typing import Dict

from mutagen import MutagenError

from .audio import Album
from .filesystem import Directory
from .metatags import AudioFile


def analyzer(directory: Directory, force_type: str) -> Dict[str, Album]:
    albums: Dict[str, Album] = []
    for _file in [x for x in directory.files if x.format != "unsupported"]:
        try:
            data: AudioFile = AudioFile(_file)
        except MutagenError:
            print("Error loading tags for {}".format())
        if 'album' in data:
            if data['album'] not in albums:
                albums[data['album']] = Album(data['album'])
    return albums
