# Powerschool COVID-19 Symptoms Form Automator 

Tired of filling out the Powerschool COVID-19 symptoms form when you're healthy? WE AUTOMATE NOW

## Setup 

Only for Google Chrome on MacOS for now. Will add options for other operating systems and browsers later. 

### Google Chrome on MacOS 

#### Getting the script to work 
You will need python on your system. 

MacOS users can use [Homebrew](https://brew.sh/) to [install python](https://formulae.brew.sh/formula/python@3.9).

Once python is installed, install the necessary packages in terminal: 

```
pip3 install selenium 
pip3 install python-dotenv
```

You also need to [get chromedriver](https://formulae.brew.sh/cask/chromedriver). Same process as installing python with homebrew. 

Download the zip of this repository and unzip it. I recommend you to put the folder inside your home directory. 

In the directory containing the script, make an .env file with USERNAME, PASSWORD, and CONSENT_NAME. USERNAME should be the account username, PASSWORD should be the account password, and CONSENT_NAME should be the account owner's name. Example: 

```
USERNAME="JohnDoe5"
PASSWORD="DefinatelyMyPassword123"
CONSENT_NAME="John Doe"
```

Run ```python3 main.py``` in the directory. The script is working if: 

1. A Google Chrome window appears and opens Powerschool, 
2. It signs in, 
3. Goes to the proper form, 
4. Fills out the empty entries, 
5. Submits

with no issues. This process should take ~20-30 seconds.

#### Running the script hands-free every morning 

MacOS comes with [cron](https://en.wikipedia.org/wiki/Cron) which we will use to schedule this script to run every morning. 

Find the path to the directory that contains your python packages. It's most likely ```/usr/local/lib/python3.9/site-packages```. 

Find the path to script. 

In terminal, enter ```crontab -e```. Enter ```* * * * * PYTHONPATH=<PATH TO PYTHON PACKAGES HERE> python3 <PATH TO SCRIPT HERE>``` 

For example: ```* * * * * PYTHONPATH=/usr/local/lib/python3.9/site-packages python3 powerschool-covid19-autoform-main/main.py```. Note that the path to your script should exclude your home directory. If you placed the folder inside your home directory, the previous example should work. 

Once you exit, you should see the mesasge ```crontab: installing new crontab```. At this point, you'll know if the scheduling is working if at every minute, the script runs without errors. 

After verifying that it works, go back to ```crontab -e``` and replace ```* * * * *``` with ```0 6 * * 1-5```. Now the script should run at 6AM every Monday-Friday. You can change the times and learn more about crontab [here](https://crontab.guru/). 

Lastly, feel free to uncomment the line ```chrome_options.add_argument("--headless")``` in main.py once everything works. Doing this will prevent the Google Chrome window from appearing on screen. The script will still run (visual aspects are removed only). 

Keep in mind that your device must be on for the cron job to actually do anything. If you set the script to run at 5AM, and you're usually sleeping at that time, one thing you can do is schedule your Mac to wake up right before the script runs. More on that [here](https://support.apple.com/en-za/guide/mac-help/mchlp2266/mac). 

**PLEASE DO NOT FORGET TO UPDATE THE FORM IF YOU DO SHOW ANY SYMPTOMS. If at any time you don't want the script by itself anymore, enter in terminal ```crontab -e``` and just remove the crontab.**

## TODO 
- Option for users to manually run script remotely (maybe from phone?) 
- Notifying users of errors that occured if script failed to run completely (email? text?) 
- Notifying users of successful runs 
- Options for differnt OS and browsers 
- Better README 
- Easier setup for non-technical users
- OK PATH TO DIRECTORIES MAY BE DIFF BUT IDK IF THAT WILL BE A PROBLEM ATM 

