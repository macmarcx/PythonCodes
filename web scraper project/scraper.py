import requests
import csv
from bs4 import BeautifulSoup

# URL of the website you want to scrape
URL = "http://books.toscrape.com/"

# Headers to mirror a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

def fetch_page(url):
    response = requests.get(url, headers=HEADERS)
    return response.text

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = []

    for item in soup.find_all('div', class_='product-item'):
        name = item.find('h2', class_='product-title').text.strip()
        price = item.find('span', class_='price').text.strip()
        products.append({
            'name': name,
            'price': price
        })
    return products

def save_to_csv(products):
    with open('products.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'price'])
        writer.writeheader()
        for product in products:
            writer.writerow(product)

def main():
    html = fetch_page(URL)
    products = parse_page(html)
    save_to_csv(products)
    print("Data saved to products.csv")

if __name__ == "__main__":
    main()
