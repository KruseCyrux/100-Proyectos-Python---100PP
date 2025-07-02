from datetime import datetime

def pedir_datos_cliente():
    print("🧍 Datos del Cliente")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    rfc = input("RFC (opcional): ")
    return {
        "nombre": nombre,
        "direccion": direccion,
        "rfc": rfc
    }

def pedir_productos():
    productos = []
    while True:
        print("\n➕ Agregar producto (deja nombre vacío para terminar)")
        nombre = input("Nombre del producto: ")
        if not nombre:
            break
        try:
            cantidad = int(input("Cantidad: "))
            precio_unitario = float(input("Precio unitario: "))
        except ValueError:
            print("❌ Entrada inválida. Intenta de nuevo.")
            continue

        subtotal = cantidad * precio_unitario
        productos.append({
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio_unitario,
            "subtotal": subtotal
        })
    return productos

def calcular_total(productos):
    return sum(p["subtotal"] for p in productos)

def generar_factura(cliente, productos):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    total = calcular_total(productos)

    factura = f"""
    🧾 FACTURA SIMPLIFICADA
    Fecha: {fecha}
    Cliente: {cliente['nombre']}
    Dirección: {cliente['direccion']}
    RFC: {cliente['rfc']}

    Productos:
    """

    for p in productos:
        factura += f" - {p['cantidad']} x {p['nombre']} @ ${p['precio']:.2f} = ${p['subtotal']:.2f}\n"

    factura += f"\nTOTAL A PAGAR: ${total:.2f}\n"
    return factura

def guardar_factura(factura):
    nombre_archivo = f"factura_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(factura)
    print(f"✅ Factura guardada en: {nombre_archivo}")

def main():
    print("🧾 Generador de Facturas")
    cliente = pedir_datos_cliente()
    productos = pedir_productos()

    if not productos:
        print("⚠️ No se ingresaron productos. Factura cancelada.")
        return

    factura = generar_factura(cliente, productos)
    print("\n" + factura)
    guardar_factura(factura)

if __name__ == "__main__":
    main()