import yt_dlp
import os

link = input("Enter the YouTube URL: ")

downloads_folder = os.path.join(os.path.expanduser('~'), "downloads")

if not os.path.exists(downloads_folder):
    os.makedirs(downloads_folder)

ydl_opts = {
    'quiet': True,
    'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=False)
        print(f"Title: {info_dict.get('title')}")
        print(f"Views: {info_dict.get('view_count')}")

        # Download highest resolution video
        ydl.download([link])

except Exception as e:
    print(f"An error occurred: {e}")


