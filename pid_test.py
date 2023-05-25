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
import PID

x=PID 




# i2c = board.I2C()
# lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

motorpin = AnalogOut(board.A1)

interrupter = DigitalInOut(board.D6)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP

interrupts = 0
time1= 0
time2= 0 
rpm =0
lastVal = False
lastlog = True
lastRpm= True

enc = rotaryio.IncrementalEncoder(board.D9, board.D8,divisor=4)

last_position = None

encBtn = digitalio.DigitalInOut(board.D7)
encbtn = digitalio.Direction.INPUT
encbtn  = digitalio.Pull.UP


log =0
intTime = 0

class RPMCalculator:
    
    def __init__(self) -> None:
        

        self.time1 = 0
        self.time2 = 0
        self.printingDelayCounter =0
        self.lastPollingVal = False
        self.RPM = 0
        self.totalInterrupts =0
        self.lastInterrupt = -1
        
    def debug(self,DelayInterval=500):
        if self.printingDelayCounter % DelayInterval == 1 :
            #all debug statements 
            print(f"{self.totalInterrupts} RPM: {self.RPM} {self.time1} {self.time2}")
    
    def RpmCompute(self):
        
        if self.totalInterrupts % 2 == 0 and self.lastInterrupt != self.totalInterrupts: 
            self.time1= time.monotonic()
            self.RPM = 1/((self.time1-self.time2 + .0001)/2)
            self.lastInterrupt = self.totalInterrupts

        elif self.totalInterrupts % 2 == 1 and self.lastInterrupt != self.totalInterrupts:
            self.time2 = time.monotonic()
            # print(self.time2,self.time1)
            self.RPM = 1/((self.time2-self.time1 + .0001)/2)

            self.lastInterrupt = self.totalInterrupts

            return self.RPM
        else:
            self.lastInterrupt = self.totalInterrupts
            
            # takes time at first and 10th interupt on cycyle and takes time from first interrupt and 10th and 
            # gets the diffrence then devide 60 by that number to get the RPM
            
    def pollingForInterrupts(self):
        
        if interrupter.value and interrupter.value != self.lastPollingVal:
            self.totalInterrupts += 1 
            self.lastPollingVal = True
            
        if  not interrupter.value:
            self.lastPollingVal = False

RPMCalculator1 = RPMCalculator()

while True: 
    enc.position = max(min(enc.position, 100),20)
    motorpin.value = (int(simpleio.map_range(enc.position,0, 100, 0, 65535)))
    #print(f"{intTime} {log} {interrupts} {rpm}")
    #time.sleep(.001)
    

    RPMCalculator1.RpmCompute()

    RPMCalculator1.printingDelayCounter += 1

    RPMCalculator1.debug(DelayInterval=500)
    
  
    
    RPMCalculator1.pollingForInterrupts()
    
        


      

