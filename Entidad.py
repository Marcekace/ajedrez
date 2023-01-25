#  Ajedrez v 0.4
#  Copyright 2022 Marcelo Kacerovsky <marcelokacerovsky@marcelos-MacBook-Air.local>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
from random import randrange


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


    def comprobarTablero(self, tablero) :
        movimientos = []

        if self.color == "blanco" :
            for i in range(-1,2,2) :
                if self.__pos[1] + i >= 0 and self.__pos[1] + i <= 7 :
                    if tablero[self.__pos[0] + 1][self.__pos[1] + i] != None :
                        if tablero[self.__pos[0] + 1][self.__pos[1] + i].getColor() == "negro" :
                            movimientos.append(((self.__pos[0] + 1), (self.__pos[1] + i)))
            if self.__m and tablero[self.__pos[0] + 2][self.__pos[1]] == None and tablero[self.__pos[0] + 1][self.__pos[1]] == None :
                movimientos.append(((self.__pos[0] + 2), (self.__pos[1])))
            if  tablero[(self.__pos[0] + 1)][self.__pos[1]] == None :
                movimientos.append(((self.__pos[0] + 1), (self.__pos[1])))
        else :
            for i in range(-1,2,2) :
                if self.__pos[1] + i >= 0 and self.__pos[1] + i <= 7 :
                    if tablero[self.__pos[0] - 1][self.__pos[1] + i] != None :
                        if tablero[self.__pos[0] - 1][self.__pos[1] + i].getColor() == "blanco" :
                            movimientos.append(((self.__pos[0] - 1), (self.__pos[1] + i)))
            if self.__m and tablero[self.__pos[0] - 2][self.__pos[1]] == None and tablero[self.__pos[0] - 1][self.__pos[1]] == None :
                movimientos.append(((self.__pos[0] - 2), (self.__pos[1])))
            if  tablero[(self.__pos[0] - 1)][self.__pos[1]] == None :
                movimientos.append(((self.__pos[0] - 1), (self.__pos[1])))
        
        return movimientos


    def __repr__(self) :
        return self.__ico


    def __str__(self) :
        return self.__ico


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


    def getPos(self) :
        return self.__pos


    def setPos(self, posn) :
        self.__pos = posn


    def comprobarTablero(self, tablero) :
        movimientos = []

        # Superior
        for i in range(self.__pos[0] - 1, -1, -1) :
            if tablero[i][self.__pos[1]] != None :
                if tablero[i][self.__pos[1]].getColor() != self.color :
                    movimientos.append(((i), (self.__pos[1])))
                    break
                else :
                    break
            else :
                movimientos.append(((i), (self.__pos[1])))
        # Inferior
        for i in range(self.__pos[0] + 1, 8) :
            if tablero[i][self.__pos[1]] != None :
                if tablero[i][self.__pos[1]].getColor() != self.color :
                    movimientos.append(((i), (self.__pos[1])))
                    break
                else :
                    break
            else :
                movimientos.append(((i), (self.__pos[1])))
        # Izquierdo
        for i in range(self.__pos[1] - 1, -1, -1) :
            if tablero[self.__pos[0]][i] != None :
                if tablero[self.__pos[0]][i].getColor() != self.color :
                    movimientos.append(((self.__pos[0]), (i)))
                    break
                else :
                    break
            else :
                movimientos.append(((self.__pos[0]), (i)))
        # Derecha
        for i in range(self.__pos[1] + 1, 8) :
            if tablero[self.__pos[0]][i] != None :
                if tablero[self.__pos[0]][i].getColor() != self.color :
                    movimientos.append(((self.__pos[0]), (i)))
                    break
                else :
                    break
            else :
                movimientos.append(((self.__pos[0]), (i)))

        return movimientos


    def __repr__(self) :
        return self.__ico


    def __str__(self) :
        return self.__ico


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


    def getPos(self) :
        return self.__pos


    def setPos(self, posn) :
        self.__pos = posn


    def comprobarTablero(self, tablero) :
        movimientos = []

        d = 1
        # diagonal superior izquierda
        for i in range(self.__pos[0] - 1, -1, -1) :
            if (self.__pos[1] - d) >= 0 :
                if tablero[i][self.__pos[1] - d] != None :
                    if tablero[i][self.__pos[1] - d].getColor() != self.color :
                        movimientos.append(((i), (self.__pos[1] - d)))
                        break
                    else :
                        break
                else :
                    movimientos.append(((i), (self.__pos[1] - d)))
                    d += 1
            else :
                break
        # diagonal superior derecha
        d = 1
        for i in range(self.__pos[0] - 1, -1, -1) :
            if (self.__pos[1] + d) <= 7 :
                if tablero[i][self.__pos[1] + d] != None :
                    if tablero[i][self.__pos[1] + d].getColor() != self.color :
                        movimientos.append(((i), (self.__pos[1] + d)))
                        break
                    else :
                        break
                else :
                    movimientos.append(((i), (self.__pos[1] + d)))
                    d += 1
            else :
                break
        # diagonal inferior izquierda
        d = 1
        for i in range(self.__pos[0] + 1, 8) :
            if (self.__pos[1] - d) >= 0 :
                if tablero[i][self.__pos[1] - d] != None :
                    if tablero[i][self.__pos[1] - d].getColor() != self.color :
                        movimientos.append(((i), (self.__pos[1] - d)))
                        break
                    else :
                        break
                else :
                    movimientos.append(((i), (self.__pos[1] - d)))
                    d += 1
            else :
                break
        # diagonal inferior derecha
        d = 1
        for i in range(self.__pos[0] + 1, 8) :
            if (self.__pos[1] + d) <= 7 :
                if tablero[i][self.__pos[1] + d] != None :
                    if tablero[i][self.__pos[1] + d].getColor() != self.color :
                        movimientos.append(((i), (self.__pos[1] + d)))
                        break
                    else :
                        break
                else :
                    movimientos.append(((i), (self.__pos[1] + d)))
                    d += 1
            else :
                break

        return movimientos


    def __repr__(self) :
        return self.__ico


    def __str__(self) :
        return self.__ico


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


    def getPos(self) :
        return self.__pos


    def setPos(self, posn) :
        self.__pos = posn


    def comprobarTablero(self, tablero) :
        movimientos = []

        # Inferior
        for i in range(-1, 2, 2) :
            if (self.__pos[0] + 2) <= 7 and (((self.__pos[1] + i) <= 7) and ((self.__pos[1] + i) >= 0)) :
                if tablero[self.__pos[0] + 2][self.__pos[1] + i] != None :
                    if tablero[self.__pos[0] + 2][self.__pos[1] + i].getColor() != self.color :
                        movimientos.append(((self.__pos[0] + 2), (self.__pos[1] + i)))
                else :
                    movimientos.append(((self.__pos[0] + 2), (self.__pos[1] + i)))
        # Superior
            if (self.__pos[0] - 2) >= 0 and (((self.__pos[1] + i) <= 7) and ((self.__pos[1] + i) >= 0)) :
                if tablero[self.__pos[0] - 2][self.__pos[1] + i] != None :
                    if tablero[self.__pos[0] - 2][self.__pos[1] + i].getColor() != self.color :
                        movimientos.append(((self.__pos[0] - 2), (self.__pos[1] + i)))
                else :
                    movimientos.append(((self.__pos[0] - 2), (self.__pos[1] + i)))
        # Derecha
            if (self.__pos[1] + 2) <= 7 and (((self.__pos[0] + i) <= 7) and ((self.__pos[0] + i) >= 0)) :
                if tablero[self.__pos[0] + i][self.__pos[1] + 2] != None :
                    if tablero[self.__pos[0] + i][self.__pos[1] + 2].getColor() != self.color :
                        movimientos.append(((self.__pos[0] + i), (self.__pos[1] + 2)))
                else :
                    movimientos.append(((self.__pos[0] + i), (self.__pos[1] + 2)))
        # Izquierda
            if (self.__pos[1] - 2) >= 0 and (((self.__pos[0] + i) <= 7) and ((self.__pos[0] + i) >= 0)) :
                if tablero[self.__pos[0] + i][self.__pos[1] - 2] != None :
                    if tablero[self.__pos[0] + i][self.__pos[1] - 2].getColor() != self.color :
                        movimientos.append(((self.__pos[0] + i), (self.__pos[1] - 2)))
                else :
                    movimientos.append(((self.__pos[0] + i), (self.__pos[1] - 2)))

        return movimientos


    def __repr__(self) :
        return self.__ico


    def __str__(self) :
        return self.__ico


class Rey(Pieza) :


    def __init__(self, color) :
        Pieza.__init__(self, color)
        if color.lower() == "blanco" :
            self.__ico = "♔"
            self.__pos = (0, 4)
        elif color.lower() == "negro" :
            self.__ico = "♚"
            self.__pos = (7, 4)


    def getPos(self) :
        return self.__pos


    def setPos(self, posn) :
        self.__pos = posn


    def comprobarTablero(self, tablero) :
        movimientos = []

        for i in range(-1, 2) :
            for j in range(-1, 2) :
                if (self.__pos[0] + i) >= 0 and (self.__pos[0] + i) <= 7 and (self.__pos[1] + j) >= 0 and (self.__pos[1] + j) <= 7 :
                    if tablero[self.__pos[0] + i][self.__pos[1] + j] != None :
                        if tablero[self.__pos[0] + i][self.__pos[1] + j].getColor() != self.color :
                            movimientos.append(((self.__pos[0] + i), (self.__pos[1] + j)))
                    else :
                        movimientos.append(((self.__pos[0] + i), (self.__pos[1] + j)))

        return movimientos


    def __repr__(self) :
        return self.__ico


    def __str__(self) :
        return self.__ico


class Reina(Pieza) :


    def __init__(self, color) :
        Pieza.__init__(self, color)
        if color.lower() == "blanco" :
            self.__ico = "♕"
            self.__pos = (0, 3)
        elif color.lower() == "negro" :
            self.__ico = "♛"
            self.__pos = (7, 3)


    def getPos(self) :
        return self.__pos


    def setPos(self, posn) :
        self.__pos = posn


    def comprobarTablero(self, tablero) :
        movimientos = []

        # Lados
        # Superior
        for i in range(self.__pos[0] - 1, -1, -1) :
            if tablero[i][self.__pos[1]] != None :
                if tablero[i][self.__pos[1]].getColor() != self.color :
                    movimientos.append(((i), (self.__pos[1])))
                    break
                else :
                    break
            else :
                movimientos.append(((i), (self.__pos[1])))
        # Inferior
        for i in range(self.__pos[0] + 1, 8) :
            if tablero[i][self.__pos[1]] != None :
                if tablero[i][self.__pos[1]].getColor() != self.color :
                    movimientos.append(((i), (self.__pos[1])))
                    break
                else :
                    break
            else :
                movimientos.append(((i), (self.__pos[1])))
        # Izquierda
        for i in range(self.__pos[1] - 1, -1, -1) :
            if tablero[self.__pos[0]][i] != None :
                if tablero[self.__pos[0]][i].getColor() != self.color :
                    movimientos.append(((self.__pos[0]), (i)))
                    break
                else :
                    break
            else :
                movimientos.append(((self.__pos[0]), (i)))
        # Derecha
        for i in range(self.__pos[1] + 1, 8) :
            if tablero[self.__pos[0]][i] != None :
                if tablero[self.__pos[0]][i].getColor() != self.color :
                    movimientos.append(((self.__pos[0]), (i)))
                    break
                else :
                    break
            else :
                movimientos.append(((self.__pos[0]), (i)))
        # Diagonales
        # Superior izquierda
        d = 1
        for i in range(self.__pos[0] - 1, -1, -1) :
            if (self.__pos[1] - d) >= 0 :
                if tablero[i][self.__pos[1] - d] != None :
                    if tablero[i][self.__pos[1] - d].getColor() != self.color :
                        movimientos.append(((i), (self.__pos[1] - d)))
                        break
                    else :
                        break
                else :
                    movimientos.append(((i), (self.__pos[1] - d)))
                    d += 1
            else :
                break
        # Superior derecha
        d = 1
        for i in range(self.__pos[0] - 1, -1, -1) :
            if (self.__pos[1] + d) <= 7 :
                if tablero[i][self.__pos[1] + d] != None :
                    if tablero[i][self.__pos[1] + d].getColor() != self.color :
                        movimientos.append(((i), (self.__pos[1] + d)))
                        break
                    else :
                        break
                else :
                    movimientos.append(((i), (self.__pos[1] + d)))
                    d += 1
            else :
                break
        # Inferior izquierda
        d = 1
        for i in range(self.__pos[0] + 1, 8) :
            if (self.__pos[1] - d) >= 0 :
                if tablero[i][self.__pos[1] - d] != None :
                    if tablero[i][self.__pos[1] - d].getColor() != self.color :
                        movimientos.append(((i), (self.__pos[1] - d)))
                        break
                    else :
                        break
                else :
                    movimientos.append(((i), (self.__pos[1] - d)))
                    d += 1
            else :
                break
        # Inferior derecha
        d = 1
        for i in range(self.__pos[0] + 1, 8) :
            if (self.__pos[1] + d) <= 7 :
                if tablero[i][self.__pos[1] + d] != None :
                    if tablero[i][self.__pos[1] + d].getColor() != self.color :
                        movimientos.append(((i), (self.__pos[1] + d)))
                        break
                    else :
                        break
                else :
                    movimientos.append(((i), (self.__pos[1] + d)))
                    d += 1
            else :
                break

        return movimientos


    def __repr__(self) :
        return self.__ico


    def __str__(self) :
        return self.__ico


class Jugador() :


    def __init__(self, color) :
        self.__eleccion = None
        self.__rey = Rey(color)
        self.__piezas = [ Torre(color), Caballo(color), Alfil(color), Reina(color), self.__rey, Alfil(color), Caballo(color), Torre(color),
                          Peon(color),  Peon(color),    Peon(color),  Peon(color),  Peon(color), Peon(color), Peon(color),    Peon(color) ]
        self.__piezas_capturadas = []


    def getPiezas(self) :
        return self.__piezas


    def getPiezasCapturadas(self) :
        return self.__piezas_capturadas


    def getEleccion(self) :
        return self.__eleccion


    def setEleccion(self, eleccion) :
        """ tupla (pieza, bg original) """
        self.__eleccion = eleccion


    def getRey(self) :
        return self.__rey


class Maquina(Jugador) :


    def __init__(self, color):
        super().__init__(color)
        self.__switch = True


    def movimiento(self, jugador, tablero) :
        """Retorna las coordenadas del movimiento de la maquina (pieza, movimiento)"""
        # Escanea el tablero en busca del rey contrario
        reyContrario = jugador.getRey().getPos()

        for i in self.getPiezas() :
            movimientos = i.comprobarTablero(tablero)
            if reyContrario in movimientos :
                return (i.getPos(), reyContrario)
        # Escanea el tablero para evitar el jaque

        for i in jugador.getPiezas() :
            movimientos = i.comprobarTablero(tablero)
            if self.getRey().getPos() in movimientos :
                return (self.getRey().getPos(), self.getRey().comprobarTablero(tablero)[randrange(0, len(self.getRey().comprobarTablero(tablero)))])

        if self.__switch :
            while True :
                pieza = self.getPiezas()[randrange(0, len(self.getPiezas()))]
                movimientos = pieza.comprobarTablero(tablero)
                if movimientos != [] :
                    self.__switch = False
                    return (pieza.getPos(), movimientos[randrange(0, len(movimientos))])

        else :
            npieza = 0
            while npieza < len(self.getPiezas()) :
                pieza = self.getPiezas()[npieza]
                if isinstance(pieza, Rey) :
                    npieza += 1
                    continue
                movimientos = pieza.comprobarTablero(tablero)
                if movimientos != [] :
                    for campo in movimientos :
                        if tablero[campo[0]][campo[1]] != None :
                            self.__switch = True
                            return (pieza.getPos(), campo)
                npieza += 1

            while True :
                pieza = self.getPiezas()[randrange(0, len(self.getPiezas()))]
                movimientos = pieza.comprobarTablero(tablero)
                if movimientos != [] :
                    self.__switch = True
                    return (pieza.getPos(), movimientos[randrange(0, len(movimientos))])