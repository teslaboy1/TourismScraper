from flask import Flask,render_template
app = Flask(__name__)
from bs4 import BeautifulSoup
import requests

url = 'https://hotelfornepal.com/'
req = requests.get(url)
bsObj = BeautifulSoup(req.text,'lxml')

hotel = bsObj.findAll('article',class_ = 'accommodation_item one-fourth')


hotel_store = []
for each_hotel in hotel:
    hotty =[]
    hotty.append(each_hotel.h3.text)
    hotty.append(each_hotel.find(class_="address").text)
    hotty.append(each_hotel.img['src'])
    
    hotel_store.append(hotty)
       


destinations = bsObj.findAll('article',class_='location_item one-fourth')
destination = []

for each_dest in destinations:
    dest=[]
    dest.append(each_dest.a['title'])
    # dest.append(each_dest.h4.text)
    dest.append(each_dest.span.text)
    dest.append(each_dest.img['src'])
    destination.append(dest)



tours = bsObj.findAll('article',class_ = 'tour_item one-fourth')

tour_res = []


for each_tour in tours:
    tour_add = []
    tour_add.append(each_tour.h3.text)
    tour_add.append(each_tour.span.text)
    tour_add.append(each_tour.img['src'])
    tour_res.append(tour_add)

airlines = bsObj.findAll('article',class_ = 'cruise_item one-fourth')

planes = []

for each_plane in airlines:
    plane_inst = []
    plane_inst.append(each_plane.h3.text)
    plane_inst.append(each_plane.img['src'])
    planes.append(plane_inst)

car = bsObj.findAll('article',class_ = 'car_rental_item one-fourth')

truck = []
bar = []

for each_car in car:
    
    truck.append(each_car.h3.text)
    bar.append(each_car.em.text)
    

petrol = bsObj.findAll('div',class_ = 'text-wrap car_type')
tire = []
for lux in petrol:
    tire.append(lux.text)


@app.route('/')
def home():
    return render_template('home.html',hotel_store=hotel_store,
    destination=destination,
    tour_res = tour_res,
    planes = planes,
    tire = tire,
    truck = truck,
    bar=bar)

if __name__ == '__main__':
    app.run(debug=True)

