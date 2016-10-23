#Filesearch Algo by Muhammad Talha
#Roll No. 34440/112202
#Advanced Programming Lab for BSCS-4C

import os
import sys
import hashlib

from os.path import join
from os.path import basename
txtFiles = {}

#Var to store number of files
count = 0

#Set Root Path
myPath = '/Users/tmughal3/documents/'

#Indexing the Files
for root, dirs, files in os.walk(myPath):
    for file in files:
        if file.endswith(".txt"):
            count = count + 1

            txtFiles[str(count)] = join(root, file.title())

#hashtable for words
wordDict = {}
wordCount = 0

#Indexing the words
for x in range(1,count+1,1):
    with open(txtFiles[str(x)],"r") as f:
        for line in f:
            for word in line.split():
                wordCount = wordCount + 1
                sha1 = hashlib.sha1()
                sha1.update(word.lower())
                if str(sha1.hexdigest()) in wordDict.keys():
                        wordDict[str(sha1.hexdigest())] = wordDict[str(sha1.hexdigest())] + "," + str(x)
                else:
                    wordDict[str(sha1.hexdigest())] = str(x)

print ("Files Found: " + str(count)+ "\n")
print ("Word Count: " + str(wordCount) + "\n")

#Infinite Search Loop
while(1):
    sTerm = str(raw_input("Enter term:"))
    sha1 = hashlib.sha1()
    sha1.update(sTerm.lower())
    sha1 = sha1.hexdigest()
    result = ""

    #Check for filenames
    for x in range(1, count + 1, 1):

        loc, fname = os.path.split(txtFiles[str(x)])

        if sTerm.lower() in [f.lower() for f in fname.split(".")]:
            print ("Filename found: " + txtFiles[str(x)] + "\n")

    if str(sha1) in wordDict.keys():
        result = wordDict[str(sha1)]
        result = result.split(",")
        tmp = ""

        for r in result:

            #To Avoid Repitition
            if tmp != r:
                print("Found In " + txtFiles[str(r)] + "\n")
            tmp = r
    else:
        print("Search Term Not Found In File Contents!" + "\n")

