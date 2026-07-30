while True: 
    
    canal = input("Ingrese un canal Wi-Fi entre 1 y 11: ") 
    
    if not canal.isdigit(): 
        print("Debe ingresar un número entero") 
        continue 
    
    canal = int(canal) 
    
    if 1 <= canal <= 11: 
        break 
    
    print("El canal está fuera del rango permitido") 
    print(f"Canal seleccionado: {canal}")