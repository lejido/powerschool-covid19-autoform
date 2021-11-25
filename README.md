# Powerschool COVID-19 Symptoms Form Automator 

Tired of filling out the Powerschool COVID-19 symptoms form when you're healthy? WE AUTOMATE NOW

## Setup 

Only for MacOS for now, but will make a guide for Windows users as well. 

### MacOS 

You will need python on your system. 

MacOS users can use [https://brew.sh/](Homebrew) to [https://formulae.brew.sh/formula/python@3.9](install python).

Once python is installed, install the necessary packages: 

pip3 install selenium 

pip3 install python-dotenv


In the directory, make a .env file with USERNAME, PASSWORD, and CONSENT_NAME. USERNAME should be the account username, PASSWORD should be the account password, and CONSENT_NAME should be the account owner's name. Example: 

```
USERNAME="JohnDoe5"
PASSWORD="DefinatelyMyPassword123"
CONSENT_NAME="John Doe"
```


## TODO 

