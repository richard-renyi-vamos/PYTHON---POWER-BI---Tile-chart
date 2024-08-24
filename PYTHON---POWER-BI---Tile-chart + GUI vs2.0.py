import tkinter as tk
from tkinter import ttk
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Metric 1': [20, 34, 30, 35, 27],
    'Metric 2': [25, 32, 34, 20, 25],
    'Metric 3': [22, 27, 31, 30, 29],
    'Metric 4': [18, 30, 27, 22, 26],
}

# Create a DataFrame
df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

# Function to create and update the tile chart
def create_tile_chart(cmap, show_annotations):
    plt.clf()  # Clear the previous plot
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(df, annot=show_annotations, cmap=cmap, cbar=True, linewidths=0.5, ax=ax)
    ax.set_title('Tile Chart (Heatmap) Example')
    ax.set_xlabel('Metrics')
    ax.set_ylabel('Categories')

    canvas.draw()

# GUI setup
root = tk.Tk()
root.title('Tile Chart Settings')

# Dropdown for colormap selection
ttk.Label(root, text="Choose Colormap:").grid(column=0, row=0, padx=10, pady=5)
colormap = tk.StringVar()
colormap_dropdown = ttk.Combobox(root, textvariable=colormap)
colormap_dropdown['values'] = ('YlGnBu', 'coolwarm', 'viridis', 'magma', 'plasma', 'cividis')
colormap_dropdown.current(0)  # Set default value
colormap_dropdown.grid(column=1, row=0, padx=10, pady=5)

# Checkbox for annotations
show_annotations = tk.BooleanVar()
ttk.Checkbutton(root, text="Show Annotations", variable=show_annotations).grid(column=0, row=1, padx=10, pady=5)

# Button to update chart
def update_chart():
    create_tile_chart(colormap.get(), show_annotations.get())

ttk.Button(root, text="Update Chart", command=update_chart).grid(column=0, row=2, columnspan=2, pady=10)

# Plot area in the GUI
fig, ax = plt.subplots(figsize=(8, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(column=0, row=3, columnspan=2)

# Initialize the chart
create_tile_chart('YlGnBu', show_annotations.get())

# Start the GUI loop
root.mainloop()
