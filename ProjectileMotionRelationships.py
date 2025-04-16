import matplotlib.pyplot as plt
import numpy as np

#Enter your Data
t=[1,2,3,4,5,6,7,8]
h=[1,2,3,4,5,6,7,8]
r=[1,2,3,4,5,6,7,8]

v0=15         #velocity (m/s)
y0=0          #change in height (m)

theta=[25,35,45,55,66,75,85,90]       #angle (degrees)
theta=[np.deg2rad(i) for i in theta]  #angle (rad)

#calculating sin,sin^2 and sin(2theta)
s=[np.sin(i) for i in theta]
ss=[np.sin(i)**2 for i in theta]
s2=[np.sin(2*i) for i in theta]

#Calculating slope of best fit line
m_s=np.polyfit(s,t,1)   #polyfit(xdata,ydata,degree)
m_ss=np.polyfit(ss,h,1)
m_s2=np.polyfit(s2,r,1)
print('T vs sin slope,',m_s)
print('H vs sin^2 slope',m_ss)
print('R vs sin(2*theta) slope',m_s2)

#Calculating g values
g_s=2*v0/m_s[0]
g_ss=v0**2/(2*m_ss[0])
g_s2=v0**2/m_s2[0]
print('g=',g_s,'from T vs sin')
print('g=',g_ss,'from H vs sin^2')
print('g=',g_s2,'from R vs sin(2*theta)')

#Plotting graphs
plt.figure()
plt.plot(s,t,'o-')                    #plot(xdata,ydata,'options')   #leave the options the same
plt.title(r'$sin^2$($\theta$) vs t')    #to change sin to sin^2, put 'sin^2' where sin is between $$, you can do the same for theta
plt.xlabel(r'$sin$($\theta$)')        #Dont cahnge 'r' or '$$' in line 32 or 33, they allow a code called latex to be used to write equations
plt.ylabel('time (s)')                
plt.show()
