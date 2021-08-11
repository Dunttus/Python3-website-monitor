import time
import modules as modules
import config as config


set_file = config.LOG_FILE
monitor_site = config.MONITOR_SITE
print("Connecting to: " + monitor_site)
search_results = modules.search_items(monitor_site)

def main():    
    if search_results == True:
        print(time.strftime("%d/%m/%y %X"), ": Request to ", monitor_site, " succeeded and server is responding.\n")
        log_file = open(set_file,"a")
        warning_text = (time.strftime("%d/%m/%y %X"), ": Request to ", monitor_site, " succeeded and server is responding.\n")
        adding_logs = log_file.writelines(warning_text)
        log_file.close()
    else:
        print(time.strftime("%X %x"), ": No response from ", monitor_site, " sending warning email.\n")
        log_file = open(set_file,"a")
        warning_text = (time.strftime("%d/%m/%y %X"), ": No response from ", monitor_site, " sending warning email.\n")
        adding_logs = log_file.writelines(warning_text)
        log_file.close()
        modules.sending_mail()

if __name__ == "__main__":
    main()

