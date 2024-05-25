import os
import dotenv
from eth_keys import keys
from eth_utils import decode_hex, encode_hex, keccak
from ecies import encrypt, decrypt

dotenv.load_dotenv()

# Your Ethereum private key (hex format)
private_key_hex = os.getenv('PRIVATE_KEY')
private_key = keys.PrivateKey(decode_hex(private_key_hex))
public_key = private_key.public_key
eth_address = public_key.to_checksum_address()
message = b"Your secret message"

print(f'public_key {private_key.public_key}')
print(f'Ethereum address: {eth_address}')

# Public key in uncompressed format (65 bytes)
public_key_bytes = b'\x04' + public_key.to_bytes()
encrypted_message = encrypt(public_key_bytes, message)

decrypted_message = decrypt(private_key.to_bytes(), encrypted_message)

assert message == decrypted_message
print(f'{message=} {decrypted_message=}')
