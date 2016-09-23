from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from fortune.imagelist import *
from fortune.models import Fortune

import random

def cleanAphorism(f):
	return str(f).replace('\n', '<br>').replace('\t', '&nbsp;' * 4)

def smallPic(url):
	# u is a string that is the url to the image, i.e. 'http://asdfasf/asdfasf/foo_b.jpg'
	# For explanation see
	# http://www.flickr.com/services/api/misc.urls.html
	return url.replace('b.jpg', 'n.jpg')

def randomKeyword():
	l = ['book', 'dancing', 'europe', 'tea', 'coffee', 'family']
	return random.choice(l)

# Create your views here.

def index(request):
	rn = random.randint(0, 14334)
	aphorism = Fortune.objects.filter(id = rn)[0].aphorism
	aphorism = cleanAphorism(aphorism)
	img_url, img_author, img_title = findAnImageFromFlickrWithKeyword(randomKeyword())
	pic = smallPic(img_url)
	t = get_template('fortune_index.html')
	html = t.render(Context({'aphorism':aphorism, 'imgurl':pic}))
	return HttpResponse(html)

def short(request):
	l = Fortune.objects.filter(size__lt = 140)
	rn = random.randint(0, len(l))
	aphorism = l[rn].aphorism
	return HttpResponse(aphorism)

def startrek(request):
	l = Fortune.objects.filter(filename = 'startrek')
	rn = random.randint(0, len(l))
	aphorism = l[rn].aphorism
	return HttpResponse(aphorism)

def detail(request, request_id):
	if int(request_id) > 14334:
		request_id = 42
	f = Fortune.objects.filter(id = request_id)[0]
	return HttpResponse(f.aphorism)
