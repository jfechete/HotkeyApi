import csv
from random import choice

DATA_FILE = "ShortcutData.csv"
KEY_SEPERATOR = "+"

fields = [] # should be ordered as program, category, hotkey, action description
hotkeys = []
categories = {}
keys = []

def init():
    retrieve_hotkeys()
    retrieve_categories()
    retrieve_keys()

def get_random_hotkey():
    return choice(hotkeys)

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

def get_hotkeys_from_keys(keys_passed):
    for key_checking in keys_passed:
        if key_checking not in keys:
            raise ValueError("Invalid key passed")

    key_string = KEY_SEPERATOR.join(keys_passed)
    hotkeys_returning = []
    for hotkey in hotkeys:
        if hotkey[fields[2]].startswith(key_string):
            hotkeys_returning.append(hotkey)

    return hotkeys_returning


def get_all_programs():
    return list(categories.keys())

def get_categories(program):
    if program not in categories:
        raise ValueError("Unknown program")
    return categories[program]

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

def retrieve_keys():
    print(len(hotkeys))
    for hotkey in hotkeys:
        current_keys = hotkey[fields[2]].split(KEY_SEPERATOR)
        for key in current_keys:
            if key not in keys:
                keys.append(key)

init()