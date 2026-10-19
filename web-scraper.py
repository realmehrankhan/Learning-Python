import requests
from bs4 import BeautifulSoup
import pandas as pd

all_books = []

for page_num in range(1, 6):
    url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    books_on_page = soup.find_all("article", class_="product_pod")

    for book in books_on_page:
        title = book.find("h3").find("a")["title"]
        price = float(book.find("p", class_="price_color").text.replace("£", ""))
        stock = book.find("p", class_="instock availability").text.strip()

        all_books.append({
            "Book Title": title,
            "Price": price,
            "Availability": stock,
            "Page Number": page_num
        })


df = pd.DataFrame(all_books)
df.to_csv("books.csv", index=False, encoding="utf-8-sig")

print(f"Done! Scraped {len(all_books)} books and saved to books.csv")
