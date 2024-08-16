import streamlit as st
import requests

# Configuración de la página
st.title("Consulta sobre Legislación y Jurisprudencia de Guatemala")

# Obtener la clave de API desde los secretos de Streamlit
api_key = st.secrets["perplexity"]["api_key"]

# Función para hacer la solicitud a la API de Perplexity
def consultar_perplexity(pregunta):
    url = "https://api.perplexity.ai/v1/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "perplexity-model",
        "prompt": pregunta,
        "max_tokens": 150
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# Interfaz de usuario
pregunta = st.text_input("Haz una pregunta sobre la legislación o jurisprudencia de Guatemala:")

if st.button("Enviar"):
    if pregunta:
        respuesta = consultar_perplexity(pregunta)
        st.write("Respuesta:")
        st.write(respuesta)
    else:
        st.write("Por favor, ingresa una pregunta.")

