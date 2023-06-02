# PID Project

## What is out project?
Our project is a wheel box controlled by PID. It will work similar to cruise control speeding up or slowing down the based on the set value. We will choose this value with a rotary encoder and an LCD screen. We hope to keep this project simple but effective and to sharpen the PID over out time period. 

## Schedule 
* CAD: 4/24 or week of 
* Code: 6/1
* Assembly: 5/10 
* Documentation: 5/20
* due date: June 1rst 

For the CAD it was fairly simple and I got it done by the time limit. There was a couple of problems I ran into, the main one was the T-slot joints. The T-slot tool was't working like I thought it would and it was making the bolts to close to the end and it was hard to find the right screw length. I ended up importing a T-slot from a different studio earlier in the year because I knew it would work but it was much less efficient. (Dylan talk here). For the assembly I finished on time but I couldn't fully manufacture until the end (bcause of wiring) which is something to consider for later projects. We also ended up straying from the design a little with the front panel(adding another switch) and on the side another peice of a breaboard, this is another reason you shouldn't fully put it together without the wiring and electronics. For the documentation we didn't finish by the time we thought and ended up finishing 6/1-2 so it was a good lesson to give time for documentation which is arguably thre most important part of the project.

![image](https://github.com/dhalber11/PIDwheel/assets/113122312/79db7c5e-b936-459c-856f-181fc560ac8e)


## Description
For this project we were assigned to make a project using PID (Porportional, Integral, Derivative) which we used to control a variable. The requirements was to use a 6AA battery pack and include a power switch and LED. We chose to do a wheel box to demonstrate the PID similar to cruise control. This project utilizes Dylan's code skills for the most part and Jinho's CAD skills. 

## Problem to Solve

The need for a continuos input from a human/source to keep a certain speed for a car or wheel. The PID solves this problem letting you sit back and relax, an example is cruise control. 

## S.M.A.R.T Goal
By June 2nd we will have built a box that will utilize PID to set the speed for a wheel and motor. When you move the Rotary encoder it will set the speed and appear on the LCD. 

## Evidence 
[onshape link](https://cvilleschools.onshape.com/documents/bc5dd0b5deaae27b6921b19d/w/315ed26b23bfec5e6ab30054/e/6f96dca158f149fec61f898a)

## Image 
![image](https://github.com/dhalber11/PIDwheel/assets/113122312/1aab1c93-ee6f-447d-937e-59c4fc4b6bea)
![Screenshot 2023-06-01 10 31 54 PM](https://github.com/dhalber11/PIDwheel/assets/113122312/a64a1bf3-57a8-459b-8d2c-994421ab17c4)
![unnamed](https://github.com/dhalber11/PIDwheel/assets/113122312/8d4feadb-e39b-4552-9924-7dc04c27270d)
![unnamed](https://github.com/dhalber11/PIDwheel/assets/113122312/d4428668-63a0-42e7-b892-13bceb14995a)
![unnamed](https://github.com/dhalber11/PIDwheel/assets/113122312/9c862686-9633-46ee-8a2a-512babb4dc16)

https://github.com/dhalber11/PIDwheel/assets/113122312/c56fbf0c-2e16-45e3-9956-1e5cb16f37f8

## Early Design 
![unnamed](https://user-images.githubusercontent.com/113122312/232816832-5ecfbff9-cc31-49a1-a10a-9a1f94366619.jpg)
For the most part the design stayed the same, we had the wheel and LCD on the top and we stuck with the T-slots. The only thing we changed was the front panel which we decided to have 1 line of controls with 2 switches, 1 LED, and a rotary encoder.

## Code
### Goals 
For this assignment we wanted to use an encoder to control a dc motor and a photointerrupter to read the RPM of that motor as its spinning. The criteria of the project state that we have to use PID to get a smooth value from the encoder to the motor. This project is very code intensive therefore there will be extensive documentation on the many issues that we had while trying to code this project. I wanted to go step by step in doing this project so I decided to start by getting a working encoder that then controlled a motor. Once that was working I started work on the photointerrupter to read the rpm of that motor. This proved to be the most difficult part. Additionally there was the issue of the LCD which was mainly rooted in wiring. Finally I wanted to add in the PID to finish the project.

### Motor and Encoder
This was the easiest part of the coding process for me. In a combination of my peers and my past documentation it was very simple to get a motor spinning to the encoder. All in all it took two lines of code and was very simple to create. I started by limiting the encoder between 0-100, this was simply an accesibility fix because I wanted to get a quicker response between the motor and encoder. This was because if the motor was at its highest RPM and you continued to spin the encoder you would have to spin it all the way back before the values began to change. The limits stopped the values of the encoder so as soon as you began to spin it back the motor responded. Once that was done there was only the issue of mapping the encoder value to the motor. This was very simple and all in all the code for this whole section came out to just a few lines. Using past documentation it was very simple code. 
This is the entirety of the code for the encoder and motor:
```python
while True: 
    enc.position = max(min(enc.position, 100),20)  #limits the encoder to the mapped value range
    motorpin.value = (int(simpleio.map_range(enc.position,0, 100, 0, 65535))) #maps the encoder value to the motor 
```
### Photointerrupter/RPM
This was what proved to be the hardest issue with coding. I spent the most time here and still had to settle for a solution that was not entirely adequate but still functioned. I worked a large amount with Paul on this and we used many different functions over the time we spent working on it. The original intent of the project was to use interrupts to read the rpm by stopping all other processes and then taking the rpm. This did not end up working as interrupts does not actually work in circuitpython. This was only a slight issue and we turned to polling to read the rpm. However here we encountered another issue. Because of the high rpm of the motors the polling was moving too fast for the computer to calculate the rpm. To stop this we used the modulo function that simply returns the remainder of division. Using this we could limit the rpm to being taken every two rotations by doubling the amount of interrupts and then taking the modulo of it. As simple as that sounds we were being thrown errors such as divide by zero. Because we were using time.monotonic to take the time between the first and last interrupt to then get RPM we found that at certain points those times would become equal to one another. We ended up using a class designed by Paul to organize the process. We had yet another issue with values of the RPM jumping rapidly and never staying steady. To find a better explanation of the RPM computing look [here](https://github.com/japhero/PID-project#rpm-computation) at Pauls documentation

The class we used: 
```python
class RPMCalculator:

    
    def __init__(self) -> None:
        
        self.printingDelayCounter =0
        self.lastPollingVal = False
        self.RPM = 0
        self.totalInterrupts =0
        self.time1 =0.0
        self.time2 =0.0
        
    def debug(self,DelayInterval=500):
        if self.printingDelayCounter % DelayInterval == 1 :
            #all debug statements 
            print(f"{self.totalInterrupts} RPM: {self.RPM}  {self.time1}  {self.time2}")
    


        
            
    def RPMcompute(self):
        
        if Interrupter.value and Interrupter.value != self.lastPollingVal:
            self.totalInterrupts += 1 
            self.lastPollingVal = True

            if self.totalInterrupts % 10 == 0: #first interrupt
                self.time1= time.monotonic_ns() 
                self.RPM = 1/((self.time1-self.time2)/(10 **9)/10) #takes nanoseconds and brings it back up to seconds for rpm, used to bypass divide by zero error
            
            elif self.totalInterrupts % 10 == 9: #second interrupt
                self.time2 = time.monotonic_ns() 
                self.RPM = 1/((self.time2-self.time1)/(10 **9)/10)
                return self.RPM
                # takes time at first and 10th interupt on cycyle and takes time from first interrupt and 10th and 
                # gets the diffrence then devide 60 by that number to get the RPM
            
        if  not Interrupter.value: # simple debounce for the interrupt
            self.lastPollingVal = False
```
The looped code that references the class: 
```python
RPMCalc.printingDelayCounter += 1
    RPMCalc.debug(DelayInterval=500)
    RPMCalc.RPMcompute()
```
### PID
This is where we fell short on this project. Because of how long the process of finding RPM took we ran out of time to incorporate PID. I did not have time to implement the code however I did do research to find libraries

### LCD
We wanted to include this as part of our documentation as it highlights another issue that we had to tackle during this project. The LCD that we were using had an i2c backpack and was wired to the SDA and SCL pins. Originally we had an issue where the LCD was pulling too much power and the board would not be able to boot. However we did not realize this at the time and since it was early in my progression of coding I decided to scrap it and move on to the next part and come back to it. As we came back to it however we realized that the issue is a little more serious than simply a power difference. My first attempt at fixing the issue was plugging the power to the LCD straight into a 6v battery pack, seperate from the board itself. However this did not seem to work and the board continued to "brown out", a term used when the board is recieving too low voltage to function. This was odd as the LCD should have been taking power from the battery pack and not from the board. To solve this issue I turned to Mr.Helmstetter for some insight on the issue.
The solution we found was to wire a switch to a pin on the board so that it was possible to do a Pull-Up on the LCD to reduce the sucking of power through the SDA and SCL pins which turned out to be the issue. This was a small issue but an annoying one as I had never had this issue with LCD i2c's in the past. This was a helpful issue to solve as it gave me a little more neccessary insight into how certain circuits work. 
## Criteria and constraints

### Criteria 
* LED                                                                                                                                
* LCD
* Has to be able to use PID-Rotary encoder Switches
* DC motor and wheel

### Constraints
* Time
* Materials
* Resources for PID (like libraries)

### wiring diagram

![image](https://github.com/dhalber11/PIDwheel/assets/113122312/9f1a9897-c018-4a30-aef1-6fa96f879815)


## Refletion

This project was challenging and broadened out code knowledge to more real life applications. One thing I learned for CAD was to make sure your project isn't too small or too big by putting it next to a part or something for reference before manufacturing the whole project in a part studio. Another problem I mentioned earlier was the T-slot tool that was a bit finicky, but I still definitely reccomend using them. Some very useful tools for this are Spur Gear, Laser joint, Rack and Pinion, etc you can find these by looking at the top right of your screen and clicking "add custom features" and look up the name of the tool. Antoher thing I also learned was that when putting in an arduino to make sure that there is an access hole in the wall or some place so the code can be adjusted and imported without having to disassemble the whole thing (especially because code implimentation usually is towards the end of the project). For the assembly I learned that it takes much longer than you may think because ogf wiring and puitting in parts so its best to finish CAD quickly. The main issue with this project was the time management, next time we would make sure to knock out the CAD and assembly quickly so I can help my partner more with code and PID which were the main parts. If we were more focused in the beggining we wouldn't have ran into this problem so this has been a real eye opener for time management and how important scheduling is in the beggining of the year. I also realized this year that CAD alone won't cut it and I need to start taking code more seriously for the future. I have always been more interested in CAD and I though it wwould be enough but for code intensive projects like this it is vital for a wider code knowledge so I can help my partner and the project.

From the code side of things this was a very difficult and frustrating project. I spent hours working out tweaks and issues and fixing problems that seemed so benign to not even finish the PID process. However it was a very beneficial experience for me and I learned so much. For one I am now much more patient with the code and have learned the valuable skill of working slowly to fix issues. I had many issues with my hardware that then led to issues with the software. These being things like the RPM jumping values very often and the photointerrupter simply not interrupting. All of these were large issues that needed solving and to do this I used my documentation from previous assignments that proved to be extremely helpful in this process. I also used my friends especially Paul Weder and Cyrus Wyatt to help with the code and wiring issues. All of the issues I referenced here are in much more detail above in the Code section. 
