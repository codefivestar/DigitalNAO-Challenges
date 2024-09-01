import os
import pandas as pd
import plotly.express as px

# Cargar los datos procesados
DATA_PATH="C:/Users/pugah/Documents/CFS/GitHub/DigitalNAO-Challenges/PythonVisualizacionDatos/data/"
FILE_CONSOLIDATED_DATA = 'oilst_processed.csv'
RESULT_PATH="C:/Users/pugah/Documents/CFS/GitHub/DigitalNAO-Challenges/PythonVisualizacionDatos/Sprint_2/Desarrolla/resultado/"
FILE_RESULT='3_d_evolution_delayed_orders_by_region.html'

data = pd.read_csv(
    os.path.join(DATA_PATH, FILE_CONSOLIDATED_DATA)
    )

# Filtrar las órdenes con retrasos prolongados
long_delay_orders = data[data['delay_status'] == 'Largo']

# Crear una columna con el año y el mes de la fecha de compra
long_delay_orders['year_month'] = pd.to_datetime(
    long_delay_orders['order_purchase_timestamp']
    ).dt.to_period('M')

# Agrupar las órdenes con retrasos prolongados por año_mes y estado
delayed_orders_by_region = long_delay_orders.groupby(
    ['year_month', 'customer_state']
    ).size().reset_index(name='order_count')

# Crear una figura de barras apiladas interactiva
fig = px.bar(delayed_orders_by_region, 
             x='year_month', 
             y='order_count', 
             color='customer_state',
             title="Evolución de Órdenes con Retrasos Prolongados por Mes y Región",
             labels={'year_month': 'Mes y Año', 'order_count': 'Cantidad de Órdenes'},
             barmode='stack')

# Ajustar la presentación del gráfico
fig.update_layout(xaxis_title="Mes y Año", 
                  yaxis_title="Cantidad de Órdenes",
                  legend_title="Estado",
                  xaxis_tickangle=-45)

# Guardar la figura interactiva en un archivo HTML
fig.write_html(os.path.join(RESULT_PATH, FILE_RESULT))

print("El archivo " + FILE_RESULT + " ha sido generado con éxito.")
