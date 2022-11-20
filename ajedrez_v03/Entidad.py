class Pieza() :
    
    def __init__(self, color) :
        self.color = color
        
    def getColor(self) :
        return self.color
        
class Peon(Pieza) :
    
    cantb = 0
    cantn = 0

    def __init__(self, color) :
        Pieza.__init__(self, color)
        self.__m = True
        if color.lower() == "blanco" :
            self.__ico = "♙"
            self.__pos = (1, Peon.cantb)
            Peon.cantb += 1
        elif color.lower() == "negro" :
            self.__ico = "♟"
            self.__pos = (6, Peon.cantn)
            Peon.cantn +=1
    
    def getM(self) :
        return self.__m
        
    def setM(self, val) :
        self.__m = val
        
    def getPos(self) :
        return self.__pos
        
    def setPos(self, posn) :
        self.__pos = posn

    def getIco(self) :
        return self.__ico
    
    def __str__(self) :
        cadena = self.getIco()
        return cadena

class Torre(Pieza) :

    cantb = 0
    cantn = 0
    
    def __init__(self, color) :
        Pieza.__init__(self, color)
        if color.lower() == "blanco" :
            self.__ico = "♖"
            self.__pos = (0, Torre.cantb)
            Torre.cantb += 7
        elif color.lower() == "negro" :
            self.__ico = "♜"
            self.__pos = (7, Torre.cantn)
            Torre.cantn +=7

    def getIco(self) :
        return self.__ico
        
    def getPos(self) :
        return self.__pos
        
    def setPos(self, posn) :
        self.__pos = posn

    def __str__(self) :
        cadena = self.getIco()
        return cadena
            
class Alfil(Pieza) :
    
    cantb = 2
    cantn = 2

    def __init__(self, color) :
        Pieza.__init__(self, color)
        if color.lower() == "blanco" :
            self.__ico = "♗"
            self.__pos = (0, Alfil.cantb)
            Alfil.cantb += 3
        elif color.lower() == "negro" :
            self.__ico = "♝"
            self.__pos = (7, Alfil.cantn)
            Alfil.cantn += 3
            
    def getIco(self) :
        return self.__ico
        
    def getPos(self) :
        return self.__pos
        
    def setPos(self, posn) :
        self.__pos = posn

    def __str__(self) :
        cadena = self.getIco()
        return cadena
            
class Caballo(Pieza) :
    
    cantb = 1
    cantn = 1

    def __init__(self, color) :
        Pieza.__init__(self, color)
        if color.lower() == "blanco" :
            self.__ico = "♘"
            self.__pos = (0, Caballo.cantb)
            Caballo.cantb += 5
        elif color.lower() == "negro" :
            self.__ico = "♞"
            self.__pos = (7, Caballo.cantn)
            Caballo.cantn += 5
            
    def getIco(self) :
        return self.__ico
        
    def getPos(self) :
        return self.__pos
        
    def setPos(self, posn) :
        self.__pos = posn

    def __str__(self) :
        cadena = self.getIco()
        return cadena
            
class Rey(Pieza) :

    def __init__(self, color) :
        Pieza.__init__(self, color)
        if color.lower() == "blanco" :
            self.__ico = "♔"
            self.__pos = (0, 4)
        elif color.lower() == "negro" :
            self.__ico = "♚"
            self.__pos = (7, 4)
            
    def getIco(self) :
        return self.__ico
        
    def getPos(self) :
        return self.__pos
        
    def setPos(self, posn) :
        self.__pos = posn

    def __str__(self) :
        cadena = self.getIco()
        return cadena
    
class Reina(Pieza) :

    def __init__(self, color) :
        Pieza.__init__(self, color)
        if color.lower() == "blanco" :
            self.__ico = "♕"
            self.__pos = (0, 3)
        elif color.lower() == "negro" :
            self.__ico = "♛"
            self.__pos = (7, 3)
            
    def getIco(self) :
        return self.__ico
        
    def getPos(self) :
        return self.__pos
        
    def setPos(self, posn) :
        self.__pos = posn
    
    def __str__(self) :
        cadena = self.getIco()
        return cadena