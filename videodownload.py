from pytube import YouTube

input_url = input("Enter the url of the video you want to download: ")
# youtube downloader with pytube
def download_video(url, path):
    yt = YouTube(url)
    yt.streams.first().download(path)
    print("Downloaded the video successfully!")
