import requests
from PyQt5.QtWidgets import *
import sys
from bs4 import BeautifulSoup
from pytube import YouTube
#copyright- abis (2017) (BIT MESRA-CSE-abisbaba1@gmail.com)
app = QApplication(sys.argv)
song, ok = QInputDialog.getText(None, "YouTube Downloader", "Enter the keyword to search :")
if ok==False:
    exit()
word_list = list(map(str, song.split(" ")))
got_song = ""
counts_ = 0;
for i in word_list:
    got_song += i
    counts_ += 1
    if counts_ != len(word_list):
        got_song += '+'
url = "https://www.youtube.com/results?search_query="
url += got_song

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
title = []
links = []
dic = {}
counts_ = 0
for link in soup.find_all('a', class_='yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link '):
    links.append(link.get("href"))
    title.append(link.text)
    dic[link.text] = counts_
    counts_ += 1
item, okPressed = QInputDialog.getItem(None, "Video Menu", "Select :", title, 0, False)
url1 = "https://www.youtube.com"
url1 += links[dic[item]]

Netlocation=url1

video = YouTube(url1)
quality = video.get_videos()
qual = []
choices = {}
counts_ = 0
for i in range(len(quality)):
    ss = quality[i].extension + " " + quality[i].resolution
    qual.append(ss)
    choices[ss] = counts_
    counts_ += 1

choice, ok = QInputDialog.getItem(None, "Resolutions Menu", "Select the Resolutions :", qual, 0, False)
path, entered = QInputDialog.getText(None, "Download Path", "Enter the path (Example:  /home/xyz/Downloads) :")
if entered==False:
     exit()
download = QMessageBox.question(None, "Download Manager", "Do you want to Start download to ->"+path,
                                QMessageBox.Yes | QMessageBox.No)
if download == QMessageBox.Yes:
    QMessageBox.question(None, "Download Manager", "Video downloading", QMessageBox.Ok)
    vi = video.get(quality[choices[choice]].extension, quality[choices[choice]].resolution)
    vi.download(path)
    QMessageBox.question(None, "Download Manager", "Download Complete", QMessageBox.Ok)

