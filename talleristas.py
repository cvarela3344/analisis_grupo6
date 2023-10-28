import requests

def buscar_en_google_custom_search(query, api_key, cx):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": api_key,
        "cx": cx
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        items = data.get("items", [])

        for item in items:
            if "tallerista" or "Tallerista" in item["title"]:
                print(f"Title: {item['title']}")
                print(f"Link: {item['link']}")
    else:
        print("Error al realizar la solicitud.")


query = input("Introduce tu consulta: ")
api_key = "AIzaSyBn_taWgFFDDDdqujQgQEr3veJEShdQUP4"
cx = "f3f64d9d762a64f38"
buscar_en_google_custom_search(query, api_key, cx)
