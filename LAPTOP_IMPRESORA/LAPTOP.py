class Laptop():
    def __init__(self,modelo,cap_disco,sistema_operativo,num_puertos_usb,procesador):
        self.modelo=modelo
        self.cap_disco=cap_disco
        self.sitema_operativo=sistema_operativo
        self.num_puertos_usb=num_puertos_usb
        self.procesador=procesador
    def instalar_programas(self):
        pass
    def getNum_puertos_usb(self):
        return self.num_puertos_usb
    def setModelo(self,modelo):
        self.modelo=modelo

