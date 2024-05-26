from centros_comerciales_implementacion import CentrosComerciales

if __name__ == "__main__":
    centros = []
    centros.append(CentrosComerciales("Mall del sol", "Av. de las americas", 200, 2000, 5000, "2024-05-22"))
    for centro in centros:
        print(centro)    
    
    CentrosComerciales.verificar_abierto_dia(centro, "Lunes")