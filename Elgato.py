from tkinter import *  # Importa todas las clases y funciones de tkinter
from tkinter import ttk  # Importa el módulo ttk para usar widgets mejorados de tkinter

### **Clase `IniciarJuego`**
class IniciarJuego:
    def __init__(self, root):
        # Jugador 1 utiliza el símbolo "O"
        self.J1 = "O"  
        # Jugador 2 utiliza el símbolo "X"
        self.J2 = "X"  
        # Tablero de 9 posiciones, inicialmente vacío representado como una lista de 9 cadenas vacías
        self.tablero = [""] * 9  
        # El primer turno corresponde al jugador 1
        self.turno_actual = self.J1  
        # Guarda la referencia a la ventana raíz de la interfaz gráfica
        self.root = root  
        # Instancia de la clase Ganador, usada para verificar el estado del juego
        self.ganador = Ganador()  
        # StringVar para manejar el texto del mensaje en la interfaz gráfica
        self.mensaje = StringVar()  
        
        # Inicia el juego llamando al método iniciar_juego
        self.iniciar_juego()

    # **Método para iniciar el juego**
    def iniciar_juego(self):
        # Crea un marco principal (frame) con padding, dentro de la ventana principal
        self.mainframe = ttk.Frame(self.root, padding="12 12 12 12")
        # Ubica el frame en la ventana principal en la posición (0,0)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # Configura las columnas y filas de la ventana raíz para expandirse cuando la ventana cambia de tamaño
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Crear los botones que representarán las casillas del tablero
        self.botones = []
        for i in range(9):
            # Crea un botón vacío y asigna una función de comando para cada botón al hacer clic
            boton = ttk.Button(self.mainframe, text="", command=lambda i=i: self.ciclo(i))
            # Ubica el botón en una cuadrícula según su índice
            boton.grid(column=(i % 3) + 1, row=(i // 3) + 1, sticky=S)
            # Añade el botón a la lista de botones
            self.botones.append(boton)

        # Crea una etiqueta para mostrar mensajes durante el juego y la ubica en la cuadrícula
        ttk.Label(self.mainframe, textvariable=self.mensaje).grid(column=4, row=3, sticky=E)
        # Aplica un margen de 5px a todos los widgets dentro del frame
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    # **Método para controlar el ciclo de juego**
    def ciclo(self, posicion):
        # Verifica si la casilla seleccionada está vacía
        if self.tablero[posicion] == "":  
            # Asigna el símbolo del jugador actual a la casilla seleccionada
            self.tablero[posicion] = self.turno_actual
            # Actualiza el texto del botón correspondiente para mostrar el símbolo
            self.botones[posicion].config(text=self.turno_actual)
            # Desactiva el botón para que no se pueda volver a seleccionar
            self.botones[posicion].state(["disabled"])  
            # Guarda el movimiento en el tablero usando el método guardar de la clase Guardar
            Guardar().guardar(posicion, self.turno_actual, self.tablero)

            # Verifica si el jugador actual ha ganado
            if self.ganador.quien_gana(self.tablero):
                # Muestra un mensaje indicando quién ha ganado
                self.mensaje.set(f"¡{self.turno_actual} ha ganado!")
                # Desactiva todos los botones del tablero
                self.deshabilitar_botones()
                # Reinicia el juego después de 2 segundos
                self.root.after(2000, self.reiniciar_juego)
            # Verifica si hay un empate
            elif self.ganador.empate(self.tablero):
                # Muestra un mensaje indicando que es un empate
                self.mensaje.set("¡Empate!")
                # Desactiva todos los botones del tablero
                self.deshabilitar_botones()
                # Reinicia el juego después de 2 segundos
                self.root.after(2000, self.reiniciar_juego)
            else:
                # Cambia el turno al otro jugador
                self.turno_actual = self.J2 if self.turno_actual == self.J1 else self.J1

    # **Método para deshabilitar botones**
    def deshabilitar_botones(self):
        # Recorre todos los botones y los desactiva
        for boton in self.botones:
            boton.state(["disabled"])

    # **Método para reiniciar el juego**
    def reiniciar_juego(self):
        # Reinicia el tablero, llenándolo de nuevo con cadenas vacías
        self.tablero = [""] * 9
        # Reinicia el turno para que empiece el jugador 1
        self.turno_actual = self.J1
        # Limpia el mensaje de la interfaz gráfica
        self.mensaje.set("")

        # Restablece todos los botones, vaciando su texto y habilitándolos nuevamente
        for boton in self.botones:
            boton.config(text="")
            boton.state(["!disabled"])

### **Clase `Ganador`**
class Ganador:
    # **Método para verificar si hay un ganador**
    def quien_gana(self, tablero):
        # Lista de combinaciones ganadoras posibles (filas, columnas, diagonales)
        combinaciones_ganadoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
            [0, 4, 8], [2, 4, 6]  # Diagonales
        ]
        # Verifica cada combinación ganadora
        for combinacion in combinaciones_ganadoras:
            # Si todas las posiciones en una combinación tienen el mismo símbolo y no están vacías, retorna True (hay un ganador)
            if tablero[combinacion[0]] == tablero[combinacion[1]] == tablero[combinacion[2]] != "":
                return True
        # Si no hay una combinación ganadora, retorna False
        return False

    # **Método para verificar si hay un empate**
    def empate(self, tablero):
        # Verifica si todas las casillas del tablero están llenas, en cuyo caso es un empate
        return all(casilla != "" for casilla in tablero)

### **Clase `Guardar`**
class Guardar:
    # **Método para guardar el símbolo en la posición del tablero**
    def guardar(self, posicion, simbolo, tablero):
        # Asigna el símbolo (X o O) a la posición correspondiente en el tablero
        tablero[posicion] = simbolo

### **Iniciar el juego**
if __name__ == "__main__":
    # Crear la ventana principal del juego
    root = Tk()
    # Establecer el título de la ventana
    root.title("Juego de Gato")
    # Crear una instancia de la clase IniciarJuego, que maneja el juego completo
    juego = IniciarJuego(root)
    # Inicia el bucle principal de la interfaz gráfica para mantener la ventana abierta
    root.mainloop()
