from flask import Flask
app = Flask(__name__) #creates app from Flask class with required input name. Flask checks that this is the current file
                        # where the app code is located
# print(__name__) #When a Python module or package is imported, __name__ is set to the module’s name.
#                 # Usually, this is the name of the Python file itself without the .py extension
#
# @app.route("/") #when the user anvigates to our URL, they want to see the home page ('/') and show them hello world.This is called a python Decorator.
# #Decorators give add. functionality to an already existing function
# def hello_world():
#     return '<h1 style="text-align: center">Hello, World!</h1>' \
#            '<p> This is a paragraph. </p>' \
#            '<img src="https://media.giphy.com/media/blZEimpBW4K4M/giphy.gif">'
# @app.route("/bye") #decorator function that lives inside an app object inside the Flask class
# def bye():
#     return "Bye"
# def make_bold(function):
#     def wrapper():
#         return "<b>" + function() + "</b>"
#     return wrapper
#
# def make_emphasis(function):
#     def wrapper():
#         return "<em>" + function() + "</em>"
#     return wrapper
#
# def make_underlined(function):
#     def wrapper():
#         return "<u>" + function() + "</u>"
#     return wrapper
# @app.route("/username/<name>") #You can add variable sections to a URL (creating variable inside URL) by marking sections with <variable_name>.Your function then receives the <variable_name> as a keyword argument
# def greet(name):
#     return f"Hello {name}!"
#
# if __name__ == "__main__": #if this is the case, we are running hello.py
#     app.run(debug=True) #does the same thing as in the terminal (flask run). Debug=True Turns on Debug mode.

#flask notes:
#pip allows us to install python packages from Pypi
#To run the application you can either use the flask command or python’s -m switch with Flask.
# Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable
#$ export FLASK_APP=hello.py
#$ flask run
#* Running on http://127.0.0.1:5000/

#terminal notes:
#terminal==command line==shell
#there are 2 types of shells: GUI and CLI
#kernel= actual program that interfaces with hardware
#shell refers to the UI i.e. user interaction with computer
#address of terminal is determined right before the prompt (%), ~
#pwd (print working directory) tells us where we are in our file path
#ls (list) will list all files and folders at your current working directory
#pwd and ls are useful for finding things out or displaying things
#We can also use the terminal to move around in our computer using the cd command (change directory)
#mkdir creates a new folder/directory by: mkdir "name"
#to create a file in the new directory, we type: touch "main.py".
#if we wanted to delete that file all we have to do is type: rm main.py
#cd .. takes us one step up to the parent folder, which in my case is the Desktop
#to delete a folder we type: rm -rf Test (example in my case)


#Python Decorator notes:

## ********Day 54 Start**********
## Functions can have inputs/functionality/output
# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1 / n2
#
# ##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
#
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
# result = calculate(add, 2, 3)
# print(result)
#
# ##Functions can be nested in other functions
#
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     nested_function()
#
# outer_function()
#
# ## Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#
# inner_function = outer_function() #returns nested function w/o parenthesis
# inner_function() #activates nested_function by adding parentheis to end essentially
#
# #By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
# #A decorator function is just another function that wraps another function and gives that function additional functionality.
# ## Simple Python Decorator Functions
# import time
#
# def delay_decorator(function): #Decorator function
#     def wrapper_function():
#         time.sleep(2)
#         #Do something before
#         function()
#         function()
#         #Do something after
#     return wrapper_function
#
# @delay_decorator #calls decorator function which in this case is delay_decorator. Decorates the function below with a decorator function
# def say_hello():
#     print("Hello")
#
# #With the @ syntactic sugar
# @delay_decorator
# def say_bye():
#     print("Bye")
#
# #Without the @ syntactic sugar
# def say_greeting():
#     print("How are you?")
# decorated_function = delay_decorator(say_greeting) #same thing as the syntactic sugar above
# decorated_function()


## ********Day 55 Start**********

## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)


