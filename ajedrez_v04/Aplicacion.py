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
        self.__tablero = [ [None for j in range(8)] for i in range(4) ]
        for i in range(2) :
            self.__tablero.insert(i, self.__maquina.getPiezas()[i])
            self.__tablero.append(self.__jugador.getPiezas()[i - 1])

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

        self.__cartel_blanco = tk.Label(text="Piezas capturadas:").place(x=400, y=20) 
        self.__cartel_negro =  tk.Label(text="Piezas capturadas:").place(x=400, y=280)
        self.__capturadas_blanco = tk.Frame(background="#FFFFFF", width=210, height=80).place(x=400, y=40)
        self.__capturadas_negro = tk.Frame(background="#FFFFFF", width=210, height=80).place(x=400, y=300)
        self.after(500, self.actualizar_tablero)


    def verificar_partida(self) :
        pass


    def coronar(self) :
        pass


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
                        self.__tablero[pos[0]][pos[1]] = self.__tablero[self.__jugador.getEleccion()[0][0]][self.__jugador.getEleccion()[0][1]]
                        
                        if isinstance(self.__tablero[pos[0]][pos[1]], e.Peon) :
                            self.__tablero[pos[0]][pos[1]].setM(False)
                        
                        self.__tablero[pos[0]][pos[1]].setPos(pos)
                        self.__tablero[self.__jugador.getEleccion()[0][0]][self.__jugador.getEleccion()[0][1]] = None
                    else :
                        # Sentencias para deseleccionar
                        self.__celdas[self.__jugador.getEleccion()[0][0]][self.__jugador.getEleccion()[0][1]].config(background=self.__jugador.getEleccion()[1])
                    self.__status = False
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