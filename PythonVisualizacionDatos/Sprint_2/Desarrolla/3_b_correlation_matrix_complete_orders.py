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
FILE_RESULT='3_b_correlation_matrix_complete_orders.png'

data = pd.read_csv(os.path.join(DATA_PATH, FILE_CONSOLIDATED_DATA))

# Filtrar las órdenes completadas
complete_orders = data[data['order_status'] == 'delivered']

# Seleccionar las variables numéricas junto con delta_days
numeric_columns = ['total_sales', 'total_products', 'delta_days', 'distance_distribution_center']

# Filtrar las columnas relevantes para las órdenes completadas
correlation_data = complete_orders[numeric_columns]

# Calcular la matriz de correlación
correlation_matrix = correlation_data.corr()

# Crear la figura y el mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidths=0.5, fmt='.2f')

# Añadir título
plt.title('Correlation Matrix for Complete Orders')

# Guardar la figura en un archivo PNG
plt.savefig(os.path.join(RESULT_PATH, FILE_RESULT))

print("El archivo " + FILE_RESULT + " ha sido generado con éxito.")
