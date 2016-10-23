import os
import sys
import hashlib

from os.path import join

txtFiles = {}

count = 0

for root, dirs, files in os.walk('/Users/tmughal3/documents/'):
    for file in files:
        if file.endswith(".txt"):
            count = count + 1
            print count
            txtFiles[str(count)] = join(root, file.title())

wordDict = {}

for x in range(1,count+1,1):
    with open(txtFiles[str(x)],"r") as f:
        for line in f:
            for word in line.split():
                sha1 = hashlib.sha1()
                sha1.update(word)
                if str(sha1.hexdigest()) in wordDict.keys():
                    wordDict[str(sha1.hexdigest())] = wordDict[str(sha1.hexdigest())] + "," + str(x)
                else:
                    wordDict[str(sha1.hexdigest())] = str(x)

while(1):
    sTerm = str(raw_input("Enter term:"))
    sha1 = hashlib.sha1()
    sha1.update(sTerm)
    sha1 = sha1.hexdigest()
    result = ""
    if str(sha1) in wordDict.keys():
        result = wordDict[str(sha1)]
        result = result.split(",")
        for r in result:
            print(txtFiles[str(r)] + "\n")
    else:
        print("Not Found!")

