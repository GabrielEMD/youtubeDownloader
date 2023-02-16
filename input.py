from tkinter import *
from downloader import *
from time import sleep

def run():
    info = 'Esperando'

    window = Tk()

    window.title("Descargar de Youtube v20221206")
    # window.iconbitmap("favicon.ico")
    window.config(bg="#e3e3e3", width="320", height="140")
    window.geometry("320x140")

    vacio = Label(window, background="#e3e3e3")
    vacio.grid(row= 1, column=1)

    text_box = Entry(window, width=30)
    text_box.grid(row= 2, column=3)
    # text_box.pack()

    text2 = Label(window, text="Link del video:", background="#e3e3e3")
    text2.grid(row= 2, column=2, sticky="e")
    # title = Label(window, text="Descarga mp4 mp3", background="#e3e3e3")
    # title.grid(row= 0, column=0)
    text1 = Label(window, text="Descargar como:", background="#e3e3e3")
    text1.grid(row= 4, column=2, sticky="e")
    text1 = Label(window, text="Estado:", background="#e3e3e3")
    text1.grid(row= 5, column=2, sticky="e")
    text2 = Label(window, text="Tipo:", background="#e3e3e3")
    text2.grid(row= 3, column=2, sticky="e")
    # text1.pack()

    button1 = Button(window, text="VIDEO", command=lambda:boton1())
    button1.grid(row= 4, column=3, sticky="w")
    button1.configure(width=10)
    button2 = Button(window, text="MP3", command=lambda:boton2())
    button2.grid(row= 4, column=3, sticky="e")
    button2.configure(width=10)
    button2 = Button(window, text="X", command=lambda:clear())
    button2.grid(row= 2, column=4, sticky="w")
    button2.configure(width=2)

    var1 = IntVar()
    check = Checkbutton(window, text="Lista", variable=var1, onvalue = 1, offvalue = 0, background="#e3e3e3")
    check.grid(row= 3, column=3, sticky="w")
    # button.pack()

    text = Label(window, text=info, background="#e3e3e3")
    text.grid(row= 5, column=3, sticky="w")
    # text.pack()

    def boton1():
        text.configure(text="Procesando")
        link = text_box.get()
        response = mp4(link, var1.get())
        text.configure(text=response)

    def boton2():
        text.configure(text="Procesando")
        link = text_box.get()
        response = mp3(link, var1.get())
        text.configure(text=response)

    def clear():
        text_box.delete(0, END)

    window.mainloop()

if __name__ == "__main__":
    run()