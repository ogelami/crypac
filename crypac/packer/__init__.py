import copy, sys
from crypac import currencies_s,  currencies_i

def pack(arguments):
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

def unpack():
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

		dataSlice = input_buffer[offset:int(offset + currencyObject.size)]

		currencyObject.setData(dataSlice)
		offset += int(currencyObject.size)

		end.append(currencyObject)

	for currency in end:
		currency.dump(True)