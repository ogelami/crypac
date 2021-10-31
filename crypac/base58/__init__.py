import base58, binascii

def b58_to_hex(wif):
	return binascii.hexlify(base58.b58decode(wif)).decode('utf-8')

def hex_to_b58(hex):
	return base58.b58encode(binascii.unhexlify(hex)).decode('utf-8')
