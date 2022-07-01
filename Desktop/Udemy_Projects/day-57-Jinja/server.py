from flask import Flask, render_template
import requests
import random
from datetime import date

app=Flask(__name__)

@app.route("/")
def home():
    today_date=date.today().year
    name="Efthimios Vlahos"
    random_number=random.randint(1,10)
    return render_template("index.html",num = random_number,current_year=today_date,my_name=name)

@app.route("/guess/<name>")
def guess(name):
    gender_url=f"https://api.genderize.io?name={name}"
    gend_response = requests.get(gender_url)
    gender_data= gend_response.json()
    gender= gender_data["gender"]
    age_url=f"https://api.agify.io?name={name}"
    agify_response=requests.get(age_url)
    age_data=agify_response.json()
    age=age_data["age"]
    return render_template("guess.html",person_name=name, gender=gender,age=age)

@app.route("/blog/<num>")
def get_blog(num):
    url_blog=" https://api.npoint.io/c790b4d5cab58020d391"
    blog_response=requests.get(url_blog)
    all_posts=blog_response.json()
    render_template("blog.html", posts=all_posts)





if __name__=="__main__":
    app.run(debug=True)