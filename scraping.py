#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="Scrape products from pccomponentes")
    parser.add_argument('-s',action="store", dest="search", help="Query to search from pccomponentes")
    parser.add_argument('-p',action="store_true", dest="print", help="Prints the results")
    return parser



class Product:
    def __init__(self, name, url, brand, price):
        self.__name = name
        self.__url = url
        self.__brand = brand
        self.__price = price
    def print(self):
        print("Product: " + self.__name)
        print("Access the product in: " + self.__url)
        print("Made by " + self.__brand + " for " + self.__price)

def scrape(target):
    html = requests.get(target)
    soup = BeautifulSoup(html.content,"html.parser")
    products = list(map(lambda product: product.find("a"), soup.find_all("article")))
    products_parsed = list(map(lambda product: Product(product["data-name"],target + product["href"],product["data-brand"],product["data-price"]),products))
    return products_parsed

def main():
    parser = get_parser()
    args = parser.parse_args()
    target = "https://www.pccomponentes.com" 
    if(args.search):
        target += "/buscar/?query=" + args.search
    products = scrape(target)
    if(args.print):
        for product in products:
            product.print()    

main()