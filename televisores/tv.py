class TV:

    _numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        TV._numTV += 1

    def getMarca(self):
        return self._marca

    def setMarca(self, marca):
        self._marca = marca

    def getCanal(self):
        return self._canal

    def setCanal(self, canal):
        if(self._estado == True and 1<= canal <=120):
            self._canal = canal 

    def getVolumen(self):
        return self._volumen

    def setVolumen(self, volumen):
        if(self._estado == True and 0<= volumen <=7):
            self._volumen = volumen

    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio):
        self._precio = precio

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado

    def canalUp(self):
        if self._canal < 120 and self._estado:
            self._canal += 1

    def canalDown(self):
        if self._canal > 1 and self._estado:
            self._canal -= 1

    def volumenUp(self):
        if self._volumen < 7 and self._estado:
            self._volumen += 1

    def volumenDown(self):
        if self._volumen > 0 and self._estado:
            self._volumen -= 1

    @classmethod
    def getNumTV(cls):
            return cls._numTV

    @classmethod 
    def setNumTV(cls, numTV):
        cls._numTV = numTV
    
    def getControl(self):
        return self._control

    def setControl(self, control):
        self._control = control