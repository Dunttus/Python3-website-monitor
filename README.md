# Python3-website-monitor
Simple crash monitoring tool for websites. When the website goes down you will receive an email from an added email address. Program recommended to use with Linux Cron job by scheduling main.py.
### Requirements
* Working internet connection
* Python 3.8
    + Python3 requests
### Usage
Start by adding your own parameters inside the config.py file. Dockerfile included with github repository can be used for testing programs but recommended running as Linux cron job. Open crontab  with command `crontab -e` and insert `*/20 * * * * python3 main.py` at the end of the crontab file. Using absolute paths in crontab for python3 and the main.py file is recommended. This will run this website-monitor script every 20 minutes.
