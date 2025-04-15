#Physics 185 GWC
#Spring 2025
#Victor Corona
#Lab 3: Projectile Motion

import numpy as np

#List of Inputs
theta=15      #angle (degrees)
v0=15      #velocity (m/s)
dy=0          #change in height (m)

#acceleration of gravity
g=-9.81       #(m/s^1) (note its negative)

#This is how you convert degrees to radians
theta=np.deg2rad(theta)

#Setting up the quadratic formula
a=g/2
b=v0*np.sin(theta)
c=-dy

#Quadratic Formula
t=((-b)-np.sqrt((b**2)-(4*a*c)))/(2*a)    #(note +- in formula)

x=v0*np.cos(theta)*t                      
h=(-(v0**2)*(np.sin(theta)**2))/(2*g)

#Output Results
print('Time of flight',t,'s')
print('Range',x,'m')
print('Max height',h,'m')