import numpy as np
import cv2
import os

FRAME_SIZE = 256

def bytes_to_frames(data, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    bytes_per_frame = FRAME_SIZE * FRAME_SIZE
    total_frames = (len(data) // bytes_per_frame) + 1

    for i in range(total_frames):
        chunk = data[i*bytes_per_frame:(i+1)*bytes_per_frame]

        if len(chunk) < bytes_per_frame:
            chunk += b'\x00' * (bytes_per_frame - len(chunk))

        frame = np.frombuffer(chunk, dtype=np.uint8)
        frame = frame.reshape((FRAME_SIZE, FRAME_SIZE))

        cv2.imwrite(f"{output_dir}/frame_{i:05d}.png", frame)

    return total_frames