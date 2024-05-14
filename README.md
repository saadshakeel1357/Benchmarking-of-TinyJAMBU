# Benchmarking of TinyJAMBU Algorithm

## Overview

The benchmarking process involves running a shell script, `build.sh`, through the NIST framework on a signboard using PlatformIO. The script automates the benchmarking process and saves the results to the outputs folder.

## Shell Script

The `build.sh` shell script contains a sequence of shell commands and is executed through the Windows Subsystem for Linux (WSL) terminal on Windows operating systems.

## Benchmarking Process

The benchmarking process includes Known Response Tests (KAT) and Size experiments. KAT results are stored in the `kat` subdirectory, while size experiments categorize results into both encryption-only and decryption-only scenarios, organizing relevant data into tables.

## Data Extraction

Data extracted includes RAM usage, Flash memory usage, execution time, encryption time, and decryption time. Extracted data is organized into tables for later analysis.

## Visualization Tool

A Python script, adapted from the author's semester 1 Bachelor Semester Project (BSP), is used to develop a visualization tool. The script utilizes Tkinter to create a graphical interface for visualizing benchmarking results stored in CSV files. This tool facilitates the comparison of performance metrics between different optimization indicators.

## Conclusion

The provided technical deliverable meets the requirements by effectively benchmarking the TinyJAMBU algorithm and providing a visualization tool for data analysis.
