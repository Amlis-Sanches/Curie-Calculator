import tkinter as tk
from tkinter import ttk
from GUI.ManualCalculation import ManualCalculation

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Decay Calculation Test")
        self.geometry("400x300")

        #Create a Notebook for the individual tabs
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        #add tabs to the notebook
        notebook.add(ManualCalculation(self), text="Manual Activity Calculation")
        notebook.add(ManualCalculation(self),text='Data Table')
        notebook.add(ManualCalculation(self),text='Activity Calculation')

#Run application
if __name__ == "__main__":
    App().mainloop()