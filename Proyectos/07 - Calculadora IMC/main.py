def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo Peso"
    elif 18.5 <= imc < 24.9:
        return "Normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidad Grado 1"
    elif 35 <= imc < 39.9:
        return "Obesidad Grado 2"
    else:
        return "Obesidad Grado 3"
    
def main():
    print("⚖️ Calculadora de IMC (Índice de Masa Corporal)")

    try:
        peso = float(input("Ingresa tu peso en kilogramos: "))
        altura = float(input("Ingresa tu estatura en metros (ej. 1.75): "))
    except ValueError:
        print("❌ Entrada inválida. Debes introducir números válidos.")
        return
    
    imc = calcular_imc(peso, altura)
    clasificacion = clasificar_imc(imc)

    print(f"\nTu IMC es: {round(imc, 2)}")
    print(f"Clasificación: {clasificacion}")

if __name__ == "__main__":
    main()