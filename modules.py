import requests
import smtplib
import config as config


# Site status checking function
def search_items(finding):
    try:
        check_status = requests.get(finding, timeout=2)
        server_status = check_status.status_code    
    except Exception as e:
        server_status = "none"         
    print("Status code:", server_status)
    return server_status

# E-mail sending function
def sending_mail():   
    email_address = config.EMAIL_ADDRESS
    email_password = config.EMAIL_PASS
    sending_to = config.SENDING_TO
    monitoring_site = config.MONITOR_SITE
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email_address, email_password)
        subject = "Website", monitoring_site, "is not responding."
        body = "Message send by Python3 website monitoring script."
        msg = f"Subject: {subject}\n\n{body}"
        smtp.sendmail(email_address, sending_to, msg)
