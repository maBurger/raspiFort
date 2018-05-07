from tkinter import *
from gpiozero import LED
from temp import read_sensor

rot = LED(5)
gelb = LED(6)
grn =LED(13)
debug = False

# Reaktion auf Mausklick im Fenster
def led_change():
    if not rot.is_lit:
        if(debug):
            print('LED an')
        rot.on()
        lbl.configure(text="Die LED leuchtet.")
        mywin.configure(background='red')
    else:
        if(debug):
            print('LED aus')
        rot.off()
        lbl.configure(text="Die LED ist ausgeschalten.")
        mywin.configure(background='lightgrey')


def setDBG():
    global debug
    debug = not debug


def check_temp():
    temp.configure(text='Temp: {}°C'.format(read_sensor()))


# Benutzeroberfläche mit Ereignisverwaltung
mywin = Tk()
# Größe des Fensters festlegen
mywin.geometry('300x200')
# Fenster nicht änderbar (Größe)
mywin.resizable(width=False, height=False)
# Den Festertitel festlegen
mywin.wm_title("LED ein/aus")
# damit ist die erste Spalte so breit wie das Fenster
mywin.columnconfigure(0, weight=1)

# Variablen definieren
ledstatus = IntVar()
debugstat = IntVar()

# Inhalt der Fensteroberfläche definieren
lbl = Label(mywin, text="Die LED ist ausgeschalten.", padx=10, pady=10)
ledbtn = Checkbutton(mywin, text="LED ein-/ausschalten", indicatoron=0, variable=ledstatus, command=led_change, padx=10, pady=10)
dbgbtn = Checkbutton(mywin, text="Debug on/off", indicatoron=1, variable=debugstat, command=setDBG, padx=10, pady=10)
temp = Label(mywin, text='Temperatur: xyz', padx=10, pady=10)
tempbtn = Button(mywin, text="Read temp sensor", command=check_temp, padx=10, pady=10)

# die Komponenten der Oberfläche im Fenster verteilen
# dafür wird ein Gitter verwendet
lbl.grid(column=0, row=0, columnspan=2)
ledbtn.grid(column=0, row=1, columnspan=2, pady=10)
dbgbtn.grid(column=0, row=2, columnspan=2)
temp.grid(column=0, row=3, padx=10)
tempbtn.grid(column=1, row=3, padx=10, pady=10)

# mainloop macht, dass das Programm läuft
mywin.mainloop()
