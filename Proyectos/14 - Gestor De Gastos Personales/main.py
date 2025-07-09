import csv
import os
from datetime import datetime

ARCHIVO = "gastos.csv"

def inicializar_archivo():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, mode="w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Fecha", "Categoría", "Descripción", "Monto"])

def agregar_gasto():
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    categoria = input("Categoría (Ej: comida, transporte, etc.): ")
    descripcion = input("Descripción del gasto: ")

    try:
        monto = float(input("Monto gastado: "))
    except ValueError:
        print("❌ Monto inválido.")
        return
    
    with open(ARCHIVO, mode="a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([fecha, categoria, descripcion, monto])
    print("✅ Gasto registrado correctamente.")

def mostrar_gastos():
    if not os.path.exists(ARCHIVO):
        print("📭 No hay registros aún.")
        return
    
    total = 0
    print("\n📜 Lista de gastos:\n")
    with open(ARCHIVO, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader) #Saltar Encabezado
        for fila in reader:
            fecha, categoria, descripcion, monto = fila
            print(f"[{fecha}] {categoria} - {descripcion} -> ${monto}")
            total += float(monto)

    print(f"\n💰 Total Gastado: ${total:.2f}")

def main():
    inicializar_archivo()
    while True:
        print("\n💸 Registro de Gastos Personales")
        print("1. Agregar Gasto")
        print("2. Ver historial de gastos")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_gasto()
        elif opcion == "2":
            mostrar_gastos()
        elif opcion == "3":
            print("👋 ¡Hasta la próxima!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()