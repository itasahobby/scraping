#!/usr/bin/python3

import requests
import webbrowser
from bs4 import BeautifulSoup
import argparse
from tabulate import tabulate
from printy import printy
from printy import inputy

def get_parser():
    parser = argparse.ArgumentParser(description="Scrape products from pccomponentes")
    parser.add_argument('-s',action="store", dest="search", help="Query to search from pccomponentes")
    parser.add_argument('-p',action="store_true", dest="print", help="Prints the results")
    parser.add_argument('-i',action="store_true", dest="interactive", help="Makes an interactive shell")
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
    def getUrl(self):
        return self.__url
    def getBrand(self):
        return self.__brand
    def getPrice(self):
        return self.__price
    def setName(self,name):
        self.__name = name
    def setUrl(self,url):
        self.__url = url
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

def open_link(products):
    val = inputy("Enter a product number to open: ","b")
    val_int = int(val)
    if (val_int > 0) or (val_int < len(products)):
        printy(f"Opening link {products[val_int].getUrl()}","y")
        webbrowser.open(products[val_int].getUrl())
        return True
    else:
        return False

def main():
    parser = get_parser()
    args = parser.parse_args()
    target = "https://www.pccomponentes.com" 
    if(args.search):
        target += "/buscar/?query=" + args.search
    products = scrape(target)
    if(args.print):
        printTable(products)
    if(args.interactive and args.print):
        open_link(products)

main()