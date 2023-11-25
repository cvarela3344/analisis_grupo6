from google_custom_search import buscar_en_google_custom_search

def buscar_tallerista(query):
    api_key = "AIzaSyBn_taWgFFDDDdqujQgQEr3veJEShdQUP4"
    cx = "f3f64d9d762a64f38"

    items=buscar_en_google_custom_search(query, api_key, cx, 5)

    json={}
    for item in items:
        if "tallerista" or "Tallerista" in item["title"]:
            print(f"Title: {item['title']}")
            print(f"Link: {item['link']}")
            json[item['title']]=item['link']

    return json
    