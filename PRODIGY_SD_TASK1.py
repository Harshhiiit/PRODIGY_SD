import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temp = float(entry_temperature.get())
        original_unit = selected_unit.get()

        if original_unit == 'Celsius':
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            result_fahrenheit.set(f"{fahrenheit:.2f} °F")
            result_kelvin.set(f"{kelvin:.2f} K")

        elif original_unit == 'Fahrenheit':
            celsius = (temp - 32) * 5/9
            kelvin = celsius + 273.15
            result_celsius.set(f"{celsius:.2f} °C")
            result_kelvin.set(f"{kelvin:.2f} K")

        elif original_unit == 'Kelvin':
            celsius = temp - 273.15
            fahrenheit = (celsius * 9/5) + 32
            result_celsius.set(f"{celsius:.2f} °C")
            result_fahrenheit.set(f"{fahrenheit:.2f} °F")

    except ValueError:
        result_celsius.set("Invalid input")
        result_fahrenheit.set("Invalid input")
        result_kelvin.set("Invalid input")

# Create the main window
root = tk.Tk()
root.title("Temperature Conversion")
root.geometry("400x250")  # Set window size
root.configure(bg="#f0f0f0")  # Set background color

# Create a style for the widgets
style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12, "bold"), foreground="#4CAF50")
style.configure("TRadiobutton", background="#f0f0f0", font=("Helvetica", 12))

# Create a frame for the input and radio buttons
frame_input = ttk.Frame(root, padding="20")
frame_input.grid(row=0, column=0, sticky=(tk.W, tk.E))

# Temperature entry
ttk.Label(frame_input, text="Enter Temperature:").grid(row=0, column=0, sticky=tk.W)
entry_temperature = ttk.Entry(frame_input, width=10, font=("Helvetica", 12))
entry_temperature.grid(row=0, column=1)

# Radio buttons for selecting the unit
selected_unit = tk.StringVar(value="Celsius")
ttk.Radiobutton(frame_input, text='Celsius', variable=selected_unit, value='Celsius').grid(row=1, column=0, sticky=tk.W)
ttk.Radiobutton(frame_input, text='Fahrenheit', variable=selected_unit, value='Fahrenheit').grid(row=1, column=1, sticky=tk.W)
ttk.Radiobutton(frame_input, text='Kelvin', variable=selected_unit, value='Kelvin').grid(row=1, column=2, sticky=tk.W)

# Convert button
ttk.Button(frame_input, text="Convert", command=convert_temperature).grid(row=2, column=1, pady=10)

# Labels for displaying the results
frame_output = ttk.Frame(root, padding="20")
frame_output.grid(row=1, column=0, sticky=(tk.W, tk.E))

result_celsius = tk.StringVar()
result_fahrenheit = tk.StringVar()
result_kelvin = tk.StringVar()

ttk.Label(frame_output, text="Celsius:").grid(row=0, column=0, sticky=tk.W)
ttk.Label(frame_output, textvariable=result_celsius).grid(row=0, column=1, sticky=tk.W)

ttk.Label(frame_output, text="Fahrenheit:").grid(row=1, column=0, sticky=tk.W)
ttk.Label(frame_output, textvariable=result_fahrenheit).grid(row=1, column=1, sticky=tk.W)

ttk.Label(frame_output, text="Kelvin:").grid(row=2, column=0, sticky=tk.W)
ttk.Label(frame_output, textvariable=result_kelvin).grid(row=2, column=1, sticky=tk.W)

# Start the GUI event loop
root.mainloop()
