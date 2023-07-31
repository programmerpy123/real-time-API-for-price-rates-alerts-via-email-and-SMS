import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_smtp_email(subject,rates):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'testdjangosendemail79@gmail.com'
    smtp_password = 'stptdptpcpizbfdz'

    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = 'amirrezamddi790@gmail.com'
    msg['To'] = 'mohammadaminmddi@gmail.com'
    msg['Subject'] = subject

    body = f'{rates}'
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, msg["To"], msg.as_string())