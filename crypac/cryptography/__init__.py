from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto import Random
from Crypto.Util.Padding import pad

import binascii,sys
from io import BufferedReader

def hashPassword(key):
	md5 = MD5.new()
	md5.update(key.encode('utf-8'))

	return binascii.unhexlify(md5.hexdigest())

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

	#printe('choosen iv', binascii.hexlify(iv))
	aes_object = AES.new(key, AES.MODE_CBC, iv)

	data = pad(data, AES.block_size)
	
	return aes_object.encrypt(data)

def decrypt(data, password, iv_prefix = False):
	key = hashPassword(password)

	if type(data) is BufferedReader:
		data = data.read()

	if iv_prefix:
		iv = data[0:16]
		data = data[16:]
	else:
		iv = key

	#printe('choosen iv', binascii.hexlify(iv))
	#printe('encrypted data', binascii.hexlify(data[16:]))
	
	aes_object = AES.new(key, AES.MODE_CBC, iv)

	return aes_object.decrypt(data)
	#printe('decrypted data', binascii.hexlify(ciphertext))

#sys.stdout.buffer.write(ciphertext)