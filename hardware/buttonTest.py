from gpiozero import LED, Button

''' button Test
Dies ist ein Beispielprogramm für das neue HAT.
VHS Esslingen - raspberry pi Fortgeschrittenen Kurs

Matthias Burger 2018-05
'''

gruen = LED(13)
gelb = LED(6)
rot = LED(5)
button = Button(18)

while True:
    if button.is_pressed:
        # wenn der Knopfgedrückt ist schalte die LEDs an
        gruen.on()
        gelb.on()
        rot.on()
    else:
        # wenn der Knopf nicht gedrückt ist, schalte die LEDS aus
        gruen.off()
        gelb.off()
        rot.off()
