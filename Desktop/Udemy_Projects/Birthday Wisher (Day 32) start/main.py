import smtplib
import datetime as dt
import random

# my_email="vlahos89@gmail.com"
# password="Efthimios123!"
#
# with smtplib.SMTP("smtp.gmail.com") as connection: #Will close connection automatically after email sends
#     connection.starttls() #Secures server
#     connection.login(user=my_email, password=password) #login to email
#     #Sends mail from my email to another email. Hello is subject and after \n\n is the body
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="efthimios.vlahos@stonybrook.edu",
#                         msg="Subject: Hello\n\n This is the body ")


# now=dt.datetime.now()
# year=now.year
# month=now.month
# day_of_week=now.weekday()
# print(type(year))
#
# date_of_birth= dt.datetime(year=1997,month=6,day=15, hour=4)
# print(date_of_birth)

# with open("quotes.txt") as file:
#     quotes=file.readlines()
#
# now=dt.datetime.now()
# day_of_week=now.weekday()
# random_quote=random.choice(quotes)
# print(random_quote)
#
# my_email="vlahos89@gmail.com"
# password="Efthimios123!"
#
# if day_of_week==3:
#     with smtplib.SMTP("smtp.gmail.com") as connection: #Will close connection automatically after email sends
#         connection.starttls() #Secures server
#         connection.login(user=my_email, password=password) #login to email
#         #Sends mail from my email to another email. Hello is subject and after \n\n is the body
#         connection.sendmail(from_addr=my_email,
#                             to_addrs="efthimios.vlahos@stonybrook.edu",
#                             msg=f"Subject: Motivational quote!\n\n {random_quote} ")


