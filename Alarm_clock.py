### Requirement need to download an mp3 file and also need to download the below modules to be used , mp3 should be save in the same folder where u are saving your file



from playsound import playsound
from datetime import datetime 

alarm_time = input("enter the alarm in this format HH:MM:SS:")
alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()

print("setting up an alarm")

while True:

    now = datetime.now()

    clock_hour = now.strftime("%I")
    clock_min = now.strftime("%M")
    clock_sec = now.strftime("%S")
    clock_period = now.strftime("%p")

    if alarm_hour == clock_hour:
        if alarm_min == clock_min:
            if alarm_sec == clock_sec:
                if alarm_period == clock_period:
                    print("wake up")
                    playsound('audio1.mp3')
                    break
