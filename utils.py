import hashlib
from datetime import datetime


# UTILIZAR ESTAS FUNCIONES CON EL METODO apply() de pandas eje:  df['rfc'] = df['rfc'].apply(funcion)

# 1 Enmascaramiento de nombre, ocultando caracteres parciales para impedir la identifiación directa
def anonimate(full_name:  str) -> str :
    return ' '.join(
        palabra[0].upper() + '*' * (len(palabra) - 1)
        for palabra in str(full_name).split(' ')
        if palabra
    )

if __name__ == '__main__':
    print(anonimate('angel raymundo pablo zenón'))


# 2. Seudoanonimizacion con hashing usando haslib 

def seudoanonimate(rfc : str) -> str :
    m = hashlib.sha256()
    m.update(str(rfc).encode())
    return m.hexdigest()


# 3. Generalizacion de fecha de nacimiento a rango de edad, para escribirlo en una columna de un dataframe

def generalizar_fecha(fecha : str) -> str :
    fecha_nacimiento = datetime.strptime(str(fecha), '%Y-%m-%d')
    edad = datetime.now().year - fecha_nacimiento.year
    if edad < 18:
        return 'Menor de 18'
    elif edad < 30:
        return '18-29'
    elif edad < 40:
        return '30-39'
    elif edad < 50:
        return '40-49'
    else:
        return '50+'
    
# 4. Perturbacion de Datos. K-anonymity.

def truncate_cp(cp : str) -> str :
    return str(cp)[:3] + "***"