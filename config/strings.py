import json

# def gettex(msg):
default_lang = 'strings-en'
cache_string = {}

def loader():
    global cache_string
    with open(f'strings/{default_lang}.json','r') as const:
        cache_string = json.load(const)
        print(cache_string)

def gettex(name):
    return cache_string[name]

loader()