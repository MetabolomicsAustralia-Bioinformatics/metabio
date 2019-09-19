# metabio

## Intro


* Currently served at: mastr-quant.bio21.unimelb.edu.au


## Setup

Local installation instructions for Ubuntu (tested on 18.04)
```
# activate env
source /path/to/venv/bin/activate

# pip3 install relevant python libraries
pip3 install -r requirements.txt

# Check django version, and to confirm that django was pip-installed
django-admin --version

```

### Server Setup

```
# Install mysql client
# For latest versions of debian/ubuntu (as of 2018), may need:
sudo apt-get install libmysqlclient-dev
sudo apt-get install default-libmysqlclient-dev # ubuntu/debian 2018

# MySQL server installation
sudo mysql_secure_installation
# set password as "root", or any other password you like. 
# be sure to update Django's settings.py file wth the password of your choice (line 96)

# login to mysql console as root
sudo mysql -u root -p

# Create database called 'backend' if it doesn't exist
CREATE DATABASE backend;

# Quit and restart mysql service
quit; # exit mysql console
service mysql restart
```


### Start server

```
# Run from wherever `manage.py` lives 
python3 manage.py runserver
```

### Teardown

Deactivate environment

```
deactivate
```