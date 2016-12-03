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


###Dependencies
+ Python 3.5.2
+ Flask Python Package
+ TensorFlow Python Package
+ Twython Python Package
+ tflearn Python Package
+ h5py Python Package
+ scipy Python Package
+ Ngrok (temporary, for tunelling local server to the internet)

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
