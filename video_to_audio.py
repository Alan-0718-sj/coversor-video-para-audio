import moviepy.editor
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def title():
    print(' Converts video to audio using Moviepy library '.upper().center(70, '#'))
    print()

clear()
title()

video = moviepy.editor.VideoFileClip('O LIVRO DOS SALMOS  CAPÍTULO 61 VERSÍCULO 1 AO 8.mp4')
audio = video.audio
audio.write_audiofile('livro_salmos_C61_V_1_8.mp3')
