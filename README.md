# metabio

# Overview

MASTR-Quant is an open-source, web-based software tool that allows users to calculate concentration values of features in mass spectrometry data through visualizing and defining calibration curves based on a range of adjustable parameters. 

* Currently served at: mastr-quant.bio21.unimelb.edu.au
* Sample data available in `/static/sample_input.csv`
* Built from Django v2.0 (tested with 2.0 and 2.2), app packaged as `metabioapp`. 

# Setup

Local installation instructions for Ubuntu (tested on 18.04)

```
# activate env
source /path/to/venv/bin/activate

# pip3 install relevant python libraries
pip3 install -r requirements.txt

# Check django version, to confirm that django was pip-installed
django-admin --version
```

### SQL-database Setup

Django is currently connected to a `mysql` backend database, with user `root`, and password `root`. These can be changed by changing the relevant parameters in `settings.py` (starting line 96). 

```
# Install mysql client if it's not already installed. Different OS's may have different clients. 
# For latest versions of debian/ubuntu (as of 2018), may need:
sudo apt-get install libmysqlclient-dev
sudo apt-get install default-libmysqlclient-dev # ubuntu/debian 2018

# MySQL server installation
sudo mysql_secure_installation
# set password as "root", or any other password you like. 
# be sure to update Django's settings.py file wth the password of your choice (line 96)

# login to mysql console as root
# sudo might be required the first time this is run
sudo mysql -u root -p

# Create database called 'backend' if it doesn't exist
CREATE DATABASE backend;

# Quit and restart mysql service
quit; # exit mysql console
service mysql restart

# Make intial migrations to update `backend` with classes from `models.py`
# Run this from the directory which manage.py lives in
python3 manage.py makemigration
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

## Licensing and References

* If you use this software, please cite:

* This app is released under a [GNU GPLv3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) license, which allows end users the freedom to study, share, distribute or modify this software for commercial and private use, with the restriction that any derivative work must be made open-source and distributed under the same license terms. 

* Contact: Dr. Vinod Narayana, vinod.narayana "at" unimelb.edu.au