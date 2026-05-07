from utils.file_utils import read_file_as_bytes, write_bytes_to_file
from core.encoder.frame_encoder import bytes_to_frames
from core.encoder.video_builder import build_video_from_frames
from core.decoder.video_parser import extract_frames
from core.decoder.frame_decoder import frames_to_bytes

INPUT_FILE = "data/input/sample.txt"
VIDEO_FILE = "data/encoded/output.mp4"
FRAME_DIR = "data/encoded/frames"
DECODED_DIR = "data/output/frames"
OUTPUT_FILE = "data/output/recovered.txt"

# Encode
data = read_file_as_bytes(INPUT_FILE)
num_frames = bytes_to_frames(data, FRAME_DIR)
build_video_from_frames(FRAME_DIR, VIDEO_FILE)

# Decode
extract_frames(VIDEO_FILE, DECODED_DIR)
recovered = frames_to_bytes(DECODED_DIR, num_frames)

write_bytes_to_file(OUTPUT_FILE, recovered)

print("Done.")