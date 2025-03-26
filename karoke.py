import time
import pygame

# Opens up and reads of the text for the lyrics
file = open("./InTheThickOfIt.txt")
Thick = file.readlines()

# Playing the audio song

pygame.mixer.init()
pygame.mixer.music.load('./assets/song.mp3')
pygame.mixer.music.play()

# Function to start the timing

def line(waitTime, lineText):
    time.sleep(waitTime)
    print(lineText)

# Timing the lyrics along with the song
line(0, Thick[0])
line(3.76, Thick[1])
line(3.46, Thick[2])
line(3.29, Thick[3])
line(3.26, Thick[4])
line(3.37, Thick[5])
line(3.26, Thick[6])
line(3.44, Thick[7])
line(3.12, Thick[8])
line(2.62, Thick[9])
line(3.82, Thick[10])
line(3.46, Thick[11])
line(3.14, Thick[12])
line(3.12, Thick[13])
line(3.44, Thick[14])
line(3.17, Thick[15])
line(3.57, Thick[16])
line(3.22, Thick[17])
line(3.24, Thick[18])
line(3.47, Thick[19])
line(3.27, Thick[20])
line(3.66, Thick[21])
line(2.77, Thick[22])
line(2.77, Thick[23])
line(3.79, Thick[24])
line(3.17, Thick[25])
line(3.12, Thick[26])
line(3.27, Thick[27])
line(3.14, Thick[28])
line(3.21, Thick[29])
line(3.37, Thick[30])
line(3.39, Thick[31])
line(3.22, Thick[32])
line(5, Thick[33])
line(9, Thick[34])
line(3.36, Thick[35])
line(2.64, Thick[36])
line(3.56, Thick[37])
line(3.19, Thick[38])
line(3.24, Thick[39])
line(3.34, Thick[40])
line(3.39, Thick[41])
line(3.22, Thick[42])
line(3.24, Thick[43])
line(3.22, Thick[44])
line(3.39, Thick[45])
line(3.19, Thick[46])
line(3.64, Thick[10])


















