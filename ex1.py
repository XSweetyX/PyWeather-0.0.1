import requests
import json
from bs4 import BeautifulSoup
from flask import Flask, render_template
city_name = "Kursk"
city_id = 538560
appid="c7b4ab95b85e8084aeaf02614988b443" 
res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?appid={appid}&q=Kursk")
res1 =requests.get(f"http://api.openweathermap.org/data/2.5/forecast?&appid={appid}&q=Kursk")
data = res1.json()


app = Flask(__name__, template_folder = 'D:/1/Learn Python VSCode/.venv/templates',static_folder='D:/1/Learn Python VSCode/.venv/static')#главное пути к папкам tamplates и statics тут указать иначе ниего не заработает

#print(data)
#print("conditions:", data["weather"][0]["description"])
#for i in range(5):
#print("temp_min:", data['list'][0]['main'])
#print("temp_min:", data['list'][1]['main'])

dictor = dict()
for i in range(40):
        
    t = data['list'][i]['main']["temp"]
    tmax =data['list'][i]['main']['temp_max']
    date = data['list'][i]['dt_txt']
    weather = data['list'][i]['weather'][0]['main']
    
    
    dictor[i]=[f"{t-273:.2f}",f"{tmax-273:.2f}",weather,date]
    
    print(date)
    
    print(f"{t-273:.2f}",f"{tmax-273:.2f}",weather)
        
print(dictor)


    
    
@app.route('/')
def index():
    
    return render_template('page1.html', di=dictor)
if __name__=="__main__":
    app.run(debug=True) 
