def contar_palabras(texto):
    palabras = texto.strip().split()
    return len(palabras)

def main():
    print("📊 Contador de Palabras")
    texto = input("Escribe una frase o texto: ")

    cantidad = contar_palabras(texto)
    print(f"📝 Total de palabras: {cantidad}")

if __name__ == "__main__":
    main()