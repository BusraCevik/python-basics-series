#https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203
from playsound import playsound
import time
import sys

def alarm(seconds):
    time_elapsed = 0
    last_len = 0

    try:
        while time_elapsed < seconds:
            time.sleep(1)
            time_elapsed += 1

            time_left = seconds - time_elapsed
            minutes_left = time_left // 60
            seconds_left = time_left % 60

            text = f"{minutes_left:02d}:{seconds_left:02d}"
            padding = ' ' * max(0, last_len - len(text))
            print('\r' + text + padding, end='', flush=True)
            last_len = len(text)

        print()
        print('\a', end='', flush=True)
        playsound("alarm_clocksound.mp3")
    except KeyboardInterrupt:
        print("\nAlarm canceled.")

def alarm_time():
    minutes = int(input("How many minutes do you want to wait? : "))
    seconds = int(input("How many seconds do you want to wait? : "))
    total_seconds = minutes * 60 + seconds
    return total_seconds

if __name__ == "__main__":

    alarms = alarm_time()
    alarm(alarms)

