from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle as pkl
import pandas as pd

app = Flask(__name__)
model=pkl.load(open('ml models\Car advisor\model.pkl','rb'))

car_dataset = pd.read_csv("ml models\Car advisor\CARS_1.csv")
used_car_dataset=pd.read_csv("ml models\Car advisor\dataset.csv")

# variables
Fuel_Type_Petrol=False
Fuel_Type_Diesel=False
Fuel_Type_LPG=False
Fuel_Type_Electric=False

Transmission_Manual=False


Owner_Type_Second=False
Owner_Type_Third=False
Owner_Type_Fourth=False

Manufacturer_BMW=False
Manufacturer_Volkswagen=False
Manufacturer_Hyundai=False
Manufacturer_Mahindra=False
Manufacturer_Maruti=False
Manufacturer_Audi=False
Manufacturer_Skoda=False
Manufacturer_Honda=False
Manufacturer_Ford=False
Manufacturer_Toyota=False
Manufacturer_Mercedes_Benz=False
Manufacturer_Tata=False
Manufacturer_Chevrolet=False
Manufacturer_Renault=False
Manufacturer_Jaguar=False
Manufacturer_Jeep=False
Manufacturer_Nissan=False
Manufacturer_Porsche=False
Manufacturer_Mini=False
Manufacturer_Land=False
Manufacturer_ISUZU=False
Manufacturer_Fiat=False
Manufacturer_Isuzu=False
Manufacturer_Mitsubishi=False
Manufacturer_Volvo=False
Manufacturer_Datsun=False
Manufacturer_Force=False
Manufacturer_Lamborghini=False



@app.route('/')
def newcar():
    return render_template('newcar.html')

@app.route('/sellcarprice')
def sellcarprice():
    return render_template('sellcarprice.html')

@app.route('/usedcar')
def usedCar():
    return render_template('usedcar.html')


@app.route('/', methods=['POST'])
def newcarpredict():
    rating = float(request.form.get('rating'))
    fuel = request.form.get('fuel')
    starting_price = float(request.form.get('starting_price'))
    ending_price = float(request.form.get('ending_price'))
    transmission = request.form.get('transmission')

    filtered_cars = car_dataset[
        (car_dataset['rating'] == rating) &
        (car_dataset['fuel_type'] == fuel) &
        (car_dataset['starting_price'] >= starting_price) &
        (car_dataset['ending_price'] <= ending_price) &
        (car_dataset['transmission_type'] == transmission)
    ]

    recommendations = filtered_cars.to_dict(orient='records')
    df = pd.DataFrame(recommendations)
    df.to_html('ml models\\Car advisor\\templates\\prediction.html')
    # used_car_recommendations = used_filtered_cars.to_dict(orient='records')
    # df = pd.DataFrame(recommendations )
    # print(recommendations)
    # recommendations=jsonify(recommendations)
    # keys=['Sr No.', 'car_name', 'reviews_count', 'fuel_type', 'engine_displacement', 'no_cylinder', 'seating_capacity', 'transmission_type', 'fuel_tank_capacity', 'body_type', 'rating', 'starting_price', 'ending_price', 'max_torque_nm', 'max_torque_rpm', 'max_power_bhp', 'max_power_rp']

    return render_template("prediction.html")

@app.route('/sellcarprice', methods=['POST'])
def sellcarpricepredict():
    year = float(request.form.get('year'))
    kilometers_driven=float(request.form.get('kilometers_driven'))
    mileage = float(request.form.get('mileage'))
    engine = float(request.form.get('engine'))
    power = float(request.form.get('power'))
    seats = float(request.form.get('seats'))
    brand=request.form.get('brand')
    fuel = request.form.get('fuel')
    owner_type=request.form.get('owner_type')
    transmission = request.form.get('transmission')


    if transmission=="automatic":
        Transmission_Manual=False
    
    else:
        Transmission_Manual=True
    

    if fuel=="Petrol":
        Fuel_Type_Petrol=True
        Fuel_Type_Diesel=False
        Fuel_Type_LPG=False
        Fuel_Type_Electric=False
    

    if fuel=="Diesel" :
        Fuel_Type_Petrol=False
        Fuel_Type_Diesel=True
        Fuel_Type_LPG=False
        Fuel_Type_Electric=False
    

    if fuel=="LPG" :
        Fuel_Type_Petrol=False
        Fuel_Type_Diesel=False
        Fuel_Type_LPG=True
        Fuel_Type_Electric=False
    

    if fuel=="Electric" :
        Fuel_Type_Petrol=False
        Fuel_Type_Diesel=False
        Fuel_Type_LPG=False
        Fuel_Type_Electric=True
    

    if owner_type=="Second" :
        Owner_Type_Second=True
        Owner_Type_Third=False
        Owner_Type_Fourth=False
    
    if owner_type=="Third" :
        Owner_Type_Second=False
        Owner_Type_Third=True
        Owner_Type_Fourth=False
    

    if owner_type=="Fourth" :
        Owner_Type_Second=False
        Owner_Type_Third=False
        Owner_Type_Fourth=True
    

    if brand=="BMW" :
        Manufacturer_BMW=True
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Volkswagen" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=True
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Hyundai" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=True
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Mahindra" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=True
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Maruti" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=True
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Audi" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=True
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Skoda" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=True
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Honda" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=True
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Ford" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=True
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Toyota" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=True
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Mercedes Benz" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=True
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Tata" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=True
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Chevrolet" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=True
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Renault" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=True
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Jaguar" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=True
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Jeep" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=True
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Nissan" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=True
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Porsche" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=True
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Mini" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=True
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Land" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=True
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="ISUZU" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=True
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Fiat" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=True
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Isuzu" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=True
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Mitsubishi" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=True
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if   brand=="Volvo" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=True
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Datsun" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=True
        Manufacturer_Force=False
        Manufacturer_Lamborghini=False
    
    if brand=="Force" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=True
        Manufacturer_Lamborghini=False
    
    if brand=="Lamborghini" :
        Manufacturer_BMW=False
        Manufacturer_Volkswagen=False
        Manufacturer_Hyundai=False
        Manufacturer_Mahindra=False
        Manufacturer_Maruti=False
        Manufacturer_Audi=False
        Manufacturer_Skoda=False
        Manufacturer_Honda=False
        Manufacturer_Ford=False
        Manufacturer_Toyota=False
        Manufacturer_Mercedes_Benz=False
        Manufacturer_Tata=False
        Manufacturer_Chevrolet=False
        Manufacturer_Renault=False
        Manufacturer_Jaguar=False
        Manufacturer_Jeep=False
        Manufacturer_Nissan=False
        Manufacturer_Porsche=False
        Manufacturer_Mini=False
        Manufacturer_Land=False
        Manufacturer_ISUZU=False
        Manufacturer_Fiat=False
        Manufacturer_Isuzu=False
        Manufacturer_Mitsubishi=False
        Manufacturer_Volvo=False
        Manufacturer_Datsun=False
        Manufacturer_Force=False
        Manufacturer_Lamborghini=True
    
    prediction=model.predict([[year, kilometers_driven, mileage, engine, power, seats, Manufacturer_BMW, Manufacturer_Chevrolet, Manufacturer_Datsun,
       Manufacturer_Fiat, Manufacturer_Force, Manufacturer_Ford,
       Manufacturer_Honda, Manufacturer_Hyundai, Manufacturer_ISUZU,
       Manufacturer_Isuzu, Manufacturer_Jaguar, Manufacturer_Jeep,
       Manufacturer_Lamborghini, Manufacturer_Land,
       Manufacturer_Mahindra, Manufacturer_Maruti,
       Manufacturer_Mercedes_Benz, Manufacturer_Mini,
       Manufacturer_Mitsubishi, Manufacturer_Nissan,
       Manufacturer_Porsche, Manufacturer_Renault, Manufacturer_Skoda,
       Manufacturer_Tata, Manufacturer_Toyota, Manufacturer_Volkswagen,
       Manufacturer_Volvo,Fuel_Type_Diesel, Fuel_Type_Electric,
       Fuel_Type_LPG, Fuel_Type_Petrol, Transmission_Manual, Owner_Type_Fourth, Owner_Type_Second, Owner_Type_Third]])

    return render_template('sellcarprice.html', recommendations=prediction)

@app.route('/usedcar', methods=['POST'])
def usedcarpredict():
    year = float(request.form.get('year'))
    kilometers_driven=float(request.form.get('kilometers_driven'))
    fuel = request.form.get('fuel')
    price = float(request.form.get('price'))
    owner_type=request.form.get('owner_type')
    transmission = request.form.get('transmission')

    used_filtered_cars = used_car_dataset[
        (used_car_dataset['Year'] >= year) &
        (used_car_dataset['Kilometers_Driven']<=kilometers_driven) &
        (used_car_dataset['Fuel_Type'] == fuel) &
        (used_car_dataset['Price'] <= price) &
        (used_car_dataset['Owner_Type'] <= owner_type) &
        (used_car_dataset['Transmission'] == transmission)
    ]

    used_car_recommendations = used_filtered_cars.to_dict(orient='records')
    df = pd.DataFrame(used_car_recommendations)
    df.to_html('ml models\\Car advisor\\templates\\prediction2.html')
    # used_car_recommendations = used_filtered_cars.to_dict(orient='records')
    return render_template('prediction2.html')


if __name__ == '__main__':
    app.run(debug=True)
