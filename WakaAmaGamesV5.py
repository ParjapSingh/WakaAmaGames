# Importing all my libraries
import os
import tkinter as tk
from tkinter import messagebox

# Create the main setup
class WakaAmaApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set up the main window which will be displayed
        self.title("Waka Ama Games")
        self.geometry("400x300")
        self.selected_year = None  # Store selected year for future use

        # Welcome screen
        self.show_welcome()

    # Clear screen for future purpose when we change screens
    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    # Show the welcome screen with input instead of buttons
    def show_welcome(self):
        self.clear_screen()

        # Welcome message (Will change font and sizes after feedback)
        tk.Label(self, text="Welcome to Waka Ama Games", font=("Arial", 20)).pack(pady=10)
        tk.Label(self, text="Enter the year you want to analyse (e.g. 2015):", font=("Arial", 12)).pack(pady=10)

        # input box
        self.year_entry = tk.Entry(self, font=("Arial", 12))
        self.year_entry.pack(pady=5)

        # search button for users when they enter a year
        tk.Button(self, text="Search", font=("Arial", 12), command=self.handle_year_input).pack(pady=10)

   
    def handle_year_input(self):
        year_input = self.year_entry.get().strip()

        # Check if input is a valid input 
        if not year_input.isdigit() or len(year_input) != 4:
            messagebox.showerror("Invalid Input", "Invalid year entered. Please enter a valid 4-digit year like 2019 and avoid using alphabet for eg two thousand nine teen.")
            return

        self.analyze_year(year_input)

    # When a year is selected, it changes the WakaNats(year) to the year selected
    def analyze_year(self, year):
        folder = f"WakaNats{year}"

        # Check if the folder exists otherwise error message and loops to start once clicked okay
        if not os.path.exists(folder):
            messagebox.showerror("Folder Not Found", f"The folder '{folder}' was not found.\nPlease make sure your code file is in the same folder as the WakaNats files.\n And make sure it is named WakaNats(year)")
            self.show_welcome()
            return

        self.clear_screen()
        self.selected_year = year

        # Title and file count display
        tk.Label(self, text=f"Waka Ama {year}", font=("Arial", 20)).pack(pady=20)

        files = os.listdir(folder)
        lif_files = [f for f in files if f.lower().endswith('.lif')]
        # to store the lif files so that when we filter to Finals only we use this and other future purpose
        self.lif_files = lif_files

        tk.Label(self, text=f"Found {len(lif_files)} .lif files in '{folder}'", font=("Arial", 12)).pack(pady=10)

        # Analyse button which will analyze the lif files and filter to finals only (.pack auttomatically positions the buttons so that I dont do it manually)
        tk.Button(self, text="Analyse This Year", font=("Arial", 12), command=self.analyze_finals).pack(pady=20)

    def analyze_finals(self):
        self.clear_screen()

        # Display "Loading..." screen (need to fix this as it isnt being displayed as it runs too fast)
        loading_label = tk.Label(self, text="Loading...", font=("Arial", 14))
        loading_label.pack(pady=30)
        self.update() 

        # Filter for only finals files
        finals_files = [f for f in self.lif_files if "final" in f.lower()]

        # Clear loading screen and show number of files
        self.clear_screen()
        tk.Label(self, text=f"Found {len(finals_files)} number of Final files", font=("Arial", 16)).pack(pady=30)

# Start the program
if __name__ == "__main__":
    app = WakaAmaApp()
    app.mainloop()
