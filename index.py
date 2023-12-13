import requests

def get_url(url):
    response = requests.get(url)
    return response.text

# Ejemplo de uso
url = "https://jsonplaceholder.typicode.com/users"
result = get_url(url)
print(result)
