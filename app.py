# Built by Brandon Waine
# Started 03/02/2022
# Bournemouth University | S5407535

from os import name
from flask import Flask, json, render_template, request
import _json
import urllib.request
from urllib.error import HTTPError

app = Flask(__name__)

@app.route('/results', methods=['POST'])
def results():
    api_key = "b73cd301703562ed9881a1879b5a27dd"
    city = request.form['city'].replace(" ", "+")
    #url = 'http://freegeoip.net/json/{}'.format(request.remote_addr)

    try:
        url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=' + api_key).read()
        data_list = json.loads(url)

        if not data_list:
            print("Cannot Find City")

        data_dict = {
            "city": str(data_list['name']),
            "temp": str(data_list['main']['temp']) + 'C'
        }

        return render_template('results.html', city=data_dict["city"], temp=data_dict["temp"])

    except HTTPError as err:
        print(err)
    

@app.route('/')
def dashboard():
    return render_template('home.html')