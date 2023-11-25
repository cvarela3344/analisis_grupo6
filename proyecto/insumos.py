import openai
import re
openai.api_key = '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'
from google_custom_search import buscar_en_google_custom_search

def buscar_insumos(query):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
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

















