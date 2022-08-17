import smtplib
import datetime as dt
import random

my_email = "my_email@gmail.com"
password = "password"
send_to = 'reciever`s_email@gmail.com'

now = dt.datetime.now()
week_day = now.weekday()
if week_day == 2:
    with open('quotes.txt') as data:
        file = data.readlines()
        random_word = random.choice(file)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        msg = f'Subject: Quote of the day\n\n{random_word}.'
        smtp.starttls()
        smtp.login(my_email, password)
        smtp.sendmail(from_addr=my_email, to_addrs=send_to, msg=msg)
