import random as rn
import pandas as pd

ruta = 'copia.csv'


    
df = pd.read_csv(ruta)
# *Agregando columna sexo a la tabla, en el indice 3
df.insert(2, 'sexo', ['m', 'f','m', 'f','m', 'f','m', 'f','m', 'f'])

# agregar 40 registros mas
# Importamos las funciones que generar los nombres :
from generate_names import generar_mujeres 
from generate_names import generar_hombres

personas = generar_hombres(20) + generar_mujeres(20)

for persona in personas :
    monto_compra = round(rn.uniform(100, 5000), 2)
    categoria_producto = rn.choice(['Farmacia', 'Cuidado Personal', 'Equipamiento'])
    df.loc[len(df)] = [len(df) + 1, persona.nombre, persona.sexo, persona.rfc, persona.fecha_nacimiento, persona.codigo_postal, monto_compra, categoria_producto]


print(df)
