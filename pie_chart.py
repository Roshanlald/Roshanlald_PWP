import matplotlib.pyplot as plt

# defining labels
activities = ['kkkkkk', 'ooooo', 'uuuuu', 'yyyyy']

# portion covered by each label
slices = [5, 8, 11, 15]

# color for each label
colors = ['g', 'm', 'r', 'y']

# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors, 
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
        radius = 1.2, autopct = '%1.1f%%')

# plotting legend
plt.legend()

# showing the plot
plt.show()
