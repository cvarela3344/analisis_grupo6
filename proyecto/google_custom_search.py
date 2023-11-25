import requests

def buscar_en_google_custom_search(query, api_key, cx, n):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": api_key,
        "cx": cx,
        "num": n
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        items = data.get("items", [])

    else:
        print("Error al realizar la solicitud.")
    
    print(response.status_code)
    return items
