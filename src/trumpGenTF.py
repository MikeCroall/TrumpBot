import os
import pickle
from six.moves import urllib

import tflearn
from tflearn.data_utils import *

class TrumpGenerator(object):
	def __init__(self):
		self.maxLength = 10
		self.path = "tweets.txt"
		self.charIDXFile = "char_idx.pickle"

	def train(self):

		char_idx = None

		if(os.path.isfile(self.charIDXFile)):
			# load previous character file
			char_idx = pickle.load(open(self.charIDXFile, 'rb'))


		X, Y, char_idx = textfile_to_semi_redundant_sequences(self.path,seq_maxlen=self.maxLength,redun_step=3)

		pickle.dump(char_idx, open(self.charIDXFile, 'wb'))

		self.g = tflearn.input_data([None,self.maxLength,len(char_idx)]);
		self.g = tflearn.lstm(self.g,512,return_seq=True)
		self.g = tflearn.dropout(self.g,0.5)
		self.g = tflearn.lstm(self.g,512,return_seq=True)
		self.g = tflearn.dropout(self.g,0.5)
		self.g = tflearn.lstm(self.g,512)
		self.g = tflearn.dropout(self.g,0.5)
		self.g = tflearn.fully_connected(self.g,len(char_idx),activation='softmax')
		self.g = tflearn.regression(self.g, optimizer='adam', loss='categorical_crossentropy',
								 learning_rate=0.001)
		self.model = tflearn.SequenceGenerator(self.g, dictionary=char_idx, seq_maxlen=self.maxLength, max_checkpoints=0,checkpoint_path='model_trump')

	def getResponse(self,input="wall"):
		m.fit(X,Y,validation_set=0.1,batch_size=128,n_epoch=1,run_id='trumpedupkicks')
		return m.generate(600,temperature=1.0,seq_seed=input)

if __name__ == "__main__":
	tg = TrumpGenerator()
	tg.train()
	print(tg.getResponse())

