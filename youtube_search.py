import urllib.request
from bs4 import BeautifulSoup

def YouTube_Search(textToSearch):
	query = urllib.parse.quote(textToSearch)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib.request.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	return 'https://www.youtube.com/embed/' + soup.find(attrs={'class':'yt-uix-tile-link'})['href'][9:]

print(YouTube_Search('Du Hast'))
