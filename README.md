# League of Legends Predictor
 Predict the probability of winning a game after 10 minutes of playing a match.
 
## Getting Started
These instructions will allow you to run a bot on your locate machine where League of Legends is being played.

## Prerequisites

* Python 3+

## Installing

* download github repository

    * can use github link: 
    
https://github.com/Vakhshoori101/League-of-Legends-Predictor.git
    
    * can download as zip file
    
## Deployment

1. Run this snippet of code in the directory containing schedule_cron.py to add the League of Legends Bot:

```sudo python3 schedule_cron.py```

 Will then ask for the user's username for their computer account:
 
 ```Please enter your computer's username: (username) ```
 
 The bot is now added.
 
 2. Once a League of Legends match is started, the bot will wait for the ten and fifteen minute marker and create a text file called ```output.txt``` in the current directory containing the probabilty of winning the match.
 
 3. To remove the bot, run this sinpper in the directory containing remove_cron.py
 
 ```sudo python3 remove_cron.py```
 
  Will then ask for the user's username for their computer account:
 
 ```Please enter your computer's username: (username) ```
 
 The bot is now removed.
 
 
## Enjoy!
