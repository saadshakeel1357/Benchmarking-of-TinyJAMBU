# TinyJAMBU Benchmark Visualization Tool

## Description
This project provides an interactive visualization interface for analyzing benchmark results of TinyJAMBU, a cryptographic algorithm. It is designed to assist users in comparing how various optimization settings affect code size, execution time, and memory usage between two versions of the TinyJAMBU implementation.

## Features
- Interactive Graphical User Interface (GUI) built with Tkinter.
- Options to select different types of experiments (e.g., Code Size, KAT).
- Dynamically updated dropdown menus based on selected visualization type.
- Plotting capabilities using Matplotlib for insightful visualizations.
- Customizable visualization options for different dependent variables (Time, RAM Memory, Flash Memory).
- Exception handling for file reading and user input validation.

## Installation
To run this visualization tool, you need Python installed on your machine along with several libraries. 

### Prerequisites
- Python 3.x
- Pandas
- Matplotlib
- Numpy
- Tkinter (usually comes pre-installed with Python)

### Setup
Clone this repository. The benchmark_results_final.csv file should be in the same directory. 

## Usage
1. Launch the tool by running the Python script.
2. Choose the type of experiment and dependent variables from the dropdown menus.
3. For 'Code Size' experiments, additional options are available for more specific visualizations.
4. Click 'Show Visualization' to view the generated plot.
