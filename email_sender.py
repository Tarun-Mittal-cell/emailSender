import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Tarun Mittal'
email['to'] = 'mittal.tarun15@gmail.com'
email['subject'] = 'You won 1,00,000 dollars!'

email.set_content('I am a Python Master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email', 'password') # replace with your email and password
    smtp.send_message(email)
    print('All done ')