# coding: utf-8

from typing import Dict, List

import click

from . import algorithm

CONTEXT_SETTINGS: Dict = dict(
    help_option_names=["-h", "--help"], ignore_unknown_options=True
)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("-d", "--debug", is_flag=True, help="enable debug output")
@click.option("-w", "--wait", default=0, show_default=True,
              help="time to wait before exiting")
@click.option("-t", "--type", "type_", type=click.Choice(["track", "disc"]),
              help="force found files to be tracks or discs")
@click.option("-3", "--mp3", is_flag=True,
              help="use mp3 output format instead of flac")
@click.version_option()
@click.argument("paths", nargs=-1, type=click.Path(exists=True))
def cli(debug: bool, wait: int, type_: str,
        mp3: bool, paths: List[str]) -> None:
    """
    Sanitize tags and convert any lossless format to flac.

    \b
    Supports FLAC, Monkey"s Audio, WavPack, TrueAudio,
    Shorten and Wave (and maybe Alac in a near future).
    """
    algorithm.main(paths)
