#!/usr/bin/env python3

import argparse, sys, copy, binascii, struct, crypac.structure

#verbose = False
arguments = False
argument_parser = False

def printe(*text):
	global arguments

	if arguments.verbose:
		print(*text, file = sys.stderr)

currencies_s = { x.symbol : x for x in crypac.structure.currencies }
currencies_i = { x.identifier : x for x in crypac.structure.currencies }

def start():
	global arguments, argument_parser

	verbose = arguments.verbose
	output = bytearray()

	if arguments.mode == 'pack':
		end = []

		for currency_key in currencies_s.keys():
			dataList = getattr(arguments, currency_key)

			if not dataList:
				continue

			for dataSet in dataList:
				currency = copy.copy(currencies_s[currency_key])
				currency.setData(dataSet[0])

				end.append(currency)

		for currency in end:
			currency.dump()

	elif arguments.mode == 'unpack':
		end = []

		offset = 0
		input_buffer = sys.stdin.buffer.read()

		while offset < len(input_buffer):
			currencyOffset = int(input_buffer[offset])

			# if null space
			if currencyOffset == 0x00:
				offset += 1
				continue

			if currencyOffset not in currencies_i:
				break

			currencyObject = copy.copy(currencies_i[int(input_buffer[offset])])
			offset += 1

			dataSlice = input_buffer[offset:int(offset + currencyObject.size / 2)]

			currencyObject.setData(dataSlice)
			offset += int(currencyObject.size / 2)
			
			end.append(currencyObject)

		for currency in end:
			currency.dump(True)
	elif arguments.mode == 'encrypt' or arguments.mode == 'decrypt':
		from Crypto.Cipher import AES
		from Crypto.Hash import MD5
		from Crypto import Random
		from Crypto.Util.Padding import pad

		key = arguments.key
		message = sys.stdin.buffer.read()

		md5 = MD5.new()
		md5.update(key.encode('utf-8'))
		key = binascii.unhexlify(md5.hexdigest())

		iv = key
		
		printe('key', binascii.hexlify(key))
		printe('key-based iv', binascii.hexlify(iv))

		if arguments.mode == 'encrypt':
			if arguments.generate_iv:
				iv = Random.new().read(AES.block_size)
				output += iv
				sys.stdout.buffer.write(iv)

			printe('choosen iv', binascii.hexlify(iv))
			aes_object = AES.new(key, AES.MODE_CBC, iv)

			message = pad(message, AES.block_size)
			ciphertext = aes_object.encrypt(message)
		else:
			if arguments.iv_prefix:
				iv = message[0:16]
				message = message[16:]

			printe('choosen iv', binascii.hexlify(iv))
			printe('encrypted data', binascii.hexlify(message[16:]))
			
			aes_object = AES.new(key, AES.MODE_CBC, iv)

			ciphertext = aes_object.decrypt(message)
			printe('decrypted data', binascii.hexlify(ciphertext))

		sys.stdout.buffer.write(ciphertext)
		#output += ciphertext
	elif arguments.mode == 'convert':
		if arguments.format == 'wif':
			import base58
			data = base58.b58decode(arguments.input)[1:33]

			print(binascii.hexlify(data).decode('utf-8'))
		elif arguments.format == 'bip39':
			from Crypto.Protocol.KDF import PBKDF2

	if len(output):
		sys.stdout.buffer.write(output)
	#else:
		#argument_parser.print_help()