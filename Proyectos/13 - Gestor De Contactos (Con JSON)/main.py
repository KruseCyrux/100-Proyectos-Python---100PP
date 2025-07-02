import json
import os

ARCHIVO = "contactos.json"

def cargar_contactos():
    if not os .path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)
    
def guardar_contactos(contactos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(contactos, f, indent=2)

def agregar_contactos(contactos):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Correo (Opcional): ")

    contactos.append({
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    })

    print("✅ Contacto agregado.")


def listar_contactos(contactos):
    if not contactos:
        print("📭 Lista vacía.")
        return

    print("\n📇 Contactos:")
    for i, c in enumerate(contactos, start=1):
        print(f"{i}. {c['nombre']} - {c['telefono']} - {c.get('email', '')}")

def buscar_contacto(contactos):
    termino = input("Buscar por nombre o teléfono: ").lower()
    resultados = [c for c in contactos if termino in c["nombre"].lower() or termino in c["telefono"]]

    if resultados:
        print("\n🔍 Resultados encontrados:")
        for c in resultados:
            print(f"- {c['nombre']} - {c['telefono']} - {c.get('email', '')}")
    else:
        print("❌ No se encontraron coincidencias.")

def eliminar_contacto(contactos):
    listar_contactos(contactos)
    try:
        idx = int(input("Número de contacto a eliminar: ")) - 1
        if 0 <= idx < len(contactos):
            eliminado = contactos.pop(idx)
            print(f"🗑️ Contacto eliminado: {eliminado['nombre']}")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada inválida.")

def main():
    contactos = cargar_contactos()

    while True:
        print("\n📇 Gestor de Contactos")
        print("1. Listar contactos")
        print("2. Agregar contacto")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            listar_contactos(contactos)
        elif opcion == "2":
            agregar_contactos(contactos)
            guardar_contactos(contactos)
        elif opcion == "3":
            buscar_contacto(contactos)
        elif opcion == "4":
            eliminar_contacto(contactos)
            guardar_contactos(contactos)
        elif opcion == "5":
            print("👋 ¡Hasta pronto!")
            guardar_contactos(contactos)
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()