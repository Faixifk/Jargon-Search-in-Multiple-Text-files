import os
import re
import datetime
from os import listdir
from os.path import isfile, join
os.chdir("D:/spam")
#open the jargon list in txt or csv format. provide full path if needed
JL = open("JargonList.txt")

#read the jargon list file
JL = JL.read()

#tokenize the words at your preferred delimeters. I have splitted using the ' / ' character because my jargon list contains multiword terms like ZTE / IPCC / CRM/ AAA
words = re.split(" / |/ |/|\n", JL)

#start the time before running the loop for 60000 files, to keep a track of how long it ran
start = datetime.datetime.now()

#counter counts the number of matched words in all the files
match_count = 0

#initial for loop that reads the 60000 files named as file1.txt, file2.txt, file3.txt . . . file59999.txt
'''''''''
for i in range(0,60000):
    fn = "file" + str(i) + ".txt"
    spamreader = open(fn,'r')
'''''''''
#note: this loop can also be replaced in order to read all the files of the directory one by one using the OS module in python
onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
for fn in onlyfiles:
    
    #open the file in read mode
    spamreader = open(fn,'r')
    
    #read the file
    spamreader = spamreader.read()
    
    #for loop that iterates over the words in our jargon list one by one
    for w in words:
        #ret stores the starting index of the word, and -1 in case the word is not found
        ret = spamreader.find(w) 

        #if word found in the file, then increment the counter
        if ret != -1:
            match_count +=1
            #print(w + " at index: " + str(ret)) #uncomment this previous line to also know the index of each word 

#print the number of words that matched
print("Matched: " + str(match_count))

#stop the timer
end = datetime.datetime.now()

#calculate the time taken from start until stop
taken = end - start

#print the time taken
print("Time Taken ", taken)

