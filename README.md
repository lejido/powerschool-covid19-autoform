# Powerschool COVID-19 Symptoms Form Automator 

Tired of filling out the Powerschool COVID-19 symptoms form when you're healthy? WE AUTOMATE NOW

## Setup 

Only for Google Chrome on MacOS for now. Will add options for other operating systems and browsers later. 

### Google Chrome on MacOS 

You will need python on your system. 

MacOS users can use [Homebrew](https://brew.sh/) to [install python](https://formulae.brew.sh/formula/python@3.9).

Once python is installed, install the necessary packages in terminal: 

```
pip3 install selenium 
pip3 install python-dotenv
```

In the directory containing the script, make an .env file with USERNAME, PASSWORD, and CONSENT_NAME. USERNAME should be the account username, PASSWORD should be the account password, and CONSENT_NAME should be the account owner's name. Example: 

```
USERNAME="JohnDoe5"
PASSWORD="DefinatelyMyPassword123"
CONSENT_NAME="John Doe"
```

Run ```python3 main.py``` in the directory. The script is working if: 
1. A Google Chrome window appears and opens Powerschool, 
2. Signs in, 
3. Goes to the proper form, 
4. Fills out the empty entries, 
5. Submits
with no issues. This process should take ~20-30 seconds.




## TODO 

