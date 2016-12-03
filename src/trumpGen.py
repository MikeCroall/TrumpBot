import os


class TrumpGenerator(object):
	def __init__(self,markovLength):
		self.gen = SentenceGenerator()
		self.markovLength = markovLength
	
	def train(self,filename):
		self.gen.buildMapping(self.gen.wordlist(filename),self.markovLength)	

	def getResponse(self,input="wall"):
		return genSentence(markovLength)

if __name__ == "__main__":
	tg = TrumpGenerator()
	tg.train()
	print(tg.getResponse())

