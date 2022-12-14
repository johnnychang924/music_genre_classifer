from pytube import Playlist
import subprocess

url = input("Please input playList url: ")
genre_name = input("Please input genre name: ")
pl = Playlist(url)
address = '.\music'
for video in pl.videos:
    mp3 = video.streams.filter(only_audio=True, file_extension='mp4')
    mp3 = mp3.order_by('abr').desc().first()
    print("downloading: ", video.title)
    mp3.download(address + '\\' + genre_name)
    path = address + '\\' + genre_name + '\\' + video.title
    subprocess.run(f'ffmpeg -i "{path}.mp4" "{path}.mp3"',shell=True, capture_output=True)