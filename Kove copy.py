from datetime import datetime
import os
import time
import subprocess
import Kovefunc
import sys
from database import *
subprocess.call(['termux-tts-speak','How may i help you sir'])
while True:
  data = str(subprocess.getoutput('termux-speech-to-text')).lower()
  print('Said:' + str(data))
  time.sleep(1)
  if 'tell time' in data:
    current_time = Kovefunc.now()
    Kovefunc.time_speak(current_time)
  elif 'close' in data:
    subprocess.call(['termux-tts-speak','Bye sir'])
    break
  elif 'set timer' in data:
    subprocess.call(['termux-tts-speak','Timer has been arranged Please tell the music'])
    music = str(subprocess.getoutput('termux-speech-to-text')).lower()
    available = ['mumbo','astro','god']
    while music not in available:
      music = str(subprocess.getoutput('termux-speech-to-text')).lower()
    print('Music has been set')
    print(music)
    subprocess.call(['termux-tts-speak','Now for the time sir in Month,day and time format'])
    music = music + '.mp3'
    timer = input("Timer: according month and day ").split()
    def timing(timer):
      time = str(datetime.now())
      try:
        index = time.index('.')
        new_time = time[:index]
      except:
        new_time = time
      date = new_time[:10]
      specifics = new_time[11:]
      splitted = date.split('-')
      splitted.pop(0)
      return splitted,specifics
    print(timing(timer))
    print(timer[2:])
    splitted,specifics = timing(timer)
    
    while splitted != timer[:2]:
      timing(timer)
    splitted,specifics = timing(timer)
    while specifics <= ''.join(timer[2:]):
      timing(timer)
      splitted,specifics = timing(timer)
    subprocess.call(['mpv',music])
 
    print('successful')
  elif 'torch on' in data:
    os.system('termux-torch on')
    torch = True
  elif 'torch off' in data:
    try:
      if torch == True:
        os.system('termux-torch off')
        torch = False
    except:
      time.sleep(1)
  elif 'open google' in data:
    os.system('am start --user 0 -n /com.google.android.googlequicksearchbox.ViewerLauncher')
  elif 'open youtube' in data:
    os.system('am start --user 0 -n com.google.android.youtube/com.google.android.youtube.HomeActivity')
  elif data == '':
    print('...')
  elif 'call ' in data:
    def contacts(name):
      inp = subprocess.getoutput('termux-contact-list')
      f = open('trial.py',mode='w')
      f.write('data1 = ' + inp)
      f.close()
      import trial
      for elem in trial.data1:
        if elem["name"].lower() == xx:
          return elem["number"]
        try:
          for c,b in zip(list(xx),list(elem["name"]))
            
      return 'Nope'
    xx = data[5:]
    numberxx = contacts(xx)
    if numberxx == 'Nope':
      subprocess.call(['termux-tts-speak','No such name there sir'])
    else:
      subprocess.call(['termux-telephony-call','Calling',xx])
      subprocess.call(['termux-telephony-call',numberxx])
  elif 'set note' in data:
    subprocess.call(['termux-tts-speak','what you want to note'])
    data = str(subprocess.getoutput('termux-speech-to-text')).lower()
    print('Noted': + data)
    
    
      
      
    
