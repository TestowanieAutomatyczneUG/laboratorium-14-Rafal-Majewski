def validateIsbnNumber(formattedIsbnNumber):
	isbnNumber = formattedIsbnNumber.replace('-', '')
	if len(isbnNumber) != 13:
		return False
	return sum([(1 + 2 * (i % 2)) * int(isbnNumber[i]) for i in range(13)]) % 10 == 0