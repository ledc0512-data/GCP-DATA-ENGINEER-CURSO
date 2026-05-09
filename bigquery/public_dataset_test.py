from google.cloud import bigquery
import pandas as pd

def consultar_a_dataframe(proyecto_id):
    try:
        print(f"Iniciando conexion con el proyecto: {proyecto_id}")
        client = bigquery.Client(project=proyecto_id)

        # Consulta SQL JOIN
        query = """
            SELECT 
                p.name as producto,
                o.product_id,
                p.id as id_original,
                p.category,
                p.brand
            FROM `bigquery-public-data.thelook_ecommerce.order_items` as o
            JOIN `bigquery-public-data.thelook_ecommerce.products` as p
            ON p.id = o.product_id
            LIMIT 100
        """

        print("Consultando BigQuery y transformando a DataFrame...")
        
        # Ejecucion y convertimos directamente a DataFrame
        df = client.query(query).to_dataframe()

        # Mostramos la informacion en consola de forma organizada
        print("\n--- VISTA PREVIA DEL DATAFRAME ---")
        print(df.head()) # Muestra las primeras 5 filas

        print("\n--- ESTADISTICAS BASICAS ---")
        print(f"Total de registros procesados: {len(df)}")
        print(f"Columnas detectadas: {list(df.columns)}")

        # OPCIONAL: Guardar a un archivo CSV para tu portafolio
        df.to_csv("reporte_productos_ecommerce.csv", index=False)
        print("\n Archivo 'reporte_productos_ecommerce.csv' generado exitosamente.")

        return df

    except Exception as e:
        print(f"Error en el proceso: {str(e)}")

if __name__ == "__main__":
    # Asegurate de que este sea tu ID del proyecto actual
    MI_NUEVO_PROYECTO = "ledc-dataengineer.test" 
    df_resultado = consultar_a_dataframe(MI_NUEVO_PROYECTO)