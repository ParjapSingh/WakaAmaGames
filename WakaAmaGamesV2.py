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

    # defining my functions to create the buttons
    def select_2017(self):
        self.analyze_year("2017")

    def select_2018(self):
        self.analyze_year("2018")

    # Show the welcome screen 2017 and 2018 buttons
    def show_welcome(self):
        self.clear_screen()

        # Welcome message (Will change font and sizes after feedback)
        tk.Label(self, text="Welcome to Waka Ama Games", font=("Arial", 16)).pack(pady=10)
        tk.Label(self, text="Choose a year to analyse:", font=("Arial", 12)).pack(pady=10)

        # Buttons for 2017 and 2018
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="2017", width=10, command=self.select_2017).pack(side="left", padx=10)
        tk.Button(button_frame, text="2018", width=10, command=self.select_2018).pack(side="left", padx=10)
        
# Start the program
if __name__ == "__main__":
    app = WakaAmaApp()
    app.mainloop()