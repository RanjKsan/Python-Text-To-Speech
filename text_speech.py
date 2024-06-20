#-----import libraries-----------
import pyttsx3
import gtts
from pydub import AudioSegment

#--------initialize the library----------------
text_to_speech=pyttsx3.init()

#---------enter the text that need to be converted--------
text_val=input("enter the text")

#---------choose language--------------
lang = input("Enter the language code")
text_to_speech.setProperty('language', lang)


#---------to change the speed of the voice-----------
# speed=2 (by using gtts)
speed = text_to_speech.getProperty('rate')
text_to_speech.setProperty ('rate', speed-300)

# --------to change the voice of the speaker----------
voices = text_to_speech.getProperty('voices')

# to check the voices available
#---method 2---
# for i, voice in enumerate(voices):
#     print(f"Voice {i+1}:")
#     print(f"- ID: {voice.id}")
#     print(f"- Name: {voice.name}")
#     print(f"- Languages: {voice.languages}")
#     print(f"- Gender: {voice.gender}")
#     print()
# select_voice = 'your id'

# ---method 1---
select_voice=None
desired_accent = input("desired accent")
for voice in voices:
    if lang in voice.languages and desired_accent in voice.name:
        select_voice = voice
        break
if select_voice is None:
    select_voice=voices[0]  #change the index value to use different voice(0-male(eng) 1-female(eng))

#-------display the text on console------
text_to_speech.setProperty('voice',select_voice.id)

text_to_speech.say(text_val)
text_to_speech.runAndWait() 

audio_file_path = "generated_speech.mp3"
text_to_speech.save_to_file(text_val, audio_file_path)

print(f"Generated speech saved as {audio_file_path}")