#!/usr/bin/env python
import re
import datetime
import time
import json
import settings
import syllables
import math

SCRIPT_ROOT = f"{settings.SCRIPTS_ROOT}/lib/parse_captions"

forbidden = (

  (
    "God Damnit",
    "God Damn",
    "godamn",
    "goddamn"
    "goddam",
    "godam",
    "God",
  ),
  (
    'Jesus Christ',
    'Jesus H Christ',
    'Jesus'
    'Christ',
  ),
  (
    'asshole',
    'asswipe',
    'ass hole',
    'ass wipe',
    'ass',
  ),
  (
    'bitch',
    'bitches',
    'bitching',
  ),
  (
    'bull shit',
    'bullshit',
    'shit',
  ),
  (
    'damn',
    'damnit',
    'dammit',
  ),
  (
    'dick head',
    'dickhead',
    'dick',
  ),
  (
    'fag',
    'faggot',
  ),
  (
    'fuck',
    'fucked',
    'fucker',
    'fucking',
  ),
  (
    'piss',
    'pissed',
    'pissing',
  ),
  (
    'shit',
    'shitting',
  ),
  (
    # misc
    'cunt',
    'hell',
    'penis',
    'pussy',
    'twat',
    'vagina',
  )
)
# # forbidden_string = f"(?=\b|\s|^)(?P<word>({'|'.join(forbidden)}))(?=\b|\s|$)"
# forbidden_string = f"(?P<word>({'|'.join(forbidden)}))"
# pattern = re.compile(forbidden_string, flags=re.IGNORECASE)
PLACEHOLDER = 'BLAH'
BUFFER_SECONDS = 1

def _convert_to_seconds(t):
  t = time.strptime(t.split(',')[0], '%H:%M:%S')

  return datetime.timedelta(
    hours=t.tm_hour,
    minutes=t.tm_min,
    seconds=t.tm_sec
  ).total_seconds()

def _format_caption(caption):

  # m = re.search(r'<font.+>(?P<text>.+)</font>', caption)
  # if m:
  #   caption = m.group('text')

  # strip tags
  caption = re.sub('<[^<]+?>', '', caption)
  caption = re.sub(r'[-]', '', caption)

  return caption

def parse_captions(filename, offset=0):

  output = []
  data = []
  cleaned_captions = []

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

    (start, end) = duration.split(' --> ')
    start = _convert_to_seconds(start) + offset
    end = _convert_to_seconds(end) + offset

    caption = ' '.join(item[2:])
    caption = _format_caption(caption)

    for forbidden_categories in forbidden:
      for word in forbidden_categories:
        pattern = re.compile(r"(?=\b|\s|^)(?P<word>(%s))(?=\b|\s|$)" % word, flags=re.IGNORECASE)
        #  = re.search(pattern, caption)
        matches = re.findall(pattern, caption)
        if len(matches) > 0:
          for (_, matched_phrase) in matches:

            proceed = input(f'Found "{matched_phrase}" in "{caption}". Proceed with removal? (y/n/stop)    ').lower()

            if proceed == 'y':
              # calculate total syllables for patched phrase, taking into account spaced words
              s = sum([syllables.estimate(matched_word) for matched_word in matched_phrase.split(" ")])
              replace_string = "".join([PLACEHOLDER for i in range(0, s)] )
              caption = re.sub(matched_phrase, replace_string, caption)
            elif proceed == 'stop':
              print('script manually aborted')
              return

    cleaned_captions.append((start, end, caption))

  for (start, end, caption) in cleaned_captions:
    if re.search(PLACEHOLDER, caption):

      words = [(w, syllables.estimate(w)) for w in caption.split(" ")]

      total_syllables = sum([syllables.estimate(w) for w in caption.split(" ")])
      total_seconds = (end-start)
      seconds_per_syllable = (total_seconds/total_syllables)

      current_time = start
      for (w, s) in words:
        if re.match(PLACEHOLDER, w):

          w_start = math.floor(current_time) - BUFFER_SECONDS
          w_end = math.ceil(w_start + (seconds_per_syllable * s)) + BUFFER_SECONDS
          output.append([w_start, w_end, 'MUTE'])

        # be sure to increment the current time
        current_time = current_time + (seconds_per_syllable * s)

  # print(json.dumps({"data": output}))
  with open(f"{SCRIPT_ROOT}/output/{filename.split('.')[0]}.json", "w") as f:
    f.write(json.dumps({"data": output}, indent=4))
