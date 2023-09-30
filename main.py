import os
import pytube
from moviepy.editor import *

# Configura tu clave de API de YouTube
from googleapiclient.discovery import build
api_key = os.getenv('TOKEN_YOUTUBE')

# Función para descargar un video de YouTube en formato MP3
def download_video_as_mp3(video_url, output_path):
    yt = pytube.YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path=output_path)

# Función para obtener información de un video de YouTube
def get_video_info(video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    video_info = youtube.videos().list(part='snippet', id=video_id).execute()
    return video_info

# Ejemplo de uso
if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=LoSm6VkplJc'
    output_path = './downloads'

    download_video_as_mp3(video_url, output_path)
    print("Video descargado como MP3 con éxito!")
