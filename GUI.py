import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import os
import requests
import json
from PIL import Image, ImageTk

def animalLookup(name):
    name = name
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'K0n0ilc/kRLfORd5u5auow==fxuuCxG3s7yt4T5Q'})
    if response.status_code == requests.codes.ok:
        return response.text
        #print(response.text)
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
        # Fetch information about the selected species and display it
        selected_species_data = None
        for species_dict in animal_data:
            if species_dict.get('name') == selected_species:
                selected_species_data = species_dict
                break
        if selected_species_data:
            img = os.path.join("images", "Penguin.PNG")
            characteristics = selected_species_data.get('characteristics')
            scientific_name = selected_species_data.get('taxonomy')
            name = selected_species_data.get('name')
            create_window(characteristics, img, scientific_name, name)
        else:
            messagebox.showerror("Error", "Species data not found")
    else:
        messagebox.showerror("Error", "Please select a species")

        

def create_window(description, img_path, facts, name):
    # Create main window
    window = tk.Toplevel()
    window.title("Information Window")

    # Create frame for the bottom half of the window
    bottom_frame = tk.Frame(window)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Create frame for the top half of the window
    top_frame = tk.Frame(window)
    top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Load and display image
    img = Image.open(img_path)
    img = img.resize((200, 200))
    photo = ImageTk.PhotoImage(img)
    photo_images.append(photo)
    image_label = tk.Label(top_frame, image=photo)
    image_label.image = photo
    image_label.pack(side=tk.LEFT, padx=10, pady=10)


   

    prey = description.get('prey', '')
    group_behavior = description.get('goup_behavior', '')
    estimated_population_size = description.get('estimated_population_size', '')
    most_distinctive_feature = description.get('distinctive_feature', '')
    if len(most_distinctive_feature) <= 3:
        most_distinctive_feature = description.get('most_distinctive_feature', '')
    habitat = description.get('habitat', '')
    diet = description.get('diet', '')
    common_name = description.get('common_name', '')
    location = description.get('location', '')
    group = description.get('group', '')
    lifespan = description.get('lifespan', '')
    family = facts.get('family', '')
    genus = facts.get('genus', '')
    scientific_name = facts.get('scientific_name', '')
    funFact = description.get('slogan', '')


    fact_text = f"""Name: {name}
    Family: {family}
    Genus: {genus}
    Scientific Name: {scientific_name}"""


 # Add more information
    info_label = tk.Label(top_frame, text=fact_text)
    info_label.pack(side=tk.RIGHT, padx=10, pady=10)

    # Add information in the bottom frame
    info_text = ''
    for thing in description:
        info_text += f'''{thing.capitalize().replace("_", " ")}: {description[thing]}\n'''
    bottom_info_label = tk.Label(bottom_frame, text=info_text)
    bottom_info_label.pack(padx=10, pady=10)

    window.mainloop()


# Create the main window
root = tk.Tk()
root.title("Animal Species Information")

# Create labels, entry, and buttons
animal_label = tk.Label(root, text="Enter Animal:")
animal_label.pack()

animal_entry = tk.Entry(root)
animal_entry.pack()

show_button = tk.Button(root, text="Show Species", command=show_species)
show_button.pack()

species_label = tk.Label(root, text="Species:")
species_label.pack()

species_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
species_listbox.pack()

info_button = tk.Button(root, text="Show Info", command=show_info)
info_button.pack()

# Run the main event loop
root.mainloop()

