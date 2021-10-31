import binascii, hashlib
from pkg_resources import resource_string

def get_word_list(language):
	word_list = resource_string('crypac.conversion.bip39.wordlist', language + '.txt')
	word_list = word_list.decode('utf-8').strip().split("\n")
	
	return word_list

def bip39_to_hex(mnemonic, language = 'english'):
	word_list = get_word_list(language)
	
	index_list = []

	for word in mnemonic:
		index_list.append(word_list.index(word))

	concatLenBits = len(index_list) * 11
	concatBits = [False] * concatLenBits

	for offset, value in enumerate(index_list):
		for ii in range(11):
			concatBits[(offset * 11) + ii] = (value & (1 << (10 - ii))) != 0

	checksumLengthBits = concatLenBits // 33
	entropyLengthBits = concatLenBits - checksumLengthBits
	entropy = bytearray(entropyLengthBits // 8)

	for ii in range(len(entropy)):
		for jj in range(8):
			if concatBits[(ii * 8) + jj]:
				entropy[ii] |= 1 << (7 - jj)

	return binascii.hexlify(entropy)

def bip39_to_mnemonic(hex, language = 'english'):
	data = binascii.unhexlify(hex)
	word_list = get_word_list(language)

	if len(data) not in [16, 20, 24, 28, 32]:
		raise ValueError(
			"Data length should be one of the following: [16, 20, 24, 28, 32], but it is not (%d)."
			% len(data)
		)

	h = hashlib.sha256(data).hexdigest()

	b = (
			bin(int.from_bytes(data, byteorder="big"))[2:].zfill(len(data) * 8)
			+ bin(int(h, 16))[2:].zfill(256)[: len(data) * 8 // 32]
	)

	result = []

	for i in range(len(b) // 11):
		idx = int(b[i * 11 : (i + 1) * 11], 2)
		result.append(word_list[idx])
		
	if language == "japanese":  # Japanese must be joined by ideographic space.
			result_phrase = u"\u3000".join(result)
	else:
			result_phrase = " ".join(result)

	return result_phrase