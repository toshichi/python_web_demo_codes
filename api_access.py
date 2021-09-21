# To get a random sentence from https://catfact.ninja/fact

import requests

if __name__ == "__main__":
    response = requests.get('https://catfact.ninja/fact')
    data = response.json()
    print(data['fact'])