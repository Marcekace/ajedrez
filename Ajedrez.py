#  Ajedrez
#  v02 de consola
#  Copyright 2022 marcelo kacerovsky <marcelokacerovsky@marcelos-MacBook-Air.local>
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

import Entidad as e
from random import randrange
from time import sleep
import os

tablero = [ [ None for j in range (8) ] for i in range(8) ]
jugador_blancas = []
jugador_negras = []
mmov = 0

def mostrartablero() :
    """Muestra el tablero actualizado despues de cada ronda"""
    print(" __________________________________________________________________________")
    print("|   A   ||   B   ||   C   ||   D   ||   E   ||   F   ||   G   ||   H   |   |")
    for i in range(8) :
        print("|-------++-------++-------++-------++-------++-------++-------++-------+---|")
        for j in range(8) :
            if tablero[i][j] == None :
                print("| ", "    ", "|", end="")
            else :
                print("|  ", tablero[i][j].getIco(), "  |", end="")
        print(" " + str(8-i) + " |", end="")
        print("")
    print("+-------++-------++-------++-------++-------++-------++-------++-------+---+")
   
def puede_mover(pieza) :
    """Toma como argumento una pieza de ajedrez y comprueba sus posibles posiciones"""
    cl = []
    x, y = pieza.getPos()[0], pieza.getPos()[1]
    t = (x, y)
    if isinstance(pieza, e.Peon) : 
        if pieza.getColor() == "blanco" :
            for i in range(-1,2,2) :
                if t[1] + i >= 0 and t[1] + i <= 7 :
                    if tablero[t[0] + 1][t[1] + i] != None :
                        if tablero[t[0] + 1][t[1] + i].getColor() == "negro" :
                            cl.append(((t[0] + 1), (t[1] + i)))
            if pieza.getM() and tablero[t[0] + 2][t[1]] == None :
                cl.append(((t[0] + 2), (t[1])))
            if  tablero[(t[0] + 1)][t[1]] == None :
                cl.append(((t[0] + 1), (t[1])))
        else :
            for i in range(-1,2,2) :
                if t[1] + i >= 0 and t[1] + i <= 7 :
                    if tablero[t[0] - 1][t[1] + i] != None :
                        if tablero[t[0] - 1][t[1] + i].getColor() == "blanco" :
                            cl.append(((t[0] - 1), (t[1] + i)))
            if pieza.getM() and tablero[t[0] - 2][t[1]] == None :
                cl.append(((t[0] - 2), (t[1])))
            if  tablero[(t[0] - 1)][t[1]] == None :
                cl.append(((t[0] - 1), (t[1])))
    elif isinstance(pieza, e.Torre) :
        # Superior
        for i in range(x - 1, -1, -1) :
            if tablero[i][t[1]] != None :
                if tablero[i][t[1]].getColor() != pieza.getColor() :
                    cl.append(((i), (t[1])))
                    break
                else :
                    break
            else :
                cl.append(((i), (t[1])))
        # Inferior
        for i in range(x + 1, 8) :
            if tablero[i][t[1]] != None :
                if tablero[i][t[1]].getColor() != pieza.getColor() :
                    cl.append(((i), (t[1])))
                    break
                else :
                    break
            else :
                cl.append(((i), (t[1])))
        # Izquierdo
        for i in range(y - 1, -1, -1) :
            if tablero[t[0]][i] != None :
                if tablero[t[0]][i].getColor() != pieza.getColor() :
                    cl.append(((t[0]), (i)))
                    break
                else :
                    break
            else :
                cl.append(((t[0]), (i)))
        # Derecha
        for i in range(y + 1, 8) :
            if tablero[t[0]][i] != None :
                if tablero[t[0]][i].getColor() != pieza.getColor() :
                    cl.append(((t[0]), (i)))
                    break
                else :
                    break
            else :
                cl.append(((t[0]), (i)))
    elif isinstance(pieza, e.Alfil) :
        d = 1
        # diagonal superior izquierda
        for i in range(x - 1, -1, -1) :
            if (t[1] - d) >= 0 :
                if tablero[i][t[1] - d] != None :
                    if tablero[i][t[1] - d].getColor() != pieza.getColor() :
                        cl.append(((i), (t[1] - d)))
                        break
                    else :
                        break
                else :
                    cl.append(((i), (t[1] - d)))
                    d += 1
            else :
                break
        # diagonal superior derecha
        d = 1
        for i in range(x - 1, -1, -1) :
            if (t[1] + d) <= 7 :
                if tablero[i][t[1] + d] != None :
                    if tablero[i][t[1] + d].getColor() != pieza.getColor() :
                        cl.append(((i), (t[1] + d)))
                        break
                    else :
                        break
                else :
                    cl.append(((i), (t[1] + d)))
                    d += 1
            else :
                break
        # diagonal inferior izquierda
        d = 1
        for i in range(x + 1, 8) :
            if (t[1] - d) >= 0 :
                if tablero[i][t[1] - d] != None :
                    if tablero[i][t[1] - d].getColor() != pieza.getColor() :
                        cl.append(((i), (t[1] - d)))
                        break
                    else :
                        break
                else :
                    cl.append(((i), (t[1] - d)))
                    d += 1
            else :
                break
        # diagonal inferior derecha
        d = 1
        for i in range(x + 1, 8) :
            if (t[1] + d) <= 7 :
                if tablero[i][t[1] + d] != None :
                    if tablero[i][t[1] + d].getColor() != pieza.getColor() :
                        cl.append(((i), (t[1] + d)))
                        break
                    else :
                        break
                else :
                    cl.append(((i), (t[1] + d)))
                    d += 1
            else :
                break
    elif isinstance(pieza, e.Caballo) :
        for i in range(-1, 2, 2) :
        # Inferior
            if (t[0] + 2) <= 7 and (((t[1] + i) <= 7) and ((t[1] + i) >= 0)) :
                if tablero[t[0] + 2][t[1] + i] != None :
                    if tablero[t[0] + 2][t[1] + i].getColor() != pieza.getColor() :
                        cl.append(((t[0] + 2), (t[1] + i)))
                else :
                    cl.append(((t[0] + 2), (t[1] + i)))
        # Superior
            if (t[0] - 2) >= 0 and (((t[1] + i) <= 7) and ((t[1] + i) >= 0)) :
                if tablero[t[0] - 2][t[1] + i] != None :
                    if tablero[t[0] - 2][t[1] + i].getColor() != pieza.getColor() :
                        cl.append(((t[0] - 2), (t[1] + i)))
                else :
                    cl.append(((t[0] - 2), (t[1] + i)))
        # Derecha
            if (t[1] + 2) <= 7 and (((t[0] + i) <= 7) and ((t[0] + i) >= 0)) :
                if tablero[t[0] + i][t[1] + 2] != None :
                    if tablero[t[0] + i][t[1] + 2].getColor() != pieza.getColor() :
                        cl.append(((t[0] + i), (t[1] + 2)))
                else :
                    cl.append(((t[0] + i), (t[1] + 2)))
        # Izquierda
            if (t[1] - 2) >= 0 and (((t[0] + i) <= 7) and ((t[0] + i) >= 0)) :
                if tablero[t[0] + i][t[1] - 2] != None :
                    if tablero[t[0] + i][t[1] - 2].getColor() != pieza.getColor() :
                        cl.append(((t[0] + i), (t[1] - 2)))
                else :
                    cl.append(((t[0] + i), (t[1] - 2)))
    elif isinstance(pieza, e.Rey) :
        cl = []
        x, y = pieza.getPos()[0], pieza.getPos()[1]
        t = (x, y)
        for i in range(-1, 2) :
            for j in range(-1, 2) :
                if (t[0] + i) >= 0 and (t[0] + i) <= 7 and (t[1] + j) >= 0 and (t[1] + j) <= 7 :
                    if tablero[t[0] + i][t[1] + j] != None :
                        if tablero[t[0] + i][t[1] + j].getColor() != pieza.getColor() :
                            cl.append(((t[0] + i), (t[1] + j)))
                    else :
                        cl.append(((t[0] + i), (t[1] + j)))
    elif isinstance(pieza, e.Reina) :
    # Lados
        # Superior
        for i in range(x - 1, -1, -1) :
            if tablero[i][t[1]] != None :
                if tablero[i][t[1]].getColor() != pieza.getColor() :
                    cl.append(((i), (t[1])))
                    break
                else :
                    break
            else :
                cl.append(((i), (t[1])))
        # Inferior
        for i in range(x + 1, 8) :
            if tablero[i][t[1]] != None :
                if tablero[i][t[1]].getColor() != pieza.getColor() :
                    cl.append(((i), (t[1])))
                    break
                else :
                    break
            else :
                cl.append(((i), (t[1])))
        # Izquierda
        for i in range(y - 1, -1, -1) :
            if tablero[t[0]][i] != None :
                if tablero[t[0]][i].getColor() != pieza.getColor() :
                    cl.append(((t[0]), (i)))
                    break
                else :
                    break
            else :
                cl.append(((t[0]), (i)))
        # Derecha
        for i in range(y + 1, 8) :
            if tablero[t[0]][i] != None :
                if tablero[t[0]][i].getColor() != pieza.getColor() :
                    cl.append(((t[0]), (i)))
                    break
                else :
                    break
            else :
                cl.append(((t[0]), (i)))
    # Diagonales
        # diagonal superior izquierda
        d = 1
        for i in range(x - 1, -1, -1) :
            if (t[1] - d) >= 0 :
                if tablero[i][t[1] - d] != None :
                    if tablero[i][t[1] - d].getColor() != pieza.getColor() :
                        cl.append(((i), (t[1] - d)))
                        break
                    else :
                        break
                else :
                    cl.append(((i), (t[1] - d)))
                    d += 1
            else :
                break
        # diagonal superior derecha
        d = 1
        for i in range(x - 1, -1, -1) :
            if (t[1] + d) <= 7 :
                if tablero[i][t[1] + d] != None :
                    if tablero[i][t[1] + d].getColor() != pieza.getColor() :
                        cl.append(((i), (t[1] + d)))
                        break
                    else :
                        break
                else :
                    cl.append(((i), (t[1] + d)))
                    d += 1
            else :
                break
        # diagonal inferior izquierda
        d = 1
        for i in range(x + 1, 8) :
            if (t[1] - d) >= 0 :
                if tablero[i][t[1] - d] != None :
                    if tablero[i][t[1] - d].getColor() != pieza.getColor() :
                        cl.append(((i), (t[1] - d)))
                        break
                    else :
                        break
                else :
                    cl.append(((i), (t[1] - d)))
                    d += 1
            else :
                break
        # diagonal inferior derecha
        d = 1
        for i in range(x + 1, 8) :
            if (t[1] + d) <= 7 :
                if tablero[i][t[1] + d] != None :
                    if tablero[i][t[1] + d].getColor() != pieza.getColor() :
                        cl.append(((i), (t[1] + d)))
                        break
                    else :
                        break
                else :
                    cl.append(((i), (t[1] + d)))
                    d += 1
            else :
                break
    return cl

def coronar(color) : 
    """Corona un peon"""
    while True :
        p = input("Ingrese la pieza que va a elejir ")
        if p.lower() == "torre" :
            return e.Torre(color)
        elif p.lower() == "alfil" :
            return e.Alfil(color)
        elif p.lower() == "reina" :
            return e.Reina(color)
        elif p.lower() == "caballo" :
            return e.Caballo(color)
        else : 
            print("Pieza invalida.")

def coord(coord) :
    """Devuelve (pos)"""
    columnas = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7}
    try :
        f = 8 - int(coord[1]) 
        c = columnas[coord[0].upper()]
        return (f, c)
    except Exception :
        return None
    
def mover(pieza, pos) :
    """Toma como argumento una pieza de ajedrez y lo mueve en la fila y columna (tupla) que recibe como argumento"""
    c = puede_mover(pieza)
    if hasattr(tablero[pos[0]][pos[1]], "color") :
        if tablero[pos[0]][pos[1]].getColor() == "blanco" :
            jugador_negras.append(tablero[pos[0]][pos[1]])
            jugadorb.remove(tablero[pos[0]][pos[1]])
        else :
            jugador_blancas.append(tablero[pos[0]][pos[1]])
            jugadorn.remove(tablero[pos[0]][pos[1]])
    if pos in c :
        tablero[pos[0]][pos[1]] = pieza
        tablero[pieza.getPos()[0]][pieza.getPos()[1]] = None
        pieza.setPos((pos[0], pos[1]))
        if isinstance(pieza, e.Peon) :
            pieza.setM(False)
            if pieza.getPos()[0] == 0 and pieza.getColor() == "negro":
                jugadorn.remove(pieza)
                np = coronar("negro")
                tablero[pos[0]][pos[1]] = np
                np.setPos((pos[0], pos[1]))
                jugadorn.append(np)
            elif pieza.getPos()[0] == 7 and pieza.getColor() == "blanco" and dosjugadores :
                jugadorb.remove(pieza)
                np = coronar("blanco")
                tablero[pos[0]][pos[1]] = np
                np.setPos((pos[0], pos[1]))
                jugadorb.append(np)
            elif pieza.getPos()[0] == 7 and pieza.getColor() == "blanco" and unjugador :
                jugadorb.remove(pieza)
                np1, np2, np3, np4 = e.Torre("blanco"), e.Alfil("blanco"), e.Caballo("blanco"), e.Reina("blanco")
                l = [np1, np2, np3, np4]
                m = l[randrange(0, len(l))]
                tablero[pos[0]][pos[1]] = m
                m.setPos((pos[0], pos[1]))
                jugadorb.append(m)
    else :
        print("Movimiento invalido.")
    os.system("clear")

def mover_m() :
    """Movimiento de la maquina"""
    global mmov
    if mmov % 2 == 0 :
        while True :
            p = jugadorb[randrange(0, len(jugadorb))]
            c = puede_mover(p)
            if c != [] :
                mov = randrange(0, len(c))
                mover(p, c[mov])
                mmov += 1
                break
    else :
        contp = 0
        t = True
        while contp < len(jugadorb) :
            p = jugadorb[contp]
            c = puede_mover(p)
            if c != [] :
                for campo in c :
                    if tablero[campo[0]][campo[1]] != None :
                        mover(p, campo)
                        contp = len(jugadorb)
                        t = False
                        mmov += 1
                        break
            contp += 1
        if t :
            while True :
                p = jugadorb[randrange(0, len(jugadorb))]
                c = puede_mover(p)
                if c != [] :
                    mov = randrange(0, len(c))
                    mover(p, c[mov])
                    mmov += 1
                    break
    os.system("clear")

def verif_partida() :
    """Devuelve un booleano que comprueba si termino o no la partida, buscando en el vector el rey"""
    if reyn not in jugadorn :
        if dosjugadores :
            print("Jugad@r B ¡ha ganado!")
            return True
        else :
            print("Has perdido!")
            return True
    elif reyb not in jugadorb :
        if dosjugadores :
            print("Jugad@r N ¡ha ganado!")
            return True
        else :
            print("Has ganado!")
            return True
    else :
        return False

tb1, tb2, cb1, cb2, alfb1, alfb2, reinab, reyb = e.Torre("blanco"), e.Torre("blanco"), e.Caballo("blanco"), e.Caballo("blanco"), e.Alfil("blanco"), e.Alfil("blanco"), e.Reina("blanco"), e.Rey("blanco")
pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8 = e.Peon("blanco"), e.Peon("blanco"), e.Peon("blanco"), e.Peon("blanco"), e.Peon("blanco"), e.Peon("blanco"), e.Peon("blanco"), e.Peon("blanco")

jugadorb = [tb1, cb1, alfb1, reinab, reyb, alfb2, cb2, tb2, pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8]

tn1, tn2, cn1, cn2, alfn1, alfn2, reinan, reyn = e.Torre("negro"), e.Torre("negro"), e.Caballo("negro"), e.Caballo("negro"), e.Alfil("negro"), e.Alfil("negro"), e.Reina("negro"), e.Rey("negro")
pn1, pn2, pn3, pn4, pn5, pn6, pn7, pn8 = e.Peon("negro"), e.Peon("negro"), e.Peon("negro"), e.Peon("negro"), e.Peon("negro"), e.Peon("negro"), e.Peon("negro"), e.Peon("negro")

jugadorn = [tn1, cn1, alfn1, reinan, reyn, alfn2, cn2, tn2, pn1, pn2, pn3, pn4, pn5, pn6, pn7, pn8]

for i in range(8) :
    tablero[0][i] = jugadorb[i]
    tablero[1][i] = jugadorb[i+8]
    tablero[6][i] = jugadorn[i+8]
    tablero[7][i] = jugadorn[i]





while True :
    print("###################################################")
    print("#                                                 #")
    print("#        Bienvenid@ elija un modo de juego        #")
    print("#        1 - Jugar sol@                           #")
    print("#        2 - Dos jugador@s                        #")
    print("#        3 - Salir                                #")
    print("#                                                 #")
    print("###################################################")     
    try :
        o = int(input(">>>  "))
        if o == 1 :
            os.system("clear")
            #   Un Jugador
            unjugador = True
            while True :
                mostrartablero()
                print()
                if verif_partida() :
                    break
                try :
                    while True :
                        m = input("Ingrese su movimiento separado por coma: ")
                        m = m.replace(",", " ")
                        m = m.split()
                        pos = coord(m[0])
                        if isinstance(tablero[pos[0]][pos[1]], e.Pieza) :
                            if tablero[pos[0]][pos[1]].getColor() == "negro" :
                                break
                            else :
                                print("Debe elejir una pieza (Negra)\n\n")
                        else :
                            print("Debe elejir una pieza valida\n\n")
                    mover(tablero[pos[0]][pos[1]], coord(m[1]))
                    mostrartablero()
                    sleep(2)
                    if verif_partida() :
                        break
                    mover_m()
                    sleep(2)
                except Exception :
                    os.system("clear")
                    print("Debe elegir un movimiento valido\n\n")
                    sleep(2)
                    os.system("clear")
        if o == 2 :
            os.system("clear")
            #   Dos jugador@s
            dosjugadores = True
            mostrartablero()
            print()
            while True :
                if verif_partida() :
                    break
                while True :
                    try :
                        m = input("Jugad@r N ingrese su movimiento separado por coma: ")
                        m = m.replace(",", " ")
                        m = m.split()
                        pos = coord(m[0])
                        if isinstance(tablero[pos[0]][pos[1]], e.Pieza) :
                            if tablero[pos[0]][pos[1]].getColor() == "negro" :
                                break
                            else :
                                print("Debe elejir una pieza (Negra)\n\n")
                        else :
                            print("Debe elejir una pieza valida\n\n")
                    except Exception :
                        print("Debe elegir un movimiento valido\n\n")
                        sleep(2)
                        os.system("clear")
                        mostrartablero()
                mover(tablero[pos[0]][pos[1]], coord(m[1]))
                mostrartablero()
                if verif_partida() :
                    break
                while True :
                    try :
                        m = input("Jugad@r B ingrese su movimiento separado por coma: ")
                        m = m.replace(",", " ")
                        m = m.split()
                        pos = coord(m[0])
                        if isinstance(tablero[pos[0]][pos[1]], e.Pieza) :
                            if tablero[pos[0]][pos[1]].getColor() == "blanco" :
                                break
                            else :
                                print("Debe elejir una pieza (Blanca)\n\n")
                        else :
                            print("Debe elejir una pieza valida\n\n")
                    except Exception :
                        print("Debe elegir un movimiento valido\n\n")
                        sleep(2)
                        os.system("clear")
                        mostrartablero()
                mover(tablero[pos[0]][pos[1]], coord(m[1]))
                mostrartablero()
                sleep(2)
        if o == 3 :
            print("Gracias por jugar.")
            break
    except ValueError :
        print("Debe elegir una opcion valida\n\n")
        sleep(2)
        os.system("clear")