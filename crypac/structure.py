import binascii, sys, struct

class CurrencyType:
	def __init__(self, symbol, identifier, size):
		self.symbol = symbol
		self.identifier = identifier
		self.size = size
	
	def setData(self, data):
		if type(data) is str:
			assert len(data) == self.size * 2

			self.data = binascii.unhexlify(data)
		elif type(data) is bytes:
			assert len(data) == self.size

			self.data = data
	
	def dump(self, pretty = False):
		if pretty:
			print('{} {}'.format(self.symbol.upper(), binascii.hexlify(self.data).decode('utf-8')))

		else:
			output = struct.pack('B', self.identifier)
			output += self.data

			sys.stdout.buffer.write(output)

# identifier 0x00 reserved for null-byte
currencies = [
	CurrencyType('xdg', 0x01, 32),
	CurrencyType('sol', 0x02, 32),
	CurrencyType('btc', 0x03, 32),
	CurrencyType('eth', 0x04, 32),
	CurrencyType('dot', 0x05, 32),
]
