# Python3-website-monitor
Simple crash monitoring tool for websites. When website goes down you will receive email from added email address. Program recomemded to use with Linux Cron job by scheduling main.py.
### Usage
Dockerfile can be used for testing program in container. First add your own parameters inside the config.py file.
Open crontab  with command `crontab -e` and insert `* * * * * python3 main.py` at end of the crometab file. This will run python script every minute.

