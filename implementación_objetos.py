from centros_comerciales_implementacion import CentrosComerciales

if __name__ == "__main__":
    centros = []
    centros.append(CentrosComerciales("Mall del sol", "Av. de las americas", 200, 1500, 5000, "2024-05-22"))
    centros.append(CentrosComerciales("San Marino", "Av. Francisco de Orellana", 180, 1200, 4500, "2024-05-23"))
    
    for centro in centros:
        print(centro)      
