import requests

name = 'cheetah'
api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': 'h8K8W92qd/ArF16fhNcVuA==wGzxTfGlhhcUlXcl'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)