import os
from senGen import SentenceGenerator


class TrumpGenerator(object):

    def __init__(self, markovLength):
        self.gen = SentenceGenerator()
        self.markovLength = markovLength

    def train(self, filename):
        self.gen.buildMapping(self.gen.wordlist(filename), self.markovLength)

    def getResponse(self, inputWord="wall"):
        return self.gen.genSentence(self.markovLength, inputWord)

if __name__ == "__main__":
    tg = TrumpGenerator(1)
    tg.train("tweets.txt")
    print(tg.getResponse())
