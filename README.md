# BirthdayWisher
This Python script sends personalized birthday wishes to your friends via email. Just store their names, email addresses, and birthdays in a simple CSV file, and the script takes care of the rest — checking daily for matches and sending out cheerful messages automatically.  Perfect for never missing a friend's birthday again!

# 🎉 Birthday Wisher Bot (Python)

Never forget a birthday again! This Python script reads a list of friends with their birthdays and sends them a personalized email when the day arrives.

## 🧰 Features

- 📅 Daily birthday check
- 📬 Sends personalized emails with custom messages
- ✅ Simple CSV format for contacts
- 💌 Uses SMTP to send real emails

## 📁 Folder Structure

📂 birthday_wisher/ ├── birthdays.csv # Your list of friends and their birthdays ├── birthday_wisher.py # Main Python script ├── message_template.txt # Birthday message (with placeholders)

markdown
Copy
Edit

## 📦 Requirements

- Python 3.6+
- An email account (Gmail or SMTP-enabled)
- `smtplib` and `pandas` (install with `pip install pandas`)

## 📝 CSV Format

Your `birthdays.csv` should look like:

```csv
name,email,year,day,month
Alice,alice@example.com,2021,10,4
Bob,bob@example.com,1959,15,4
