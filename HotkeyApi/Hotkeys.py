import csv
from random import choice

DATA_FILE = "ShortcutData.csv"

tips = []

def init():
    get_tips()

def random_tip():
    return choice(tips)

def get_tips():
  with open(DATA_FILE,"r",encoding="utf-8") as data_file:
    data_reader = csv.reader(data_file)
    fields = next(data_reader)
    for row in data_reader:
      tip = {}
      for i,value in enumerate(row):
        tip[fields[i]] = value
      tips.append(tip)

init()