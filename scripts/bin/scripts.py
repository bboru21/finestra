#!/usr/bin/env python

# enable access to lib by adding to path
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from lib.parse_captions import parse_captions
from lib.transcribe import transcribe


import click


@click.group()
def cli():
  pass

@cli.command('run_parse_captions')
@click.option('--filename', help='Name of the .srt file within ./input directory to parse.', required=True)
@click.option('--offset', help='Number of seconds with which to offset the parsing timestamps.', required=False, default=0)
def run_parse_captions(filename, offset):
  parse_captions(filename=filename, offset=offset)

@cli.command('run_transcribe')
@click.option('--filepath', help='Filename and immediate parent directory of the video file to be transcribed.', required=True)
def run_transcribe(filepath):
  transcribe(filepath=filepath)


if __name__ == '__main__':
    cli()
