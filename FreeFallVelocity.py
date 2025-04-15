#Physics 185 GWC
#Lab 2; Acceleration of Gravity
#Spring 2025
#Victor Corona

#This is a basic introduction to python
#Everything in green after a # is a comment not code

#import python librabries to use more functions
import matplotlib.pyplot as plt  #This is the graph plotting library
import numpy as np               #This is the math functions library

#Enter data
dx=[3, 4, 5.2, 6.3, 7.3, 8.4]   #distance (cm)
dt=[1/30]                       #time (s)

v= [x/dt[0] for x in dx]        #calculating velocity
print(v)

#to create a time list to plot, a new time list needs to be made
t=[]                            #first you need to create an empty list for time
for i in range(len(dx)):        #this for loop will loop from i=0 to i=5
  t.append(dt[0]+(i*dt[0]))     #t.append will append the new time to the empty list

#Next find the best fit line and slope of the line
m=np.polyfit(t,v,1)             #polyfit will find the cefficents of the polynomial degree
print(m)                        #polyfit(x-data,y-data,degree) 
#print(m) will give two numbers, the slope and y-intercept

#This is how you create the graph
plt.figure()
plt.plot(t,v,'o-')              #plot(x-axis,y-axis,'options')
plt.title("Velocity vs Time")
plt.xlabel("time (s)")
plt.ylabel("Velocity (cm/s)")
plt.show()