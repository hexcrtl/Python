#!/usr/bin/python3

import requests

post_file =  open('post.raw','r')
post_data= post_file.read()

headers = {'content-type': 'application/x-www-form-urlencoded'}
url = (input("enter url"(str))
r= requests.post("gooogle.com", data=post_data,headers=headers)
print (r.text)
~                
