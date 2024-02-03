from bs4 import BeautifulSoup
import requests

print("What do you want to know the price of? (for multiple items seperate with comma)")
products = input("I want: ")
products = products.split(",")
for idx in range(len(products)):
    product = products[idx].split()
    product = "%20".join(product)
    products[idx] = product
print(products)
url = f"https://www.countdown.co.nz/shop/searchproducts?search={product}&sort=PriceAsc&inStockProductsOnly=true"
url = "https://www.countdown.co.nz/shop/searchproducts?search=chicken%20%20breast%20550g"
page = requests.get(url)
doc = BeautifulSoup(page, "html.parser")
print(doc)
page_text = doc.find(class_="productStrap-text")
page_text = doc.find(class_="heading--2 presentPrice ng-star-inserted")

print(page_text)
