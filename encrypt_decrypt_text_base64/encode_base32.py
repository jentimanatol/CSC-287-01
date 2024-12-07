import base64

# Function to encode a string using Base32
def encode_base32(message):
    # Convert string to bytes
    message_bytes = message.encode('utf-8')
    # Encode the bytes using Base32
    base32_bytes = base64.b32encode(message_bytes)
    # Convert the encoded bytes back to a string
    base32_message = base32_bytes.decode('utf-8')
    return base32_message

# Function to decode a Base32 encoded string
def decode_base32(base32_message):
    # Convert string to bytes
    base32_bytes = base32_message.encode('utf-8')
    # Decode the bytes from Base32
    message_bytes = base64.b32decode(base32_bytes)
    # Convert the decoded bytes back to a string
    message = message_bytes.decode('utf-8')
    return message

# Example usage
original_message = 'Hello, World!'
encoded_message = encode_base32(original_message)
decoded_message = decode_base32(encoded_message)

print(f'Original Message: {original_message}')
print(f'Encoded Message: {encoded_message}')
print(f'Decoded Message: {decoded_message}')
