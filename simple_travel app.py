import tkinter as tk 

from tkinter import messagebox

# Dictionary for base travel cost

DESTINATIONS = {

    "Paris" : 1200,

    "New York" : 1000,

    "Tokyo" : 1500,

    "London" : 1100

}

#Extra cost based on model of travel

TRAVEL_MODE_COST = {

    "Flight" : 300,

    "Train" : 100

} 

def calculate_cost():
    
    name = name_entry.get()

    destination = destination_var.get()

    mode = mode_var.get()

    if not name:

        messagebox.showerror("Error", "Please enter your name.")

        return
    
    if destination == "" or mode == "":

        messagebox.showerror("Error", "Please select destination and travel mode.")

        return

    cost = DESTINATIONS[destination] + TRAVEL_MODE_COST[mode]

    result = f"Hi {name}, your estimated travel cost to {destination} by {mode} is ${cost}."

    messagebox.showinfo("Travel Estimate", result)

#create main window

root = tk.Tk()

root.title("Basic Traveling App")

root.geometry("350x300")

    # Widgets

tk.Label(root, text="Welcome to TravelEasy", font=("Helvetica", 16)).pack(pady=10)

tk.Label(root, text="Enter your name:").pack()

name_entry = tk.Entry(root)

name_entry.pack()

tk.Label(root, text="Choose Destination:").pack()

destination_var = tk.StringVar()

destination_menu = tk.OptionMenu(root, destination_var, *DESTINATIONS.keys())

destination_menu.pack()

tk.Label(root, text="Select Travel Mode:").pack()

mode_var = tk.StringVar()

tk.Radiobutton(root, text="Flight", variable=mode_var, value="Flight").pack()

tk.Radiobutton(root, text="Train", variable=mode_var, value="Train").pack()

tk.Button(root, text="Calculate Cost", command=calculate_cost).pack(pady=10)

# Run the app

root.mainloop()




