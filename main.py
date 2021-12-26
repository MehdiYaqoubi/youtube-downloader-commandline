import os
import time

from pytube import YouTube
from pytube.cli import on_progress
from progress.spinner import MoonSpinner


def file_path():
    """
    The path to save the downloaded video. In the absence of a directory,
    the desired path will be created
    :return: download_path
    """
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    return download_path


def progress_bar():
    """
    After running the program the progress bar runs
    """
    spinner = MoonSpinner('Loading... ')
    finished = False
    while not finished:
        for i in range(100):
            time.sleep(0.02)
            spinner.next()
        finished = True
    spinner.finish()


def start():
    # input from the user
    video_url = input("Enter YouTube URL Here: ")

    print("Select Quality: ")
    quality_list = {
        '1': '144p',
        '2': '360p',
        '3': '480p',
        '4': '720p',
        '5': 'Audio Only'
    }
    # Showing resolution options
    for i, q in quality_list.items():
        print(f"{i}.{q}")
    chosen = input("\nEnter the number you've chosen: ")

    yt = YouTube(video_url, on_progress_callback=on_progress)
    video = yt.streams.get_highest_resolution()
    # Gets the title of the video
    title = yt.title
    print(f"\nTitle: {title}")
    # Gets the size of the video
    file_size = video.filesize
    print(f"File size: {file_size // 1048576} M")
    # Select option 5 to download only Audio from the YouTube
    try:
        if chosen != '5':
            video = yt.streams.filter(
                mime_type="video/mp4", res=quality_list[chosen],
                progressive=True
            ).first()
            video.download(output_path=file_path())

        elif chosen == '5':
            audio = yt.streams.filter(type="audio").first()
            audio.download(output_path=file_path())

        print("\nDownload Completed!")

    except Exception as es:
        print(f"Error due to {es}")


if __name__ == "__main__":
    progress_bar()
    start()
