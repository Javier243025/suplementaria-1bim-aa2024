class CentrosComerciales:
    def __init__(self, nombre, direccion, numero_tiendas, capacidad_parqueo, area_total, fecha_inauguracion):
        self.nombre = nombre
        self.direccion = direccion
        self.numero_tiendas = numero_tiendas
        self.capacidad_parqueo = capacidad_parqueo
        self.area_total = area_total
        self.fecha_inauguracion = fecha_inauguracion
        self.autos = fecha_inauguracion

    def __str__(self):
        return f"{self.nombre} ubicado en {self.direccion} con {self.numero_tiendas} tiendas y capacidad de parqueo para {self.capacidad_parqueo} autos. Area total: {self.area_total} metros cuadrados. Inaugurado el {self.fecha_inauguracion}."

    def calcular_porcentaje_ocupacion_parqueo(self, autos_estacionados):
        return (autos_estacionados / self.capacidad_parqueo) * 100

    def verificar_abierto_dia(self, dia):
        #dias_abiertos =["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", " Sabado", "Domingo"]
        if dia != "Lunes":
            print("Si esta abierto el día:", dia) 
        else:
            print("No esta abierto el día:", dia) 
    

