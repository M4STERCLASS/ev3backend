import pandas as pd
from clientes.models import Cliente

def cargar_datos():
    # Leer el archivo CSV y eliminar duplicados
    df = pd.read_csv('clientes/clientes_banco.csv')
    df = df.drop_duplicates()
    
    # Rellenar valores nulos con valores predeterminados
    df = df.fillna({'Edad': 0, 'Genero': 'M', 'Saldo': 0, 'Activo': 0, 'Nivel_de_Satisfaccion': 1})
    
    # Iterar sobre cada fila del dataframe
    for _, row in df.iterrows():
        # Verificar si el cliente ya existe
        if not Cliente.objects.filter(cliente_id=row['Cliente_ID']).exists():
            # Crear un nuevo cliente si no existe
            Cliente.objects.create(
                cliente_id=row['Cliente_ID'],
                edad=int(row['Edad']),
                genero=row['Genero'][0] if pd.notna(row['Genero']) else 'M',
                saldo=float(row['Saldo']),
                activo=bool(row['Activo']),
                nivel_de_satisfaccion=int(row['Nivel_de_Satisfaccion']),
            )
    
    print("Datos cargados exitosamente.")
