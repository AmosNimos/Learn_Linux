#!/usr/bin/env python3
# importing the libraries
from bs4 import BeautifulSoup
import requests
import os
import webbrowser
import dmenu
import sys
import wget
import datetime

#----------------------------------------------------------------------------------#
# ARGUMENTS                                                                        #
#----------------------------------------------------------------------------------#
pageSelect=False
episodeSelect=False;
download=False;
if(len(sys.argv)>0):
	for i in range(len(sys.argv)):
		arg = str(sys.argv[i])
		if arg == "-p":
			pageSelect=True
		if arg == "-e":
			episodeSelect=True
		if arg == "-d":
			download=True

#----------------------------------------------------------------------------------#
# FUNCTIONS                                                                        #
#----------------------------------------------------------------------------------#
def genList(size,start,befor,after):
	tempList=[]
	if start>0 and befor != None:
		tempList.append(str(befor))
	for x in range(size):
		tempList.append(str(x+start))
	if after != None:
		tempList.append(str(after))
	return tempList

#----------------------------------------------------------------------------------#
# Optional                                                                         #
#----------------------------------------------------------------------------------#
page=0
if pageSelect == True:
	pagesIndex=0
	loop=True
	menuSize=6
	more=">"
	less="<"
	while loop==True:
		options=genList(menuSize,pagesIndex,less,more)
		choice = dmenu.show(options, prompt='select page')
		if str(choice) == less:
			pagesIndex-=menuSize
		elif str(choice) == more:
			pagesIndex+=menuSize
		else: 
			loop=False
			page=int(choice)

#----------------------------------------------------------------------------------#
# SCAN                                                                             #
#----------------------------------------------------------------------------------#
## scan anime kisa for new anime
url="https://animekisa.tv/latest/"+str(page)

#check if page alredy loaded
if(page==0):
	date = datetime.datetime.now()
	now = date.strftime("%d")+'-'+date.strftime("%w")
	html = open(os.path.join(sys.path[0], "data/date.txt"), "r")
	lastDate = html.readline()
	if lastDate != now:
		html.close()
		html = open(os.path.join(sys.path[0], "data/date.txt"), "w")
		html.write(now)
		html.close()
		html_content = requests.get(url).text
		html = open(os.path.join(sys.path[0], "data/animekisa.html"), "w")
		html.write(html_content)
		html.close()
	else:
		html = open(os.path.join(sys.path[0], "data/animekisa.html"), "r")
		html_content=html.read()
		html.close()
else :
	html_content = requests.get(url).text

frontPage = BeautifulSoup(html_content, "lxml")
links = frontPage.find_all("a", {"class": "an"})
animes = str(links).split('href="/')
animes.pop(0)
n=0
nEpisode=0
last=""
names=[]
#store anime name in a list
for index in animes:
	name = str(animes[n]).split('"', 1)[0]
	if name != last and "episode-" not in name:
		last = name
		#temporary until dmenu
		#print(" "+str(nEpisode)+": "+name)
		nEpisode+=1
		names.append(name)
	n+=1

#----------------------------------------------------------------------------------#
# OPTIONS                                                                          #
#----------------------------------------------------------------------------------#
choice = dmenu.show(names, prompt='select anime')

#----------------------------------------------------------------------------------#
# SCAN                                                                             #
#----------------------------------------------------------------------------------#
## scan anime kisa for available anime episode
url="https://animekisa.tv/"+str(choice)
html_content = requests.get(url).text
animePage = BeautifulSoup(html_content, "lxml")
links = animePage.find_all("div", {"class": "centerv"})
episodes =  str(links).split('"')
episode=[]

for index in episodes:
	if "<" in index and ">" in index:
		isIndex=''
		for s in index: 
			if s.isdigit():
				isIndex += str(s);
		if isIndex != '':
			episode.append(isIndex)

#----------------------------------------------------------------------------------#
# Optional                                                                         #
#----------------------------------------------------------------------------------#
# use dmenu here instead to select the episode
selectedEpisode=episode[0]
if episodeSelect == True:
	firstEpisode = 1
	options=genList(int(episode[0]),firstEpisode,None,None)
	selectedEpisode = dmenu.show(options, prompt='select episode')

## scan anime kisa for download link
url="https://animekisa.tv/"+str(choice)+"-episode-"+str(selectedEpisode)
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
js = soup.find_all('script')

index = 6
VidStreaming = ""
jss = str(js[index]).split(';')
for lines in jss:
	if "var VidStreaming = " in lines:
		VidStreaming = str(lines).split('"')

## scan download page for download
# example "https://gogo-play.net/load.php?id=MTUyNTE4&title=Beastars+2nd+Season&typesub=SUB&sub=&cover=Y292ZXIvYmVhc3RhcnMtMm5kLXNlYXNvbi5wbmc="

url=str(VidStreaming[1])
if download==True:
	##to download
	html_content = requests.get(url).text
	downPage = BeautifulSoup(html_content, "lxml")
	js = downPage.find_all('script')
	links = []
	for index in js:
		if "https://gogo-play.net/download?id=" in str(index):
			links=str(index)
	links = links.split('"')
	for index in links:
		if "https://gogo-play.net/download?id=" in str(index):
			url=str(index)
	#to download video directly
	html_content = requests.get(url).text
	downVideo = BeautifulSoup(html_content, "lxml")
	url=""
	loop=0
	finalRes=""
	res=["(360P - mp4)","(480P - mp4)","(720P - mp4)","(1080P - mp4)","(HDP - mp4)"]
	while url=="" and loop<len(res):
		for index in downVideo.find_all('a', href=True):
			text = str(index.get_text())
			#print(text[-12:])
			if text[-12:] == res[loop]:
				url = index['href']
				finalRes=res[loop]
		loop+=1
	if url == "":
		print("no download available.")
		exit()
	#finalRes = str(finalRes)[:4]
	#finalRes = str(finalRes)[-3:]
	#videoName=str(choice)+'-episode-'+str(selectedEpisode)+'-'+finalRes+'p.mp4'
	#videoFile='~/anime/'
	#download_file(url,videoFile+videoName)
	#print("downloading"+videoName+"please wait")
	#myfile = requests.get(url)
	#open(videoFile+videoName+'.mp4', 'wb').write(myfile.content)
	#wget.download(url, videoFile+videoName+'.mp4')
	# example https://gogo-play.net/download?id=MTUwMzA3&title=Tatoeba+Last+Dungeon+Mae+no+Mura+no+Shounen+ga+Joban+no+Machi+de+Kurasu+Youna+Monogatari&typesub=SUB
webbrowser.open(str(url))

## scan downlink for actual download link




#rawj = soup.find_all('script')
#rawj = rawj.split('var VidStreaming = ')
#print(str(rawj))
