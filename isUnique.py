string = "isUnique"

def isUnique(string):
	if len(string) > 128: return False
	else:
		characters = [False] * 128

		for char in string:
			intValue = ord(char)
			if characters[intValue]:
				return False
			else:
				characters[intValue] = True
		return True

print(isUnique(string))