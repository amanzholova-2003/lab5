
def sortSur(nameList):
	
	
	nameList.sort(key=lambda x: x.split()[-1])
	
	
	return nameList



nameList = ['John Wick Class A', 'Jason Voorhees Class B',
			'Freddy Krueger Class C', 'Keyser Soze Class D',
			'Mohinder Singh Pandher Class E']


print('\nList of Names:\n', nameList)
print('\nAfter sorting:\n', sortSur(nameList))

