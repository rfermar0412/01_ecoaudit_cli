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
    
    # Validación robusta de la opción introducida
    try:
        opcion = int(entrada)
    except ValueError:
        print("Error: Debe introducir un número entero.")
        continue
    
    if opcion == 1:
        print("\n[OPCIÓN 1] Iniciando proceso de auditoría...")
        print("\n--- AUDITORÍA ENERGÉTICA ---")
        proceso = input("Nombre del equipo/proceso: ").strip()
        potencia = float(input("Potencia consumida en Vatios (W): "))
        horas = float(input("Horas de uso diario: "))
        try:
            num_iter = int(input("Introduce número de iteraciones: ").strip())
            if num_iter <= 0:
                print("El valor debe ser mayor que cero.")
            else:
                print(f"Configurado con éxito para {num_iter} iteraciones.")
        except ValueError:
            print("Error de formato: debe introducir un número entero.")
        
        consumo = estimar_consumo_wh(potencia, horas, num_iter)
        huella = calcular_huella_co2(consumo)
        print(f"\n Resultados calculados para '{proceso}':")
        print(f"Consumo total: {consumo:.2f} Wh")
        print(f"Huella de carbono estimada: {huella:.4f} g CO2")
    
    elif opcion == 2:
        print("\n[OPCIÓN 2] Consultando registros históricos...")
    
    elif opcion == 3:
        print("\nSaliendo de EcoAudit CLI. ¡Hasta pronto!")
        break
    
    else:
        print("⚠️ Opción no válida. Elija un número entre 1 y 3.")