#Physics 185 GWC
#Spring 2025
#Victor Corona

#Lab 1 Graphs
#This is a basic introduction to python
#Everything in green after a # is a comment not code

#import python librabries to use more functions
import matplotlib.pyplot as plt  #This is the graph plotting library

#Contant Velocity
#Input your data, each number needs to be seperated by a , to count as a new one
t=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    #time (s)
v=[1.2,1.2,1.2,1.2,1.2,1.2,1.2,1.2,1.2,1.2,1.2]   #velocity (m/s)
x=[-7.91,-6.65,-5.65,-4.35,-3.15,-1.8,-0.75,0.5,1.75,2.9,4]   #position (m) (my data)

#Plotting Data
plt.figure(1)        #setting up first plot
plt.plot(t,v,'o-')   #plot(x-axis,y-axis,'plot options')
plt.title("Walking Man Velocity vs Time")
plt.xlabel("time (s)")
plt.ylabel("Velocity (m/s)")

plt.figure(2)
plt.plot(t,x,'o-')
plt.title("Walking Man Position vs Time")
plt.xlabel("time (s)")
plt.ylabel("Position (m)")
plt.show()

#sometimes trinket wont show all the plots, you might need to run it a few times
#You can also add 'plt.show()' to line 24 to show one plot at a time