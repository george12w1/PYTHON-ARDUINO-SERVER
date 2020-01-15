from django.shortcuts import render
from django.http import HttpResponse
from .templates.grabber import Grabber
from .templates.connecter import Connection
from .forms import ContactForm
import json
from urllib.parse import urlparse
from urllib.parse import unquote

import uuid
from bs4 import BeautifulSoup
def returnCaractere(url):

    r = Grabber(url).returnPage()
    index = 0
    for e, x in enumerate(r.text):
        index += 1
    index -= 1
    return index


def hi(request,url):
    data = {}
    x = Connection().connection()
    collection = x["test"]["test"]
    #post1 = {"id":str(uuid.uuid4()),"name":"bill"}
    #post = {"_id":str(uuid.uuid4()),"url":"https://docs.google.com/spreadsheets/d/e/2PACX-1vTLGH01X3cdPQ8lqJSjXfY1i1jraieqDEEApPKxUpI0D3ZnuLYuwUYrKnxhHs1k4XBkFNM4rUr2tRko/pubhtml#","caractere":index}
    #exempluPost = {"id":str(uuid.uuid4()),"name":"bill","caractere":n,"url":url}
    #collection.insert_one(post)
    #collection.find({"_id":url})
    if collection.find({"_id":url}).count() :
        rc =returnCaractere(collection.find({"_id":url})[0]["url"])
        data["url"]=collection.find({"_id":url})[0]["url"]
        data["current_characters"]=rc
        data["initial_characters"]=collection.find({"_id":url})[0]["caractere"]
        if rc == collection.find({"_id":url})[0]["caractere"] :
            modified = "NO"
        else : modified = "YES"
        data["modified"]=modified
        json_data = json.dumps(data)
        return HttpResponse(json_data)
    else : return HttpResponse(404)
def form(request):
    form = ContactForm()
    return render(request,'DEMOAPP/hi.html',{"form":form})
def add(request):
    link = ""
    for e,x in enumerate(request):
        link  = str(x.decode())
        print(str(e) + "-"+ str(x))
    date = link.split("&")
    descriere = ""
    url=""
    if date.__len__() == 3 :
        descriere = date[1].split("=")[1]
        url = unquote(date[2].split("=")[1])
    x = Connection().connection()
    collection = x["test"]["test"]
    if collection.find({"url": url}).count():
        return  HttpResponse(collection.find({"url": url})[0]["_id"])
    else :
        myvar = str(uuid.uuid4())
        cars = returnCaractere(url)
        exempluPost = {"_id":myvar,"name":"bill","caractere":cars,"url":url,"descriere":descriere}
        collection.insert_one(exempluPost)
        return HttpResponse(myvar)