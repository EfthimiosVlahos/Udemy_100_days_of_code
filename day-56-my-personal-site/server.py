from flask import Flask,render_template

app=Flask(__name__) #creates flask application. () contains "name of current directory.
@app.route("/") #uses route decorator to target the home route
def home():
    return render_template('index.html')

#Whenever you create a flask app, 9/10 times we need to create it with a templates folder and a static folder
#Templates is where the "index.html" code goes (i.e. the HTML code)
#Static is where all the pics, videos, css files, or in general, static files goes








if __name__== "__main__":
    app.run(debug=True)
