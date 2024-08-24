# Importar librerias
import os
import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

# Cargar los datos procesados --> 1°ro Ejecutar el programa 1_1_oils_processed.py
DATA_PATH="C:/Users/pugah/Documents/CFS/GitHub/DigitalNAO-Challenges/PythonVisualizacionDatos/data/"
FILE_CONSOLIDATED_DATA = 'oilst_processed.csv'
RESULT_PATH="C:/Users/pugah/Documents/CFS/GitHub/DigitalNAO-Challenges/PythonVisualizacionDatos/Sprint_1/Desarrolla/resultado/"
FILE_RESULT='prop_sales_delay_status_by_quarte.csv'

data = pd.read_csv(os.path.join(DATA_PATH, FILE_CONSOLIDATED_DATA))

# Filtrar los datos para el rango de años 2016 a 2018
filtered_data = data[(data['year'] >= 2016) & (data['year'] <= 2018)]

# Agrupar los datos por año, trimestre y delay_status, y sumar las ventas
grouped_data = filtered_data.groupby(['year', 'quarter', 'delay_status']).agg({'total_sales': 'sum'}).reset_index()

# Calcular la proporción de ventas por categoría de delay_status para cada trimestre
grouped_data['total_sales_quarter'] = grouped_data.groupby(['year', 'quarter'])['total_sales'].transform('sum')
grouped_data['sales_proportion'] = grouped_data['total_sales'] / grouped_data['total_sales_quarter']

# Seleccionar las columnas finales
final_data = grouped_data[['year', 'quarter', 'delay_status', 'sales_proportion']]

# Guardar el resultado en un archivo CSV
final_data.to_csv(os.path.join(RESULT_PATH, FILE_RESULT), index=False)

print("El archivo " + FILE_RESULT + " ha sido generado con éxito.")
