Proyecto Integrador – Ciencia de Datos

## Estructura del proyecto

- `app.py`: interfaz principal de la aplicación
- `etl.py`: módulo para el flujo ETL y conexión con MongoDB
- `utils.py`: funciones auxiliares para importar y limpiar datos
- `pages/`: secciones adicionales de Streamlit (EDA, comparación)
- `static/`: recursos gráficos y diagramas de arquitectura
- `data/`: archivos de entrada y resultados procesados

## Pasos para ejecutar

```bash
python -m venv venv
venv\Scripts\activate       # o source venv/bin/activate en Linux/Mac
pip install -r requirements.txt
python etl.py -f data/ejemplo.xlsx
streamlit run app.py
```
