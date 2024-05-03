#!/usr/bin/env python
import re
import datetime
import time
import json
import settings

SCRIPT_ROOT = f"{settings.SCRIPTS_ROOT}/lib/parse_captions"

forbidden = [
  'God',
  'Jesus',
  'Christ',

  'ass',
  'asshole',
  'asswipe',
  'bitch',
  'bitches',
  'bitching',
  'bullshit',
  'cunt',
  'damn',
  'damnit',
  'dammit',
  'dick',
  'fag',
  'faggot',
  'fuck',
  'fucker',
  'fucking',
  'hell',
  'penis',
  'piss',
  'pussy',
  'shit',
  'shitting',
  'twat',
  'vagina',
]
# forbidden_string = f"(?=\b|\s|^)(?P<word>({'|'.join(forbidden)}))(?=\b|\s|$)"
forbidden_string = f"(?P<word>({'|'.join(forbidden)}))"
pattern = re.compile(forbidden_string, flags=re.IGNORECASE)


def _convert_to_seconds(t):
  t = time.strptime(t.split(',')[0], '%H:%M:%S')

  return datetime.timedelta(
    hours=t.tm_hour,
    minutes=t.tm_min,
    seconds=t.tm_sec
  ).total_seconds()

def parse_captions(filename, offset=0):

  output = []
  data = []

  caption = []
  with open(f'{SCRIPT_ROOT}/input/{filename}') as f:
    for line in f:

      line = line.strip()

      if line:
        caption.append(line)
      else:
        data.append(caption)
        caption = []

  for item in data:
    num = item[0]
    duration = item[1]

    caption = ' '.join(item[2:])
    m = re.search(r'<font.+>(?P<text>.+)</font>', caption)
    if m:
      caption = m.group('text')

    m = re.search(pattern, caption)
    if m:

      proceed = input(f"Proceed with match (y/n/stop): {caption}    ")

      if proceed == 'y':

        (start, end) = duration.split(' --> ')
        start = _convert_to_seconds(start) + offset
        end = _convert_to_seconds(end) + offset

        output.append([int(start), int(end), 'MUTE'])
      if proceed == 'stop':
        print('script manually aborted')
        break

  # print(json.dumps({"data": output}))
  with open(f"{SCRIPT_ROOT}/output/{filename.split('.')[0]}.json", "w") as f:
    f.write(json.dumps({"data": output}, indent=4))
