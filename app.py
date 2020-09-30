import base64
from PIL import Image
import io
import requests
import configparser
import pdb
from flask import Flask, render_template, request
import datetime
# import pdb;pdb.set_trace(

app = Flask(__name__)


@app.route('/')
def weather_dashboard():
    return render_template('home.html')


@app.route('/home', methods=['POST'])
def render_results():

    city_name = request.form["city"]
    data = get_weather_results(
        city_name, apikey='8d195f72c65049d55c801a702f095e96')

    weather = data['list'][0]['weather'][0]['description']
    temp = data['list'][0]['main']['temp']
    feels_like = data['list'][0]['main']['humidity']
    icon = data['list'][0]['weather'][0]['icon']
    location = data["city"]

    tomorrow_weather = data['list'][1]['weather'][0]['description']
    tomorrow_temp = data['list'][1]['main']['temp']
    tomorrow_feels_like = data['list'][1]['main']['humidity']
    tomorrow_location = data["city"]
    tomorrow_icon = data['list'][1]['weather'][0]['icon']
    # After Tomorrow

    aftertomorrow_weather = data['list'][2]['weather'][0]['description']
    aftertomorrow_temp = data['list'][2]['main']['temp']
    aftertomorrow_feels_like = data['list'][2]['main']['humidity']
    aftertomorrow_location = data["city"]
    aftertomorrow_icon = data['list'][2]['weather'][0]['icon']

    fourth_weather = data['list'][3]['weather'][0]['description']
    fourth_temp = data['list'][3]['main']['temp']
    fourth_feels_like = data['list'][3]['main']['humidity']
    fourth_location = data["city"]
    fourth_icon = data['list'][3]['weather'][0]['icon']

    dt = datetime.date.today()+datetime.timedelta(days=0)
    dt = dt.strftime("%A")

    dt1 = datetime.date.today()+datetime.timedelta(days=1)
    dt1 = dt1.strftime("%A")

    dt2 = datetime.date.today()+datetime.timedelta(days=2)
    dt2 = dt2.strftime("%A")

    dt3 = datetime.date.today()+datetime.timedelta(days=3)
    dt3 = dt3.strftime("%A")

    return render_template('home.html', location=location, temp=temp, weather=weather, feels_like=feels_like, city_name=city_name, tomorrow_weather=tomorrow_weather, tomorrow_feels_like=tomorrow_feels_like, tomorrow_location=tomorrow_location, tomorrow_temp=tomorrow_temp, aftertomorrow_weather=aftertomorrow_weather, aftertomorrow_temp=aftertomorrow_temp, aftertomorrow_location=aftertomorrow_location, aftertomorrow_feels_like=aftertomorrow_feels_like, icon=icon, tomorrow_icon=tomorrow_icon, aftertomorrow_icon=aftertomorrow_icon, fourth_feels_like=fourth_feels_like, fourth_icon=fourth_icon, fourth_location=fourth_location, fourth_temp=fourth_temp, fourth_weather=fourth_weather, dt=dt, dt1=dt1, dt2=dt2, dt3=dt3)


def get_weather_results(city, apikey):
    api_url = "http://api.openweathermap.org/data/2.5/forecast/?q={}&appid={}&units=imperial".format(
        city, apikey)
    r = requests.get(api_url)
    return r.json()


@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly

    return render_template('home.html')


print(get_weather_results("kabul", "8d195f72c65049d55c801a702f095e96"))


if __name__ == "__main__":
    app.run()
