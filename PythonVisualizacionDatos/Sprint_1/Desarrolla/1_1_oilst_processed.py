# Se importa la libreria pandas 
import pandas as pd

# Cargar los datos desde las diferentes fuentes en dataframes 
orders = pd.read_csv("./data/olist_orders_dataset.csv")
customers = pd.read_csv("./data/olist_customers_dataset.csv") # se exporta el archivo original excel a csv
geolocation = pd.read_csv("./data/olist_geolocation_dataset.csv")
states = pd.read_csv("./data/brasil_regions.csv")

# Campos calculados:

# Agregar el total de productos 
order_items = pd.read_csv("./data/olist_order_items_dataset.csv")
total_products = order_items.groupby('order_id').size().reset_index(name='total_products')

# Agregar el total de ventas 
order_items['price'] = order_items['price'].astype(float)
total_sales = order_items.groupby('order_id')['price'].sum().reset_index(name='total_sales')

# Join total_products y total_sales a la tabla de órdenes
orders = orders.merge(total_products, on='order_id', how='left')
orders = orders.merge(total_sales, on='order_id', how='left')

# Calcular campos de fecha
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
orders['year'] = orders['order_purchase_timestamp'].dt.year
orders['month'] = orders['order_purchase_timestamp'].dt.month
orders['quarter'] = orders['order_purchase_timestamp'].dt.quarter
orders['year_month'] = orders['order_purchase_timestamp'].dt.to_period('M')

# Calcular delta_days y delay_status
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])

orders['delta_days'] = (orders['order_estimated_delivery_date'] - orders['order_delivered_customer_date']).dt.days

# Función para categorizar el retraso
def categorize_delay(days):
    if days < 0:
        if days >= -3:
            return 'Corto'
        else:
            return 'Largo'
    else:
        return 'No hubo retraso'

orders['delay_status'] = orders['delta_days'].apply(categorize_delay)

# Unir la tabla orders con customers y geolocation
orders = orders.merge(customers, on='customer_id', how='left')
orders = orders.merge(geolocation, left_on='customer_zip_code_prefix', right_on='geolocation_zip_code_prefix', how='left')

# Unir con la tabla de estados
orders = orders.merge(states, left_on='customer_state', right_on='abbreviation', how='left')

# Seleccionar las columnas finales
final_columns = [ 'order_id', 'customer_unique_id', 'total_products', 'total_sales', 'year', 'month'
                , 'quarter', 'year_month', 'delta_days', 'delay_status', 'customer_city', 'customer_state'
                , 'geolocation_lat', 'geolocation_lng', 'geolocation_city', 'geolocation_state', 'state_name'
                , 'distance_distribution_center'
                ]

# Crear el dataframe final
final_df = orders[final_columns]

# Guardar el dataframe en un archivo CSV
final_df.to_csv('oilst_processed.csv', index=False)

print("El archivo oilst_processed.csv ha sido generado con éxito.")
