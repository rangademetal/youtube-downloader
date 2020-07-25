from __future__ import unicode_literals
import youtube_dl
from moviepy.editor import *
import youtube_dl.utils


def downloaderMp4Youtube(link, path):
    ydl_opts = {'outtmpl': f'{path}'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    return path


def Convertor(filename_mp4, filename_mp3):
    videoClip = VideoFileClip(filename_mp4)
    audio = videoClip.audio
    audio.write_audiofile(filename_mp3)
    audio.close()
    videoClip.close()
    os.remove(filename_mp4)