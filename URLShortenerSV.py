#Acortador de URLS
import pyshorteners 
import streamlit as st

#Titulo de nuestra pagina web
st.title ("URL shortener, by Santiago Verellen 😄")

#Campo de texto, donde ingresar la URL
url = st.text_input("Please, paste the URL")

#Boton para acortar la URL
if st.button("Shorten URL"):
    if url != "":
        #Acortamos la URL con tinyURL
        s = pyshorteners.Shortener()
        shorturl = s.tinyurl.short(url)
        st.success(f"Shortened URL -->  {shorturl}")
    else:
        st.error("Please, enter a valid URL")