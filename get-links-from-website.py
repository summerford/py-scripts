import urllib2
import re
import json


#connect to a URL
website = urllib2.urlopen('https://ec.europa.eu/commission/index_en')

#read html code
html = website.read()

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

print links

with open("links.txt", "w") as text_file:
    text_file.write("Links: %s" % links)
