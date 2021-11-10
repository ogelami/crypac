import binascii, sys, struct

class CurrencyType:
	def __init__(self, symbol, identifier):
		self.symbol = symbol
		self.identifier = identifier
	
	def setData(self, data):
		if type(data) is str:
			self.data = binascii.unhexlify(data)
		elif type(data) is bytes:
			self.data = data
	
	def dump(self, pretty = False):
		if pretty:
			print('{} {}'.format(self.symbol.upper(), binascii.hexlify(self.data).decode('utf-8')))

		else:
			output = struct.pack('B', self.identifier)
			output += struct.pack('B', len(self.data))
			output += self.data

			sys.stdout.buffer.write(output)

# identifier 0x00 reserved for null-byte
currencies = [
	CurrencyType('xdg', 0x01),
	CurrencyType('sol', 0x02),
	CurrencyType('btc', 0x03),
	CurrencyType('eth', 0x04),
	CurrencyType('dot', 0x05)
]
