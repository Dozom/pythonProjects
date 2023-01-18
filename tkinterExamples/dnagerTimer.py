# Llibreria de botons i coses complexes de tkinter
from tkinter import Tk, BOTH, Button, TOP, BOTTOM, Entry
# Llibreria de botons i coses simples Tkinter
from tkinter.ttk import Frame
# Llibreria per fer sonar el big ben
from playsound import playsound
# llibreries per threading i timer
import threading
import time

# Classe Container que hereda de Frame per a colocar els elements
class Container(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Timer Daniel Nager")
        # Botó clear all, que llança clearAll i esborra tots els threads que estan alive
        btn2 = Button(self.parent, text="CLEAR ALL", width=70, command=clearAll)
        btn2.pack(side=BOTTOM)
        # Cuadre de text
        entry = Entry(self.parent, width=70)
        # Botó que agafa el valor del cuadre de text un cop s'ha clicat, i crea un thread de timer 
        btn1 = Button(self.parent, text="SET", width=70, command= lambda: setTimer(self.parent, entry.get()))
        # Colocació dins del frame a través del widget manager pack
        btn1.pack(side=BOTTOM)
        entry.pack(side=BOTTOM)
        self.pack(fill=BOTH, expand=True)

def setTimer(root, value):
    """ Funció que crea un timer que s'executa passats X segons"""
    alarm = threading.Timer(int(value), soundMan)
    alarm.start()
def soundMan():
    """ Funció, que fa sonar un só"""
    playsound('./sound.wav')
def clearAll():
    """Funció que neteja tots els threads excepte el main thread"""
    filPrincipal = threading.main_thread()
    # Segons la documentació de python, tots els threads de enumerate, estàn alive, pel que sobra el is_alive
    # Referencia: https://docs.python.org/3/library/threading.html
    """
            is_alive()

                Return whether the thread is alive.

                This method returns True just before the run() method starts until just after the
                run() method terminates. The module function enumerate() returns a list of all alive threads.
    """
    for fil in threading.enumerate():
        if fil is filPrincipal:
            continue
        # cancelar fil
        fil.cancel()
# Funció main amb propietats de la finestra
def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Container(root)
    root.mainloop()
if __name__ == '__main__':
    main()
