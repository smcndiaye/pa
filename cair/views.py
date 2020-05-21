from django.shortcuts import render

# Create your views here.
import requests 

while True:
    r = requests.get('https://dslweb.herokuapp.com/')
    print(r.status_code)
