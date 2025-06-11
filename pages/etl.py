# etl.py actualizado con limpieza y exportación
import streamlit as st
import pandas as pd
from pymongo import MongoClient, errors
from utils import cargar_datos, limpiar_datos
import os

st.set_page_config(page_title="Flujo ETL", layout="wide")
st.title("Simulación ETL → MongoDB ")

# Parámetros de conexión (lo ideal: .env + st.secrets)
uri = st.text_input("URI MongoDB", "mongodb://localhost:27017")
db_name = st.text_input("Base de datos", "etl_demo")
col_name = st.text_input("Colección destino", "registros")

archivo = st.file_uploader("Sube archivo para cargar")

if st.button("Ejecutar ETL") and archivo:
    df = cargar_datos(archivo)
    st.write("Datos cargados:", df.shape)

    df = limpiar_datos(df)
    st.write("Después de limpieza:", df.shape)

    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=3000)
        client.server_info()  # test rápido
    except errors.ServerSelectionTimeoutError as e:
        st.error(f"Error de conexión: {e}")
        st.stop()

    df = df.astype(object).where(pd.notnull(df), None)
    inserted = client[db_name][col_name].insert_many(df.to_dict("records")).inserted_ids
    st.success(f"Cargados {len(inserted)} documentos en {db_name}.{col_name}")

    st.subheader("Muestra de datos insertados")
    st.dataframe(df.head())

    # Exportación CSV limpio
    os.makedirs("data/processed", exist_ok=True)
    archivo_nombre = archivo.name.split(".")[0] + "_clean.csv"
    ruta_salida = os.path.join("data/processed", archivo_nombre)
    df.to_csv(ruta_salida, index=False)
    st.success(f"CSV limpio guardado en {ruta_salida}")
