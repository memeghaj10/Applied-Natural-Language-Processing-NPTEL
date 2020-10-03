#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:34:36 2020

@author: oem
"""

#importing libraries

import re
from operator import itemgetter
import nltk
import pandas as pd

frequency ={}
words_emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))

for word in words_emma:
    count = frequency.get(word,0)
    frequency[word]=count+1
    
rank=1


#Zipf's Law


column_header = ['Rank','Frequency','Frequency*Rank']
df = pd.DataFrame(columns=column_header)


for word,freq in reversed(sorted(frequency.items(),key=itemgetter(1))):
    df.loc[word] = [rank,freq,rank*freq]
    rank=rank+1

print(df)
    


#Mandellbrot Approx

column_header = ['Rank','Frequency','Frequency*(Rank+Offset)']
df = pd.DataFrame(columns=column_header)

rank=1
for word,freq in reversed(sorted(frequency.items(),key=itemgetter(1))):
    df.loc[word] = [rank,freq,(rank+2.7)*freq]
    rank=rank+1

print(df)

