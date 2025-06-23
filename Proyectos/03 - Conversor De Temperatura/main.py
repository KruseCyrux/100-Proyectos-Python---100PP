def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_a_kelvin(c):
    return c + 273.15

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_a_kelvin(f):
    return (f + 459.67) * 5/9

def kelvin_a_celsius(k):
    return k - 273.15

def kelvin_a_fahrenheit(k):
    return (k * 9/5) - 459.67

def main():
    print("Conversor de Temperatura 🌡️")
    print("Unidades disponibles: Celsius (C), Fahrenheit (F), Kelvin (K)")

    origen = input("Unidad de Origen (C/F/K): ").upper()
    destino = input("Unidad de Destino (C/F/K): ").upper()
    valor = float(input("Temperatura a Convertir: "))

    if origen == destino:
        print(f"No hay nada que convertir. Resultado: {valor}°{destino}")
        return
    
    resultado = None
    if origen == "C" and destino == "F":
        resultado = celsius_a_fahrenheit(valor)
    elif origen == "C" and destino == "K":
        resultado = celsius_a_kelvin(valor)
    elif origen == "F" and destino == "C":
        resultado = fahrenheit_a_celsius(valor)
    elif origen == "F" and destino == "K":
        resultado = fahrenheit_a_kelvin(valor)
    elif origen == "K" and destino == "C":
        resultado = kelvin_a_celsius(valor)
    elif origen == "K" and destino == "F":
        resultado = kelvin_a_fahrenheit(valor)
    else:
        print("Unidades no válidas.")
        return
    print(f"{valor}°{origen} equivale a {round(resultado, 2)}°{destino}")

if __name__ == "__main__":
    main()