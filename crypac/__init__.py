#!/usr/bin/env python3

import sys, copy, binascii, struct, logging, crypac.structure

arguments = False

logger = logging.getLogger('crypac')

currencies_s = { x.symbol : x for x in crypac.structure.currencies }
currencies_i = { x.identifier : x for x in crypac.structure.currencies }

def start():
	global arguments

	output = bytearray()

	if arguments.mode == 'pack':
		from crypac.packer import pack

		pack(arguments)

	elif arguments.mode == 'unpack':
		from crypac.packer import unpack

		unpack()

	elif arguments.mode == 'encrypt':
		from crypac.cryptography import encrypt

		data, iv = encrypt(arguments.data, arguments.key)

		sys.stdout.buffer.write(iv)
		sys.stdout.buffer.write(data)

	elif arguments.mode == 'decrypt':
		from crypac.cryptography import decrypt
		
		sys.stdout.buffer.write(decrypt(arguments.data, arguments.key))

	elif arguments.mode == 'convert':
		if arguments.format == 'base58':
			from crypac.conversion.base58 import b58_to_hex, hex_to_b58

			if not arguments.input:
				arguments.input = input('Input: ')

			if arguments.reverse:
				print(hex_to_b58(arguments.input))
			else:
				print(b58_to_hex(arguments.input))
			
		elif arguments.format == 'bip39':
			from crypac.conversion.bip39 import bip39_to_hex, bip39_to_mnemonic

			if arguments.reverse:
				if not arguments.input:
					arguments.input = [input('Input: ')]

				for hex in arguments.input:
					print(bip39_to_mnemonic(hex, arguments.language))
			else:
				if not arguments.input:
					arguments.input = input('Input: ').split()

				print(bip39_to_hex(arguments.input, arguments.language).decode('utf-8'))

	if len(output):
		sys.stdout.buffer.write(output)