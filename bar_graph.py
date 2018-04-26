#BAR GRAPH

import matplotlib.pyplot as plt
 
# x-coordinates of left sides of bars 
left = [1, 2, 3, 4, 5]
 
# heights of bars
height = [10, 40, 20, 50, 30]
 
# labels for bars
tick_label = ['one', 'two', 'three', 'four', 'five']
 
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.5, color = ['yellow', 'red'])
 
# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')
 
# function to show the plot
plt.show()
