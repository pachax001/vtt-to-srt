import os
import subprocess

# Get the list of files in the current working directory
cwd = os.getcwd()
files = os.listdir(cwd)

# Loop through each file and convert .mp4 to .mkv using ffmpeg
for file in files:
    if file.endswith('.mp4'):
        input_path = os.path.join(cwd, file)
        output_path = os.path.join(cwd, file.replace('.mp4', '.mkv'))
        subprocess.run(['ffmpeg', '-i', input_path, '-codec', 'copy', output_path])

        # Delete the original .mp4 file permanently without going to recycle bin
        os.remove(input_path)
#Remeber this deletes the original mp4 file.
