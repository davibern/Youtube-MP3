import os
from src.youtupe import Youtube

# Clave de la API de YouTube
api_key = os.getenv('TOKEN_YOUTUBE')

if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=wNMZRTROYuw'
    output_path = './downloads'

    youtube = Youtube(api_key)
    youtube.download_video_audio_as_mp3(video_url, output_path)
    print("Audio del video descargado como MP3 con éxito!")
