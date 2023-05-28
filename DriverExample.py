#pip instll bs4, requests,lxml,selenium
import requests

from bs4 import BeautifulSoup
from selenium import webdriver
#response = requests.get('https://yandex.ru/pogoda/kursk?lat=51.730848&lon=36.193015')  # проверяем успешен ли запрос?
#print(response.text)  # выводим полученный ответ на экран
#это пример не очень качественного кода с долгим выполнением
#данный код запускает драйвер хрома из-за чего происходит фактически программный поиск содержимого
website ='https://yandex.ru/pogoda/kursk?lat=51.730848&lon=36.193015'
driver = webdriver.Chrome("D:\1\Learn Python VSCode\.venv\Drivers\chromedriver.exe")
driver.get(website) 
html = driver.page_source
bs = BeautifulSoup(html,"html.parser")

temp = bs.find('span', 'temp__value temp__value_with-unit')
print(temp.text)
#иногда из-за динамики обновления содержимого страници мы не можем просто вытащить значения с html кода - для этого нужно целиком прогрузить страницу