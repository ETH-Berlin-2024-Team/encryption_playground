from ecies import encrypt, decrypt
from eth_account import Account
from eth_keys import keys
from eth_utils import decode_hex


private_key = '0xf192a8df09cd3219a0f5b16020e3a3310be1625a0a4152599a1fa0ff5f7ed6bc'
account = Account.from_key(private_key)

# Corresponding public key
public_key = account.public_key

# Public key in uncompressed format (65 bytes)
public_key_bytes = public_key.to_bytes()

# Encrypt message with public key
message = b"Your secret message"
encrypted_message = encrypt(public_key_bytes, message)

# Decrypt message with private key
decrypted_message = decrypt(private_key.to_bytes(), encrypted_message)

assert message == decrypted_message
