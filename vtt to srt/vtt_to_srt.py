import os
import subprocess

# Get the list of files in the current working directory
cwd = os.getcwd()
files = os.listdir(cwd)

# Loop through each file and convert .vtt to .srt using ffmpeg
for file in files:
    if file.endswith('.vtt'):
        input_path = os.path.join(cwd, file)
        output_path = os.path.join(cwd, file.replace('.vtt', '.srt'))
        subprocess.run(['ffmpeg', '-i', input_path, output_path])
