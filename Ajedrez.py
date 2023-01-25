#  Ajedrez
#  v03 Basica de escritorio
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
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont
from platform import system

tablero_gui = [ [ None for j in range (11) ] for i in range(11) ]
filas_gui = ["A", "B", "C", "D", "E", "F", "G", "H"]
tablero = [ [ None for j in range (8) ] for i in range(8) ]
jugador_blancas = []
jugador_negras = []
mmov = 0
ind = False
tuple_coronar = ()

def mostrartablero() :
    """Muestra el tablero actualizado despues de cada ronda"""
    for i in range(8) :
        for j in range(8) :
            if tablero[i][j] == None :
                tablero_gui[i][j].config(text="")
            else :
                tablero_gui[i][j].config(text=tablero[i][j].getIco())

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

def coronar() : 
    """Corona un peon"""
    global tuple_coronar
    eleccion = coronar_opciones.get()
    if eleccion == "Reina" :
        pieza = e.Reina("negro")
    elif eleccion == "Torre" :
        pieza = e.Torre("negro")
    elif eleccion == "Alfil" :
        pieza = e.Alfil("negro")
    elif eleccion == "Caballo" :
        pieza = e.Caballo("negro")
    jugadorn.remove(tablero[tuple_coronar[0]][tuple_coronar[1]])
    tablero[tuple_coronar[0]][tuple_coronar[1]] = pieza
    pieza.setPos((tuple_coronar[0], tuple_coronar[1]))
    jugadorn.append(pieza)
    coronar_opciones.destroy()
    coronar_boton.destroy()
    campo.place(x=20, y=410, width=150)
    boton_mover.place(x=200, y=410)
    cartel.config(text="Ingrese su movimiento (separado por coma): ")
    mover_m()
    mostrartablero()

def cambiarbotones() :
    coronar_opciones.place(x=20, y=410, width=150)
    coronar_boton.place(x=200, y =410)

def coord(coord) :
    """Devuelve (pos)"""
    columnas = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7}
    try :
        f = 8 - int(coord[1]) 
        c = columnas[coord[0].upper()]
        return (f, c)
    except Exception :
        return None
    
def verif_partida() :
    """Devuelve un booleano que comprueba si termino o no la partida, buscando en el vector el rey"""
    if reyn not in jugadorn or reyb not in jugadorb :
        return True
    else :
        return False
    
def mover(pieza, pos) :
    """Toma como argumento una pieza de ajedrez y lo mueve en la fila y columna (tupla) que recibe como argumento"""
    c = puede_mover(pieza)
    if pos in c :
        if hasattr(tablero[pos[0]][pos[1]], "color") :
            if tablero[pos[0]][pos[1]].getColor() == "blanco" :
                jugador_negras.append(tablero[pos[0]][pos[1]])
                jugadorb.remove(tablero[pos[0]][pos[1]])
            else :
                jugador_blancas.append(tablero[pos[0]][pos[1]])
                jugadorn.remove(tablero[pos[0]][pos[1]])
        tablero[pos[0]][pos[1]] = pieza
        tablero[pieza.getPos()[0]][pieza.getPos()[1]] = None
        pieza.setPos((pos[0], pos[1]))
        global ind, tuple_coronar
        ind = True
        if isinstance(pieza, e.Peon) :
            pieza.setM(False)
            if pieza.getPos()[0] == 0 and pieza.getColor() == "negro":
                cambiarbotones()
                tuple_coronar = pos
                cartel.config(text="Elija una pieza: ")
                ind = False
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
        if verif_partida() :
            if reyn not in jugadorn :
                cartel.config(text="Has perdido!")
                boton_mover.config(text="Salir", command=master.destroy)
            elif reyb not in jugadorb :
                cartel.config(text="Has ganado!")
                boton_mover.config(text="Salir", command=master.destroy)
    else :
        ind = False

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

def mov() :
    """Mueve la pieza seleccionada por el jugador"""
    movimiento = campo.get()
    movimiento = movimiento.replace(","," ")
    movimiento = movimiento.split()
    try :
        pieza = coord(movimiento[0])
        pos = coord(movimiento[1])
        mover(tablero[pieza[0]][pieza[1]],pos)
        if ind :
            mover_m()
            mostrartablero()
        else :
            pass
    except Exception :
        pass
    finally :
        jb = []
        for i in (jugador_blancas) :
            jb.append(i.getIco())
        jb = str(jb).replace("'", "")
        jb = jb.replace("[", "")
        jb = jb.replace("]", "")
        jb = jb.replace(",", " ")
        if len(jb) <= 22 :
            piezas_jugblanco.config(text=jb)
        else :
            piezas_jugblanco2.config(text=jb[24:])
        jn = []
        for i in (jugador_negras) :
            jn.append(i.getIco())
        jn = str(jn).replace("'", "")
        jn = jn.replace("[", "")
        jn = jn.replace("]", "")
        jn = jn.replace(",", " ")
        if len(jn) <= 22 :
            piezas_jugnegro.config(text=jn)
        else :
            piezas_jugnegro2.config(text=jn[24:]) 
        campo.delete(0, tk.END)
        mostrartablero()

def acerca_de() :
    messagebox.showinfo(title="Acerca de", message="Este juego va a dedicado a todas las personas que me apoyaron en este hermoso camino de la programacion especialmente a mi novia Romina y a mis papas Marisa y Marcelino.")

def licencia() :
    licencia = tk.Toplevel()
    licencia.config(width=600, height=380)
    licencia.title("Licencia")
    licencia.resizable(0, 0)
    if system() == "Windows" :
        f = tkFont.Font(licencia, size=10)
    else :
        f = tkFont.Font(licencia, size=12)
    l = tk.Label(licencia,
        text="""Ajedrez 1 vs 1
    Copyright (C) 2022  Marcelo David Kacerovsky

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    Contact marcelokace@icloud.com""", font=f)
    l.place(x=10, y=10)
    b = ttk.Button(licencia, text="Aceptar", command=licencia.destroy)
    if system() == "Windows" :
        b.place(x=280, y=370)
    else :
        b.place(x=250, y=340)

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

unjugador = True
dosjugadores = False

master = tk.Tk()
master.title("Ajedrez v0.3")
master.resizable(0, 0)
color = 0
fontstyle = tkFont.Font(size=25)

menu = tk.Menu()
menu_ayuda = tk.Menu(menu, tearoff=0)
menu_salir = tk.Menu(menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)
menu_ayuda.add_command(label="Ver licencia", command=licencia)
menu.add_cascade(label="Ayuda", menu=menu_ayuda)
menu.add_cascade(label="Salir", menu=menu_salir, command=master.destroy)
menu_salir.add_command(label="Salir", command=master.destroy)

master.config(width=620, height=450, menu=menu)
if system() == "Windows" :
    master.iconbitmap('icono.ico')
    master.config(width=650, height=500, menu=menu)

c1 = tk.Label(background="#693610")
c1.place(x=20, y=20, width=20, height=20)
c2 = tk.Label(background="#693610")
c2.place(x=360, y=20, width=20, height=20)
c3 = tk.Label(background="#693610")
c3.place(x=20, y=360, width=20, height=22)
c4 = tk.Label(background="#693610")
c4.place(x=360, y=360, width=20, height=22)

for i in range(1, 9) :
    tablero_gui[0][i - 1] = tk.Label(text=filas_gui[i - 1], background="#693610")
    tablero_gui[0][i - 1].place(x=(40 * i), y=20, width=40)
    tablero_gui[8][i - 1] = tk.Label(text=filas_gui[i - 1],  background="#693610")
    tablero_gui[8][i - 1].place(x=(40 * i), y=360, width=40)
    tablero_gui[i - 1][0] = tk.Label(text=(9 - i),  background="#693610")
    tablero_gui[i - 1][0].place(x=20, y=(40 * i), width=20, height=40)
    tablero_gui[i - 1][10] = tk.Label(text=(9 - i),  background="#693610")
    tablero_gui[i - 1][10].place(x=360, y=(40 * i), width=20, height=40)
for i in range(1, 9) :
    for j in range(1, 9) :
        if (color + i) % 2 == 0 :
            tablero_gui[i - 1][j - 1] = tk.Label(background="#A66023", fg="#000000", font=fontstyle)
            tablero_gui[i - 1][j - 1].place(x=(40 * j), y=(40 * i), width=40, height=40)
            color += 1
        else :
            tablero_gui[i - 1][j - 1] = tk.Label(background="#E8DDAC", fg="#000000", font=fontstyle)
            tablero_gui[i - 1][j - 1].place(x=(40 * j), y=(40 * i), width=40, height=40)
            color += 1

cartel = tk.Label(text="Ingrese su movimiento (separado por coma): ")
cartel.place(x=20, y=385)

campo = tk.Entry()
campo.place(x=20, y=410, width=150)

boton_mover = ttk.Button(text="Mover", command=mov)
boton_mover.place(x=200, y=410)

coronar_opciones = ttk.Combobox(values=["Reina", "Torre", "Alfil", "Caballo"])
coronar_boton = ttk.Button(text="Coronar", command=coronar)

cartel_jugblanco = ttk.Label(text="Piezas capturadas:")
cartel_jugblanco.place(x=400, y=20)
piezas_jugblanco = ttk.Label(font=fontstyle)
piezas_jugblanco.place(x=400, y=40, width=210, height=40)
piezas_jugblanco2 = ttk.Label(font=fontstyle)
piezas_jugblanco2.place(x=400, y=80, width=210, height=40)

cartel_jugnegro = ttk.Label(text="Piezas capturadas:")
cartel_jugnegro.place(x=400, y=280)
piezas_jugnegro = ttk.Label(font=fontstyle)
piezas_jugnegro.place(x=400, y=300, width=210, height=40)
piezas_jugnegro2 = ttk.Label(font=fontstyle)
piezas_jugnegro2.place(x=400, y=340, width=210, height=40)

if system() == "Windows" :
    fontwin = tkFont.Font(size=15)
    piezas_jugblanco = ttk.Label(font=fontwin)
    piezas_jugblanco.place(x=400, y=40, width=250, height=40)
    piezas_jugblanco2 = ttk.Label(font=fontwin)
    piezas_jugblanco2.place(x=400, y=80, width=250, height=40)
    piezas_jugnegro = ttk.Label(font=fontwin)
    piezas_jugnegro.place(x=400, y=300, width=250, height=40)
    piezas_jugnegro2 = ttk.Label(font=fontwin)
    piezas_jugnegro2.place(x=400, y=340, width=250, height=40)

mostrartablero()
master.mainloop()
