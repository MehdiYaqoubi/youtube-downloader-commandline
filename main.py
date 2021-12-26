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
    title = yt.title
    print(f"\nTitle: {title}")
    file_size = video.filesize
    print(f"File size: {file_size // 1048576} M")
    video.download(file_path())
    print(f"Your video will be saved to: {file_path()}")


if __name__ == "__main__":
    start()
