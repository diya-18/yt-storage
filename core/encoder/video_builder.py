import os

def build_video_from_frames(frame_dir, output_video):
    command = f"ffmpeg -y -framerate 1 -i {frame_dir}/frame_%05d.png -c:v libx264 -pix_fmt yuv420p {output_video}"
    os.system(command)