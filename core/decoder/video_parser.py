import os

def extract_frames(video_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    command = (
        f"ffmpeg -i {video_path} "
        f"-start_number 0 "
        f"-pix_fmt gray "
        f"{output_dir}/frame_%05d.png"
    )
    os.system(command)