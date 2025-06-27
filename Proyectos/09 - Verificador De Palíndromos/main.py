def es_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    return texto == texto[::-1]

def main():
    print("🔁 Verificador De Palíndromos")
    frase = input("Escribe una palabra o frase: ")

    if es_palindromo(frase):
        print("✅ Es un Palíndromo")
    else:
        print("❌ No es un Palíndromo")

if __name__ == "__main__":
    main()