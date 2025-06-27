import random

def main():
    print("🎯 ¡Bienvenido al juego: Adivina El Número!")
    print("Estoy pensando en un número del 1 al 100... ¿puedes adivinar cuál es?")

    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    while not adivinado:
        try:
            intento = int(input("Introduce tu número: "))
            intentos += 1

            if intento < numero_secreto:
                print("Demasiado Bajo 📉")
            elif intento > numero_secreto:
                print("Demasiado Alto 📈")
            else:
                print(f"🎉 ¡Correcto! El número era {numero_secreto}. Lo lograste en {intentos} intento(s).")
                adivinado = True
        except ValueError:
            print(f"❌ Entrada inválida. Por favor, introduce un número entero.")

if __name__ == "__main__":
    main()