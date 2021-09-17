
import datetime
import os
import subprocess
#Current time func
def now():
    current_time = str(datetime.datetime.now())
    if '.' in current_time:
        dot_index = current_time.index('.')
        current_time = current_time[:dot_index]
    return current_time


#Current time speak
def time_speak(current_time):
    large_specifics = current_time[:10]
    print(large_specifics)
    large_specifics = large_specifics.split('-')
    small_specifics = current_time[11:]
    small_specifics = small_specifics.split(':')
    hour = small_specifics[0]
    if int(hour) > 12:
        hour = int(hour) - 12
    minute = small_specifics[1]
    date = large_specifics[2]
    day = datetime.date(int(large_specifics[0]),int(large_specifics[1]),int(large_specifics[2])).strftime('%A')
    time_speech =f'Today is {date} {day} and time is {hour} {minute}' 
    subprocess.call(['termux-tts-speak',time_speech])