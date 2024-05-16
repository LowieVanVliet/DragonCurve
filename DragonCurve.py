import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import numpy as np

# Precompute the directions for faster lookup
directions_map = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]], dtype=np.int8)

def letter(arr):
    new_arr = (arr + 1) % 4
    return np.concatenate((arr, new_arr[::-1]))

def dragoncurve(n, ax):
    ax.clear()  # Clear the previous plot
    directions = np.array([1], dtype=np.int8)
    for _ in range(1, n):
        directions = letter(directions)
    
    # Compute cumulative sum of directions
    steps = np.cumsum(directions_map[directions], axis=0)
    
    # Add (0,0) as the starting point
    steps = np.vstack([[0, 0], steps])

    ax.plot(steps[:, 0], steps[:, 1])
    ax.set_aspect('equal', adjustable='box')

def on_increment_button_clicked(event):
    global n
    n += 1
    dragoncurve(n, ax)
    update_counter(n)

def on_decrement_button_clicked(event):
    global n
    n = max(1, n - 1)
    dragoncurve(n, ax)
    update_counter(n)

def update_counter(n):
    counter_text.set_text(f'Fold Count = {n-1}')
    counter_text_length.set_text(f'Number of Lines = {2**(n-1)}')
    plt.draw()

n = 1  # Initial value of n

# Create the main figure
fig, ax = plt.subplots()

# Plot the Dragon Curve
dragoncurve(n, ax)

# Create a subplot for the increment button
increment_button_ax = plt.axes([0.05, 0.9, 0.15, 0.05])  # Define the position of the increment button
increment_button = widgets.Button(increment_button_ax, 'Fold Paper')
increment_button.on_clicked(on_increment_button_clicked)

# Create a subplot for the decrement button
decrement_button_ax = plt.axes([0.25, 0.9, 0.15, 0.05])  # Define the position of the decrement button
decrement_button = widgets.Button(decrement_button_ax, 'Unfold Paper')
decrement_button.on_clicked(on_decrement_button_clicked)

# Add counter text outside of the plot
counter_text = fig.text(0.02, 0.05, f'Fold Count = {n-1}', fontsize=12)
counter_text_length = fig.text(0.6, 0.9, f'Number of Lines = {2**(n-1)}', fontsize=12)

plt.show()
