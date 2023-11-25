import openai
import requests
import re
import json

openai.api_key = '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'
api_key = "AIzaSyCy1y474q1qS3OLBfcauIISBSXVZSsR7AU"

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

#ESPACIOSSSSS


def buscar_espacios(query):
    cx="d29f55b8b82f846e4"

    items=buscar_en_google_custom_search(query, api_key, cx, 5)

    json={}
    for item in items:
            print(f"Title: {item['title']}")
            print(f"Link: {item['link']}")
            json[item['title']]=item['link']

    return json


#INSUMOOOOOSSS

def buscar_insumos(query):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query+" Enlistame todo y con las cantidades especificas entre parentesis al final de cada linea, ya sean unidades, kilos o litros. Delante de cada nombre de insumo ponle un guion.",
        max_tokens=500 
    )

    print(response.choices[0].text.strip())
    texto=response.choices[0].text.strip()

    insumos = {}

    patron = re.compile(r'-(.*)\((.*?)\)')

    lineas = texto.strip().split('\n')

    for linea in lineas:
        match = patron.match(linea)
        if match:
            nombre_insumo = match.group(1).strip()
            cantidad = match.group(2)
            insumos[nombre_insumo] = cantidad


    print(insumos)

    api_key = "AIzaSyCy1y474q1qS3OLBfcauIISBSXVZSsR7AU"
    cx = "57b7d679f20704b69"

    json={}

    for insumo in insumos:
        items=buscar_en_google_custom_search(insumo, api_key, cx, 1)

        for item in items:
            print("\n"+f"Title: {item['title']}")
            print(f"Link: {item['link']}")
            json[item['title']]=item['link']

    return json

#TALLERISTASSSSSS

def buscar_tallerista(query):
    cx = "f3f64d9d762a64f38"

    items=buscar_en_google_custom_search(query, api_key, cx, 5)

    json={}
    for item in items:
        if "tallerista" or "Tallerista" in item["title"]:
            print(f"Title: {item['title']}")
            print(f"Link: {item['link']}")
            json[item['title']]=item['link']

    return json


def hacer_taller(json_data):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=json_data["user_input"]+" en base a eso necesito que me enumeres 3 cosas poniendo el numero al comienzo. lo que quiero que me enumeres es, 1: que profesional necesito para impartir el taller, 2: que insumos necesito a su vez estos deben estar enlistados todos y con las cantidades especificas entre parentesis al final de cada linea, ya sean unidades, kilos o litros. Delante de cada nombre de insumo ponle un guion y para finalizar 3:que lugar necesito arrendar para realizar el taller, pero sin describirlo, solo el tipo de establecimiento",
        max_tokens=500 
    )

    print(response.choices[0].text.strip())
    texto=response.choices[0].text.strip().split(":")
    
    query1=texto[0][1:]
    query2=texto[1][1:]
    query3=texto[2][1:]
    
    tallerista=buscar_tallerista(query1)
    
    insumos=buscar_insumos(query2)
    
    espacios=buscar_espacios(query3+"para arrendar")
    
    json = {}
    json['Posibles talleristas']=tallerista
    json['Posibles espacios']=espacios
    json['Lista de insumos']=insumos
    json['Fecha de inicio']=json_data["selected_date"]
    json['Duracion']=json_data["selected_hours"]
    
    with open("logs/sample.json", "w") as outfile:
        json.dump(json, outfile)
    
    return json
    