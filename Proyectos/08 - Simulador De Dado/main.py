import random

def lanzar_dado(lados=6):
    return random.randint(1, lados)

def main():
    print("🎲 Simulador de Dado")
    print("Presiona ENTER para lanzar el dado o escribe 'salir' para terminar.")

    while True:
        entrada = input(">>> ").strip().lower()
        if entrada == "salir":
            print("👋 ¡Gracias por jugar!")
            break
        resultado = lanzar_dado()
        print(f"Obtuviste: {resultado}")

if __name__ == "__main__":
    main()