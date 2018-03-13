# importing the required module
import matplotlib.pyplot as plt
 
# x axis values
x = [0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6,4.0,4.4,4.8,5.2,5.6,6.0,6.4,6.8,7.2,7.6,8.0,8.4,8.8,9.2,9.6,9.0,10.4,10.8,11.2,11.6,12.0,12.4,12.8,13.2,13.6,14.0,14.4,14.8,15.2,15.6,16.0,16.4,16.8,17.2,17.8]
# corresponding y axis values
y = [130,190,198,200,204,205,212,220,225,230,240,245,250,255,256,257,265,267,272,273,278,280,282,288,290,294,298,300,302,305,306,315,324,330,335,342,343,345,346,370,388,392,430,552,700]
 
# plotting the points 
plt.plot(x, y)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('potentiometer!')
 
# function to show the plot
plt.show()
            # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

