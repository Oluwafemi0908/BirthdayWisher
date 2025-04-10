##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib
# 1. Update the birthdays.csv
birthdays = pd.read_csv('birthdays.csv')
celebrants = []
my_email = "oluwafemiakinode909@gmail.com"
password = "whrhbmyadrxqapie"
def pick_letter():
    num = random.randint(1,3)
    with open(f'letter_templates/letter_{num}.txt') as letters:
        letter = letters.read()
    return letter




# 2. Check if today matches a birthday in the birthdays.csv
def check_birthday():
    now = dt.datetime.now()
    month = now.month
    day = now.day
    for _, birthday in birthdays.iterrows():
        if birthday['month'] == month and birthday['day'] == day:
            celebrants.append(birthday.to_dict())
check_birthday()
print(celebrants)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for celebrant in celebrants:
    name = celebrant['name']
    message = pick_letter()
    edited = message.replace('[NAME]', name)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=celebrant['email'],
                            msg=f"Subject: Happy Birthday\n\n{edited}")

# 4. Send the letter generated in step 3 to that person's email address.




