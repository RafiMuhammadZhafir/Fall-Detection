import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Model Matematis

def generate_signal(sensor_type, t):
    if sensor_type == "Gyroscope":
        dt = t[1] - t[0]
        omega_x = 1 * np.sin(2 * np.pi * 0.5 * t)
        omega_y = 1 * np.cos(2 * np.pi * 0.5 * t)
        omega_z = 0.5 * np.sin(2 * np.pi * 0.5 * t + np.pi / 4)

        alpha = np.zeros(len(t))
        for i in range(1, len(t)):
            alpha[i] = alpha[i-1] + dt * (omega_y[i-1] * np.cos(0) - omega_z[i-1] * np.sin(0))
        return alpha, 0.1  # noise_std

    elif sensor_type == "Akselerometer":
        V_ref = 5
        C0 = 10e-12
        k = 1e-12
        a = np.sin(2 * np.pi * 2.5 * t)
        C1 = C0 + k * a
        C2 = C0 - k * a
        Vo = V_ref * (C1 - C2) / (C1 + C2)
        return Vo, 0.05  # noise_std

    elif sensor_type == "Tekanan":
        K_ps = 0.5
        P = 10 * np.sin(2 * np.pi * 1 * t)
        U_p = K_ps * P
        return U_p, 0.2  # noise_std

    elif sensor_type == "PIR":
        delta_T = np.piecewise(t, [t < 3, (t >= 3) & (t < 5), t >= 5], [0, 2, 0])
        sensitivity = 0.8
        return sensitivity * delta_T, 0.1  # noise_std

    elif sensor_type == "Piezo resistif":
        R0 = 1000
        kp = 0.01
        Rf = 1000
        Vref = 5.0
        P_max = 10
        frequency = 2
        P_t = P_max * np.sin(2 * np.pi * frequency * t)
        R_t = R0 * (1 + kp * P_t)
        Vrow_t = Vref * (R_t / (R_t + Rf))
        return Vrow_t, 0.15  # noise_std

    else:
        return np.zeros_like(t), 0

# Operasi sinyal
def add_signals(signal1, signal2):
    return signal1 + signal2

def calculate_dft(signal):
    return np.abs(np.fft.fft(signal))[:len(signal) // 2]

# Update Grafik
def update_plot(sensor_type):
    t = np.linspace(0, 10, 1000)
    signal, noise_std = generate_signal(sensor_type, t)
    noise = noise_std * np.random.normal(0, 1, len(t))
    signal_with_noise = add_signals(signal, noise)
    dft_result = calculate_dft(signal_with_noise)
    freq = np.linspace(0, len(dft_result), len(dft_result))

    # Grafik Sensor Signal
    axs[0].cla()
    axs[0].plot(t, signal, color='#1F77B4')
    axs[0].set_title(f"{sensor_type} Signal", color="white")
    axs[0].set_xlabel("Time [s]", color="white")
    axs[0].set_ylabel("Amplitude", color="white")
    axs[0].grid(color='#444444', linestyle='--')
    axs[0].tick_params(colors="white")

    # Grafik Noise
    axs[1].cla()
    axs[1].plot(t, noise, color='#FF7F0E')
    axs[1].set_title("Noise Signal", color="white")
    axs[1].set_xlabel("Time [s]", color="white")
    axs[1].set_ylabel("Amplitude", color="white")
    axs[1].grid(color='#444444', linestyle='--')
    axs[1].tick_params(colors="white")

    # Grafik Signal with Noise
    axs[2].cla()
    axs[2].plot(t, signal_with_noise, color='#2CA02C')
    axs[2].set_title("Signal with Noise", color="white")
    axs[2].set_xlabel("Time [s]", color="white")
    axs[2].set_ylabel("Amplitude", color="white")
    axs[2].grid(color='#444444', linestyle='--')
    axs[2].tick_params(colors="white")

    # Grafik DFT
    axs[3].cla()
    axs[3].plot(freq, dft_result, color='#9467BD')
    axs[3].set_title("DFT Result", color="white")
    axs[3].set_xlabel("Frequency [Hz]", color="white")
    axs[3].set_ylabel("Amplitude", color="white")
    axs[3].grid(color='#444444', linestyle='--')
    axs[3].tick_params(colors="white")

    canvas.draw()

# GUI dengan tema gelap
root = tk.Tk()
root.title("Sensor Signal Visualization")
root.geometry("1200x900")
root.configure(bg="#1E1E1E")

header = tk.Label(root, text="Sensor Signal Visualization", font=("Helvetica", 24, "bold"), bg="#1E1E1E", fg="#FFFFFF")
header.pack(pady=10)
subheader = tk.Label(root, text="Rafi Muhammad Zhafir\n2042231038\n3B", font=("Helvetica", 14), bg="#1E1E1E", fg="#FFFFFF")
subheader.pack()
separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", pady=10)

# Kontrol
control_frame = tk.Frame(root, bg="#1E1E1E")
control_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=15, pady=10)

ttk.Label(control_frame, text="Select Sensor:", background="#1E1E1E", foreground="white").pack(pady=5)
sensor_options = ["Gyroscope", "Akselerometer", "Tekanan", "PIR", "Piezo resistif"]
for sensor in sensor_options:
    ttk.Button(control_frame, text=sensor, command=lambda s=sensor: update_plot(s)).pack(pady=2)

ttk.Label(control_frame, text="Noise Amplitude:", background="#1E1E1E", foreground="white").pack(pady=5)
noise_amp = tk.DoubleVar(value=3.0)
tk.Scale(control_frame, variable=noise_amp, from_=0, to=10, resolution=0.1, orient=tk.HORIZONTAL, bg="#1E1E1E", fg="white", highlightthickness=0).pack()

ttk.Label(control_frame, text="Noise Frequency:", background="#1E1E1E", foreground="white").pack(pady=5)
noise_freq = tk.DoubleVar(value=1.0)
tk.Scale(control_frame, variable=noise_freq, from_=0, to=10, resolution=0.1, orient=tk.HORIZONTAL, bg="#1E1E1E", fg="white", highlightthickness=0).pack()

# Plot
fig, axs = plt.subplots(4, 1, figsize=(8, 12), facecolor="#1E1E1E")
fig.subplots_adjust(left=0.1, hspace=0.5, top=0.95, bottom=0.05)
for ax in axs:
    ax.set_facecolor("#1E1E1E")
    ax.spines['bottom'].set_color("white")
    ax.spines['top'].set_color("white")
    ax.spines['right'].set_color("white")
    ax.spines['left'].set_color("white")

canvas = FigureCanvasTkAgg(fig, root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

root.mainloop()