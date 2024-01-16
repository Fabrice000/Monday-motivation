import smtplib
import datetime as dt
import random

current_day = dt.datetime.now()
day_of_week = current_day.weekday()
if day_of_week == 0:
    with open("quotes.txt") as quote_file:
        quotes = quote_file.readlines()
        quote_to_send = random.choice(quotes)
        print(quote_to_send)
    my_email = "YOUR EMAIL"
    # notice that here you will specify your host name mine is "stmp.gmail.com" so i put it here
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password="YOUR PASSWORD")
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:Monday motivation\n\n{quote_to_send}".encode('utf-8'))
    






