####_Google Workshop Project_####
__Author__ = "Garrett Marchese"
__Date__ = 7/1/17
__Version__ = 2

### Update ###
# Create function for regex 
# Adding file io features (license plate data) #
	#Initial file IO will deal with properly formatted
	#license plate data 
		#Next update will extract the improperly formatted data
		#and notify the user upon completion of the program
		#while providing the solutions for the correct data
# Write corpus data out to file and manipulate henseforth #

#***NOTES***#
# 1
	# Letter frequency matching algo needs fixing 
	# Example:
	# shortest word with to make with abcdef is "feedback"
	# program returns "backfeild"
# 2
	# Some words are not in the nltk such as 
	# shortest word that contains all 5 vowels "Eunoia"

#***FIXED***#
#1

import nltk
import re
import collections 
#nltk.download() # toggle if nltk has not been downloaded 

# Get list of words for comparisons
from nltk.corpus import words
word_list = words.words()

# if any("eunoia" in s for s in word_list): # verify word in list
#  	print("Yessir")

# Save word list to file 
dictionaryFile = open('dictFile.txt','w')
for word in word_list:
 	dictionaryFile.write("%s\n" % word.lower())


# Letter frequency function
# Store letters and frequency in dictionary
# Return Dictionary
def findLetterFrequency(word):
	# Using collections 
	lfDictionary = collections.Counter(word)
	return lfDictionary

#def regExEvalForPlates(plate):


while(True):
	# Get 7-8 digit license plate string from user (exp. "C4H23EIF")
	licensePlate = input("Enter license plate: ")
	
	# Check that string is 7-8 chars/digits long
	if len(licensePlate) < 7 or len(licensePlate) > 8:
		print("Please enter a string with 7-8 characters/digits")

	elif bool(re.search('[a-zA-Z]', licensePlate)):
		try:
			# Remove alpha characters from input
			strippedChars = ''.join(i for i in licensePlate if i.isalpha()) # list comprehension
			strippedChars = strippedChars.lower()

			print(strippedChars)
			#print(type(strippedChars))
			# listOfShit.append(strippedChars)
			# print("Line 54")
			# print(listOfShit)
			# Store processed chars in list
			charsList = list(strippedChars)

			# Break from while loop	
			break

		except:
			print("hit except")
			continue

	else: 
		print("Please enter license plate with at least one character")


plateCharFreqsDict = findLetterFrequency(charsList)
print(plateCharFreqsDict)

allMatching = False
relevantWords = list()

# Iterate through each word in word list
for word in word_list:

	for key, val in plateCharFreqsDict.items():   

		if word.count(key) < val:   			   
			allMatching = False
			break

		elif word.count(key) >= val:
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
