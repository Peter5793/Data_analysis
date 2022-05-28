# -*- coding: utf-8 -*-
"""
This a utility tool that can perform analysis on a given text

@author: Peter Lugalia
"""
import re
import string
marks = string.punctuation

class analysedText():
    def __init__(self, text):
        format_text = text.replace('.','').replace('!','').replace('?','').replace(',','')
        format_text = format_text.lower()
        self.format_text = format_text
    
    def freqAll(self):
        word_list = self.format_text.split('')
        
        #create a dictionary
        freqmap = {}
        for word in set(word_list): # use the set to remove duplicates
            fremap[word] = word_list.count(word)
        return freqmap
    
    def wordFreq(self, word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
        
import sys

sampleMap = {'eirmod': 1,'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1, 'tempor': 1, 'dolor': 1, 'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

print("Constructor: ")
try:
    samplePassage = analysedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
    print(testMsg(samplePassage.format_text == "lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet"))
except:
    print("Error detected. Recheck your function " )
print("freqAll: ")
try:
    wordMap = samplePassage.freqAll()
    print(testMsg(wordMap==sampleMap))
except:
    print("Error detected. Recheck your function " )
print("freqOf: ")
try:
    passed = True
    for word in sampleMap:
        if samplePassage.wordFreq(word) != sampleMap[word]:
            passed = False
            break
    print(testMsg(passed))
    
except:
    print("Error detected. Recheck your function  " )
    
    
