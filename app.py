Para crear una aplicación de Streamlit que utilice la API de Perplexity para responder preguntas sobre la legislación vigente de Guatemala y la jurisprudencia de Guatemala, primero necesitas obtener una clave de API de Perplexity. Luego, puedes almacenar esta clave en los secretos de Streamlit para mantenerla segura.

A continuación, te proporciono un ejemplo de código para una aplicación de Streamlit que hace esto:

1. **Guardar la clave de API en los secretos de Streamlit**:
   - Crea un archivo `.streamlit/secrets.toml` en tu proyecto.
   - Añade la clave de API de Perplexity en este archivo:

     ```toml
     [perplexity]
     api_key = "tu_clave_de_api_de_perplexity"
     ```

2. **Código de la aplicación de Streamlit**:

   ```python
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

   ```

3. **Ejecutar la aplicación**:
   - Guarda el código en un archivo, por ejemplo, `app.py`.
   - Ejecuta la aplicación con el siguiente comando:

     ```bash
     streamlit run app.py
     ```

Este código crea una interfaz simple donde los usuarios pueden ingresar preguntas sobre la legislación y jurisprudencia de Guatemala. La aplicación envía estas preguntas a la API de Perplexity y muestra las respuestas. La clave de API se mantiene segura almacenándola en los secretos de Streamlit.
