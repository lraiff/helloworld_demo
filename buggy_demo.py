import numpy as np
import matplotlib.pyplot as plt
 
 
def compute_average_firing_rate(spike_counts, duration):
    """Compute average firing rate (spikes per second) for a list of neurons."""
    firing_rates = []
    for count in spike_counts:
        rate = count / duration
        firing_rates.append(rate)
    return firing_rates
 
 
def find_most_active_neuron(firing_rates):
    """Return the index and firing rate of the most active neuron."""
    max_rate = 0
    max_index = 0
    for i in range(len(firing_rates)):
        if firing_rates[i] > max_rate:
            max_rate = firing_rates[i]
            max_index = i
    return max_index, max_rate
 
 
def normalize(firing_rates):
    """Normalize firing rates to a 0-1 scale."""
    min_rate = min(firing_rates)
    max_rate = max(firing_rates)
    normalized = [(r - min_rate) / (max_rate - min_rate) for r in firing_rates]
    return normalized
 
 
# Spike counts recorded from 6 neurons over a 2-second window
spike_counts = [18, 42, 7, 55, 23, 36]
duration = 2  # seconds
 
# BUG 1: TypeError — 'duration' is passed as a string by accident
# duration = "2"
 
firing_rates = compute_average_firing_rate(spike_counts, duration)
print("Firing rates (Hz):", firing_rates)
 
# BUG 2: Off-by-one — loop goes one step too far and causes an IndexError
for i in range(len(firing_rates)):
    print(f"Neuron {i}: {firing_rates[i]:.2f} Hz")
 
most_active_idx, most_active_rate = find_most_active_neuron(firing_rates)
print(f"\nMost active neuron: Neuron {most_active_idx} at {most_active_rate:.2f} Hz")
 
# BUG 3: Logic error — normalized values are wrong because min and max are swapped
# Uncomment the lines below to introduce the bug (and comment out the real normalize call):
normalized = [(r - max(firing_rates)) / (min(firing_rates) - max(firing_rates)) for r in firing_rates]
# normalized = normalize(firing_rates)
print("\nNormalized firing rates:", [round(r, 2) for r in normalized])
 
# Plot
neuron_labels = [f"N{i}" for i in range(len(firing_rates))]
plt.figure(figsize=(8, 4))
plt.bar(neuron_labels, normalized, color="steelblue")
plt.xlabel("Neuron")
plt.ylabel("Normalized Firing Rate")
plt.title("Normalized Firing Rates Across Neurons")
plt.tight_layout()
plt.show()