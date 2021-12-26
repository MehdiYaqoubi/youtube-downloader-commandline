from pytube import YouTube
from pytube.cli import on_progress


def start():
    # input from the user
    video_url = input("Enter YouTube URL Here: ")
    yt = YouTube(video_url, on_progress_callback=on_progress)
    video = yt.streams.get_highest_resolution()
    video.download()


if __name__ == "__main__":
    start()
