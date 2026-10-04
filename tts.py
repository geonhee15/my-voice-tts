import os
import pygame

pygame.init()
pygame.mixer.init()

current_path = os.path.dirname(__file__)

text = input("Your text: ")
words = list(text)
print(words)

en = {"기": "gi", "가": "ga",
      "날": "nal", "녕": "nyung", "는": "neun", "나": "na", "니": "ni",
      "보": "bo", "바": "ba",
      "상": "sang", "세": "se",
      "안": "an", "어": "uh", "요": "yo", "이": "i", "아": "a", "업": "ub", "없": "ubs", "을": "eul", "야": "ya",
      "저": "ju", "지": "ji",
      "하": "ha"}

for word in words: 
    if word == " ":
        pygame.time.delay(200) 
        continue
    elif word == ",":
        pygame.time.delay(400) 
        continue

    eng = en.get(word)

    audio_path = os.path.join(current_path, "sounds", f"{eng}.mp3")

    if os.path.exists(audio_path):
        sound = pygame.mixer.Sound(audio_path)
        channel = sound.play()
        
        while channel.get_busy():
            pygame.time.Clock().tick(45)
    else:
        print(f"경고: {eng}.mp3 파일을 찾을 수 없습니다.")

pygame.quit()