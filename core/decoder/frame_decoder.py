import cv2

def frames_to_bytes(frame_dir, num_frames):
    data = bytearray()

    for i in range(num_frames):
        path = f"{frame_dir}/frame_{i:05d}.png"
        frame = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        data.extend(frame.flatten())

    return bytes(data)