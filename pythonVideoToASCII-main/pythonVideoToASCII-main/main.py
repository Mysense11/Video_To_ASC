from image_to_ascii import image_to_ascii, numpy_to_image
from video_to_frame import extract_video_frame
from donwload_youtube import download_youtube_video
import os
import time
import json
import re
from pydub import AudioSegment
import pygame

# FFmpeg와 FFprobe의 경로 설정
os.environ["IMAGEIO_FFMPEG_EXE"] = "C:\\path\\to\\ffmpeg.exe"
os.environ["FFPROBE_PATH"] = "C:\\path\\to\\ffprobe.exe"

# pygame 초기화
pygame.mixer.init()

with open("settings.json") as f:
    data = json.load(f)
    FRAME = data["FRAME"]

youtube_url = input("Input Youtube Video URL (Recommend 1 minute or less) > ")

try:
    title = download_youtube_video(youtube_url)

    print("Extracting Frame...")
    frames = extract_video_frame(f"{title}.mp4")
    ascii_frames = []

    print("Loading...")

    audio = AudioSegment.from_file(f"{title}.m4a", format="m4a")
    audio.export(f"{title}.wav", format="wav")

    # 오디오 속도를 조절
    sound = AudioSegment.from_file(f"{title}.wav")
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * 0.8)
    })
    sound_with_altered_frame_rate.export(f"{title}_altered.wav", format="wav")

    audio = pygame.mixer.Sound(f"{title}_altered.wav")

    for frame in frames:
        img = numpy_to_image(frame)
        ascii_frames.append(image_to_ascii(img))

    for i, frame in enumerate(ascii_frames):
        os.system("cls")  # 혹은 "clear" (터미널에 따라 다를 수 있음)
        print(frame)
        time.sleep(FRAME / 1000)
        if i < len(ascii_frames) - 1:
            audio.play()
            time.sleep(FRAME / 1000)

finally:
    os.remove(f"{title}.mp4")
    os.remove(f"{title}.m4a")
    os.remove(f"{title}.wav")
    os.remove(f"{title}_altered.wav")
