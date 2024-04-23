
import tkinter as tk

class Pokedex:
    def __init__(self, master):
        self.master = master
        self.master.title("AnimalDex")

        self.label_name = tk.Label(master, text="Animal Name:")
        self.label_name.grid(row=0, column=0, sticky="w")

        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1)

        self.btn_search = tk.Button(master, text="Search", command=self.search_animal)
        self.btn_search.grid(row=0, column=2)

        self.label_info = tk.Label(master, text="Animal Information:")
        self.label_info.grid(row=1, column=0, columnspan=3, sticky="w")

        self.text_info = tk.Text(master, width=50, height=10)
        self.text_info.grid(row=2, column=0, columnspan=3)

    def search_animal(self):
        animal_name = self.entry_name.get()
        animal_info = self.get_animal_info(animal_name)
        self.display_animal_info(animal_info)

    def get_animal_info(self, animal_name):
        # placeholder function to search information about the animal
        # will update function later to show pictures and more animals
        animal_data = {
            "Tiger": "The tiger is the largest cat species and a member of the genus Panthera.",
            "Elephant": "Elephants are mammals of the family Elephantidae and the largest existing land animals.",
            "Penguin": "Penguins are a group of aquatic flightless birds.",
            # more animals go here
        }
        return animal_data.get(animal_name, "Animal not found in AnimalDex.")

    def display_animal_info(self, animal_info):
        self.text_info.delete(1.0, tk.END)
        self.text_info.insert(tk.END, animal_info)

def main():
    root = tk.Tk()
    app = Pokedex(root)
    root.mainloop()

if __name__ == "__main__":
    main()


