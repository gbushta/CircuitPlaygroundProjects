# CircuitPlayground Accelerometer
# using board module and not adafruit_circuitplayground module

from time import sleep
import board
import adafruit_lis3dh
import busio
import neopixel

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
lis3dh.range = adafruit_lis3dh.RANGE_8_G

leds = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05, auto_write=True)


def pixelOff():
        for i in range(10):
            leds[i] = ((0,0,0))

while True:
    x, y, z = lis3dh.acceleration
    y = int(y)
    x = int(x)
    if (y > 3):
        pixelOff()
        if x < 0:
            leds[5] = ((0,128,255))
        else:
            leds[4] = ((0,128,255))
    elif (y > 0 and y < 4):
        pixelOff()
        if x < 0:
            leds[6] = ((0,128,255))
        else:
            leds[3] = ((0,128,255))
    elif (y == 0 and x == 0):
        for i in range(10):
            leds[i] = ((128, 128, 255))
    elif (y == 0):
        pixelOff()
        if x < 0:
            leds[7] = ((0,128,255))
        else:
            leds[2] = ((0,128,255))
    elif (y < 0 and y > -4):
        pixelOff()
        if x < 0:
            leds[8] = ((0,128,255))
        else:
            leds[1] = ((0,128,255))
    elif (y < -3):
        pixelOff()
        if x < 0:
            leds[9] = ((0,128,255))
        else:
            leds[0] = ((0,128,255))
    sleep(.5)