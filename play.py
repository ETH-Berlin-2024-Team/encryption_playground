from ecies import encrypt, decrypt
from eth_keys import keys
from eth_utils import decode_hex

# Your Ethereum private key (hex format)
private_key_hex = '0xf192a8df09cd3219a0f5b16020e3a3310be1625a0a4152599a1fa0ff5f7ed6bc'
private_key = keys.PrivateKey(decode_hex(private_key_hex))

# Corresponding public key
public_key = private_key.public_key

# Public key in uncompressed format (65 bytes)
public_key_bytes = b'\x04' + public_key.to_bytes()

# Encrypt message with public key
message = b"Your secret message"
encrypted_message = encrypt(public_key_bytes, message)

# Decrypt message with private key
decrypted_message = decrypt(private_key.to_bytes(), encrypted_message)

assert message == decrypted_message
print(f'{message=} {decrypted_message=}')
