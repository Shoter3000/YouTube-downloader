# YOUTUBE DOWNLOADER

## Introduction
A Python script for downloading and converting YouTube videos into mp3 audio files. The script makes use of the following libraries: `os`, `tkinter`, `pytube`, `moviepy`, `shutil`, `pathlib`, and `eyed3`.

## Libraries
- os
- tkinter
- pytube
- moviepy
- shutil
- pathlib
- eyed3

## Functions

### select_path()
This function allows the user to select a path where the downloaded files will be saved.

### download_file()
This function is used to download YouTube videos in their original format. It first gets the user's link for the video, and then it gets the selected path. It uses the `pytube` library to download the video and saves it in the selected path using the `shutil` library.

### download_file_mp3()
This function is used to download and convert YouTube videos into mp3 audio files. It first gets the user's link for the video, and then it gets the selected path. It uses the `pytube` library to download the video and converts it into mp3 format using the `moviepy` library. It then saves the mp3 audio file in the selected path using the `shutil` library. It also has an option to add metadata to the mp3 file using the `eyed3` library.

### download_playlist()
This function is used to download and convert a YouTube playlist into mp3 audio files. It first gets the user's link for the playlist, and then it gets the selected path. It uses the `pytube` library to download the playlist and converts the videos into mp3 format using the `moviepy` library. It then saves the mp3 audio files in a folder named "Playlist" in the selected path. It also has an option to add metadata to the mp3 files using the `eyed3` library.

## GUI
The script creates a GUI using the `tkinter` library for the user to enter the YouTube video or playlist link and select the path for saving the files. The GUI also has buttons for downloading the video or playlist in the original format or converting them into mp3 audio files.
