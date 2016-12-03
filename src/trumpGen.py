import os
import pickle
from six.moves import urllib

import tflearn
from tflearn.data_utils import *

class TrumpGenerator(Object):
	def __init__(self):
		self.maxLength = 10

	def train(self):
		g = tflearn.input_data([None,self.maxLength,len(char_idx)]);
		g = tflearn.lstm(g,512,return_seq=True)
		g = tflearn.dropout(g,0.5)
		g = tflearn.lstm(g,512,return_seq=True)
		g = tflearn.dropout(g,0.5)
		g = tflearn.lstm(g,512)
		g = tflearn.dropout(g,0.5)
		g = tflearn.fully_connected(g,len(char_idx),activation='softmax')
		g = tflearn.regression(g, optimizer='adam', loss='categorical_crossentropy',
								 learning_rate=0.001)
		self.model = tflearn.SequenceGenerator(g, dictionary=char_idx, seq_maxlen=self.maxLength,
												clip_gradients=5.0, 
												checkpoint_path='model_trump')

	def getResponse(self,input="wall"):
		m.fit(X,Y,validation_set=0.1,batch_size=128,n_epoch=1,run_id='trumpedupkicks')
		m.generate(600,temperature=1.0,seq_seed=input)
