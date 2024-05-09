import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import json
from createimage import fetch_image, save_image

def animalLookup(name):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'K0n0ilc/kRLfORd5u5auow==fxuuCxG3s7yt4T5Q'})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        print("Error:", response.status_code, response.text)

animal_data = None
photo_images = []

def show_species():
    global animal_data
    animal = animal_entry.get().lower()
    animal_data_json = animalLookup(animal)
    if animal_data_json:
        animal_data = json.loads(animal_data_json)
        species_listbox.delete(0, tk.END)
        for species_dict in animal_data:
            species_name = species_dict.get('name')
            if species_name:
                species_listbox.insert(tk.END, species_name)
    else:
        messagebox.showerror("Error", "Animal not found")

def show_info():
    global animal_data
    selected_index = species_listbox.curselection()
    if selected_index:
        selected_species = species_listbox.get(selected_index)
        selected_species_data = next((species_dict for species_dict in animal_data if species_dict.get('name') == selected_species), None)
        if selected_species_data:
            img = fetch_image(selected_species.lower())
            img_path = save_image(selected_species.lower(), img)
            if img_path:
                create_window(selected_species_data['characteristics'], img_path, selected_species_data['taxonomy'], selected_species_data['name'])
            else:
                messagebox.showerror("Error", "Failed to save image")
        else:
            messagebox.showerror("Error", "Species data not found")
    else:
        messagebox.showerror("Error", "Please select a species")

def create_window(description, img_path, facts, name):
    window = tk.Toplevel()
    window.title("Information Window")

    top_frame = tk.Frame(window)
    top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    bottom_frame = tk.Frame(window)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    img = Image.open(img_path)
    img = img.resize((200, 200))
    photo = ImageTk.PhotoImage(img)
    photo_images.append(photo)
    image_label = tk.Label(top_frame, image=photo)
    image_label.image = photo
    image_label.pack(side=tk.LEFT, padx=10, pady=10)

    family = facts.get('family', '')
    genus = facts.get('genus', '')
    scientific_name = facts.get('scientific_name', '')

    fact_text = f"""Name: {name}
    Family: {family}
    Genus: {genus}
    Scientific Name: {scientific_name}"""

    info_label = tk.Label(top_frame, text=fact_text)
    info_label.pack(side=tk.RIGHT, padx=10, pady=10)

    info_text = ''
    for thing in description:
        info_text += f'''{thing.capitalize().replace("_", " ")}: {description[thing]}\n'''
    bottom_info_label = tk.Label(bottom_frame, text=info_text)
    bottom_info_label.pack(padx=10, pady=10)

    window.mainloop()

root = tk.Tk()
root.title("Animal Species Information")

animal_label = tk.Label(root, text="Enter Animal:")
animal_label.pack()

animal_entry = tk.Entry(root, width=50, font=('Helvetica', 14))
animal_entry.pack()

show_button = tk.Button(root, text="Show Species", command=show_species)
show_button.pack()

species_label = tk.Label(root, text="Species:")
species_label.pack()

species_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=60, height=10, font=('Helvetica', 12))
species_listbox.pack()

info_button = tk.Button(root, text="Show Info", command=show_info)
info_button.pack()

root.mainloop()
