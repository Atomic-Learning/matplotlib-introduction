import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Heat map example
data = np.random.rand(10, 10)

fig1, ax1 = plt.subplots()
im = ax1.imshow(data, cmap='viridis', aspect='auto')
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.set_title('Heat Map')
fig1.colorbar(im, ax=ax1, label='Value')

fig1.savefig('resources/heat_map.png')

# Animated plot example - moving sine wave
fig2, ax2 = plt.subplots()
x_data = np.linspace(0, 2*np.pi, 100)
line, = ax2.plot([], [], 'b-', linewidth=2)

ax2.set_xlim(0, 2*np.pi)
ax2.set_ylim(-1.5, 1.5)
ax2.set_xlabel('x')
ax2.set_ylabel('sin(x + phase)')
ax2.set_title('Animated Sine Wave')
ax2.grid(True)

def init():
    line.set_data([], [])
    return line,

def animate(frame):
    # Shift the sine wave by changing the phase
    y_data = np.sin(x_data + frame * 0.1)
    line.set_data(x_data, y_data)
    return line,

# Create animation with 60 frames
anim = FuncAnimation(fig2, animate, init_func=init, frames=60, interval=50, blit=True)

# Save as GIF (requires Pillow: pip install pillow)
anim.save('resources/animated_sine.gif', writer='pillow', fps=20)
print("Animation saved as animated_sine.gif")

plt.close('all')

