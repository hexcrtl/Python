#!/usr/bin/python3

import requests

with open ('urls.txt') as f:
    urls = f.read().splitlines()


for url in urls:
    r = requests.get(url)
    print (url+ ":  "+ r.headers['server'])
