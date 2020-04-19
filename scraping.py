#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import argparse
from tabulate import tabulate
from printy import printy

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
    def toList(self):
        return [self.__name, self.__brand, self.__price]
    def toDict(self):
        return {
            "name": self.__name,
            "brand": self.__brand,
            "price": self.__price
        }
    def getName(self):
        return self.__name
    def getBrand(self):
        return self.__brand
    def getPrice(self):
        return self.__price
    def setName(self,name):
        self.__name = name
    def setBrand(self,brand):
        self.__brand = brand
    def setPrice(self,price):
        self.__price = price

def printTable(products):
    products_list = []
    i = 0
    for product in products:
        products_list.append([str(i)] + product.toList())
        i += 1
    printy(tabulate(products_list, headers=["","Name","brand","price"],tablefmt="fancy_grid"),"r")

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
        printTable(products)

main()