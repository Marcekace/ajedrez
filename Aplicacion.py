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


import tkinter as tk
from platform import system
from tkinter import messagebox, ttk
import tkinter.font as tkf
import Entidad as e
from random import randrange


class LabelAjedrez(tk.Label) :

    def __init__(self, master=None, pos=None, cnf={}, **kw) :
        tk.Label.__init__(self, master, cnf={}, **kw)
        self.coord = pos


class App(tk.Tk) :


    def __init__(self) :
        tk.Tk.__init__(self)

        self.__status = False
        self.__jugador = e.Jugador("negro")
        self.__maquina = e.Maquina("blanco")
        self.__tablero = [ [None for j in range(8)] for i in range(8) ]
        for i in range(2) :
            for j in range(8) :
                self.__tablero[i][j] = self.__maquina.getPiezas()[j + (8 * i)]
                self.__tablero[7 - i][j] = self.__jugador.getPiezas()[j + (8 * i)]

        self.title("Ajedrez")
        self.resizable(0, 0)
        self.__menu = tk.Menu()
        self.__menu_ayuda = tk.Menu(self.__menu, tearoff=0)
        self.__acerca_de = lambda : messagebox.showinfo(title="Acerca de", message="Este juego va a dedicado a todas las personas que me apoyaron en este hermoso camino de la programacion especialmente a mi novia Romina y a mis papas Marisa y Marcelino.\n\nCopyright 2022 Marcelo Kacerovsky\n<marcelokacerovsky@marcelos-MacBook-Air.local>")
        self.__menu_ayuda.add_cascade(label="Acerca de", command=self.__acerca_de)
        self.__menu_ayuda.add_cascade(label="Salir", command=self.destroy)
        self.__menu.add_cascade(label="Ayuda", menu=self.__menu_ayuda)

        if system() == "Windows" :
            self.config(width=650, height=500, menu=self.__menu)
            self.__font = tkf.Font(size=22)
        else :
            self.config(width=620, height=450, menu=self.__menu)
            self.__font = tkf.Font(size=25)

        self.__f1 = tk.Frame(width=360, height=360, background="#693610")
        self.__f1.place(x=20, y=20)
        self.__f2 = tk.Frame(master=self.__f1, width=320, height=320)
        self.__f2.place(x=20, y=20)
        self.__filas = "ABCDEFGH"

        self.__borde1 = [ tk.Label(master=self.__f1, text=self.__filas[i], background="#693610") for i in range(8) ]
        self.__borde2 = [ tk.Label(master=self.__f1, text=self.__filas[i], background="#693610") for i in range(8) ]
        self.__borde3 = [ tk.Label(master=self.__f1, text=(i + 1), background="#693610") for i in range(8) ]
        self.__borde4 = [ tk.Label(master=self.__f1, text=(i + 1), background="#693610") for i in range(8) ]

        for i in range(8) :
            self.__borde1[i].place(x=(20 + (40 * i)) ,y=0, width=40, height=20)
            self.__borde2[i].place(x=(20 + (40 * i)) ,y=340, width=40, height=20)
            self.__borde3[i].place(x=0, y=(300 - (40 * i)), width=20, height=40)
            self.__borde4[i].place(x=340, y=(300 - (40 * i)), width=20, height=40)

        self.__celdas = [[ LabelAjedrez(master=self.__f2, pos=(i, j), background="#E8DDAC", fg="#000000", font=self.__font) if (i + j) % 2 == 0 
        else LabelAjedrez(master=self.__f2, pos=(i, j), background="#A66023", fg="#000000", font=self.__font) for j in range(8) ] for i in range(8)]

        for i in range(8) :
            for j in range(8) :
                self.__celdas[i][j].place(x=(40 * j), y=(40 * i), width=40, height=40)
                self.__celdas[i][j].bind("<Button-1>", self.mover_pieza)

        self.__capturadas_blanco = tk.Frame(width=210, height=80)
        self.__capturadas_blanco.place(x=400, y=40)
        self.__capturadas_negro = tk.Frame(width=210, height=80)
        self.__capturadas_negro.place(x=400, y=300)
        self.after(500, self.actualizar_tablero)


    def verificar_partida(self, jugador, maquina) :
        if jugador.getRey() not in jugador.getPiezas() :
            for i in range(8) :
                for j in range(8) :
                    self.__celdas[i][j].unbind("<Button-1>")
            messagebox.showinfo(message="Has perdido!")
        if maquina.getRey() not in maquina.getPiezas() :
            for i in range(8) :
                for j in range(8) :
                    self.__celdas[i][j].unbind("<Button-1>")
            messagebox.showinfo(message="Has ganado!")


    def coronar(self) :
        if self.__coronar_opciones.get() == "♛" :
            pieza = e.Reina("negro")
        elif self.__coronar_opciones.get() == "♜" :
            pieza = e.Torre("negro")
        elif self.__coronar_opciones.get() == "♝" :
            pieza = e.Alfil("negro")
        else :
            pieza = e.Caballo("negro")
        self.__jugador.getPiezas().remove(self.__tablero[self.__jugador.getEleccion()[0]][self.__jugador.getEleccion()[1]])
        self.__jugador.getPiezas().append(pieza)
        pieza.setPos((self.__jugador.getEleccion()[0], self.__jugador.getEleccion()[1]))
        self.__tablero[self.__jugador.getEleccion()[0]][self.__jugador.getEleccion()[1]] = pieza
        self.after(200, self.actualizar_tablero)
        for i in range(8) :
            for j in range(8) :
                self.__celdas[i][j].bind("<Button-1>", self.mover_pieza)
        self.__coronar_boton.destroy()
        self.__coronar_opciones.destroy()


    def mover_pieza(self, event=None) :
        if event != None :
            if event.widget['text'] not in ("♙", "♖", "♗", "♘", "♔", "♕", "") and self.__status != True :
                # Selecciona una pieza
                self.__jugador.setEleccion((event.widget.coord, event.widget['background']))
                event.widget.config(background="#76D665")
                self.__status = True
            else :
                if self.__status :
                    pos = event.widget.coord 
                    movimientos = self.__tablero[self.__jugador.getEleccion()[0][0]][self.__jugador.getEleccion()[0][1]].comprobarTablero(self.__tablero)
                    if pos in movimientos :
                        # Mueve la pieza si el movimiento es valido
                        self.__celdas[self.__jugador.getEleccion()[0][0]][self.__jugador.getEleccion()[0][1]].config(background=self.__jugador.getEleccion()[1])
                        if hasattr(self.__tablero[pos[0]][pos[1]], "color") :
                            if self.__tablero[pos[0]][pos[1]].getColor() == "blanco" :
                                self.__jugador.getPiezasCapturadas().append(self.__tablero[pos[0]][pos[1]])
                                self.__maquina.getPiezas().remove(self.__tablero[pos[0]][pos[1]])
                                label = tk.Label(master=self.__capturadas_negro, text=self.__jugador.getPiezasCapturadas()[-1], font=self.__font)
                                if len(self.__jugador.getPiezasCapturadas()) <= 8 :
                                    label.grid(row=1, column=len(self.__jugador.getPiezasCapturadas()))
                                else :
                                    label.grid(row=2, column=len(self.__jugador.getPiezasCapturadas()) - 8)
                        self.__tablero[pos[0]][pos[1]] = self.__tablero[self.__jugador.getEleccion()[0][0]][self.__jugador.getEleccion()[0][1]]
                        self.__tablero[pos[0]][pos[1]].setPos(pos)
                        self.__tablero[self.__jugador.getEleccion()[0][0]][self.__jugador.getEleccion()[0][1]] = None

                        self.after(500, self.actualizar_tablero)
                        if isinstance(self.__tablero[pos[0]][pos[1]], e.Peon) :
                            self.__tablero[pos[0]][pos[1]].setM(False)
                            if self.__tablero[pos[0]][pos[1]].getPos()[0] == 0 :
                                self.__coronar_opciones = ttk.Combobox(values=("♛", "♜", "♝", "♞"), font=self.__font)
                                self.__coronar_opciones.place(x=100, y=390, width=50, height=40)
                                self.__coronar_boton = ttk.Button(text="Coronar", command=self.coronar)
                                self.__coronar_boton.place(x=200, y=390, height=40)
                                for i in range(8) :
                                    for j in range(8) :
                                        self.__celdas[i][j].unbind("<Button-1>")
                                self.__jugador.setEleccion(pos)
                                self.__status = False
                        self.after(100, self.verificar_partida(self.__jugador, self.__maquina))

                        if self.__status :
                            self.mover_maquina()
                    else :
                        # Sentencias para deseleccionar
                        self.__celdas[self.__jugador.getEleccion()[0][0]][self.__jugador.getEleccion()[0][1]].config(background=self.__jugador.getEleccion()[1])
                    self.__status = False
            self.after(500, self.actualizar_tablero)


    def mover_maquina(self) :
        # Movimiento de la maquina
        jugada = self.__maquina.movimiento(self.__jugador, self.__tablero)
        if hasattr(self.__tablero[jugada[1][0]][jugada[1][1]], "color") :
            if self.__tablero[jugada[1][0]][jugada[1][1]].getColor() == "negro" :
                self.__maquina.getPiezasCapturadas().append(self.__tablero[jugada[1][0]][jugada[1][1]])
                self.__jugador.getPiezas().remove(self.__tablero[jugada[1][0]][jugada[1][1]])
                label = tk.Label(master=self.__capturadas_blanco, text=self.__maquina.getPiezasCapturadas()[-1], font=self.__font)
                if len(self.__maquina.getPiezasCapturadas()) <= 8 :
                    label.grid(row=1, column=len(self.__maquina.getPiezasCapturadas()))
                else :
                    label.grid(row=2, column=len(self.__maquina.getPiezasCapturadas()) - 8)
        self.__tablero[jugada[1][0]][jugada[1][1]] = self.__tablero[jugada[0][0]][jugada[0][1]]
        self.__tablero[jugada[1][0]][jugada[1][1]].setPos((jugada[1][0], jugada[1][1]))
        self.__tablero[jugada[0][0]][jugada[0][1]] = None

        if isinstance(self.__tablero[jugada[1][0]][jugada[1][1]], e.Peon) :
            self.__tablero[jugada[1][0]][jugada[1][1]].setM(False)
            if self.__tablero[jugada[1][0]][jugada[1][1]].getPos()[0] == 7 :
                piezas = [e.Torre("blanco"), e.Alfil("blanco"), e.Caballo("blanco"), e.Reina("blanco")]
                pieza = piezas[randrange(0, len(piezas))]
                self.__maquina.getPiezas().remove(self.__tablero[jugada[1][0]][jugada[1][1]])
                self.__maquina.getPiezas().append(pieza)
                self.__tablero[jugada[1][0]][jugada[1][1]] = pieza
                pieza.setPos((jugada[1][0], jugada[1][1]))

        self.after(100, self.verificar_partida(self.__jugador, self.__maquina))
        self.after(500, self.actualizar_tablero)


    def actualizar_tablero(self, event=None) :
        for i in range(8) :
            for j in range(8) :
                if self.__tablero[i][j] == None :
                    self.__celdas[i][j].config(text="")
                else :
                    self.__celdas[i][j].config(text=self.__tablero[i][j])


    def start(self) :
        self.mainloop()