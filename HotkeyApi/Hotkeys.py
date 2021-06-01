import csv
from random import choice

DATA_FILE = "ShortcutData.csv"

fields = [] # should be ordered as program, category, hotkey, action description
hotkeys = []
categories = {}

def init():
    retrieve_hotkeys()
    retrieve_categories()
    print(categories)

def get_random_hotkey():
    return choice(hotkeys)

def get_all_programs():
    return list(categories.keys())

def get_categories(program):
    if program not in categories:
        raise ValueError("Unknown program")
    return categories[program]

def get_all_hotkeys_for_category(program, category):
    if program not in categories:
        raise ValueError("Unknown program")
    if category not in categories[program]:
        raise ValueError("Unknown category")

    hotkeys_returning = []
    for hotkey in hotkeys:
        if hotkey[fields[0]] == program and hotkey[fields[1]] == category:
            hotkeys_returning.append(hotkey)
    return hotkeys_returning

def retrieve_hotkeys():
    global fields
    with open(DATA_FILE,"r",encoding="utf-8") as data_file:
        data_reader = csv.reader(data_file)
        fields = next(data_reader)
        for row in data_reader:
            hotkey = {}
            for i,value in enumerate(row):
                hotkey[fields[i]] = value
            hotkeys.append(hotkey)

def retrieve_categories():
    program_key = fields[0]
    category_key = fields[1]
    for hotkey in hotkeys:
        if hotkey[program_key] not in categories:
            categories[hotkey[program_key]] = []
        if hotkey[category_key] not in categories[hotkey[program_key]]:
            categories[hotkey[program_key]].append(hotkey[category_key])

init()