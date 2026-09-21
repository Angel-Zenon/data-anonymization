import random as rn
import pandas as pd
from generate_names import generar_mujeres 
from generate_names import generar_hombres
from utils import anonimate, seudoanonimate, generalizar_fecha, truncate_cp

ruta = 'copia.csv'
    
df = pd.read_csv(ruta)
df.insert(2, 'sexo', ['m', 'f','m', 'f','m', 'f','m', 'f','m', 'f'])

personas = generar_hombres(20) + generar_mujeres(20)

for persona in personas :
    monto_compra = round(rn.uniform(100, 5000), 2)
    categoria_producto = rn.choice(['Farmacia', 'Cuidado Personal', 'Equipamiento'])
    df.loc[len(df)] = [len(df) + 1, persona.nombre, persona.sexo, persona.rfc, persona.fecha_nacimiento, persona.codigo_postal, monto_compra, categoria_producto]

df['Nombre'] = df['Nombre'].apply(anonimate)
df['RFC'] = df['RFC'].apply(seudoanonimate)
df['Fecha_Nacimiento'] = df['Fecha_Nacimiento'].apply(generalizar_fecha)
df['Codigo_Postal'] = df['Codigo_Postal'].apply(truncate_cp)

print(df)

# Guardamos el df escribiendolo en un .csv 'data_anonima.csv'
# Usar manejo de excepciones para errores al guardar el archivo
try :
    df.to_csv('data_anonima.csv', index=False)
except Exception as e :
    print(f"Error al guardar el archivo : {e}")