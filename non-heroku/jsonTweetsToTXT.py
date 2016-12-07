import json
import re
saveStr = "";
with open('tweets.json', encoding='utf-8') as data_file:
	data = json.loads(data_file.read())
	for key, value in data['tweets'].items():
		sanitisedTweet = re.sub(r'https?://(\S)+', '', value)
		saveStr += sanitisedTweet + "\n"
	print(saveStr)

##now write the text file
text_file = open("tweets.txt","w")
text_file.write(saveStr)
text_file.close()	
