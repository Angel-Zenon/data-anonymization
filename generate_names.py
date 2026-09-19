import pandas as pd
import random as rn
import string
from datetime import date, timedelta

ruta_hombres = 'n_hombres.csv'
ruta_mujeres = 'n_mujeres.csv'
apellidos_csv = 'apellidos.csv'


class Persona:
    def __init__(self, nombres: str, a_paterno: str, a_materno: str, sexo: str):
        self.nombres = nombres
        self.a_paterno = a_paterno
        self.a_materno = a_materno
        # Data que se usará por cada persona
        self.nombre = f"{nombres} {a_paterno} {a_materno}"
        self.sexo = sexo
        self.fecha_nacimiento = None
        self.codigo_postal = None
        self.rfc = None

    def generarFechaNacimiento(self, anio_min: int = 1950, anio_max: int = 2005) -> str:
        inicio = date(anio_min, 1, 1)
        fin = date(anio_max, 12, 31)
        dias_totales = (fin - inicio).days
        fecha = inicio + timedelta(days=rn.randint(0, dias_totales))
        self.fecha_nacimiento = fecha.strftime("%Y-%m-%d")
        return self.fecha_nacimiento

    def generarCodigoPostal(self) -> int:
        cps = [1040, 1050, 3100, 3102, 3105, 44100, 44120, 64000, 64010, 64020]
        self.codigo_postal = rn.choice(cps)
        return self.codigo_postal

    def generarRFC(self) -> str:
        if not self.fecha_nacimiento:
            self.generarFechaNacimiento()

        paterno = self.a_paterno.upper()
        materno = self.a_materno.upper()
        nombre = self.nombres.upper().split()[0]

        letra1 = paterno[0]
        vocales = "AEIOU"
        letra2 = next((c for c in paterno[1:] if c in vocales), paterno[1])
        letra3 = materno[0]
        letra4 = nombre[0]

        aa, mm, dd = self.fecha_nacimiento.split("-")
        fecha_rfc = f"{aa[-2:]}{mm}{dd}"
        homoclave = "".join(rn.choices(string.ascii_uppercase + string.digits, k=3))

        self.rfc = f"{letra1}{letra2}{letra3}{letra4}{fecha_rfc}{homoclave}"
        return self.rfc

    def __getitem__(self, item: str):
        return getattr(self, item)


def generar_hombres(numero_nombres: int) -> list[Persona]:
    n_hombres = pd.read_csv(ruta_hombres)['nombre'].head(numero_nombres)
    apellidos = pd.read_csv(apellidos_csv)['apellido'].head(numero_nombres * 2)
    lista_personas = []

    for hombre in n_hombres:
        paterno = apellidos.iloc[rn.randint(0, len(apellidos) - 1)]
        materno = apellidos.iloc[rn.randint(0, len(apellidos) - 1)]
        persona = Persona(nombres=hombre, a_paterno=paterno, a_materno=materno, sexo='m')
        persona.generarFechaNacimiento()
        persona.generarCodigoPostal()
        persona.generarRFC()
        lista_personas.append(persona)

    return lista_personas


def generar_mujeres(numero_nombres: int) -> list[Persona]:
    n_mujeres = pd.read_csv(ruta_mujeres)['NOMBRE'].head(numero_nombres)
    apellidos = pd.read_csv(apellidos_csv, encoding='latin-1')['apellido'].head(numero_nombres * 2)
    lista_personas = []

    for mujer in n_mujeres:
        paterno = apellidos.iloc[rn.randint(0, len(apellidos) - 1)]
        materno = apellidos.iloc[rn.randint(0, len(apellidos) - 1)]
        persona = Persona(nombres=mujer, a_paterno=paterno, a_materno=materno, sexo='f')
        persona.generarFechaNacimiento()
        persona.generarCodigoPostal()
        persona.generarRFC()
        lista_personas.append(persona)

    return lista_personas
