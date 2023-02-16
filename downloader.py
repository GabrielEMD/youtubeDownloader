import os
# importing the module
# import pytube.exceptions as exceptions
from pytube import YouTube, Playlist
from pathlib import Path

def mp4(link, lista):
    # where to save
    folder = "videos"
    try:
        os.mkdir(folder)
    except Exception:
        pass

    if lista == 0:
        # link of the video to be downloaded
        try:
            # object creation using YouTube
            # which was imported in the beginning
            youtubeObject = YouTube(link)
        except:
            print("Connection Error") #to handle exception
        try:
            youtubeObject = youtubeObject.streams.get_highest_resolution()
        except Exception:
            print(f"Error {Exception}")
        try:
            # downloading the video
            youtubeObject.download(folder)
        except:
            return "Error!"
        return 'Video descargado!'
    else:
        playlist = Playlist(link)
        x = len(playlist.video_urls)
            # downloading the video
        for video in playlist.video_urls:
            try:
                youtubeObject = YouTube(video)
            except Exception:
                print(f"error descarga {video}")
                x -= 1
                continue
            try:
                youtubeObject = youtubeObject.streams.get_highest_resolution()
            except Exception:
                print(f"error descarga {video}")
                x -= 1
                continue
            try:
                youtubeObject.download(folder)
            except Exception:
                print(f"error descarga {video}")
                x -= 1
                continue
        return f'{x} Videos descargados!'

def mp3(link, lista):
    # where to save
    folder = "musica"
    try:
        os.mkdir(folder)
    except Exception:
        pass
    if lista == 0:
        # link of the video to be downloaded
        try:
            # object creation using YouTube
            # which was imported in the beginning
            youtubeObject = YouTube(link)
        except:
            print("Connection Error") #to handle exception
        try:
            youtubeObject = youtubeObject.streams.filter(abr='160kbps').last()
        except Exception:
            return f"Error {Exception}"
        try:
            # downloading the video
            out_file = youtubeObject.download(folder)
            base, ext = os.path.splitext(out_file)
            new_file = Path(f'{base}.mp3')
            os.rename(out_file, new_file)
        except:
            return "Error!"
        return 'Canción descargada!'
    else:
        playlist = Playlist(link)
        x = len(playlist.video_urls)
        # downloading the video
        for video in playlist.video_urls:
            try:
                youtubeObject = YouTube(video)
            except Exception:
                print(f"error descarga {video}")
                x -= 1
                continue
            try:
                youtubeObject = youtubeObject.streams.filter(abr='160kbps').last()
            except Exception:
                print(f"error descarga {video}")
                x -= 1
                continue
            try:
                out_file = youtubeObject.download(folder)
                base, ext = os.path.splitext(out_file)
                new_file = Path(f'{base}.mp3')
                os.rename(out_file, new_file)
            except Exception:
                print(f"error descarga {video}")
                x -= 1
                continue
        return f'{x} Canciones descargados!'
