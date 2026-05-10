import os
from utils.ffmpeg_wrapper import run_ffmpeg

def build_video_from_frames(frame_dir, output_video):
    command = (
        f"ffmpeg -y -framerate 1 -i {frame_dir}/frame_%05d.png "
        f"-c:v libx264 -crf 0 -preset veryslow "
        f"-pix_fmt gray "
        f"{output_video}"
    )

    run_ffmpeg(command)