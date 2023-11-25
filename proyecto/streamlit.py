import streamlit as st
import pandas as pd
import json
import requests
from datetime import datetime

from crear_taller import *



def crear_taller():
    
    st.title('Crea un taller!')
    
    
    user_input = st.text_input("Introduce una breve descripcion del taller que deseas realizar", 
                               "Escribe aqui!")
    
    # Selector de intervalo de fechas
    selected_date = st.date_input("Selecciona un día", min_value=datetime(2023, 1, 1), max_value=datetime(2023, 12, 31))
    
    # Selector de horas
    selected_hours = st.slider("Selecciona las horas en las cuales te gustaria hacer el taller:", 0, 23, (8, 18))
    
    # Mostrar resultados seleccionados
    st.write(f"Dia del taller: {selected_date}")
    st.write(f"Horas seleccionadas: de {selected_hours[0]}:00 a {selected_hours[1]}:00")
    
    # Convertir a formato JSON
    data = {
        "user_input": user_input,
        "selected_date": selected_date.strftime("%Y-%m-%d"),
        "selected_hours": {
            "start": selected_hours[0],
            "end": selected_hours[1]
        }
    }
    
    
    
    # Mostrar resultados seleccionados
    st.write("Datos en formato JSON:")
    st.code(data)
    
    if st.button('Enviar a la API'):
        if user_input:
            st.write(f"Enviando data a la API...")
            api_response = hacer_taller(data)

            if api_response:
                st.write("Respuesta de la API:")
                st.write(api_response)
            else:
                st.write("Hubo un problema al obtener la respuesta de la API.")
        else:
            st.write("Por favor, introduce algún texto antes de enviar a la API.")


def busqueda_insumos():

    user_input = st.text_input("Introduce los insumos que deseas buscar, recuerda separarlos con comas.")

    
    
    if st.button('Enviar a la API'):
        if user_input:
            st.write(f"Enviando data a la API...")
            api_response = buscar_insumos(user_input)

            if api_response:
                st.write("Respuesta de la API:")
                st.write(api_response)
            else:
                st.write("Hubo un problema al obtener la respuesta de la API.")
        else:
            st.write("Por favor, introduce algún texto antes de enviar a la API.")
            

def busqueda_talleristas():

    user_input = st.text_input("Introduce el area de la cual buscas un tallerista, tambien puedes añadir una ubicacion.")

    
    if st.button('Enviar a la API'):
        if user_input:
            st.write(f"Enviando data a la API...")
            api_response = buscar_tallerista(user_input)

            if api_response:
                st.write("Respuesta de la API:")
                st.write(api_response)
            else:
                st.write("Hubo un problema al obtener la respuesta de la API.")
        else:
            st.write("Por favor, introduce algún texto antes de enviar a la API.")


def busqueda_espacios():
    
    user_input = st.text_input("Introduce una breve descripcion del lugar que buscas")    
    
    

    if st.button('Enviar a la API'):
        if user_input:
            st.write(f"Enviando data a la API...")
            api_response = buscar_espacios(user_input+"en arriendo")

            if api_response:
                st.write("Respuesta de la API:")
                st.write(api_response)
            else:
                st.write("Hubo un problema al obtener la respuesta de la API.")
        else:
            st.write("Por favor, introduce algún texto antes de enviar a la API.")


def main():
    

    st.title('Bienvenido al sistema de gestion de talleres!')

    app_selection = st.sidebar.selectbox(
        'Selecciona una aplicación:',
        ('Crea un taller', 'Busca insumos para tu taller', 'Busca talleristas',
         'Busca espacios')
    )

    if app_selection == 'Crea un taller':
        crear_taller()
    elif app_selection == 'Busca insumos para tu taller':
        busqueda_insumos()
    elif app_selection == 'Busca talleristas':
        busqueda_talleristas()
    elif app_selection == 'Busca espacios':
        busqueda_espacios()

if __name__ == "__main__":
    main()