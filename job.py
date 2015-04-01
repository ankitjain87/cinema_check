#!/usr/bin/python


import urllib2
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP

MAIL_SERVER = ''
PORT = 25
FROM_EMAIL = ''
TO_EMAIL = ''
SUBJECT = ''
CONTENT = ''
URL = 'http://in.bookmyshow.com/getJSData/?file=/data/js/GetShowDatesByEvent_ET00020475_BANG.js&cmd=GETSHOWDATESBYEVENTWEB&ec=ET00020475&rc=BANG&_=1427793974767&_=1427793974767'


def sendmail(sender, receivers, subject, content):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receivers

    msg.preamble = 'Multipart message.\n'

    part = MIMEText(content)
    msg.attach(part)

    mailer = SMTP(MAIL_SERVER, PORT)
    mailer.sendmail(msg['From'], msg['To'].split(', '), msg.as_string())
    mailer.close()


response = urllib2.urlopen(URL)
data = response.read()

if 'CXBL' in data:  //CXBL => Cinemax Bellandur
    sendmail(FROM_EMAIL, TO_EMAIL, SUBJECT, CONTENT)

