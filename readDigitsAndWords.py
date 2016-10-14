# 01.12.2015
# Input: the name of a file that contains eather words or digits
# digits: print the max, the min, the mean, the meadian, the std
# words: print number of unique words and 5 most common words

import numpy

# returns 1 if theList is only digits otherwise 0
def isOnlyNumbers(theList):
	match = 1
	for i in range(len(theList)):
		if not theList[i].isdigit():
			match = 0
	return match

# Finds in setList the most frequent value in theList
# returns the position of the word in setList
def findMax(theList,setList):
	theMax = 0
	for i in range(len(setList)):
		counter = 0
		for j in range(len(theList)):
			if setList[i] == theList[j]:
				counter += 1
		if counter > theMax:
			theMax = counter
			intvalue = i
	return intvalue

# presume that the numbers are separated with space
# presume that words are separated with , or . 
thename = input('Enter the filename:')
thefile = open(thename, 'r')
n = thefile.read()
t = n.split()
thefile.close()

if isOnlyNumbers(t) == 1:
	a = list()
	for i in range(len(t)):
		a.append(int(t[i]))

	print('The mean is:', numpy.mean(a))
	print('The meadian is:', numpy.median(a))
	print('The min is:', numpy.min(a))
	print('The max is:',numpy.max(a))
	print('The std is:', numpy.std(a))

else:
	s = set()
	for i in range(len(t)):
		t[i] = t[i].lower()
		t[i] = t[i].replace('.', '')
		t[i] = t[i].replace(',', '')
		s.add(t[i])

	print('The number of unique words:', len(s))

	sList = list(s)

	print('The five most common words:')

	j = 0
	while j < 5:
		x = findMax(t,sList)
		print(sList[x])
		sList[x] = ''
		j += 1



