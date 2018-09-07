# Fan PWM Control
import time
from time import sleep
import piface.pfio as pfio
pfio.init()

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
my_pwm = GPIO.PWM(7,1000)
last_time = time.time()
this_time = time.time()
RPM = 0


from Tkinter import *

import Tkinter as tk

a=0

class App:
    
    def __init__(self, master):
            self.master=master
            frame = Frame(master)
            frame.pack()
            
            self.TACHO = Label(frame, text=RPM)
            self.TACHO.grid(row=0, column=0)
        
            self.button0 = Button(frame, text='Start Fan', command=self.convert0)
            self.button0.grid(row=2, column=0)
            self.LED0 = Label(frame, image=logo2)
            self.LED0.grid(row=2, column=1)
            
            self.button1 = Button(frame, text='Fan 30% Duty Cycle', command=self.convert1)
            self.button1.grid(row=3, column=0)
            self.LED1 = Label(frame, image=logo2)
            self.LED1.grid(row=3, column=1)
            
            self.button2 = Button(frame, text='Fan 45% Duty Cycle', command=self.convert2)
            self.button2.grid(row=4, column=0)
            self.LED2 = Label(frame, image=logo2)
            self.LED2.grid(row=4, column=1)
            
            self.button3 = Button(frame, text='Fan 60% Duty Cycle', command=self.convert3)
            self.button3.grid(row=5, column=0)
            self.LED3 = Label(frame, image=logo2)
            self.LED3.grid(row=5, column=1)
            
            self.button4 = Button(frame, text='Fan 75% Duty Cycle', command=self.convert4)
            self.button4.grid(row=6, column=0)
            self.LED4 = Label(frame, image=logo2)
            self.LED4.grid(row=6, column=1)
            
            self.button5 = Button(frame, text='Fan 90% Duty Cycle', command=self.convert5)
            self.button5.grid(row=7, column=0)
            self.LED5 = Label(frame, image=logo2)
            self.LED5.grid(row=7, column=1)
            
            self.button6 = Button(frame, text='Fan 100% Duty Cycle', command=self.convert6)
            self.button6.grid(row=8, column=0)
            self.LED6 = Label(frame, image=logo2)
            self.LED6.grid(row=8, column=1)
            
            self.button7 = Button(frame, text='STOP FAN', command=self.convert7)
            self.button7.grid(row=9, column=0)

            self.button8 = Button(frame, text='Exit', command=self.convert8)
            self.button8.grid(row=10, column=0)
            

            #self.button9 = Button(frame, text='Display RPM', command=self.Tach)    Stopped using this button
            #self.button9.grid(row=11, column=0)    Stopped using this button

            self.TimerInterval = 500#This sets the time interval between RPM readings
            self.Tach()         #This will start the 'Tach' method when the GUI starts
    
    def convert0(self):

            print('Fan 15% Duty Cycle')
            global a
            a = 1
            self.button0.config(text='Fan 15% Duty Cycle')
            self.LED0.config(image = logo)
            my_pwm.start(15)
            pfio.digital_write(0,1) #turn on
            self.LED1.config(image = logo2)
            self.LED2.config(image = logo2)
            self.LED3.config(image = logo2)
            self.LED4.config(image = logo2)
            self.LED5.config(image = logo2)
            self.LED6.config(image = logo2)
            pfio.digital_write(1,0) #turn off
            pfio.digital_write(2,0) #turn off
            pfio.digital_write(3,0) #turn off
            pfio.digital_write(4,0) #turn off
            pfio.digital_write(5,0) #turn off
            pfio.digital_write(6,0) #turn off
            pfio.digital_write(7,0) #turn off
            
            
    def convert1(self):

        if a==0:

            print('Please Start the Fan')

        else:

            print('Fan 30% Duty Cycle')
            self.button1.config(text='Fan 30% Duty Cycle')
            self.LED1.config(image = logo)
            my_pwm.ChangeDutyCycle(30)
            pfio.digital_write(1,1) #turn on
            self.LED0.config(image = logo2)
            self.LED2.config(image = logo2)
            self.LED3.config(image = logo2)
            self.LED4.config(image = logo2)
            self.LED5.config(image = logo2)
            self.LED6.config(image = logo2)
            pfio.digital_write(0,0) #turn off
            pfio.digital_write(2,0) #turn off
            pfio.digital_write(3,0) #turn off
            pfio.digital_write(4,0) #turn off
            pfio.digital_write(5,0) #turn off
            pfio.digital_write(6,0) #turn off
            pfio.digital_write(7,0) #turn off

    def convert2(self):

        if a==0:

            print('Please Start the Fan')

        else:
      
            print('Fan 45% Duty Cycle')
            self.button2.config(text='Fan 45% Duty Cycle')
            self.LED2.config(image = logo)
            my_pwm.ChangeDutyCycle(45)
            pfio.digital_write(2,1) #turn on
            self.LED0.config(image = logo2)
            self.LED1.config(image = logo2)
            self.LED3.config(image = logo2)
            self.LED4.config(image = logo2)
            self.LED5.config(image = logo2)
            self.LED6.config(image = logo2)
            pfio.digital_write(0,0) #turn off
            pfio.digital_write(1,0) #turn off
            pfio.digital_write(3,0) #turn off
            pfio.digital_write(4,0) #turn off
            pfio.digital_write(5,0) #turn off
            pfio.digital_write(6,0) #turn off
            pfio.digital_write(7,0) #turn off

    def convert3(self):

        if a==0:

            print('Please Start the Fan')

        else:

            print('Fan 60% Duty Cycle')
            self.button3.config(text='Fan 60% Duty Cycle')
            self.LED3.config(image = logo)
            my_pwm.ChangeDutyCycle(60)
            pfio.digital_write(3,1) #turn on
            self.LED0.config(image = logo2)
            self.LED1.config(image = logo2)
            self.LED2.config(image = logo2)
            self.LED4.config(image = logo2)
            self.LED5.config(image = logo2)
            self.LED6.config(image = logo2)
            pfio.digital_write(0,0) #turn off
            pfio.digital_write(1,0) #turn off
            pfio.digital_write(2,0) #turn off
            pfio.digital_write(4,0) #turn off
            pfio.digital_write(5,0) #turn off
            pfio.digital_write(6,0) #turn off
            pfio.digital_write(7,0) #turn off

    def convert4(self):

        if a==0:

            print('Please Start the Fan')

        else:

            print('Fan 75% Duty Cycle')
            self.button4.config(text='Fan 75% Duty Cycle')
            self.LED4.config(image = logo)
            my_pwm.ChangeDutyCycle(75)
            pfio.digital_write(4,1) #turn on
            self.LED0.config(image = logo2)
            self.LED1.config(image = logo2)
            self.LED2.config(image = logo2)
            self.LED3.config(image = logo2)
            self.LED5.config(image = logo2)
            self.LED6.config(image = logo2)
            pfio.digital_write(0,0) #turn off
            pfio.digital_write(1,0) #turn off
            pfio.digital_write(2,0) #turn off
            pfio.digital_write(3,0) #turn off
            pfio.digital_write(5,0) #turn off
            pfio.digital_write(6,0) #turn off
            pfio.digital_write(7,0) #turn off

    def convert5(self):

        if a==0:

            print('Please Start the Fan')

        else:

            print('Fan 90% Duty Cycle')
            self.button5.config(text='Fan 90% Duty Cycle')
            self.LED5.config(image = logo)
            my_pwm.ChangeDutyCycle(90)
            pfio.digital_write(5,1) #turn on
            self.LED0.config(image = logo2)
            self.LED1.config(image = logo2)
            self.LED2.config(image = logo2)
            self.LED3.config(image = logo2)
            self.LED4.config(image = logo2)
            self.LED6.config(image = logo2)
            pfio.digital_write(0,0) #turn off
            pfio.digital_write(1,0) #turn off
            pfio.digital_write(2,0) #turn off
            pfio.digital_write(3,0) #turn off
            pfio.digital_write(4,0) #turn off
            pfio.digital_write(6,0) #turn off
            pfio.digital_write(7,0) #turn off

    def convert6(self):

        if a==0:

            print('Please Start the Fan')

        else:

            print('Fan 100% Duty Cycle')
            self.button6.config(text='Fan 100% Duty Cycle')
            self.LED6.config(image = logo)
            my_pwm.ChangeDutyCycle(100)
            pfio.digital_write(6,1) #turn on
            self.LED0.config(image = logo2)
            self.LED1.config(image = logo2)
            self.LED2.config(image = logo2)
            self.LED3.config(image = logo2)
            self.LED4.config(image = logo2)
            self.LED5.config(image = logo2)
            pfio.digital_write(0,0) #turn off
            pfio.digital_write(1,0) #turn off
            pfio.digital_write(2,0) #turn off
            pfio.digital_write(3,0) #turn off
            pfio.digital_write(4,0) #turn off
            pfio.digital_write(5,0) #turn off
            pfio.digital_write(7,0) #turn off

    def convert7(self):


            print('STOP FAN')
            global a
            a = 0
            self.button7.config(text='STOP FAN')
            my_pwm.stop()
            pfio.digital_write(7,1) #turn on
            self.LED0.config(image = logo2)
            self.LED1.config(image = logo2)
            self.LED2.config(image = logo2)
            self.LED3.config(image = logo2)
            self.LED4.config(image = logo2)
            self.LED5.config(image = logo2)
            self.LED6.config(image = logo2)
            self.button0.config(text='Start Fan')
            pfio.digital_write(0,0) #turn off
            pfio.digital_write(1,0) #turn off
            pfio.digital_write(2,0) #turn off
            pfio.digital_write(3,0) #turn off
            pfio.digital_write(4,0) #turn off
            pfio.digital_write(5,0) #turn off
            pfio.digital_write(6,0) #turn off

            
    def convert8(self):


            print('EXIT PROGRAM')
            my_pwm.stop()
            quit()

    def EventsPerTime(self):
        global RPM, this_time, last_time
        if GPIO.input(self) > 0.5:
            this_time = time.time()
            RPM = (1/(this_time - last_time))*30
            last_time = this_time
            

    GPIO.add_event_detect(18, GPIO.RISING, callback=EventsPerTime, bouncetime=3)
    
    def Tach(self):
        print 'RPM is %d' % RPM
        self.TACHO.config(text='RPM is %d' % RPM)
        self.master.after(self.TimerInterval,self.Tach) #Used 'after' to repeat this method at the time interval

            
root = Tk()
logo2 = PhotoImage(file="/home/pi/Off LED.gif")
logo = PhotoImage(file="/home/pi/Red LED.gif")
    

root.wm_title('FAN PWM Control program')
app = App(root)

root.mainloop()

