import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3


url = "http://pizzafunk30.ru/pizza/"  #{count}  для множества страниц

base_url = "http://pizzafunk30.ru"


resource = requests.get(url)

html = resource.text

soup = BeautifulSoup(html, "html.parser")

container = soup.select_one("div.row")

products = container.find_all("div")

urls = []
for product in products:
    url = product.select_one("a")
    urls.append(urls)

dannie = []
for url in urls:
    html = resource.text
    soup = BeautifulSoup(html, "html.parser")
    name = soup.select_one("h3").text
    price = soup.select_one("span")
    img = soup.select_one("img").text
    info = str(soup.select_one("p.ingredients"))
    dannie.append((name, price, info, img))

for r in dannie:
    print(r)
    break




#
#     for i in data:
#         card_url = "https://scrapingclub.com" + i.find("a").get("href")
#         yield card_url
#
# def array():
#     for card_url in get_url():
#
#         resource = requests.get(card_url, headers=headers)
#         sleep(3)
#
#         soup = BeautifulSoup(resource.text, "lxml")
#
#         data = soup.find("div", class_="card")
#         name = data.find("h3", class_="card-title")
#         price = data.find("h4", class_="card-price")
#         text = data.find("p", class_="card-description")
#         url_img = data.find("img", class_="card-img-top img-fluid")
#         print(data, name, price, text, url_img)
#
#
#     conn = sqlite3.connect(mydata.db)
#
#     cursor = conn.cursor()
#     cursor.executemany("INSERT INTO fastfud VALUES (?, ?, ?, ?)", data)
#     cunn.commit()
#     conn.close()





        # url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")
        # name = data.find("h4", class_="card-title").text.replace("\n", "")
        # price = data.find("h5").text
        #
        #
        # print(name + "\n" + price + "\n" + url_img + "\n\n")

