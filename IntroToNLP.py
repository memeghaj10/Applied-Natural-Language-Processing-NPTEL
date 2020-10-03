# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#importing libraries
import nltk

from nltk.probability import FreqDist

from nltk.corpus import stopwords


#loading tehe stop words
stop_words=set(stopwords.words('english'));


#reading the corpus
words = nltk.Text(nltk.corpus.gutenberg.words('bryant-stories.txt'))


#converting to small letters
words = [word.lower() for word in words if word.isalpha()]

words = [word.lower() for word in words if word not in stop_words]


#analysing the data using freqDist
fDist = FreqDist(words)

for x,y in fDist.most_common(10):
    print(x,y)
    


#this is the term frequency of the words!
for x,y in fDist.most_common(10):
    print(x,y/len(fDist))
    
    