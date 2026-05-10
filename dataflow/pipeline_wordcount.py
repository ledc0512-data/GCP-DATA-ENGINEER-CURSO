import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run():
    # 1. Configuración inicial
    # Usamos DirectRunner para ejecutarlo localmente en tu PC
    options = PipelineOptions(
        runner='Dataflowrunner',
        project='ledc-dataengineer-pipeline', # Reemplaza con tu ID actual
        region='us-central1',
        temp_location='gs://lenin-bucket-logistica-2026/temp' # Reemplaza con el bucket que creaste
    )

    print("Iniciando el pipeline de procesamiento...")

    # 2. Definición del Pipeline
    with beam.Pipeline(options=options) as p:
        (
            p 
            # PASO 1: Extraer - Leemos un archivo de texto público de Google
            | 'Leer archivo' >> beam.io.ReadFromText('gs://dataflow-samples/shakespeare/kinglear.txt')
            
            # PASO 2: Transformar - Separar por palabras
            | 'Separar palabras' >> beam.FlatMap(lambda line: line.split())
            
            # PASO 3: Transformar - Contar ocurrencias de cada palabra
            | 'Contar palabras' >> beam.combiners.Count.PerElement()
            
            # PASO 4: Cargar - Guardar el resultado en TU bucket
            | 'Guardar resultados' >> beam.io.WriteToText('gs://lenin-bucket-logistica-2026/output/wordcount')
        )

    print(" Pipeline ejecutado exitosamente. Revisa tu bucket en la carpeta /output.")

if __name__ == "__main__":
    run()