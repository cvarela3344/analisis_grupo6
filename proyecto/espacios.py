import requests
from google_custom_search import buscar_en_google_custom_search

def buscar_espacios(query):
    cx="d29f55b8b82f846e4"
    api_key = "AIzaSyCy1y474q1qS3OLBfcauIISBSXVZSsR7AU"

    items=buscar_en_google_custom_search(query, api_key, cx, 5)

    json={}
    for item in items:
            print(f"Title: {item['title']}")
            print(f"Link: {item['link']}")
            json[item['title']]=item['link']

    return json