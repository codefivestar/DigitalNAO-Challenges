# Importar librerias
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

# Cargar los datos procesados
DATA_PATH="C:/Users/pugah/Documents/CFS/GitHub/DigitalNAO-Challenges/PythonVisualizacionDatos/data/"
FILE_CONSOLIDATED_DATA = 'oilst_processed.csv'
RESULT_PATH="C:/Users/pugah/Documents/CFS/GitHub/DigitalNAO-Challenges/PythonVisualizacionDatos/Sprint_1/Desarrolla/resultado/"
FILE_RESULT='histogram_sales_long_delay.png'

data = pd.read_csv(os.path.join(DATA_PATH, FILE_CONSOLIDATED_DATA))

# Filtrar las órdenes con delay_status "Largo"
filtered_data = data[data['delay_status'] == 'Largo']

# Extraer la variable total_sales para estas órdenes
total_sales = filtered_data['total_sales']

# Calcular media y desviación estándar
mean_sales = total_sales.mean()
std_sales = total_sales.std()

# Calcular los intervalos según la regla empírica débil para el 88.88% de los datos
z_score = 1.75  # Aproximadamente 88.88% en una distribución normal
lower_bound = mean_sales - z_score * std_sales
upper_bound = mean_sales + z_score * std_sales

# Crear el histograma
plt.figure(figsize=(10, 6))
plt.hist(total_sales, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# Añadir líneas de los intervalos
plt.axvline(mean_sales, color='red', linestyle='dashed', linewidth=1.5, label=f'Mean = {mean_sales:.2f}')
plt.axvline(lower_bound, color='green', linestyle='dashed', linewidth=1.5, label=f'Lower bound = {lower_bound:.2f}')
plt.axvline(upper_bound, color='green', linestyle='dashed', linewidth=1.5, label=f'Upper bound = {upper_bound:.2f}')

# Añadir etiquetas y título
plt.title('Histogram of Total Sales for Orders with Long Delay')
plt.xlabel('Total Sales')
plt.ylabel('Frequency')
plt.legend()

# Guardar el histograma como archivo PNG
plt.savefig(os.path.join(RESULT_PATH, FILE_RESULT))

print("El archivo " + FILE_RESULT + " ha sido generado con éxito.")
