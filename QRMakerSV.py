import qrcode
import streamlit as st
import io
from PIL import Image


st.title("QR Code generator, by Santiago Verellen")

url = st.text_input("Please insert the URL or text you want to transform into a QR code")

if st.button("Generate code"):
    
    #Creo un objeto de QR
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    #Aca creo la imagen 
    img = qr.make_image(fill="black", back_color="white")

    #Estoy transformando la imagen de formato PIL a PNG, pq streamlit no admite el formato PIL
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    byte_im = buf.getvalue()

    #Muestro el qr generado
    st.image(byte_im, caption="Generated code", use_column_width=True)

    #Aca estoy creando un boton que directamente descargue el qr como PNG
    st.download_button(
        label=("Download QR code"), #La etiqueta que aparecera en el boton
        data=byte_im, #Aca le paso el archivo a descargar
        file_name= "QR_CODE.png", #Le doy nombre al archivo a descargar
        mime="image/png" #Le estoy dando a entender al navegador que es un archivo tipo imagen/png
    )