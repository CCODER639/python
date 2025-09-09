import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from reSnakCopy import SPEED as speed
# Global speed variable

def increase_speed(event):
    global speed
    speed *= 2
    print("Speed:", speed)

def decrease_speed(event):
    global speed
    speed /= 2
    print("Speed:", speed)

# Example plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)  # make space for buttons

ax_increase = plt.axes([0.7, 0.05, 0.1, 0.075])  # x, y, width, height
ax_decrease = plt.axes([0.81, 0.05, 0.1, 0.075])
btn_increase = Button(ax_increase, 'Speed+')
btn_decrease = Button(ax_decrease, 'Speed-')

btn_increase.on_clicked(increase_speed)
btn_decrease.on_clicked(decrease_speed)

# Example of using speed in your plotting loop
import time

scores = [10, 20, 15, 30]
for s in scores:
    ax.clear()
    ax.plot(scores[:scores.index(s)+1])
    plt.pause(1 / speed)  # adjust pause with speed
