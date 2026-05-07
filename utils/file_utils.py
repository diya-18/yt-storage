def read_file_as_bytes(path):
    with open(path, "rb") as f:
        return f.read()

def write_bytes_to_file(path, data):
    with open(path, "wb") as f:
        f.write(data)