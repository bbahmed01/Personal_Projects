import os 
from pytube import Playlist
from art import *

tprint("BBA")
print('Developed by Boubaker Corp.')
print('------------------------------------')

#function to get the links from from one or multiple playlists
def get_playlist(playlists):
    urls = []
    #get links from playlists
    for playlist in playlists:
        playlist_urls = Playlist(playlist)

        for url in playlist_urls:
            urls.append(url)
    
    return urls

#main code

plink = input("enter the playlist link: ")


#takes one or multiple playlist links
playlists = []
playlists.append(plink)

#execute the previously defined function
pl_urls = get_playlist(playlists)

#save the urls in a file
with open("./linkslist.txt","w") as f:
    for url in pl_urls:
        print(url)
        f.write(url+'\n')

print("video links saved successfully"+ os.getcwd())
input()