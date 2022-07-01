##################### Normal Starting Project ######################
import pandas
import smtplib
import datetime as dt
import random

date_of_birth= dt.datetime(year=1997,month=6,day=15, hour=4)


today=(date_of_birth.month,date_of_birth.day)


data=pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}



if today in birthdays_dict:
    letters=["letter_1.txt", "letter_2.txt","letter_3.txt"]
    with open(f"./letter_templates/{random.choice(letters)}") as file:
        letter_contents=file.read()
        birthday_person=birthdays_dict[today]["name"]
        updated_letter= letter_contents.replace("[NAME]",birthday_person)

        my_email = "vlahos89@gmail.com"
        password="Efthimios123!"

    with smtplib.SMTP("smtp.gmail.com") as connection: #Will close connection automatically after email sends
        connection.starttls() #Secures server
        connection.login(user=my_email, password=password) #login to email
        #Sends mail from my email to another email. Hello is subject and after \n\n is the body
        connection.sendmail(from_addr=my_email,
                                to_addrs="efthimios.vlahos@stonybrook.edu",
                                msg=f"Subject: Happy Birthday\n\n{updated_letter} ")



# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



