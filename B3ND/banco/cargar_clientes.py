import os
import django
import pandas as pd

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banco.settings')  # Ajusta 'banco' según el nombre de tu proyecto
django.setup()

from clientes.models import Cliente

# Ruta del archivo CSV
csv_file = 'clientes/clientes_banco.csv'

def cargar_datos():
    # Leer el archivo CSV
    df = pd.read_csv(csv_file)
    
    # Limpiar y preparar los datos
    df = df.drop_duplicates()
    df = df.fillna({
        'Edad': 0,
        'Genero': 'No especificado',
        'Saldo': 0,
        'Activo': 0,
        'Nivel_de_Satisfaccion': 1
    })

    # Iterar sobre las filas e insertar en la base de datos
    for _, row in df.iterrows():
        Cliente.objects.update_or_create(
            cliente_id=int(row['Cliente_ID']),
            defaults={
                'edad': row['Edad'],
                'genero': row['Genero'][:10],
                'saldo': row['Saldo'],
                'activo': bool(row['Activo']),
                'nivel_de_satisfaccion': int(row['Nivel_de_Satisfaccion']),
            }
        )
    print("Datos cargados exitosamente.")

if __name__ == '__main__':
    cargar_datos()
