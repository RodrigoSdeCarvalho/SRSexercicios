# Classificador de triângulos com orientação a objetos.

import tkinter as tk

class Triangle:
    def __init__(self, side_a:int, side_b:int, side_c:int) -> None:
        if not self.is_triangle(side_a, side_b, side_c):
            raise ValueError("Os lados não formam um triângulo válido.")
    
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c
        self.set_kind()

    def is_triangle(self) -> bool:
        if self.__side_a + self.__side_b >= self.__side_c and self.__side_a + self.__side_c >= self.__side_b and self.__side_b + self.__side_c >= self.__side_a:
            return True
        else:
            return False

    @property
    def side_a(self) -> int:
        return self.__side_a
    
    @property
    def side_b(self) -> int:
        return self.__side_b
    
    @property
    def side_c(self) -> int:
        return self.__side_c
    
    @property
    def kind(self) -> str:
        return self.__kind

    def set_kind(self) -> str:
        if self.is_equilateral():
            self.__kind = "Equilátero"
        elif self.is_isosceles():
            self.__kind = "Isósceles"
        elif self.is_scalene():
            self.__kind = "Escaleno"

    def is_equilateral(self) -> bool:
        if self.__side_a == self.__side_b and self.__side_b == self.__side_c:
            return True
        else:
            return False

    def is_isosceles(self) -> bool:
        if self.__side_a == self.__side_b or self.__side_b == self.__side_c or self.__side_a == self.__side_c:
            return True
        else:
            return False

    def is_scalene(self) -> bool:
        if self.__side_a != self.__side_b and self.__side_b != self.__side_c and self.__side_a != self.__side_c:
            return True
        else:
            return False


class TriangleGUI:
    def __init__(self, master):
        self.master = master
        master.title("Classificador de Triângulos")

        self.side_a_label = tk.Label(master, text="Lado A:")
        self.side_a_label.grid(row=0, column=0)

        self.side_a_entry = tk.Entry(master)
        self.side_a_entry.grid(row=0, column=1)

        self.side_b_label = tk.Label(master, text="Lado B:")
        self.side_b_label.grid(row=1, column=0)

        self.side_b_entry = tk.Entry(master)
        self.side_b_entry.grid(row=1, column=1)

        self.side_c_label = tk.Label(master, text="Lado C:")
        self.side_c_label.grid(row=2, column=0)

        self.side_c_entry = tk.Entry(master)
        self.side_c_entry.grid(row=2, column=1)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2)

        self.classify_button = tk.Button(master, text="Classificar", command=self.classify_triangle)
        self.classify_button.grid(row=4, column=0, columnspan=2)

    def classify_triangle(self):
        side_a = int(self.side_a_entry.get())
        side_b = int(self.side_b_entry.get())
        side_c = int(self.side_c_entry.get())

        try:
            triangle = Triangle(side_a, side_b, side_c)
            result_text = f"Tipo de triângulo: {triangle.kind}"
        except ValueError as e:
            result_text = f"Erro: {e}"

        self.result_label.config(text=result_text)


root = tk.Tk()
triangle_gui = TriangleGUI(root)
root.mainloop()
