import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

class RealTimeCurrencyConverter():
    def __init__(self, url):
        self.data = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
        self.currencies = self.data['rates']
        print(self.currencies['TRY'])

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount


        if from_currency != 'USD' :
            amount = amount / self.currencies[from_currency]



        amount = round(amount * self.currencies[to_currency], 4)
        return amount


url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = RealTimeCurrencyConverter(url)
print(converter.convert('TRY','NZD',100))

def __init__(self, converter):
    tk.Tk.__init__(self)
    self.title = 'Currency Converter'
    self.currency_converter = converter

