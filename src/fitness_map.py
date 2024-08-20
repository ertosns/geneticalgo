import matplotlib.pyplot as plt

fig, ax = plt.subplots()

settings = ['joint_evolution', 'link-shae', 'control', 'population evaluation']
fitness = [0.34, 0.33, 0.32, 0.14]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(settings, fitness, label=bar_labels, color=bar_colors)

ax.set_ylabel('fitness')
ax.set_title('fitness by evolution')
ax.legend(title='settings')


plt.show()
fig.savefig('../data/pics/graph.png')
