import tkinter
import customtkinter
import config


from gui.skeleton import setup_skeleton


def show_gui():
    root = tkinter.Tk()
    root.geometry("1000x600")
    root.title("Data Analysis Tool")

    config.root = root

    setup_skeleton(root)

    root.mainloop()
