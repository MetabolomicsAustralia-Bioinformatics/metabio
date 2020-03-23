# MASTR-Quant

## Overview

Targeted analysis in mass spectrometry uses a calibration curve to compute the concentration of a substance, by comparison to a set of samples of known concentration. This is canonically done by fitting a straight line of best fit, in a linear regression, to samples with known concentrations and abundance values. New samples with known abundance values but unknown concentrations can then be computed via simple linear interpolation using this fitted linear model.

MASTR-Quant is an open-source web application that allows users to calculate the concentration values of features in mass spectrometry data through visualizing and fitting calibration curves, based on a range of adjustable parameters, as well as instrument-related model-fitting options such as special treatment of internal standards, and background subtractions. The final output is downloadable as an Excel file with multiple sheets containing detailed results of the individual steps involved in the calculation process.

MASTR-Quant is being served live [here](mastr-quant.bio21.unimelb.edu.au).

## Statement of Need

MASTR-Quant provides an open-access, transparent way of calculating calibration curves, which would otherwise be inaccessible due to the need to utilize proprietary vendor software, which are usually only compatible with their respective mass spectrometry instruments as well. The methods used by MASTR-Quant are compatible across all vendors.

## Local Installation

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

Django is currently connected to a mysql backend database, with user root, and password root. These can be changed by changing the relevant parameters in settings.py (starting line 96).


1. Install mysql client if it's not already installed. Different OS's may have different clients. 

```
# For latest versions of debian/ubuntu (as of 2018), may need:
sudo apt-get install libmysqlclient-dev
sudo apt-get install default-libmysqlclient-dev # ubuntu/debian 2018
```

MySQL server installation:
```
sudo mysql_secure_installation
```

Set password to any password you like. Be sure to update Django's `settings.py` file wth the password of your choice (line 96). 

Now login the the `mysql` console as root to create the backend database, just called `backend`. `sudo` might be required the first time this is run:

```
sudo mysql -u root -p

CREATE DATABASE backend;
```

Now quit and restart the `mysql` service
```
quit; # exit mysql console
service mysql restart
```

Make intial migrations to update `backend` with classes from `models.py` Run this from the directory which manage.py lives in:
```
python3 manage.py makemigration
```

### Start server

Run from wherever `manage.py` lives:
```
python3 manage.py runserver
```

To deactivate environment:

```
deactivate
```

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
