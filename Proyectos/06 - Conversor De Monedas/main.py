def obtener_tasa(origen, destino):
    tasas = {
        "USD": {"MXN": 18.0, "EUR": 0.85, "USD": 1.0},
        "MXN": {"USD": 0.055, "EUR": 0.047, "MXN": 1.0},
        "EUR": {"USD": 1.17, "MXN": 21.3, "EUR": 1.0},
    }

    try:
        return tasas[origen][destino]
    except KeyError:
        return None
    
def main():
    print("💱 Conversor de Monedas")
    print("Monedas disponibles: USD, MXN, EUR")

    origen = input("Moneda de Origen (USD/MXN/EUR): ").upper()
    destino = input("Moneda de Destino (USD/MXN/EUR): ").upper()

    try:
        cantidad = float(input("Cantidad a Convertir: "))
    except ValueError:
        print(f"❌ Entrada inválida. Debes introducir un número.")
        return
    
    tasa = obtener_tasa(origen, destino)

    if tasa is None:
        print(f"❌ Moneda no válida o combinación no soportada.")
    else:
        resultado = cantidad * tasa
        print(f"{cantidad} {origen} = {round(resultado, 2)} {destino}")

if __name__ == "__main__":
    main()