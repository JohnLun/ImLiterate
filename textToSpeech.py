from gtts import gTTS
from pygame import mixer

mixer.init()

def saveMp3(myText):
    myText.replace("\n", " ")
    language = 'en'
    output = gTTS(text = myText, lang = language, slow = False)
    output.save("output.mp3")
    mixer.music.load('output.mp3')
    mixer.music.play()
    play = True
    while True:
        ch = input()
        if (ch == "p"):
            play = not play
            if(play == True):
                mixer.music.unpause()
            elif(play == False):
                mixer.music.pause()