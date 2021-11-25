from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Util.Padding import pad, unpad

import binascii, sys
from io import BufferedReader
from crypac import logger

def hashPassword(key):
	sha256 = SHA256.new()
	sha256.update(b'\x6c\x81\x18\xc4\xdd\x29\xe3\xa8\x1c\x5a\x8e\xad\xc5\x89\xf3\xc8')
	sha256.update(key.encode('utf-8'))
	sha256.update(b'\xcb\x8c\x52\xc6\xc2\xc3\xed\xce\x08\x1e\x20\xd1\xad\xf4\xa3\x97')

	return sha256.digest()

def promptPassword():
		from getpass import getpass

		password = getpass()
		assert password == getpass('Re-type Password:')

		return password

def encrypt(data, password):
	if not password:
		password = promptPassword()

	key = hashPassword(password)

	if type(data) is BufferedReader:
		data = data.read()
	elif type(data) is str:
		data = data.encode('utf-8')

	iv = Random.new().read(AES.block_size)

	logger.info('KEY {0}'.format(binascii.hexlify(key).decode('utf-8')))
	logger.info('IV  {0}'.format(binascii.hexlify(iv).decode('utf-8')))

	aes_object = AES.new(key, AES.MODE_CBC, iv[:16])

	data = pad(data, AES.block_size)
	
	return aes_object.encrypt(data), iv

def decrypt(data, password):
	if not password:
		password = promptPassword()
		
	key = hashPassword(password)

	if type(data) is BufferedReader:
		data = data.read()

	assert len(data) % 16 == 0, 'Wrong length of data {0} should maybe be {1} or {2}'.format(len(data), len(data) - len(data) % 16, 16 + len(data) - len(data) % 16)

	iv = data[:16]
	data = data[16:]

	aes_object = AES.new(key, AES.MODE_CBC, iv)

	decrypted_data = aes_object.decrypt(data)

	return unpad(decrypted_data, AES.block_size)