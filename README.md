Evaluación Integrada – Ciencia de Datos

## Organización

- `app.py`: aplicación principal
- `etl.py`: proceso ETL con conexión a MongoDB
- `utils.py`: utilidades para carga y limpieza de datos
- `pages/`: páginas de Streamlit (EDA, comparativo)
- `static/`: imagen del diagrama de arquitectura
- `data/`: archivos de entrada y salida procesados

## Instrucciones de uso

```bash
python -m venv venv
venv\Scripts\activate       # o source venv/bin/activate
pip install -r requirements.txt
python etl.py -f data/ejemplo.xlsx
streamlit run app.py
```
