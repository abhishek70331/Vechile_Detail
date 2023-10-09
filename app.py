from flask import Flask, request, render_template,jsonify
import requests

app = Flask(__name__)

@app.route('/')
@app.route("/index", methods=['GET','POST'])
def index():

    if request.method=="POST":
        num = request.form["num"]
        print(num)


        url = "https://rto-vehicle-details.p.rapidapi.com/"

        payload = { "vehicleId": num }
        headers = {
            "content-type": "application/json",
            "Content-Type": "application/json",
            "X-RapidAPI-Key": "b33d464979mshe3a8c07ccdc8295p173c96jsn8fd067383797",
            "X-RapidAPI-Host": "rto-vehicle-details.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.json())
        
        data = response.json()
        name = data['owner_name']
        car = data['brand_model']
        number = data['license_plate']
        address = data['permanent_address']
        register = data['registration_date']
        fuel = data['fuel_type']

        return render_template("index.html",name=name,car=car,number=number,address=address,register=register,fuel=fuel)
    return render_template("index.html")

@app.route("/home")
def home():

    return render_template("index.html")

if __name__ == '__main__':
   app.run()