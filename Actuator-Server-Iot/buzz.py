import gpiozero
import time

def buzz():
    buzzer = gpiozero.Buzzer(3)
    buzzer.on()
    time.sleep(2)
    buzzer. off()


while True:
    i = int(input("Distance: "))
    if (i>17):
        buzz()
        time.sleep(2)



