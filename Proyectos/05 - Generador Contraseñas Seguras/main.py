import random
import string

def generar_contraseña(longitud=12):
    if longitud < 4:
        return "Longitud mínima recomendada: 4"
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    print("🔐 Generador de Contraseñaas Seguras")

    try:
        longitud = int(input("Introduce la longitud deseada para la contraseña (mínimo 4): "))
        contraseña = generar_contraseña(longitud)
        print(f"Tu nueva contraseña es: {contraseña}")
    except ValueError:
        print("❌ Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()