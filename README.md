# Sensor Signal Visualization

## Author
**Rafi Muhammad Zhafir**  
NRP: 2042231038  

## Overview
This project visualizes signals from various sensor types with noise and provides their frequency domain analysis using DFT (Discrete Fourier Transform). The graphical user interface (GUI) is built using **Tkinter** and integrated with **Matplotlib** for signal plotting.

## Features
- **Signal Simulation**: Generates signals for different sensor types, including Gyroscope, Accelerometer, Pressure, PIR, and Piezo-resistive sensors.
- **Noise Addition**: Simulates real-world noise in signals.
- **Frequency Analysis**: Computes and displays the DFT of noisy signals.
- **Interactive GUI**: Users can select sensor types, adjust noise parameters, and visualize results dynamically.

## Requirements
To run this project, ensure you have the following installed:
- Python 3.x
- Tkinter (comes pre-installed with Python)
- Matplotlib
- NumPy

## How to Use
1. Run the script: `python coba.py`.
2. Select a sensor type from the options.
3. Adjust noise amplitude and frequency using the sliders.
4. Observe the generated signal, noise, combined signal, and its DFT in real time.

## File Contents
- **`coba.py`**: Main Python script containing the GUI and signal processing code.

## Preview
The GUI features an intuitive layout with:
- Signal visualization.
- Noise parameter controls.
- Real-time updates upon user interaction.

## License
This project is open-source and available under the MIT License.
