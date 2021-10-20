# Jargon-Search-in-Multiple-Text-files
This is a simple python script to search a list of jargons in multiple text files. It was made after a lot of searching on different text matching algorithms. Despite many other algorithms, this is one of the best approach provided that you have multiple files of 2000 to 2500 words each, and a jargon list of around 100+ words (or terms). Other fast string match algorithms are not useful in this case as most of them require a preprocessing time in addition to the matching time and hence are not very efficient for multiple files. This simple script tokenizes the words in the jargon list and looks for them in the text files. It can match up 70 words in 60000 files each of  10000+ words within 1 minute (40 to 50 seconds on average).