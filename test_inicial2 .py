pareja_autora = input("Dime los dos nombres: ").strip()
potatil = input("dime el nombre del dispositivo: ").strip()
potencia_str= input("dime su potencia: ").strip()
potencia_wh = float(potencia_str)
result = potencia_wh * 24
print(f"La pareja {pareja_autora} con el portatil {potatil} gasta una potencia de {result}Wh")