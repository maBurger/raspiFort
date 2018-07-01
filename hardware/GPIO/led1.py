from gpiozero import LED
from time import sleep

zeit = 0.1

rot  = LED(5)
gelb = LED(6)
grn  = LED(13)

while True:
    grn.on()
    sleep(zeit)
    gelb.on()
    sleep(zeit)
    rot.on()
    sleep(zeit)
    grn.off()
    sleep(zeit)
    gelb.off()
    sleep(zeit)
    rot.off()
    sleep(zeit)
    
