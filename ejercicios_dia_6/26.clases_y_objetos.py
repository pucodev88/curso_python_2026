class Dispositivo:
    def __init__(self, codigo, nombre, direccion_ip):
        self.codigo = codigo 
        self.nombre = nombre 
        self.direccion_ip = direccion_ip 
        self.estado_activo = True  
    
    def actualizar_estado(self, estado_actual):
        self.estado_activo = estado_actual
        return self.estado_activo
    
    def mostrar_info(self):
        print(f"Codigo: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Dirección ip: {self.direccion_ip}")
        print(f"Estado: {self.estado_activo}")

dispositivo_1 = Dispositivo("DISP001", "Equipo de Red", "192.168.10.5")
dispositivo_1.actualizar_estado(False) 
#dispositivo_1.mostrar_info()

dispositivo_2 = Dispositivo("DISP002", "Servidor", "192.168.20.5")
dispositivo_3 = Dispositivo("DISP003", "Router", "192.168.30.5")

lista_dispositivos = []
lista_dispositivos.append(dispositivo_1)
lista_dispositivos.append(dispositivo_2)
lista_dispositivos.append(dispositivo_3)

#print(lista_dispositivos[0])

codigo_a_eliminar = "DISP003"
for dispositivo in lista_dispositivos.copy():
    if dispositivo.codigo == codigo_a_eliminar:
        lista_dispositivos.remove(dispositivo)
    else: 
        dispositivo.mostrar_info()

# HERENCIA

class Router(Dispositivo):
    def __init__(self, codigo, nombre, direccion_ip, numero_puertos):
        super().__init__(codigo, nombre, direccion_ip)
        self.numero_puertos = numero_puertos
    
    def mostrar_info_personalizado(self):
        info_base = super().mostrar_info()
        return (f"{info_base}", f"{self.numero_puertos}")
        

router_cisco = Router("cisco_001", "Cisco Modelo X", "192.168.40.5", 16)

router_cisco.mostrar_info_personalizado()

        
        

    
    