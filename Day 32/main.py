from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = 'mrende@gmail.com'
MY_PASSWORD = '123456'

today_tuple = (datetime.now().month, datetime.now().day)

data = pandas.read_csv('Day 32/birthdays.csv')

new_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in new_dict:
    birthday_person = new_dict[today_tuple]
    file_path = f"Day 32/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person['name'])
        print(contents)

    with smtplib.SMTP('smpt.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person['email'],
        msg=f"Subject:Happy Birthday!\n\n\{contents}")


