from reedsolo import RSCodec

# Number of parity bytes
PARITY_BYTES = 32

rsc = RSCodec(PARITY_BYTES)

def encode_data(data):
    return rsc.encode(data)

def decode_data(data):
    return rsc.decode(data)[0]