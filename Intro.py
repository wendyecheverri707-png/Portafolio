import streamlit as st
from PIL import Image, ImageOps

def cargar_imagen_estandar(ruta_imagen):
    imagen = Image.open(ruta_imagen)
    # Define el tamaño fijo que quieres (Ancho, Alto) en píxeles. 
    # 400x250 es un buen tamaño horizontal.
    tamano_fijo = (400, 250) 
    # ImageOps.fit recorta la imagen centrándola para que no se vea estirada o deforme
    imagen_recortada = ImageOps.fit(imagen, tamano_fijo, Image.Resampling.LANCZOS)
    return imagen_recortada

st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial.")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

# AQUÍ ESTÁ EL CAMBIO PRINCIPAL: Se declaran 3 columnas
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Vectores y Matrices")
    image = cargar_imagen_estandar('Vectores y matrices.png')
    st.image(image, use_container_width=True)
    st.write("En la siguiente enlace veremos una aplicación de frutas para verificar que los datos son vectores y matrices, y aprender es transformar esos vectores de un espacio a otro.") 
    url = "https://frutasapppy-cddzbmoos3hrekqyvqybpj.streamlit.app/"
    st.write(f"[Enlace]({url})")

    st.subheader("Calculo aplicado, gradiente")
    image = cargar_imagen_estandar('Gradiente.png')
    st.image(image, use_container_width=True)
    st.write("En la siguiente enlace veremos una app que nos permite explorar cómo las derivadas y el gradiente permiten transformar un problema matemático en un proceso computacional de búsqueda y optimización.") 
    url = "https://appgradientpy-baegvfk4xabfhbs8x5rd7c.streamlit.app/"
    st.write(f"[Enlace]({url})")

    st.subheader("Lógica, Big-O y Vectorización")
    image = cargar_imagen_estandar('Logica bigO.png')
    st.image(image, use_container_width=True)
    st.write("En la siguiente enlace veremos una app que nos permite explorar un Detector de Anomalías: Lógica + Big-O + NumPy") 
    url = "https://appmodulo4detectoranomaliaspy-jnlas87d9kvg2xq45eq3hd.streamlit.app/"
    st.write(f"[Enlace]({url})")
    
    st.subheader("Preparación de datos")
    image = cargar_imagen_estandar('Preparación de datos.png')
    st.image(image, use_container_width=True)
    st.write("En la siguiente veremos una app que permite experimentar en vivo con cada concepto de preparación y estructura de datos usando un dataset sintético de sensores IoT.") 
    url = "https://4r4zsfpubh4mpfem3u2nia.streamlit.app/"
    st.write(f"[Enlace]({url})")

with col2: 
    st.subheader("Aplicación Preparación de datos")
    image = cargar_imagen_estandar('Aplicación Preparación de datos.png')
    st.image(image, use_container_width=True)
    st.write("En la siguiente enlace veremos una app con datos ambientales reales obtenidos a través de la plataforma MARCO de Cornare, utilizando APIs y endpoints para acceder a información de estaciones de monitoreo") 
    url = "https://appnivelcornarepy-aw7a8kne3vqp2fsusv2t9f.streamlit.app/"
    st.write(f"[Enlace]({url})")

    st.subheader("Regresión Lineal")
    image = cargar_imagen_estandar('Regresión Lineal.png')
    st.image(image, use_container_width=True)
    st.write("En la siguiente enlace veremos una app que recorre, de forma interactiva, las piezas que componen un modelo de regresión: el modelo, la función de costo, el gradiente, el algoritmo de aprendizaje y las métricas para evaluar qué tan bien predice. Todo con datos reales de vivienda en California.") 
    url = "https://regresionconceptosapppy-pex7inucytvp8wdlti9djb.streamlit.app/"
    st.write(f"[Enlace]({url})")

    st.subheader("Series de Tiempo")
    image = cargar_imagen_estandar('Series de Tiempo.png')
    st.image(image, use_container_width=True)
    st.write("En la siguiente app veremos como se pronostica el futuro a partir de datos históricos mediante el análisis de series de tiempo con un Sensor IoT interactivo") 
    url = "https://appseriestiempopy-frrzpqrja5tna8kybqgejh.streamlit.app/"
    st.write(f"[Enlace]({url})")

    st.subheader("Predicción y modelado de la calidad de aire")
    image = cargar_imagen_estandar('Predicción y modelado de la calidad de aire.png')
    st.image(image, use_container_width=True)
    st.write("En la siguiente enlace veremos una app Predictor de calidad del aire — CORNARE (MARCO) que nos permite cargar modelos para generaer predicciones.") 
    url = "https://apppronosticocornarepy-6gnfwufowbvzjgpp2jmc8m.streamlit.app/"
    st.write(f"[Enlace]({url})")

with col3: 
    st.subheader("Sistema de IoT Captura de datos y procesamiento")
    image = cargar_imagen_estandar('Sistema de IoT Captura de datos y procesamiento.png')
    st.image(image, use_container_width=True)
    st.write("En la siguiente enlace veremos una app con Datos reales de temperatura y humedad tomados por un sensor IoT, usados para entrenar un modelo de regresión lineal que predice la sensación térmica") 
    url = "https://ncnfepgfhuhlq32thbl6u9.streamlit.app/"
    st.write(f"[Enlace]({url})")

    st.subheader("De la regresión lineal a la logísitica")
    image = cargar_imagen_estandar('De la regresión lineal a la logísitica.png')
    st.image(image, use_container_width=True)
    st.write("En la siguiente enlace veremos una app de regresión Logística interactiva") 
    url = "https://appregresionlogisticapy-ku965ravxq7nrxgi4pihpq.streamlit.app/"
    st.write(f"[Enlace]({url})")

    st.subheader("Clasificación Knn")
    image = cargar_imagen_estandar('Clasificación Knn.png')
    st.image(image, use_container_width=True)
    st.write("En la siguiente enlace veremos una app que explora K vecinos más cercanos (KNN)") 
    url = "https://c2zlpl39ccubjahxtsc2pg.streamlit.app/"
    st.write(f"[Enlace]({url})")
    
    st.subheader("Aplicación Knn")
    image = cargar_imagen_estandar('Clasificación de fertilidad de  suelos.png')
    st.image(image, use_container_width=True)
    st.write("En la siguiente enlace veremos una app que explora KNN con datos de suelos de AGROSAVIA") 
    url = "https://c2zlpl39ccubjahxtsc2pg.streamlit.app/"
    st.write(f"[Enlace]({url})")

