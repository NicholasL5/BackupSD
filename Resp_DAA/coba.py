import tkinter as tk

# Create the main window
window = tk.Tk()

# Create the outer frame
outer_frame = tk.Frame(window, width=200, height=100)

# Create the inner frame
inner_frame = tk.Frame(outer_frame, width=100, height=50)

# Create the buttons
button1 = tk.Button(inner_frame, text="Button 1")
button2 = tk.Button(inner_frame, text="Button 2")
button3 = tk.Button(inner_frame, text="Button 3")
button4 = tk.Button(inner_frame, text="Button 4")

# Add the buttons to the inner frame using the pack layout manager
button1.pack(side="top", fill="both", expand=True)
button2.pack(side="top", fill="both", expand=True)
button3.pack(side="bottom", fill="both", expand=True)
button4.pack(side="bottom", fill="both", expand=True)

# Add the inner frame to the outer frame using the pack layout manager
inner_frame.pack(fill="both", expand=True)

# Add the outer frame to the main window using the pack layout manager
outer_frame.pack(fill="both", expand=True)

# Run the main loop
window.mainloop()
