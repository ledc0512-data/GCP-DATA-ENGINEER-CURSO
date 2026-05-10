import google.cloud
from google.cloud import storage

def crear_bucket_gcp(nombre_bucket, proyecto_id, region="us-central1"):
    try:
        # Aquí le decimos a Python EXACTAMENTE en qué proyecto trabajar
        storage_client = storage.Client(project=proyecto_id)

        bucket = storage_client.bucket(nombre_bucket)
        bucket.storage_class = "STANDARD"

        nuevo_bucket = storage_client.create_bucket(bucket, location=region)

        print(f"EXITO: Bucket {nuevo_bucket.name} creado en el proyecto {proyecto_id}")
        return nuevo_bucket

    except Exception as e:
        # Imprimimos el error de forma simple para evitar fallos de codificacion
        print(f"ERROR: {str(e)}")
        return None

# --- CONFIGURACION ---
# REEMPLAZA ESTO: Pon entre las comillas el ID que copiaste en el paso 1
MI_PROYECTO = "ledc-dataengineer-pipeline" 

# REEMPLAZA ESTO: Un nombre unico (solo letras minusculas, numeros y guiones)
MI_BUCKET = "lenin-bucket-logistica-2026"

crear_bucket_gcp(MI_BUCKET, MI_PROYECTO)