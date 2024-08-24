# Importar librerias
import os
import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

# Lectura de datos
DATA_PATH="C:/Users/pugah/Documents/CFS/GitHub/DigitalNAO-Challenges/PythonVisualizacionDatos/data/"
FILE_CUSTOMERS = 'olist_customers_dataset.xlsx'
FILE_GEOLOCATIONS = 'olist_geolocation_dataset.csv'
FILE_ITEMS = 'olist_order_items_dataset.csv'
FILE_PAYMENTS = 'olist_order_payments_dataset.csv'
FILE_ORDERS = 'olist_orders_dataset.csv'
FILE_STATES_ABBREVIATIONS = 'states_abbreviations.json'
FILE_CONSOLIDATED_DATA = 'oilst_processed.csv'

# Leemos con pandas
customers = pd.read_excel(os.path.join(DATA_PATH, FILE_CUSTOMERS))
geolocations = pd.read_csv(os.path.join(DATA_PATH, FILE_GEOLOCATIONS))
order_items = pd.read_csv(os.path.join(DATA_PATH, FILE_ITEMS))
order_payments = pd.read_csv(os.path.join(DATA_PATH, FILE_PAYMENTS))
orders = pd.read_csv(os.path.join(DATA_PATH, FILE_ORDERS))
states_abbreviations = pd.read_json(os.path.join(DATA_PATH, FILE_STATES_ABBREVIATIONS))

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
orders = orders.merge(geolocations, left_on='customer_zip_code_prefix', right_on='geolocation_zip_code_prefix', how='left')

# Unir con la tabla de estados
orders = orders.merge(states_abbreviations, left_on='customer_state', right_on='abbreviation', how='left')

# Seleccionar las columnas finales
final_columns = [ 'order_id' , 'customer_id' , 'order_status' , 'order_purchase_timestamp' , 'order_approved_at' , 'order_delivered_carrier_date' , 'order_delivered_customer_date'
                , 'order_estimated_delivery_date' , 'distance_distribution_center' , 'year' , 'month' , 'quarter' , 'year_month' , 'delta_days' , 'delay_status' , 'total_products'
                , 'total_sales' , 'customer_unique_id' , 'customer_zip_code_prefix' , 'customer_city' , 'customer_state' , 'geolocation_zip_code_prefix' , 'geolocation_lat' , 'geolocation_lng'
                , 'geolocation_city' , 'geolocation_state' , 'abbreviation' , 'state_name' ]

# Crear el dataframe final
final_df = orders[final_columns]

# Guardar el dataframe en un archivo CSV
final_df.to_csv(os.path.join(DATA_PATH, FILE_CONSOLIDATED_DATA))

print("El archivo oilst_processed.csv ha sido generado con éxito.")