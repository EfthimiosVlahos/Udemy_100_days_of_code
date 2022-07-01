# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import json


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    password_letters=[random.choice(letters) for _ in range(nr_letters)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list=password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    text_with_password.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(*args):

    website= text_with_web.get()
    email=text_with_email.get()
    password=text_with_password.get()

    new_data={
        website: {
            "email": email,
            "password": password
        }

    }

    if len(text_with_web.get())==0 or len(text_with_password.get())==0:
        messagebox.showinfo(title="oops", message="Put something in momo")
    else:
        try:
            with open("data.json",mode="r") as data_file:
                #Reading old data
                data=json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                #Saving updated data
                json.dump(new_data, data_file,indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            text_with_web.delete(0,END)
            text_with_password.delete(0,END)


def find_password():

    website = text_with_web.get()
    try:
        with open("data.json","r") as data_file:
            data=json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message= "No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} file found")

# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas= Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1,row=0)

website_label= Label(text="Website:")
website_label.grid(column=0,row=1)

text_with_web= Entry(width=21)
text_with_web.grid(row=1,column=1)
text_with_web.focus()

search_button=Button(text="Search", command=find_password)
search_button.grid(column=2,row=1)

email_label= Label(text="Email/Username:")
email_label.grid(column=0,row=2)

text_with_email= Entry(width=35)
text_with_email.grid(row=2,column=1,columnspan=2)
text_with_email.insert(0, "vlahos89gmail.com")

password_label= Label(text="Password:")
password_label.grid(column=0,row=3)

text_with_password= Entry(width=21)
text_with_password.grid(row=3,column=1)

button_with_pass=Button(text="Generate Password", command=generate_password)
button_with_pass.grid(row=3,column=2)


add_label= Button(text="Add", width=36, command = save)
add_label.grid(column=1,row=4, columnspan=2)


















window.mainloop()