# Finestra Scripts

Python scripts for transcribing `.srt` files from video files, and parsing them into cuepoints for backend injestion.

# Setup

  scripts$ python3 -m venv venv
  scripts$ source venv/bin/activate
  scripts$ pip install --upgrade pip
  scripts$ pip install -r requirements.txt


# Transcribe

  (venv) scripts$ python bin/scripts.py run_transcribe --filepath='Top Gun/Top Gun.mp4'

# Parse Captions

  (venv) scripts$ python bin/scripts.py run_parse_captions --filename=='Top Gun.srt'