import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

# Cargar los datos procesados
data = pd.read_csv('oilst_processed.csv')

# Filtrar las órdenes con un retraso mayor a 10 días y con status completo
filtered_data = data[(data['delta_days'] > 10) & (data['delay_status'] == 'Largo')]

# Seleccionar las columnas relevantes para la matriz de correlación
relevant_columns = ['total_sales', 'total_products', 'delta_days', 'distance_distribution_center']
correlation_data = filtered_data[relevant_columns]

# Calcular la matriz de correlación
correlation_matrix = correlation_data.corr()

# Crear la figura para la matriz de correlación
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0, linewidths=0.5)

# Añadir título y etiquetas
plt.title('Correlation Matrix for Orders with Delay > 10 Days')
plt.savefig('correlation_matrix_10_days_delay.png')

print("El archivo correlation_matrix_10_days_delay.png ha sido generado con éxito.")
