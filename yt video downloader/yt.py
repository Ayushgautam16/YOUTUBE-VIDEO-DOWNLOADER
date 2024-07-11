import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory()
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    url = input("Enter the YouTube video URL: ")
    save_path = open_file_dialog()
    download_video(url, save_path)
