import tkinter as tk
from tkinter import ttk
from Module.Equasions import calc_atoms, decay_constant, decay


class ManualCalculation(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Input fields for gram, isotope weight, and half-life
        self.create_input("Grams of Material:", "grams", 0)
        self.create_input("Isotope Weight (g/mol):", "isotope_weight", 1)
        self.create_input("Half-life:", "half_life", 2)

        # Dropdown for units of half-life
        self.units_var = tk.StringVar(value="Yr")
        tk.Label(self, text="Units for Half-life:").grid(row=3, column=0, pady=5)
        ttk.Combobox(self, textvariable=self.units_var, values=["Yr", "Day", "Hr", "min", "sec", "ms", "micros", "ns", "ps", "fs", "as", "zs"]).grid(row=3, column=1)

        # Calculate Button
        calc_button = tk.Button(self, text="Calculate", command=self.calculate_results)
        calc_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Results Labels
        self.result_atoms = tk.Label(self, text="Atoms: ")
        self.result_atoms.grid(row=5, column=0, columnspan=2, pady=5)
        self.result_constant = tk.Label(self, text="Decay Constant: ")
        self.result_constant.grid(row=6, column=0, columnspan=2, pady=5)
        self.result_decay = tk.Label(self, text="Decay: ")
        self.result_decay.grid(row=7, column=0, columnspan=2, pady=5)

    def create_input(self, label_text, var_name, row):
        setattr(self, var_name, tk.DoubleVar())
        tk.Label(self, text=label_text).grid(row=row, column=0, pady=5)
        tk.Entry(self, textvariable=getattr(self, var_name)).grid(row=row, column=1)

    def calculate_results(self):
        try:
            # Fetch values from input fields
            grams = self.grams.get()
            isotope_weight = self.isotope_weight.get()
            half_life = self.half_life.get()
            units = self.units_var.get()

            # Perform calculations
            atoms = calc_atoms(grams, isotope_weight)
            constant = decay_constant(half_life, units)
            decay_result = decay(constant, atoms)

            # Update result labels
            self.result_atoms.config(text=f"Atoms: {atoms:.3e}")
            self.result_constant.config(text=f"Decay Constant: {constant:.3e}")
            self.result_decay.config(text=f"Decay: {decay_result:.3e}")

        except Exception as e:
            # Display error message if calculations fail
            tk.messagebox.showerror("Error", f"An error occurred: {e}")

# Run the application
if __name__ == "__main__":
    app = TestApp()
    app.mainloop()
