import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

# Cargar los datos procesados
DATA_PATH="C:/Users/pugah/Documents/CFS/GitHub/DigitalNAO-Challenges/PythonVisualizacionDatos/data/"
FILE_CONSOLIDATED_DATA = 'oilst_processed.csv'
RESULT_PATH="C:/Users/pugah/Documents/CFS/GitHub/DigitalNAO-Challenges/PythonVisualizacionDatos/Sprint_2/Desarrolla/resultado/"
FILE_RESULT='3_a_histogram_sales_short_long_delays.png'

data = pd.read_csv(os.path.join(DATA_PATH, FILE_CONSOLIDATED_DATA))

# Filtrar las órdenes con retrasos moderados y prolongados
short_delay_orders = data[data['delay_status'] == 'Corto']
long_delay_orders = data[data['delay_status'] == 'Largo']

# Extraer las ventas de las órdenes completas para cada categoría de retraso
short_sales = short_delay_orders['total_sales']
long_sales = long_delay_orders['total_sales']

# Crear la figura y los ejes para los histogramas
plt.figure(figsize=(10, 6))

# Histogramas para retrasos cortos y largos
plt.hist(short_sales, bins=30, color='blue', alpha=0.6, label='Retraso Corto')
plt.hist(long_sales, bins=30, color='red', alpha=0.6, label='Retraso Largo')

# Añadir etiquetas y título
plt.xlabel('Total Sales')
plt.ylabel('Frequency')
plt.title('Histogram of Total Sales for Short and Long Delays')
plt.legend()

# Guardar la imagen como un archivo PNG
plt.savefig(os.path.join(RESULT_PATH, FILE_RESULT))

print("El archivo " + FILE_RESULT + " ha sido generado con éxito.")
