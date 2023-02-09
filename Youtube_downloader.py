import os
from os import path
from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy import *
from moviepy.editor import VideoFileClip
import shutil
from pathlib import Path
import re
from pytube import Playlist
import moviepy.editor as mp
import tkinter as tk
import eyed3


#functions
def select_path():
    #allows user to select a path
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title("Downloading...")
    #download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move to selected directory
    shutil.move(mp4_video, user_path)
    screen.title("Download completed")

def download_file_mp3():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title("Downloading...")
    #download video
    mp3_audio = YouTube(get_link).streams.get_lowest_resolution().download()
    vid_clip = VideoFileClip(mp3_audio)
    #getting name
    full_file_name = os.path.basename(mp3_audio)
    file_name = Path(full_file_name).stem
    #converting
    screen.title("Converting...")
    mp3_converted = f'{file_name}.mp3'
    audio_clip = vid_clip.audio
    audio_clip.write_audiofile(mp3_converted)
    #getting metadata
    if var1.get() == 1:
        channel_name = YouTube(get_link).author
        substring = " - Topic"
        if substring in channel_name: #delitig " - Topic"
            channel_name = channel_name.replace(" - Topic", "")
        #modifying artist
        audioFile = eyed3.load(mp3_converted)
        audioFile.tag.artist = channel_name
        audioFile.tag.save()
    #move to selected directory, delete mp4 file
    shutil.move(mp3_converted, user_path)
    audio_clip.close()
    vid_clip.close()
    os.remove(full_file_name)
    
    screen.title("Download completed")

def download_playlist():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title("Downloading...")
    #get url for download
    playlist = Playlist(get_link)
    #creating folder
    main_dir = user_path + "\Playlist"
    if os.path.exists(main_dir):
        print("Error: Playlist folder already exists")
    else:
        os.mkdir(main_dir,mode = 0o666)
        videos_num = len(playlist.video_urls)
    #download playlist
    n=0
    for url in playlist:
        YouTube(url).streams.get_lowest_resolution().download(main_dir)
        screen.title("Downloading...    " + "/" + str(videos_num))
        for file in os.listdir(main_dir):
            if re.search('mp4', file):
                mp4_path = os.path.join(main_dir,file)
                mp3_path = os.path.join(main_dir,os.path.splitext(file)[0]+'.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                #counting
                for files in os.listdir(main_dir):
                    if files.endswith('.mp4'):
                        n=n+1
                screen.title("Downloading...    " + str(n) + "/" + str(videos_num))
                print("Downloading...    " + str(n) + "/" + str(videos_num))
                #remove mp4
                os.remove(mp4_path)
                #adding metadata
                if var1.get() == 1:
                    full_file_name = os.path.basename(mp3_path)
                    file_name = Path(full_file_name).stem
                    channel_name = YouTube(url).author
                    substring = " - Topic"
                    if substring in channel_name:
                        channel_name = channel_name.replace(" - Topic", "")
                    audioFile = eyed3.load(mp3_path)
                    audioFile.tag.artist = channel_name
                    audioFile.tag.title = file_name
                    audioFile.tag.save()    

    screen.title("Download complited")


screen = Tk()
#tkinter logo
screen.iconbitmap("icon_logo.ico")
title = screen.title("YouTube Downloader")
canvas = Canvas(screen, width=500, height=500, bg="#414141")
canvas.pack()


#YouTube logo
logo_img = PhotoImage(file="yt_dark.png")
logo_img = logo_img.subsample(13, 13)
canvas.create_image(250, 80, image = logo_img)


#link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Insert download link: ", font=("Arial", 17), bg="#414141")

#Select Path for saving path
path_label = Label(screen, text="Choose a storage location", font=("Arial", 15), bg="#414141")
select_btn = Button(screen, text="Choose", bg="#D6D6D6", command=select_path)
#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 310, window=select_btn)


#Add widgets to window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)


#Download button mp4
download_btn1 = Button(screen, text="DOWNLOAD MP4", bg="#D6D6D6", command=download_file)
#add to canvas
canvas.create_window(250, 390, window=download_btn1)

#Download button mp3
download_btn2 = Button(screen, text="DOWNLOAD MP3", bg="#D6D6D6", command=download_file_mp3)
#add to canvas
canvas.create_window(250, 420, window=download_btn2)

#Download button playlist
download_btn3 = Button(screen, text="DOWNLOAD PLAYLIST", bg="#D6D6D6", command=download_playlist)
#add to canvas
canvas.create_window(250, 450, window=download_btn3)

#Mp3 checkbox
var1 = IntVar()
c1 = Checkbutton(screen, text="Add metadata", bg="#D6D6D6", variable=var1)
c1.pack()
#add to canvas
canvas.create_window(250, 480, window=c1)

screen.mainloop()
