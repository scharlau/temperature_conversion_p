# a temperature conversion app
from flask import Flask, render_template, request
app = Flask(__name__)

def convert(temp, option):
    if option == 'Fahrenheit':
        converted_t = (temp-32)*0.5556
    elif option == 'Celsius':
        converted_t = (temp * 9/5)+32
    return converted_t

@app.route('/', methods=["GET", "POST"])
def index():
    converted_t = None
    temp = None
    if request.method== "POST":
        temp = int(request.form["temp"])
        option = request.form["option"]
        converted_t = convert(temp, option)
    return render_template("index.html", converted_t=converted_t, temp=temp, option=option)
