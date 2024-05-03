import requests


def getanimalinfo(animal: str):
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal}'
    response = requests.get(api_url, headers={'X-Api-Key': 'h8K8W92qd/ArF16fhNcVuA==wGzxTfGlhhcUlXcl'})
    if response.status_code == requests.codes.ok:
        data = response.json()
        print(data[0]['taxonomy']['scientific_name'])
    else:
        print("Error:", response.status_code, response.text)

getanimalinfo('penguin')



