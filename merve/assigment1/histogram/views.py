from django.shortcuts import render
from django.http import HttpResponse
from assigment1.settings import BASE_DIR
import os

def frequency(request,filename):
	try:
		fileroot= os.path.join(os.path.dirname(BASE_DIR),"static","templates",filename)
		filee = open(fileroot)
		hdict={}
		for word in filee.read().split(" "):
			if not hdict.has_key(word):
				hdict[word]=[]
			hdict[word].append(word)
		result = "Name: %s <br> Words: <br>" % filename
		for i in hdict:
			result += "%s: %d <br>"%(i,len(hdict[i]))
		return HttpResponse(result)
	except:
		return HttpResponse("There is no file named as %s" %filename)

