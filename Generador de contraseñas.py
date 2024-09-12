import random
import string
import argparse

# Función para generar una contraseña segura
def generar_contraseña(longitud=12, incluir_ascii=False):
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    # Si incluir_ascii está activado, agregar todos los caracteres imprimibles de ASCII
    if incluir_ascii:
        ascii_extra = ''.join(chr(i) for i in range(32, 127))
        todo = ascii_extra
    else:
        todo = mayusculas + minusculas + numeros + simbolos

    # Garantizar que la contraseña contenga al menos un carácter de cada tipo
    contraseña = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Completar la longitud especificada
    if longitud < 4:
        raise ValueError("La longitud mínima debe ser de 4 caracteres")
    
    contraseña += random.choices(todo, k=longitud - 4)

    # Mezclar los caracteres
    random.shuffle(contraseña)
    return ''.join(contraseña)

# Función para generar múltiples contraseñas
def generar_varias_contraseñas(cantidad, longitud=12, incluir_ascii=False):
    return [generar_contraseña(longitud, incluir_ascii) for _ in range(cantidad)]

# Configuración del script para la línea de comandos
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generador de contraseñas seguras y complejas.")
    
    # Argumentos del script
    parser.add_argument("-l", "--longitud", type=int, default=12, help="Longitud de la contraseña (por defecto 12 caracteres).")
    parser.add_argument("-c", "--cantidad", type=int, default=1, help="Cantidad de contraseñas a generar.")
    parser.add_argument("-a", "--ascii", action="store_true", help="Incluir caracteres ASCII imprimibles adicionales.")
    
    args = parser.parse_args()
    
    # Generar las contraseñas
    contraseñas = generar_varias_contraseñas(args.cantidad, args.longitud, args.ascii)
    
    # Mostrar las contraseñas generadas
    for i, password in enumerate(contraseñas, 1):
        print(f"Contraseña {i}: {password}"
