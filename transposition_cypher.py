def split_list(myList):
	length = len(myList)//2
	if len(myList)%2 == 0:
		return [myList[:length], myList[length:]]
	else:
		return [myList[:length], myList[length]]


def encrypt(message):
	if len(message)%2 != 0:
		message += " "
	myList = list(message)
	mySplitList = split_list(myList)
	encrypted = ""

	innerCount = 0
	while innerCount < len(mySplitList[0]):
		encrypted += mySplitList[0][innerCount]
		encrypted += mySplitList[1][innerCount]
		innerCount += 1
	return encrypted



def decrypt(encrypted):
	myList = list(encrypted)
	decrypted = ""
	for letter in myList:
		if myList.index(letter)%2 == 0:
			decrypted += letter
	for letter in myList:
		if myList.index(letter)%2 != 0:
			decrypted += letter
	return decrypted
	
	
	
	
message = "what's up"
encrypted = encrypt(message)
print(encrypted)
print(decrypt(encrypted))
