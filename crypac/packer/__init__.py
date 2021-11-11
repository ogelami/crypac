import copy, sys
from crypac import currencies_s,  currencies_i

def promptKey(keyType):
	from getpass import getpass

	key = getpass('Enter {0} key:'.format(keyType))
	assert key == getpass('Re-type {} Key:'.format(keyType))

	return key

def pack(arguments):
	end = []

	for currency_key in currencies_s.keys():
		data_list = getattr(arguments, currency_key)

		if not data_list:
			continue

		for data_set in data_list:
			if not data_set:
				data_set = promptKey(currency_key)

			currency = copy.copy(currencies_s[currency_key])
			currency.setData(data_set)

			end.append(currency)

	for currency in end:
		currency.dump()

def unpack():
	end = []

	offset = 0
	input_buffer = sys.stdin.buffer.read()

	while offset < len(input_buffer):
		currency_offset = int(input_buffer[offset])

		# if null space
		if currency_offset == 0x00:
			offset += 1
			continue

		if currency_offset not in currencies_i:
			break

		currency_object = copy.copy(currencies_i[int(input_buffer[offset])])
		offset += 1

		read_size = int(input_buffer[offset])
		offset += 1
		data_slice = input_buffer[offset:int(offset + read_size)]

		offset += len(data_slice)

		currency_object.setData(data_slice)

		end.append(currency_object)

	for currency in end:
		currency.dump(True)