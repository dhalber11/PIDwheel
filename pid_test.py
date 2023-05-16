import rotaryio
import time
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import digitalio 
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor  import motor
from analogio import AnalogIn,AnalogOut
import simpleio 


# i2c = board.I2C()
# lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

motorpin = AnalogOut(board.A1)
read = AnalogIn(board.A5)

interrupter = DigitalInOut(board.D6)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP

interrupts = 0
time1= 0
time2= 0 
rpm =0
lastVal = True
lastlog = True

enc = rotaryio.IncrementalEncoder(board.D9, board.D8,divisor=4)

last_position = None

encBtn = digitalio.DigitalInOut(board.D7)
encbtn = digitalio.Direction.INPUT
encbtn  = digitalio.Pull.UP


log =1
intTime = 0
while True: 
    enc.position = max(min(enc.position, 100),20)
    # print(f"{interrupter.value} {int(simpleio.map_range(enc.position,0, 100, 0, 6553))} {rpm} {interrupts} {interrupts %5} ")
    # time.sleep(0.01)
    motorpin.value = (int(simpleio.map_range(enc.position,0, 100, 0, 65535)))
    #print(f"{interrupter.value}" )
    # time.sleep(0.01)
    intTime +=1
    print(f"{intTime} {log}")
    time.sleep(.001)
    if intTime % 500 ==1 :
        log +=1
        time.sleep(0.001)
        if interrupter.value and interrupter.value != lastVal:
            interrupts += 1 
            lastVal = True
    if log != lastlog and interrupter.value == True:
        #calculate rpm
        
        lastlog = log
        


      

