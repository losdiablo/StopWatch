import time
import datetime
import pygame 




def setAlarm(alarmTime):
    print(f"alarm set for {alarmTime}")
    soundFile="D:/WebS/stopwatch/s.mp3"
    isRuning=True
    while isRuning:
        currentTime=datetime.datetime.now().strftime("%H:%M:%S")
        print(currentTime)
        if currentTime == alarmTime:
            print("wake up motherfucker!")
            pygame.mixer.init()
            pygame.mixer.music.load(soundFile)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            isRuning=False
                 
        time.sleep(1)
    
if __name__ == "__main__":
    alarmTime=input("Enter the alarm time (HH:MM:SS)")
    setAlarm(alarmTime)
    



