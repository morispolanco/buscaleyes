import streamlit as st
import requests

# Configuración de la página
st.title("Consulta sobre Legislación y Jurisprudencia de Guatemala")

# Obtener la clave de API desde los secretos de Streamlit
api_key = st.secrets["perplexity"]["api_key"]

# Función para hacer la solicitud a la API
def consultar_perplexity(pregunta):
    url = "https://api.perplexity.ai/chat/completions"  # Updated endpoint
    headers = {
        "Authorization": f"Bearer {api_key}",
        "accept": "application/json",
        "content-type": "application/json"
    }
    data = {
        "model": "llama-3.1-sonar-small-128k-online",  # Updated model
        "messages": [
            {
                "role": "system",
                "content": "Be precise and concise."
            },
            {
                "role": "user",
                "content": pregunta
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Levantará un error si la respuesta no es 2xx
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return f"Error de Conexión: {errc}"
    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        return f"Request Error: {err}"

# Interfaz de usuario
pregunta = st.text_input("Haz una pregunta sobre la legislación o jurisprudencia de Guatemala:")

if st.button("Enviar"):
    if pregunta:
        respuesta = consultar_perplexity(pregunta)
        st.write("Respuesta:")
        st.write(respuesta)
    else:
        st.write("Por favor, ingresa una pregunta.")
