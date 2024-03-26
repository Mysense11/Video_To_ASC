from pytube import YouTube
import os
import re


def download_youtube_video(url):
    yt = YouTube(url)

    title = re.sub('[\/:*@?"<>|]', "", yt.title)

    video_filter = yt.streams.filter(
        mime_type="video/mp4", res="720p", progressive=False
    )
    print("======= Video Download Start ========")
    video_filter.first().download(filename=f"{title}.mp4")

    print("======= Sound Download Start ========")
    sound_filter = yt.streams.filter(mime_type="audio/mp4", abr="128kbps")
    sound_filter.first().download(filename=f"{title}.m4a")

    return title



