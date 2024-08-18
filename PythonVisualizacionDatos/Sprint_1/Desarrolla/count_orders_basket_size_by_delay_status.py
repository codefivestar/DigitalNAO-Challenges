import pandas as pd

# Cargar los datos procesados
data = pd.read_csv('oilst_processed.csv')

# Agrupar los datos por tamaño de la cesta (total_products) y delay_status
grouped_data = data.groupby(['total_products', 'delay_status']).size().reset_index(name='order_count')

# Guardar el resultado en un archivo CSV
grouped_data.to_csv('count_orders_basket_size_by_delay_status.csv', index=False)

print("El archivo count_orders_basket_size_by_delay_status.csv ha sido generado con éxito.")
