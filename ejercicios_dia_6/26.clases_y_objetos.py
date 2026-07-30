import os 
os.system('cls')

class Router:
    def __init__ (self, fabricante, ipv4):
        self.fabricante = fabricante
        self.ipv4 = ipv4
    
    def mostrar_informacion(self):
        print(f"Router [ {self.fabricante},{self.ipv4}]")

router1 = Router("Cisco", "192.168.11.25")
router2 = Router("Mikrotik", "192.168.10.12")

router1.mostrar_informacion();