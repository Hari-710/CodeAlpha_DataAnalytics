import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/catalogue/page-{}.html"

data = []

for p in range(1, 51):
    url1 = url.format(p)
    response = requests.get(url=url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, 'lxml')

    book_list = soup.find_all("article", {"class":"product_pod"})

    if not book_list:
        break

    for book in book_list:
        title = book.h3.a['title']

        price = book.find("p",{"class":"price_color"}).text.replace("£","")
        price = float(price)

        availability = book.find("p", {"class":"instock availability"}).text.strip()

        rating_tag = book.find("p", {"class":"star-rating"})
        if rating_tag:
            ratings = rating_tag['class'][1]
            rating_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
            rating = rating_map.get(ratings,None)

        link = "https://books.toscrape.com/catalogue/" + book.h3.a['href']


        data.append([title, price, availability, rating, link])

df = pd.DataFrame(data, columns=["Title", "Price", "Availability", "Rating", "Link"])

df.to_csv("books_list.csv", index=False, encoding="utf-8-sig")

print(df.head())