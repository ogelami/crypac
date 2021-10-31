#!/usr/bin/env python3

import sys, copy, binascii, struct, crypac.structure

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
		from crypac.packer import pack

		pack(arguments)

	elif arguments.mode == 'unpack':
		from crypac.packer import unpack

		unpack()

	elif arguments.mode == 'encrypt':
		from crypac.cryptography import encrypt

		sys.stdout.buffer.write(encrypt(arguments.data, arguments.key))

	elif arguments.mode == 'decrypt':
		from crypac.cryptography import decrypt
		
		sys.stdout.buffer.write(decrypt(arguments.data, arguments.key))

	elif arguments.mode == 'convert':
		if arguments.format == 'base58':
			from crypac.conversion.base58 import b58_to_hex, hex_to_b58

			for fragment in arguments.input:
				if arguments.reverse:
					print(hex_to_b58(fragment))
				else:
					print(b58_to_hex(fragment))
			
		elif arguments.format == 'bip39':
			from crypac.conversion.bip39 import bip39_to_hex, bip39_to_mnemonic

			if arguments.reverse:
				for hex in arguments.input:
					print(bip39_to_mnemonic(hex, arguments.language))
			else:
				print(bip39_to_hex(arguments.input, arguments.language).decode('utf-8'))

	if len(output):
		sys.stdout.buffer.write(output)
	#else:
		#argument_parser.print_help()