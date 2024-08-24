import os
import pandas as pd
import folium
import geopandas as gpd

# Cargar los datos procesados
DATA_PATH="C:/Users/pugah/Documents/CFS/GitHub/DigitalNAO-Challenges/PythonVisualizacionDatos/data/"
FILE_GEODATA = 'brasil_geodata.json'
FILE_CONSOLIDATED_DATA = 'oilst_processed.csv'
RESULT_PATH="C:/Users/pugah/Documents/CFS/GitHub/DigitalNAO-Challenges/PythonVisualizacionDatos/Sprint_2/Desarrolla/resultado/"
FILE_RESULT='3_f_map_monetary_value_long_delays_by_state.html'

data = pd.read_csv(os.path.join(DATA_PATH, FILE_CONSOLIDATED_DATA))

# Filtrar las órdenes con retrasos prolongados
long_delay_orders = data[data['delay_status'] == 'Largo']

# Agrupar el valor monetario total de las órdenes con retrasos prolongados por estado
monetary_value_by_state = long_delay_orders.groupby('customer_state')['total_sales'].sum().reset_index()

# Cargar el GeoJSON con las fronteras de los estados (ajusta la ruta al archivo)
geodata = gpd.read_file(os.path.join(DATA_PATH, FILE_GEODATA))

# Crear un mapa centrado en Brasil
m = folium.Map(location=[-15.7801, -47.9292], zoom_start=4)

# Añadir la capa de colores por estado basada en el valor monetario
folium.Choropleth(
    geo_data=geodata,
    name="choropleth",
    data=monetary_value_by_state,
    columns=["customer_state", "total_sales"],
    key_on="feature.properties.ESTADO", 
    fill_color="YlGnBu",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Valor Monetario de Retrasos Prolongados por Estado (total_sales)",
).add_to(m)

# Guardar el mapa en un archivo HTML
m.save(os.path.join(RESULT_PATH, FILE_RESULT))

print("El archivo " + FILE_RESULT + " ha sido generado con éxito.")
