from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto import Random
from Crypto.Util.Padding import pad

import binascii, sys
from io import BufferedReader
from crypac import logger

def hashPassword(key):
	md5 = MD5.new()
	md5.update(key.encode('utf-8'))

	return md5.digest()

def encrypt(data, password, generate_iv = False):
	key = hashPassword(password)

	if type(data) is BufferedReader:
		data = data.read()
	elif type(data) is str:
		data = data.encode('utf-8')

	if generate_iv:
		iv = Random.new().read(AES.block_size)
		output += iv
		sys.stdout.buffer.write(iv)
	else:
		iv = key

	logger.info('KEY {0}'.format(binascii.hexlify(key).decode('utf-8')))
	logger.info('IV  {0}'.format(binascii.hexlify(iv).decode('utf-8')))

	aes_object = AES.new(key, AES.MODE_CBC, iv)

	data = pad(data, AES.block_size)
	
	return aes_object.encrypt(data)

def decrypt(data, password, iv_prefix = False):
	key = hashPassword(password)

	if type(data) is BufferedReader:
		data = data.read()

	assert len(data) % 16 == 0, 'Wrong length of data {0} should maybe be {1} or {2}'.format(len(data), len(data) - len(data) % 16, 16 + len(data) - len(data) % 16)

	if iv_prefix:
		iv = data[0:16]
		data = data[16:]
	else:
		iv = key

	aes_object = AES.new(key, AES.MODE_CBC, iv)

	return aes_object.decrypt(data)