import subprocess

def run_ffmpeg(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print("FFmpeg command executed successfully.")

    except subprocess.CalledProcessError as e:
        print("FFmpeg command failed.")
        print(e)