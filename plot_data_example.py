import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 1, 500)
signal = np.sin(2 * np.pi * 10 * time) + np.random.normal(0, 0.2, 500)

plt.plot(time, signal)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Simulated Neural Signal")
plt.show()