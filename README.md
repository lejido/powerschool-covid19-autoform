# Powerschool COVID-19 Symptoms Form Automator 

Tired of filling out the Powerschool COVID-19 symptoms form when you're healthy? WE AUTOMATE NOW

## Setup 

Only for Google Chrome on MacOS for now. Will add options for other operating systems and browsers later. 

### Google Chrome on MacOS 

#### →Dependencies 
You will need chromedriver and python3. 
You will also need selenium and python-dotenv: 

```
pip3 install selenium 
pip3 install python-dotenv
```

#### →Running the script 
Clone the repo, then make an .env file in the directory. 
Example .env file: 

```
USERNAME="JohnDoe5"
PASSWORD="DefinatelyMyPassword123"
CONSENT_NAME="John Doe"
```

Run ```python3 main.py```. Check your form logs after 20-30 seconds to see if the script worked.

#### →Running the script hands-free every morning (still under development)  

MacOS comes with [cron](https://en.wikipedia.org/wiki/Cron) which we will use to schedule this script to run every morning. 

Find the path to the directory that contains your python packages. It's most likely ```/usr/local/lib/python3.9/site-packages```. 

Find the path to script. 

In terminal, enter ```crontab -e```. Enter ```* * * * * PYTHONPATH=<PATH TO PYTHON PACKAGES HERE> python3 <PATH TO SCRIPT HERE>``` 

For example: ```* * * * * PYTHONPATH=/usr/local/lib/python3.9/site-packages python3 powerschool-covid19-autoform-main/main.py```. Note that the path to your script should exclude your home directory. If you placed the folder inside your home directory, the previous example should work. 

Once you exit, you should see the mesasge ```crontab: installing new crontab```. At this point, you'll know if the scheduling is working if at every minute, the script runs without errors. 

After verifying that it works, go back to ```crontab -e``` and replace ```* * * * *``` with ```0 6 * * 1-5```. Now the script should run at 6AM every Monday-Friday. You can change the times and learn more about crontab [here](https://crontab.guru/). 

Lastly, feel free to uncomment the line ```chrome_options.add_argument("--headless")``` in main.py once everything works. Doing this will prevent the Google Chrome window from appearing on screen. The script will still run (visual aspects are removed only). 

Keep in mind that your device must be on for the cron job to actually do anything. If you set the script to run at 5AM, and you're usually sleeping at that time, one thing you can do is schedule your Mac to wake up right before the script runs. More on that [here](https://support.apple.com/en-za/guide/mac-help/mchlp2266/mac). 

**PLEASE DO NOT FORGET TO UPDATE THE FORM IF YOU DO SHOW ANY SYMPTOMS. If at any time you don't want the script to run by itself anymore, enter in terminal ```crontab -e``` and just remove the crontab.**

## TODO
- Implement notification system 
  - https://www.quora.com/How-can-I-send-a-push-notification-to-my-Android-phone-with-a-Python-script
  - https://notify.run/
- Option for users to manually run script remotely (maybe from phone?) 
- Options for differnt OS and browsers 
- Easier setup for non-technical users

