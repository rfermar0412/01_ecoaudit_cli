from calculadora import estimar_consumo_wh, calcular_huella_co2
# =====================================================================
# EcoAudit CLI - Módulo Principal
# Autores: [Nombre Alumno 1] & [Nombre Alumno 2]
# =====================================================================

while True:
    print("\n=========================================")
    print(" 🌿 ECOAUDIT CLI - MENÚ PRINCIPAL 🌿 ")
    print("=========================================")
    print("1. Realizar nueva auditoría")
    print("2. Consultar histórico")
    print("3. Salir")
   
    entrada = input("\nSeleccione una opción (1-3): ").strip()
    try:
        opcion = int(entrada)
    except ValueError:
        print("Error: Debe introducir un número entero.")
        continue
   
    if opcion == 1:
        print("\n[OPCIÓN 1] Iniciando proceso de auditoría...")
        print("\n--- AUDITORÍA ENERGÉTICA ---")
       # Validación robusta de la opción introducida #
        try:
            proceso = input("Nombre del equipo/proceso: ").strip()
            potencia = float(input("Potencia consumida en Vatios (W): "))
            horas = float(input("Horas de uso diario: "))
            num_iter = int(input("Introduce número de iteraciones: ").strip())
            consumo = estimar_consumo_wh(potencia, horas, num_iter)
            huella = calcular_huella_co2(consumo)
            print(f"\n Resultados calculados para '{proceso}':")
            print(f"Consumo total: {consumo:.2f} Wh")
            print(f"Huella de carbono estimada: {huella:.4f} g CO2")
            # SIMULACIÓN ITERATIVA PASO A PASO (PARA INSPECCIÓN EN DEPURADOR)
            print("\nIniciando simulación ciclo a ciclo...")
            consumo_ciclo = estimar_consumo_wh(potencia, horas, 1) # Consumo de un solo ciclo
            consumo_acumulado = 0.0
            ciclo = 1

            while ciclo <= num_iter:
                consumo_acumulado = consumo_acumulado + consumo_ciclo # <--- PONDRÉIS AQUÍ EL PUNTO ROJO
                print(f" [Ciclo {ciclo}] Consumo acumulado parcial: {consumo_acumulado:.2f} Wh")
                ciclo = ciclo + 1
              # Guardado persistente en el archivo CSV
            with open("auditorias.csv", mode="a", encoding="utf-8") as archivo:
            # Escribimos los datos separados por comas y terminamos con salto de línea (\n)
                    archivo.write(f"{proceso},{potencia},{horas},{num_iter},{consumo:.2f},{huella:.4f}\n")
                    print("Registro guardado con éxito en 'auditorias.csv'.")
            if num_iter <= 0:
                print("El valor debe ser mayor que cero.")
            else:
                print(f"Configurado con éxito para {num_iter} iteraciones.")
        except ValueError:
            print("Error de formato: debe introducir un número entero.")
       
    elif opcion == 2:
        print("\n[OPCIÓN 2] Consultando registros históricos...")
        print("\n================ HISTORIAL DE AUDITORÍAS ================")
        try:
            with open("auditorias.csv", mode="r", encoding="utf-8") as archivo:
                contenido = archivo.read()
            print(contenido)
            pass # Comodín temporal para evitar errores de sintaxis en bloques vacíos. ¡Bórralo al escribir tu código!
        except FileNotFoundError:
            # Si el archivo NO existe en el disco duro, evitamos el bloqueo crítico y mostramos este aviso:
            print(" Aún no existen registros. Realiza una auditoría primero.")
   
    elif opcion == 3:
        print("\nSaliendo de EcoAudit CLI. ¡Hasta pronto!")
        break
   
    else:
        print("Opción no válida. Elija un número entre 1 y 3.")