####_Google Workshop Project_####
__Author__ = "Garrett Marchese"
__Date__ = 7/1/17
__Version__ = 1

import nltk
import re
import collections 
#nltk.download() # toggle if nltk has not been downloaded 

# Get list of words for comparisons
from nltk.corpus import words
word_list = words.words()

#print(word_list[3455])

# Letter frequency function
# Store letters and frequency in dictionary
# Return Dictionary
def findLetterFrequency(word):

	# Using collections 
	lfDictionary = collections.Counter(word)
	return lfDictionary

while(True):
	# Get 7-8 digit license plate string from user (exp. "C4H23EIF")
	licensePlate = input("Enter license plate: ")
	
	# Check that string is 7-8 chars/digits long
	if len(licensePlate) < 7 or len(licensePlate) > 8:
		print("Please enter a string with 7-8 characters/digits")

	elif bool(re.search('[a-zA-Z]', licensePlate)):
		try:
			# Remove alpha characters from input
			strippedChars = ''.join(i for i in licensePlate if i.isalpha())
			strippedChars = strippedChars.lower()

			print(strippedChars)
	
			# Store processed chars in list
			charsList = list(strippedChars)
			#print(charsList)
			
		except:
			print("hit except")
			continue

		# Break from while loop	
		break

	else: 
		print("Please enter license plate with at least one character")


plateCharFreqsDict = findLetterFrequency(charsList)
print(plateCharFreqsDict)

allMatching = False
relevantWords = list()

# Iterate through each word in word list
for word in word_list:

	for key, val in plateCharFreqsDict.items():   

		if word.count(key) != val:   			   
			allMatching = False
			break

		elif word.count(key) == val:
			allMatching = True

	if allMatching == True:
		relevantWords.append(word)

#print(relevantWords)

try:
	# Print shortest word
	print(min(relevantWords, key=len)) 

except:
	# No word found
	print("No word found")							
