#!/usr/bin/python

import re
import random
import sys


class SentenceGenerator(object):

    def __init__(self):
        self.tempMapping = {}
        self.mapping = {}
        self.starts = []

    def fixCaps(self, word):
        if word.isupper() and word != "I":
            word = word.lower()
        elif word[0].isupper():
            word = word.lower().capitalize()
        else:
            word = word.lower()
        return word

    def toHashKey(self, lst):
        return tuple(lst)

    def wordlist(self, filename):
        f = open(filename, 'r')
        wordlist = [self.fixCaps(w)
                    for w in re.findall(r"#?[\w']+|[.,!?;]", f.read())]
        f.close()
        return wordlist

    def addItemToTempMapping(self, history, word):
        while len(history) > 0:
            first = self.toHashKey(history)
            if first in self.tempMapping:
                if word in self.tempMapping[first]:
                    self.tempMapping[first][word] += 1.0
                else:
                    self.tempMapping[first][word] = 1.0
            else:
                self.tempMapping[first] = {}
                self.tempMapping[first][word] = 1.0
            history = history[1:]

    # Building and normalizing the mapping.
    def buildMapping(self, wordlist, markovLength):
        self.starts.append(wordlist[0])
        for i in range(1, len(wordlist) - 1):
            if i <= markovLength:
                history = wordlist[: i + 1]
            else:
                history = wordlist[i - markovLength + 1: i + 1]
            follow = wordlist[i + 1]
            # if the last elt was a period, add the next word to the start list
            if history[-1] == "." and follow not in ".,!?;":
                self.starts.append(follow)
            self.addItemToTempMapping(history, follow)
        # Normalize the values in tempMapping, put them into mapping
        for first, followset in self.tempMapping.items():
            total = sum(followset.values())
            # Normalizing here:
            self.mapping[first] = dict([(k, v / total)
                                        for k, v in followset.items()])

    # Returns the next word in the sentence (chosen randomly),
    # given the previous ones.
    def next(self, prevList):
        sum = 0.0
        retval = ""
        index = random.random()
        # Shorten prevList until it's in mapping
        while self.toHashKey(prevList) not in self.mapping:
            prevList.pop(0)
        # Get a random word from the mapping, given prevList
        for k, v in self.mapping[self.toHashKey(prevList)].items():
            sum += v
            if sum >= index and retval == "":
                retval = k
        return retval

    def genSentence(self, markovLength, startWord=None):

        if(startWord is None):
            startWord = "wall"
        # Start with a random "starting word"
        curr = startWord
        sent = curr.capitalize()
        prevList = [curr]
        if(len(self.next([curr])) == 0):
            curr = "wall"
            sent = "WALL"
            prevList = [curr]
        # Keep adding words until we hit a period
        while (curr not in "."):
            curr = self.next(prevList)
            prevList.append(curr)
            # if the prevList has gotten too long, trim it
            if len(prevList) > markovLength:
                prevList.pop(0)
            if (curr not in ".,!?;"):
                sent += " "  # Add spaces between words (but not punctuation)
            sent += curr
        return sent


# These mappings can get fairly large -- they're stored globally to
# save copying time.

# (tuple of words) -> {dict: word -> number of times the word appears following the tuple}
# Example entry:
#    ('eyes', 'turned') => {'to': 2.0, 'from': 1.0}
# Used briefly while first constructing the normalized mapping
# (tuple of words) -> {dict: word -> *normalized* number of times the word appears following the tuple}
# Example entry:
#    ('eyes', 'turned') => {'to': 0.66666666, 'from': 0.33333333}

# Contains the set of words that can start sentences

# We want to be able to compare words independent of their capitalization.
# affect processing time too negatively.
# Returns the contents of the file, split into a list of words and
# (some) punctuation.
# Self-explanatory -- adds "word" to the "tempMapping" dict under "history".
# tempMapping (and mapping) both match each word to a list of possible next
# words.
# Given history = ["the", "rain", "in"] and word = "Spain", we add "Spain" to
# the entries for ["the", "rain", "in"], ["rain", "in"], and ["in"].
