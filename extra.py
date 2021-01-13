from flask import Flask,render_template
app = Flask(__name__)
from bs4 import BeautifulSoup
import requests


url2 = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'

req2 = requests.get(url2)

bsObj2 = BeautifulSoup(req2.text,'lxml')

# hotel2 = bsObj2.findAll('td',class_ = 'titleColumn')
print(bsObj2)
# for smth in hotel2:
#     print(smth.a.text)
# preus = []
# for room in hotel:
#     seus = []
    
#     seus.append(room.a.text)
#     seus.append(room.find(class_ = 'property-review').text)
#     preus.append(seus)
   


# @app.route('/')
# def home2():
#     return render_template('home2.html',preus = preus)

# if __name__ == '__main__':
#     app.run(debug=True)

