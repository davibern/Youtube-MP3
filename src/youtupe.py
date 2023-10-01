import os
import pytube
from googleapiclient.discovery import build

class Youtube:
    def __init__(self, api_key):
        self.api_key = api_key

    def download_video_audio_as_mp3(self, video_url, output_path):
        yt = pytube.YouTube(video_url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path=output_path)

        video_title = yt.title
        mp4_path = os.path.join(output_path, f"{video_title}.mp4")
        mp3_path = os.path.join(output_path, f"{video_title}.mp3")

        os.rename(mp4_path, mp3_path)
        
        print(yt.title)
        print(yt.author)
        print(yt.length)
        print(yt.thumbnail_url)
        print(yt.publish_date)

    
    def get_audio_info(self):
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        audio_info  = youtube.videos().list(part='snippet', id=self).execute()
        return audio_info
        