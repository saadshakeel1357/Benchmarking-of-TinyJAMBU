import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Attempt to read a CSV file and handle exceptions if any errors occur
try:
    df = pd.read_csv('benchmark_results_final.csv')
except Exception as e:
    messagebox.showerror("Error", "An error occurred while reading the file:\n" + str(e))
    exit()

def get_axis(graph_type, y_value, additional=None):
    """
    Determines the y-axis values for the plot based on the graph type, y-value, and additional options.
    
    Parameters:
        graph_type (str): The type of graph to be plotted.
        y_value (str): The primary y-value for the graph.
        additional (str, optional): Additional criteria for determining y-axis values.

    Returns:
        list: A list of columns from the DataFrame that match the criteria for the y-axis.
    """
    if additional is not None:
        # Filter columns that match the criteria when 'additional' is provided
        matching_columns = [col for col in df.columns if graph_type.split()[1].lower() in col.lower()]
        matching_columns_2 = [col for col in matching_columns if y_value.split()[0].lower() in col.lower()]
        y_axis_values = [col for col in matching_columns_2 if additional.split()[0][:3].lower() in col.lower()]
        return y_axis_values
    else:
        # Filter columns that match the criteria when 'additional' is not provided
        matching_columns = [col for col in df.columns if graph_type.split()[0].lower() in col.lower()]
        y_axis_values = [col for col in matching_columns if y_value.split()[0].lower() in col.lower()]
        return y_axis_values

def plot_visual(graph_type, y_value, additional=None):
    """
    Plots a bar chart based on the specified parameters.

    Parameters:
        graph_type (str): The type of graph to be plotted.
        y_value (str): The primary y-value for the graph.
        additional (str, optional): Additional criteria for determining y-axis values.
    """
    x_value = df["release"]
    x_label = "Optimization Flag"

    # Set up positions for bars
    bar_width = 0.35
    index = np.arange(len(x_value))

    # Plot the graph based on additional parameter
    if additional is not None:
        y_axis_values = get_axis(graph_type, y_value, additional)
        plt.bar(index, df[y_axis_values[0]], width=bar_width, label='Original code')
        plt.bar(index + bar_width, df[y_axis_values[1]], width=bar_width, label='Modified code')
        plt.title(f'{graph_type} experiment {y_value} with {additional}')

    else:
        y_axis_values = get_axis(graph_type, y_value)
        plt.bar(index, df[y_axis_values[0]], width=bar_width, label='Original code')
        plt.bar(index + bar_width, df[y_axis_values[1]], width=bar_width, label='Modified code')

        plt.title(f'{graph_type} experiment {y_value}')

    # Customize the plot
    if y_value == "Time":
        plt.ylabel(f"{y_value} (in seconds)")
    else:
        plt.ylabel(f"{y_value} usage pecentage (in %)")
    plt.xlabel(x_label)
    plt.xticks(index + bar_width / 2, x_value)
    plt.legend()

    plt.show()

def click():
    """
    Handles the button click event. This function is called when the 'Show Visualization' button is clicked.
    It triggers the plot generation based on the selected dropdown options.
    """
    # Display error if nothing selected
    if options1.get() == "Type of Experiment" or options2.get() == "Dependent variables":
        messagebox.showwarning("Message", "Please properly specify the visualisation desired ")
    else:
        if options1.get() == "Code Size":
            if options3.get() == "Options for Code Size Experiment":
                messagebox.showwarning("Message", "Please properly specify the visualisation desired ")
            plot_visual(options1.get(), options2.get(), options3.get())
        else:
            plot_visual(options1.get(), options2.get())


def on_type_selection(*args):
    """
    Callback function that updates the options in the third dropdown based on the selected visualization type.
    This is linked to the 'options1' dropdown.
    """
    selected_type = options1.get()

    # Update the visibility of options3 based on the selected type
    if selected_type == "Code Size":
        opt_menu3.grid(row=2, column=0)
    else:
        opt_menu3.grid_forget()

# Create the root window for the application
root = tk.Tk()
root.geometry("500x400")
root.title("Interactive Visualization Interface")

# Display heading inside tkinter window
heading = tk.Label(root, text="Visualization Tool for TinyJAMBU benchmark results", font=("Georgia", 18))
heading.pack(padx=30, pady=30)

# Define the layout grid for buttons/checkbox
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)

# Create dropdown menu to choose type of visualization
vis_type = ["Code Size", "KAT"]
options1 = tk.StringVar(root)
options1.set("Type of Experiment")
opt_menu1 = tk.OptionMenu(buttonframe, options1, *vis_type)
opt_menu1.config(font=("Arial", 12))
opt_menu1.grid(row=0, column=0)
options1.trace_add('write', on_type_selection)  # Add callback for type selection

# Create dropdown menu to choose dependent variable
dep_vars = ["Time", "RAM Memory", "Flash Memory"]
options2 = tk.StringVar(root)
options2.set("Dependent variables")
opt_menu2 = tk.OptionMenu(buttonframe, options2, *dep_vars)
opt_menu2.config(font=("Arial", 12))
opt_menu2.grid(row=1, column=0)

# Create dynamically updated dropdown menu based on the selected type
options3 = tk.StringVar(root)
options3.set("Options for Code Size Experiment")
opt_menu3 = tk.OptionMenu(buttonframe, options3, "Both Encryption and Decryption", "Encryption only", "Decryption only")
opt_menu3.config(font=("Arial", 12))

# Display the grid and the buttons/checkboxes
buttonframe.pack(fill='x', padx=50, pady=30)

# Add button that executes the "click" function when clicked
optbtn1 = tk.Button(root, text="Show Visualization", command=click, font=('Arial', 14))
optbtn1.pack(pady=10)

# Run the Tkinter Window
root.mainloop()
