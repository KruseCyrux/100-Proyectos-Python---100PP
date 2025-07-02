import os

ARCHIVO = "tareas.txt"

def cargar_tareas():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def guardar_tareas(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for tarea in tareas:
            f.write(tarea + "\n")

def mostrar_tareas(tareas):
    if not tareas:
        print("📭 No hay tareas pendientes.")
        return
    print("\n📋 Lista de tareas:")
    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea}")

def agregar_tarea(tareas):
    nueva = input("✍️ Escribe la nueva tarea: ")
    tareas.append(f"[ ] {nueva}")
    print("✅ Tarea agregada.")

def completar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        idx = int(input("Número de la tarea completada: ")) - 1
        if 0 <= idx < len(tareas):
            if "[x]" in tareas[idx]:
                print("⚠️ Esa tarea ya estaba completada.")
            else:
                tareas[idx] = tareas[idx].replace("[ ]", "[x]")
                print("🎉 ¡Tarea completada!")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada no válida.")

def main():
    tareas = cargar_tareas()

    while True:
        print("\n📝 Gestor de Tareas")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
            guardar_tareas(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
            guardar_tareas(tareas)
        elif opcion == "4":
            print("👋 ¡Hasta luego!")
            guardar_tareas(tareas)
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()