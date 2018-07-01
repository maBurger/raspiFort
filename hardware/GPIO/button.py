from gpiozero import LED, Button

led = LED(13)
button = Button(18)

while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()
