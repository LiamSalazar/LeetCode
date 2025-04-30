import random
import string

def procesar_apellidos():
    n = int(input("¿Cuántos apellidos paternos tienes?: "))
    ultimo_apellido = ""

    for x in range(1, n + 1):
        apellido = input(f"Ingrese su apellido paterno número {x}: ").upper().strip()
        if x == n:
            ultimo_apellido = apellido

    return ultimo_apellido


def procesar_nombres():
    k = int(input("¿Cuántos nombres tienes?: "))
    nombres = []

    for i in range(1, k + 1):
        nombre = input(f"Ingrese su nombre número {i}: ").upper().strip()
        nombres.append(nombre)

    return nombres


def obtener_nombre_clave(nombres):
    if len(nombres) > 1 and nombres[0] in ("JOSE", "MARIA"):
        return nombres[1]
    return nombres[0]


def censurar_palabra(palabra):
    malas_palabras = {"BUEI", "BUEY", "CACA", "CAGA", "CAGO", "COGE", "COGI", "COJA",
                      "COJE", "COJI", "COJO", "CULO", "FETO", "GUEY", "JOTO", "KACA",
                      "KACO", "KOGE", "KOJO", "MAME", "MAMO", "MEAR", "MEAS", "MEON",
                      "MION", "MOCO", "PEDA", "PEDO", "PENE", "PUTA", "PUTO", "QULO",
                      "RATA", "RUIN"}
    return "X" + palabra[1:] if palabra[:4] in malas_palabras else palabra


def primera_vocal_interna(texto):
    for letra in texto[1:]:
        if letra in "AEIOU":
            return letra
    return "X"


def primera_consonante_interna(texto):
    for letra in texto[1:]:
        if letra in "BCDFGHJKLMNPQRSTVWXYZ":
            return letra
    return "X"


def generar_homoclave():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))


def obtener_rfc(nombre, apellido_paterno, apellido_materno, fecha_nacimiento):
    rfc = apellido_paterno[:2] + apellido_materno[:1] + nombre[:1]
    rfc = censurar_palabra(rfc)
    año, mes, dia = fecha_nacimiento.split("-")
    rfc += año[2:] + mes + dia
    return rfc


def obtener_curp(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado):
    estados = {
        "AGUASCALIENTES": "AS", "BAJA CALIFORNIA": "BC", "BAJA CALIFORNIA SUR": "BS",
        "CAMPECHE": "CC", "COAHUILA": "CL", "COLIMA": "CM", "CHIAPAS": "CS",
        "CHIHUAHUA": "CH", "CDMX": "DF", "CIUDAD DE MEXICO": "DF", "DURANGO": "DG",
        "GUANAJUATO": "GT", "GUERRERO": "GR", "HIDALGO": "HG", "JALISCO": "JC",
        "ESTADO DE MEXICO": "MC", "MICHOACAN": "MN", "MORELOS": "MS", "NAYARIT": "NT",
        "NUEVO LEON": "NL", "OAXACA": "OC", "PUEBLA": "PL", "QUERETARO": "QT",
        "QUINTANA ROO": "QR", "SAN LUIS POTOSI": "SP", "SINALOA": "SL", "SONORA": "SR",
        "TABASCO": "TC", "TAMAULIPAS": "TS", "TLAXCALA": "TL", "VERACRUZ": "VZ",
        "YUCATAN": "YN", "ZACATECAS": "ZS"
    }

    clave_estado = estados.get(estado.upper(), "NE")
    año, mes, dia = fecha_nacimiento.split("-")
    año = año[2:]

    curp = (
        apellido_paterno[0] +
        primera_vocal_interna(apellido_paterno) +
        apellido_materno[0] +
        nombre[0] +
        año + mes + dia +
        sexo +
        clave_estado +
        primera_consonante_interna(apellido_paterno) +
        primera_consonante_interna(apellido_materno) +
        primera_consonante_interna(nombre) +
        generar_homoclave()
    )

    return censurar_palabra(curp)


def obtener_clave_elector(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado):
    año, mes, dia = fecha_nacimiento.split("-")
    año = año[2:]
    clave = apellido_paterno[:2] + apellido_materno[:1] + nombre[:1]
    return clave + año + mes + dia + sexo + estado[:2]


nombres = procesar_nombres()
nombre_clave = obtener_nombre_clave(nombres)
apellido_paterno = procesar_apellidos()
apellido_materno = input("Ingresa tu apellido materno: ").strip().upper()
fecha_nacimiento = input("Ingresa tu fecha de nacimiento (AAAA-MM-DD): ").strip()
sexo = input("Ingresa tu sexo (H/M): ").strip().upper()
estado = input("Ingresa tu estado de nacimiento: ").strip().upper()

rfc = obtener_rfc(nombre_clave, apellido_paterno, apellido_materno, fecha_nacimiento)
curp = obtener_curp(nombre_clave, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado)
clave_elector = obtener_clave_elector(nombre_clave, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado)

print("\n--- RESULTADOS ---")
print(f"RFC: {rfc}")
print(f"CURP: {curp}")
print(f"Clave de Elector: {clave_elector}")
