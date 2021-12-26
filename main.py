import os

from pytube import YouTube
from pytube.cli import on_progress


def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    return download_path


def start():
    # input from the user
    video_url = input("Enter YouTube URL Here: ")
    yt = YouTube(video_url, on_progress_callback=on_progress)
    video = yt.streams.get_highest_resolution()
    video.download(file_path())


if __name__ == "__main__":
    start()
