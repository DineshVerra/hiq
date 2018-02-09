import os
import requests
import webbrowser

from bs4 import BeautifulSoup
#from proxy import my_proxy


headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
song_name_raw = input('Please enter a song name: ')
song_name = song_name_raw.replace(' ','%20')
url = 'https://gaana.com/search/{}'.format(song_name)
source_code = requests.get(url,headers=headers,timeout=5)
plain_text = source_code.content
soup=BeautifulSoup(plain_text,"html.parser")
links = soup.find_all('a',{'class':'rt_arw'})
webbrowser.open(links[0]['href'])
