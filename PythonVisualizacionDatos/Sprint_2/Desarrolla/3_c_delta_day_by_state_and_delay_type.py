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
FILE_RESULT='3_c_delta_day_by_state_and_delay_type.png'

data = pd.read_csv(os.path.join(DATA_PATH, FILE_CONSOLIDATED_DATA))

# Crear la figura para la visualización
plt.figure(figsize=(14, 8))

# Crear un gráfico de cajas (boxplot) para observar la distribución de delta_days por estado y delay_status
sns.boxplot(x='customer_state', y='delta_days', hue='delay_status', data=data)

# Añadir título y etiquetas
plt.title('Distribución de Delta Days por Estado y Tipo de Retraso')
plt.xlabel('Estado')
plt.ylabel('Delta Days')

# Rotar las etiquetas del eje x para una mejor legibilidad
plt.xticks(rotation=45)

# Guardar la figura en un archivo PNG
plt.savefig(os.path.join(RESULT_PATH, FILE_RESULT))

print("El archivo " + FILE_RESULT + " ha sido generado con éxito.")
