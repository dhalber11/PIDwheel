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
![image](https://github.com/dhalber11/PIDwheel/assets/113122312/2accb607-c651-4054-a02c-0275baa62f2e)

## Early Design 
![unnamed](https://user-images.githubusercontent.com/113122312/232816832-5ecfbff9-cc31-49a1-a10a-9a1f94366619.jpg)
For the most part the design stayed the same, we had the wheel and LCD on the top and we stuck with the T-slots. The only thing we changed was the front panel which we decided to have 1 line of controls with 2 switches, 1 LED, and a rotary encoder.

## Code
### Goals 
For this assignment we wanted to use an encoder to control a dc motor and a photointerrupter to read the RPM of that motor as its spinning. The criteria of the project state that we have to use PID to get a smooth value from the encoder to the motor. This project is very code intensive therefore there will be extensive documentation on the many issues that we had while trying to code this project. I wanted to go step by step in doing this project so I decided to start by getting a working encoder that then controlled a motor. Once that was working I started work on the photointerrupter to read the rpm of that motor. This proved to be the most difficult part. Finally I wanted to add in the PID to finish the project. 

### Motor and Encoder
This was the easiest part of the coding process for me. In a combination of my peers and my past documentation it was very simple to get a motor spinning to the encoder. All in all it took two lines of code and was very simple to create. I started by limiting the encoder between 0-100, this was simply an accesibility fix because I wanted to get a quicker response between the motor and encoder. This was because if the motor was at its highest RPM and you continued to spin the encoder you would have to spin it all the way back before the values began to change. The limits stopped the values of the encoder so as soon as you began to spin it back the motor responded. Once that was done there was only the issue of mapping the encoder value to the motor. This was very simple and all in all the code for this whole section came out to just a few lines. Using past documentation it was very simple code. 

python```
while True: 
    enc.position = max(min(enc.position, 100),20)  #limits the encoder to the mapped value range
    motorpin.value = (int(simpleio.map_range(enc.position,0, 100, 0, 65535))) #maps the encoder value to the motor 
```

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

