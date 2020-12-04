from pytube import YouTube

url = "https://www.youtube.com/watch?v=URBSvqib0xw&ab_channel=Socratica"
yt = YouTube(url)
title = yt.title
streams = yt.streams.order_by("./youtube_downloader/downloads")
# print(title)
# streams = yt.streams.first().download()
print(streams)
