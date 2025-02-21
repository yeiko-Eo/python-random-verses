import json, random, tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk() 
root.config(bd=5, relief="solid")
root.title("Random verse generator") # Set the title of the window
root.geometry("1080x250") # Set the size of the window
root.resizable(False, False) # Disable resizing
root.configure(bg="#222831") # Set the background color of the window

def load_verses(filename = "rand-verses.json"): # Load verses from a JSON file
    try:
        with open(filename, "r", encoding="utf-8") as file: # Open the file in read mode with UTF-8 encoding
            data = json.load(file) # Load the JSON file into the data variable
        return data["verses"] # Return the list of verses
    except FileNotFoundError as x: 
        messagebox.showerror(f"Error: {x}") 
        return []
    except json.JSONDecodeError: # If there is an error reading the JSON file
        messagebox.showerror("Error reading the JSON file")
        return [] # Return an empty list

def get_random_verse():
    verses = load_verses()
    if verses: 
        return random.choice(verses) # Return a random verse
    return "No verses available" # If no verses are available

# Create the answer
result_var = tk.StringVar()
result = tk.Entry(root, justify="center", state="readonly", textvariable=result_var, font=("Arial", 9, "bold"))

def update_verse():
    verse = get_random_verse() # Get a random verse
    result_var.set(verse) # Update the text of the entry

# Create the options
menu_label = tk.Label(root, text="-- VERSES --", font=("Arial", 12, "bold"), bg="#FBFFE4")
opc = tk.Button(root, text="Generate a random verse", command=update_verse)

# Adding borders
menu_label.config(borderwidth=2.5, relief='solid', fg="#00ADB5")
result.config(borderwidth=2.5, relief='solid', fg="#00ADB5")
opc.config(borderwidth=2.5, relief='solid', fg="#00ADB5")

# Positions
menu_label.pack(pady=10)
result.pack(pady=20, ipadx=10, ipady=10)
opc.pack(ipady=7, pady=5)

# Adjust the size of the entry to fit the text
result.bind("<Configure>", lambda e: result.config(width=len(result_var.get())))
result.pack(fill="x", expand=True, pady=10, ipadx=5, ipady=5)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop() # Start the main loop