from centros_comerciales_implementacion import CentrosComerciales

if __name__ == "__main__":
    centros = []
    centros.append(CentrosComerciales("Mall del sol", "Av. de las americas", 200, 2000, 5000, "2024-05-22"))
    for centro in centros:
        print(centro)    
    
    print("El porcentaje de ocupación de parqueo es: ", CentrosComerciales.calcular_porcentaje_ocupacion_parqueo(centro,2000), "%")
   
    