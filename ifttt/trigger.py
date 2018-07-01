#!/usr/bin/python

import time, os, requests
from gpiozero import Button
from signal import pause

def trigger(webhook="https://maker.ifttt.com/trigger/{}/with/key/[YOUR_IFTTT_APP_KEY]",event="vhs_kurs"):
	r = requests.get(webhook.format(event))
	return(r.status_code)


button = Button(18)

button.when_pressed = trigger

pause()
