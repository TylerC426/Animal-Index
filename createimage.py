import requests
from bs4 import BeautifulSoup
from PIL import Image
import io
import os


def fetch_image_url(animal):
    search_query = f"{animal} animal site:unsplash.com"
    search_url = f"https://www.google.com/search?q={search_query}&tbm=isch"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()  # Check for HTTP request errors
        soup = BeautifulSoup(response.text, 'html.parser')
        # Look for direct image URLs
        for img in soup.find_all('img'):
            img_url = img.get('src')
            if img_url.startswith('http'):
                return img_url
        print("No valid images found.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image URL: {e}")
        return None

def fetch_image(animal):
    image_url = fetch_image_url(animal)
    if image_url:
        try:
            response = requests.get(image_url)
            response.raise_for_status()  # Check for HTTP errors
            img = Image.open(io.BytesIO(response.content))
            animal_image.save(os.path.join('images', f'{animal}.gif'))
            return img
        except requests.exceptions.RequestException as e:
            print(f"Error fetching image: {e}")
            return None
    else:
        return None

# Example usage:
animal_name = "adelie penguin"
animal_image = fetch_image(animal_name)
if animal_image:
    animal_image.show()
    animal_image.save(os.path.join('images', f'{animal_name}.gif'))
else:
    print("Image not found.")
