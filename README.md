# TrumpBot
## A chat bot to emulate Donald Trump's speech

###Goals
+ API that receives a string, returns a string response in the style of Donald Trump
  * /response will return a Trump style statement.
  * /response?q=Query will return Trump's thoughts on your Query
+ Automatically determine Donald Trump's style via tweet analysis (TensorFlow)
+ Text message wrapper for API calls (Twilio)
+ Web wrapper for API calls
+ Android App wrapper for API calls (eventually...)

API Functionality
+ Train Neural Network
+ getResponse : input string -> output string

###Problems We Encountered
+ Tensorflow didn't seem to work, so after many hours of attempted (and failed) bug fixes, we switched from LSTM networks to simple Markov Chains.
+ Twitter has a limit on the number of tweets you can download. An alternative method of harvesting tweets was found.

###Dependencies
+ Python 3.5.2
+ Flask Python Package
+ Twython Python Package
+ h5py Python Package
+ scipy Python Package
+ Ngrok (temporary, for tunelling local server to the internet)
+ OhmGeek's fork of markov-sentence-generator (for generating the sentences)

###Running the bot
On Linux, simply open terminal, navigate to the folder where `run.sh` is located
```
$ cd /path/to/server/
```
Make sure run.sh is executable (note: this requires root)
```
$ chmod +x run.sh
```
Finally, run the script    
```
$ ./run.sh
```
