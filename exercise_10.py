import numpy as np
import matplotlib.pyplot as plt

# Create a figure of size 8x6 inches, 80 dots per inch
plt.figure(figsize=(8, 6), dpi=80)

# Create a new subplot from a grid of 1x1
plt.subplot(1, 1, 1)

ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# Plot cosine with a blue continuous line of width 1 (pixels)
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-", label="cosine")

# Plot sine with a green continuous line of width 1 (pixels)
plt.plot(X, S, color="green", linewidth=1.0, linestyle="-", label="sine")

# Set x limits
plt.xlim(X.min() * 1.1, X.max() * 1.1)

# Set x ticks
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

# Set y limits
plt.ylim(C.min() * 1.1, C.max() * 1.1)

# Set y ticks
plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])

#メモリを見やすいようにフィルターをかける
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    #label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
    label.set_bbox({"facecolor": "white", "edgecolor": "None","alpha":0.65, 'lw':0})

#以下点の詳細記述
t = 2 * np.pi / 3
#破線
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=1.0, linestyle="--")
#点
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')

#注釈式
plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data', 
             xytext=(-90, -50), textcoords='offset points', fontsize=16, 
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

#sineも同様に
plt.plot([t, t],[0, np.sin(t)], color='green', linewidth=1.0, linestyle="--")
plt.scatter([t, ],[np.sin(t), ], 50, color='green')

plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# Save figure using 72 dots per inch
# plt.savefig("exercise_2.png", dpi=72)

# showing a regend
plt.legend(loc='upper left')

# Show result on screen
plt.show()