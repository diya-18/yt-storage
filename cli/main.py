from utils.file_utils import read_file_as_bytes, write_bytes_to_file
from core.encoder.frame_encoder import bytes_to_frames
from core.encoder.video_builder import build_video_from_frames
from core.decoder.video_parser import extract_frames
from core.decoder.frame_decoder import frames_to_bytes
from core.metadata.metadata_manager import save_metadata, load_metadata
from core.error_correction.fec import encode_data, decode_data
import os

INPUT_FILE = "data/input/sample.txt"
VIDEO_FILE = "data/encoded/output.mp4"
FRAME_DIR = "data/encoded/frames"
DECODED_DIR = "data/output/frames"
OUTPUT_FILE = "data/output/recovered.txt"
METADATA_FILE = "data/encoded/metadata.json"

# Encode: Convert file to video
raw_data = read_file_as_bytes(INPUT_FILE)
data = encode_data(raw_data)
num_frames = bytes_to_frames(data, FRAME_DIR)

metadata = {
    "original_size": len(raw_data),
    "num_frames": num_frames,
    "frame_size": 256,
    "filename": os.path.basename(INPUT_FILE)
}

save_metadata(METADATA_FILE, metadata)
build_video_from_frames(FRAME_DIR, VIDEO_FILE)

# Decode: Extract frames from video and convert back to bytes
metadata = load_metadata(METADATA_FILE)

extract_frames(VIDEO_FILE, DECODED_DIR)
recovered = frames_to_bytes(DECODED_DIR, metadata["num_frames"])

# Trim padding: The last frame may have padding bytes, so we trim the recovered data to the original file size.
# also this fixes padding corruption issue where the last frame is padded with zeros which can cause issues when reconstructing the original file.
expected_size = metadata["original_size"] + 32
recovered = recovered[:expected_size]

recovered = decode_data(recovered)
recovered = recovered[:metadata["original_size"]]

write_bytes_to_file(OUTPUT_FILE, recovered)

print("Recovery complete.")