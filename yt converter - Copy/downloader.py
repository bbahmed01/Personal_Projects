import pafy
import sys
from yt_to_mp3 import *
from art import *

tprint('Yoda Converter')
print('welcome to the youtube -> mp3 converter!!')
answer = "9"
while answer != '0':
    answer = '9'
    print('choose one of the following choices please:')
    print('1 : to convert a video')

    print('2 : to convert a Playlist')

    print('3 : to see Credits')

    print('0 : to Quit')
    
    while ((answer != '1') and (answer != '2') and (answer != '3') and (answer != '0')):
        answer = input('enter your choice:')

    if answer == '2':
        f = open("./linkslist.txt","r")
        links = f.read()
        links = links.split('\n')


        for link in links:
            if link != '':
                Start_download(link)
    if answer == '1':
        link = input("enter the link of the video : ")
        Start_download(link)
    if answer == '3':
        tprint('BBA Corp.') 
        print('this app was created by Ben Boubaker Ahmed, mainly for his family and friends to download')
        print('music off of youtube')  
        print('if you want to report any bug(s) please e-mail him at bbahmed166@gmail.com')
        input()
    if answer == "0":
        quit


