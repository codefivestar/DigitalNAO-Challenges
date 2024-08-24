# Importar librerias
import os
import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

# Cargar los datos procesados
DATA_PATH="C:/Users/pugah/Documents/CFS/GitHub/DigitalNAO-Challenges/PythonVisualizacionDatos/data/"
FILE_CONSOLIDATED_DATA = 'oilst_processed.csv'
RESULT_PATH="C:/Users/pugah/Documents/CFS/GitHub/DigitalNAO-Challenges/PythonVisualizacionDatos/Sprint_1/Desarrolla/resultado/"
FILE_RESULT='count_orders_basket_size_by_delay_status.csv'

data = pd.read_csv(os.path.join(DATA_PATH, FILE_CONSOLIDATED_DATA))

# Agrupar los datos por tamaño de la cesta (total_products) y delay_status
grouped_data = data.groupby(['total_products', 'delay_status']).size().reset_index(name='order_count')

# Guardar el resultado en un archivo CSV
grouped_data.to_csv(os.path.join(RESULT_PATH, FILE_RESULT), index=False)

print("El archivo " + FILE_RESULT + " ha sido generado con éxito.")
