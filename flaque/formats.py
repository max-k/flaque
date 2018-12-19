# coding: utf-8

from re import fullmatch, I
from typing import Dict

REGEXPS = {
    r"\.wave?": "wav",
    r"\.flac": "flac",
    r"\.wv": "wv",
    r"\.ape": "ape",
    r"\.shn": "shn",
    r"\.tta": "tta",
}

FORMATS = {
    "wav": {
        "fullname": "waveform",
    },
    "flac": {
        "fullname": "FLAC",
    },
    "wv": {
        "fullname": "WavPack",
    },
    "ape": {
        "fullname": "Monkey's Audio",
    },
    "shn": {
        "fullname": "shorten",
    },
    "tta": {
        "fullname": "TruAudio",
    },
    "unsupported": {
        "fullname": "Unsupported format"
    },
}


def checker(ext: str) -> Dict:
    for regexp in REGEXPS:
        if fullmatch(regexp, ext, I):
            return FORMATS[REGEXPS[regexp]]
    return FORMATS["unsupported"]
