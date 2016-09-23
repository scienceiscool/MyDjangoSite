from urllib.request import urlopen
from bs4 import BeautifulSoup
import random

def findAnImageFromFlickrWithKeyword(keyword):
  debug = False
  response = urlopen('http://api.flickr.com/services/feeds/photos_public.gne?tags=' + keyword + '&lang=en-us&format=rss_200').read( ).decode('utf-8')

  soup = BeautifulSoup(response, 'lxml')

  image_url_list = []

  for item in soup.find_all('item'):
    author_list = list(item.find_all('author'))
    media_list = list(item.find_all('media:content'))
    title_list = list(item.find_all('media:title'))
    if len(author_list) == len(media_list):
      for i in range(len(author_list)):
        image_url_list.append((media_list[i]['url'], author_list[i]['flickr:profile'], title_list[i].string))
  return random.choice(image_url_list)

def main( ):
  x = findAnImageFromFlickrWithKeyword('cat')
  print(x)

if __name__ == '__main__':
  main( )


