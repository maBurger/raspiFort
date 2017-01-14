#! /usr/bin/python3

import re, os, time
import urllib.parse
import urllib.request

def SendHTTPMessage( Value ):
    url = "https://api.thingspeak.com/update"

    params = urllib.parse.urlencode({'field1': Value, 'key':'NQOZ5AFSZNUL6V5M'})
    params = params.encode('utf-8')

    req = urllib.request.Request(url, params)
    req.add_header('User-agent', 'Temp Logger Burger')

    f = urllib.request.urlopen(req)
    jsonstr = f.read()
    # print(jsonstr)


# function: read and parse sensor data file
def read_sensor(path):
    value = "U"
    try:
      f = open(path, "r")
      line = f.readline()
      if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", line):
        line = f.readline()
        m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)
        if m:
          value = str(float(m.group(2)) / 1000.0)
      f.close()
    except (IOError, e):
      print(time.strftime("%x %X"), "Error reading", path, ": ", e)
    return value


# define pathes to 1-wire sensor data
pathes = (
  "/sys/bus/w1/devices/28-00000577c27b/w1_slave",
)

if __name__ == "__main__":
    value = read_sensor(pathes[0])
    # print('Temp: {}'.format(value))
    SendHTTPMessage(value)