import matplotlib.pyplot as plt
 
# x axis values
x = [3,4,5,6,6.5,6.5,6,5,4,3,2.5,2.5,3]
# corresponding y axis values
y = [6,7,7,6,5,4,3,2,2,3,4,5,6]
 
# plotting the points 
plt.plot(x, y, color='red', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='yellow', markersize=12)
 
# setting x and y axis range
plt.ylim(1,8)
plt.xlim(1,8)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('Some cool customizations!')
 
# function to show the plot
plt.show()