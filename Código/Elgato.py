from tkinter import *

class IniciarJuego:
    def __init__(self, root):
        # Inicializa los atributos del juego
        self.J1 = "O"  # Símbolo del jugador 1
        self.J2 = "X"  # Símbolo del jugador 2
        self.tablero = [""] * 9  # Inicializa el tablero con 9 posiciones vacías
        self.turno_actual = self.J1  # El turno actual comienza con el jugador 1
        self.root = root  # La ventana principal de Tkinter
        self.mensaje = StringVar()  # Variable para mostrar mensajes en la interfaz gráfica
        self.iniciar_juego()  # Llama al método para iniciar el juego




    def iniciar_juego(self):
        # Crea y configura los botones del tablero
        self.botones = []  # Lista para almacenar los botones del tablero
        for i in range(9):
            # Crea un botón para cada casilla del tablero
            boton = Button(self.root, text="", width=10, height=3, command=lambda i=i: self.ciclo(i))
            boton.grid(row=i // 3, column=i % 3)  # Organiza los botones en una cuadrícula 3x3
            self.botones.append(boton)  # Agrega el botón a la lista
        # Crea una etiqueta para mostrar mensajes
        Label(self.root, textvariable=self.mensaje).grid(row=3, column=1)




    def ciclo(self, posicion):
        # Maneja el ciclo del juego cuando se hace clic en un botón
        if self.tablero[posicion] == "":
            # Si la casilla está vacía, coloca el símbolo del jugador actual
            self.tablero[posicion] = self.turno_actual
            self.botones[posicion].config(text=self.turno_actual)  # Actualiza el texto del botón
            if self.quien_gana():
                # Si hay un ganador, muestra el mensaje y reinicia el juego después de 2 segundos
                self.mensaje.set(f"¡{self.turno_actual} ha ganado!")
                self.root.after(2000, self.reiniciar_juego)  # Llama a reiniciar_juego después de 2000 ms
            elif all(self.tablero):
                # Si el tablero está lleno y no hay ganador, muestra el mensaje de empate y reinicia el juego
                self.mensaje.set("¡Empate!")
                self.root.after(2000, self.reiniciar_juego)  # Llama a reiniciar_juego después de 2000 ms
            else:
                # Cambia el turno al siguiente jugador
                self.turno_actual = self.J2 if self.turno_actual == self.J1 else self.J1





    def quien_gana(self):
        # Verifica si hay un ganador
        combinaciones = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
            [0, 4, 8], [2, 4, 6]  # Diagonales
        ]
        for combinacion in combinaciones:
            # Verifica cada combinación ganadora
            if self.tablero[combinacion[0]] == self.tablero[combinacion[1]] == self.tablero[combinacion[2]] != "":
                return True  # Retorna True si hay una combinación ganadora
        return False  # Retorna False si no hay ganador





    def reiniciar_juego(self):
        # Reinicia el juego para una nueva partida
        self.tablero = [""] * 9  # Limpia el tablero
        self.turno_actual = self.J1  # Reinicia el turno al jugador 1
        self.mensaje.set("")  # Limpia el mensaje mostrado
        for boton in self.botones:
            boton.config(text="", state=NORMAL)  # Reinicia el texto y habilita los botones




if __name__ == "__main__":
    # Código para ejecutar la aplicación
    root = Tk()  # Crea la ventana principal de Tkinter
    IniciarJuego(root)  # Crea una instancia de la clase IniciarJuego
    root.mainloop()  # Ejecuta el bucle principal de la interfaz gráfica
