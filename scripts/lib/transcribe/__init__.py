#!/usr/bin/env python
import assemblyai as aai

import settings


def transcribe(filepath):


  aai.settings.api_key = settings.AAI_SETTINGS_API_KEY
  transcriber = aai.Transcriber()

  # transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
  # transcript = transcriber.transcribe("./my-local-audio-file.wav")
  transcript = transcriber.transcribe(f"{settings.MOVIES_FILE_PATH}/{filepath}")

  # print(transcript)
  # print(dir(transcript))
  # print(transcript.text)

  text = transcript.export_subtitles_srt()
  with open(f"{settings.SCRIPTS_ROOT}/lib/transcribe/output/Top Gun.srt", "w") as f:
    f.write(text)

  print('finis')