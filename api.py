import requests
from GUI import *
from images import *


def getanimalinfo(animal: str):
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal}'
    headers = {'X-Api-Key': 'h8K8W92qd/ArF16fhNcVuA==wGzxTfGlhhcUlXcl'}
    response = requests.get(api_url, headers=headers)

    if response.status_code == requests.codes.ok:
        data = response.json()[0]
        description = f"{data[0]['name']} belongs to the family {data['taxonomy']['family']} and the order {data['taxonomy']['order']}."
        facts = (f"Lifespan: {data[0]['characteristics']['lifespan']}\n"
                 f"Habitat: {data[0]['characteristics']['habitat']}\n"
                 f"Locations: {', '.join(data[0]['locations'])}")

        # Creates the image and saves it

        img_path = f"{data[0]['name']}.jpg"
        create_window(description, img_path, facts)
    else:
        print("Error:", response.status_code, response.text)



# Example call to test
getanimalinfo("Adelie Penguin")




