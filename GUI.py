import tkinter as tk
from tkinter import PhotoImage
import os
def create_window(description, img_path, facts):
    # Create main window
    window = tk.Tk()
    window.title("Information Window")

    # Create frame for the bottom half of the window
    bottom_frame = tk.Frame(window)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Create frame for the top half of the window
    top_frame = tk.Frame(window)
    top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Load and display image
    img = PhotoImage(file=img_path)
    image_label = tk.Label(top_frame, image=img)
    image_label.pack(side=tk.LEFT, padx=10, pady=10)

    # Add more information
    info_label = tk.Label(top_frame, text=facts)
    info_label.pack(side=tk.RIGHT, padx=10, pady=10)

    # Add information in the bottom frame
    info_text = description
    bottom_info_label = tk.Label(bottom_frame, text=info_text)
    bottom_info_label.pack(padx=10, pady=10)

    window.mainloop()

# Call the function to create the window

penguin = {}

desc = """Penguins are a group of aquatic flightless birds. They live almost exclusively 
        in the Southern Hemisphere. Highly adapted for life in the ocean water, penguins
        have countershaded dark and white plumage and flippers for swimming. Most penguins
        feed on kill, fish, squid and other forms of sea life which they catch with their bills 
        and swallow while swimming."""

img = os.path.join("images", "penguin.PNG")

facts = """Family: Spheniscidae\nOrder: Sphenisciformes\n
other\ninfomration\n probably"""
create_window(desc, img, facts)