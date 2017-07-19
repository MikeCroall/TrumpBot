# TrumpBot
## A chat bot to emulate Donald Trump's speech

### Download the App (Android 4.3+)
The Android app is now available on the play store! You can find it [here](https://play.google.com/store/apps/details?id=co.brookesoftware.mike.trumpbot) or by searching for TrumpBot.

### Web Messenger
A long long time after the hackathon, we eventually built a web version. We used Vue.js to create the application.
Try it out [here](http://trumpbot.ohmgeek.co.uk)
### TrumpBot API
#### GET /
Response: ```API Working```

This is just a test to determine whether the API is online.

#### GET /response
This will return a completely random sentence.

You can customise it by sending a parameter:
```
?q=<SENTENCE>
```

### Problems We Encountered
+ Tensorflow didn't seem to work, so after many hours of attempted (and failed) bug fixes, we switched from LSTM networks to simple Markov Chains.
+ Twitter has a limit on the number of tweets you can download. An alternative method of harvesting tweets was found.

### Dependencies
+ Python 3.5.2
+ Flask Python Package
+ Twython Python Package
+ h5py Python Package
+ scipy Python Package
+ Ngrok (temporary, for tunelling local server to the internet)
+ OhmGeek's fork of markov-sentence-generator (for generating the sentences)

### Running the bot
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

### Twilio
To use Twilio, you will need to create an account, and go through all the Twilio sign up procedure (including gettting a phone number).

Once you have done this, go to the phone.py script and enter the URI of the main bot server.

```
$ python3 phone.py
```
This will run the phone server. Then enter the URI of the phone server in the section called 'Web Hooks' on Twilio.

## License
This project is distributed under the MIT License. Feel free to adapt these components for another project!
