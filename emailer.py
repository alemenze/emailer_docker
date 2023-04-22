"""Email sender for dockerfile

This script allows the docker file to send the email via an smtp based send. 
I used outlook as the easiest one to set up here, but you can customize as needed. 

The dockerfile command should send this as:
sender_email, sender_pw, recipient_email, email_subject, email_text
"""
import smtplib
import sys,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

opts=open('/app/.env','r')
opts=opts.readlines()
if "MAILSENDER" in opts[0].replace('\n',''):
    sender=str(opts[0].replace('\n','').split("=")[1].strip("'"))
else:
    print('Error in getting the MAILSENDER variable')

if "MAILPASSWORD" in opts[1].replace('\n',''):
    password=str(opts[1].replace('\n','').split("=")[1].strip("'"))
else:
    print('Error in getting the MAILSENDER variable')

def send_email(recipient,subject,body):
    msg=MIMEMultipart()
    msg['From']=sender
    msg['To']=recipient
    msg['Subject']=subject
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP('smtp.outlook.com', 587)
    server.starttls()
    server.login(sender, password)

    try:
        text = msg.as_string()
        server.sendmail(sender, recipient, text)
        
    except:
        print('Error')

    server.quit()

send_email(sys.argv[1],sys.argv[2],sys.argv[3])
