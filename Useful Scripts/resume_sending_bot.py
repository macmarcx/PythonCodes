import requests
import re
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print('Automation started...')
time.sleep(2)
print('')

print('Accessing the INDEED website for job vacancies...')
time.sleep(3)
print('')

print('Starting email capture...')
print('')
print('')

x = 0
list = []

with open('email_list.txt', 'w') as arquivo:  # CREATING THE TXT FILE TO SAVE EMAILS

    for i in range(0, 70):  # NUMBER OF PAGES TO CROSS
        url = (f"https://ie.indeed.com/jobs?q=cyber+security&l=Dublin%2C+County+Dublin&vjk=763c418d4f40d108{x}")

        html_page = requests.get(url)
        html_source = html_page.text

        emails = re.findall('\w+@\w+\.{1}\w+', html_source)

        for email in emails:
            if email in list:
                pass

            elif email == '0252655a41544fd28ae41f8b8ff36917@sentry.indeed':
                pass

            else:
                list.append(email)
                print(email)
                print(email, file=arquivo)

        x = x + 10

valor = len(list)
print('')
print('')
print(f'{valor} captured and saved emails...')
time.sleep(2)
print('')

print('Accessing the email list...')
time.sleep(2)
print('')

# DON'T FORGET TO ACTIVATE 'AUTHORIZE LESS SECURE PROGRAMS' IN YOUR GMAIL ACCOUNT!
# GMAIL ONLY AUTHORIZES 500 EMAILS PER DAY...DO NOT ABUSE IT!

with open('curriculo.txt', 'r', encoding='utf-8') as arquivo2:
    resume = arquivo2.read()

print('Starting to send emails to companies...')
time.sleep(2)
print('')
print('.')
print('.')
print('.')
print('')

for i in range(1, 501):  # NUMBER OF EMAILS TO SEND
    fromaddr = "youremail@gmail.com"  # ENTER YOUR EMAIL HERE
    toaddr = list[i]
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "RESUME"

    body = resume

    msg.attach(MIMEText(body, 'plain'))

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "password-of-your-gmail")  # ENTER YOUR GMAIL PASSWORD HERE
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

    print(f'Email {i}/500 Sent with success!')
    # time.sleep(30)

print('')
print('.')
print('.')
print('.')
print('')
print('Automation completed successfully!')