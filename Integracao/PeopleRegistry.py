import tkinter as tk
import pandas as pd
from os.path import exists
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from os.path import exists
import pandas as pd
import os

class PeopleRegistry:
    PEOPLE_REGISTRY_CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "people_registry.csv")

    def __init__(self) -> None:
        if not exists(PeopleRegistry.PEOPLE_REGISTRY_CSV_PATH):
            self.__database = self.create_people_registry()
        else:
            self.__database = pd.read_csv(PeopleRegistry.PEOPLE_REGISTRY_CSV_PATH, index_col="CPF")

    def create_people_registry(self) -> None:
        people_registry = pd.DataFrame(columns=["CPF", "nome", "idade", "telefone"])
        people_registry = people_registry.set_index("CPF")
        people_registry.to_csv(PeopleRegistry.PEOPLE_REGISTRY_CSV_PATH)

        return people_registry

    def insert_person(self, cpf:str, name:str, age:int, phone:str) -> None:
        self.check_if_person_data_is_valid(cpf, name, age, phone)

        people_registry = self.__database
        people_registry.loc[cpf] = [name, age, phone]
        people_registry.to_csv(PeopleRegistry.PEOPLE_REGISTRY_CSV_PATH)

    def check_if_person_data_is_valid(self, cpf:str, name:str, age:str, phone:str) -> None:
        if not cpf.isnumeric():
            raise ValueError("O CPF deve conter apenas números.")
        elif not name.replace(' ','').isalpha():
            raise ValueError("O nome deve conter apenas letras.")
        elif not age.isnumeric():
            raise ValueError("A idade deve conter apenas números.")
        elif not phone.isnumeric():
            raise ValueError("O telefone deve conter apenas números.")

    def delete_person(self, cpf:str) -> None:
        cpf = int(cpf)
        people_registry = self.__database
        if cpf in people_registry.index:
            people_registry.drop(index=cpf, inplace=True)
            people_registry.to_csv(PeopleRegistry.PEOPLE_REGISTRY_CSV_PATH)
        else:
            raise ValueError("Não foi possível excluir a pessoa. CPF não encontrado.")

    def get_person(self, cpf:str) -> pd.Series:
        cpf = int(cpf)
        self.__database = pd.read_csv(PeopleRegistry.PEOPLE_REGISTRY_CSV_PATH, index_col="CPF") # Atualiza o banco de dados
        people_registry = self.__database

        try:
            return people_registry.loc[cpf]
        except:
            return None

    def generate_report_on_how_many_people_are_of_a_specific_age(self, age:int) -> dict:
        people_registry = self.__database
        people_of_age = people_registry[people_registry["idade"] == age]
        total_of_people = len(people_of_age)
        report = {"idade": age, "pessoas": total_of_people, "total": len(people_registry)}

        return report

    def generate_report_on_peoples_age(self) -> dict:
        people_registry = self.__database
        youngest_person = people_registry.loc[people_registry["idade"] == people_registry["idade"].min()]
        oldest_person = people_registry.loc[people_registry["idade"] == people_registry["idade"].max()]
        mean_age = people_registry["idade"].mean()

        report = {
            "mais_novo": {"nome": youngest_person["nome"].values[0], "idade": youngest_person["idade"].values[0]},
            "mais_velho": {"nome": oldest_person["nome"].values[0], "idade": oldest_person["idade"].values[0]},
            "media": mean_age
        }

        return report


class PeopleRegistryGUI:
    def __init__(self, master:tk.Tk) -> None:
        self.master = master
        self.master.title("People Registry")
        self.create_widgets()
        self.people_registry = PeopleRegistry()

    def create_widgets(self) -> None:
        # Entrada de CPF
        self.label_cpf = ttk.Label(self.master, text="CPF")
        self.label_cpf.grid(row=0, column=0, padx=5, pady=5)

        self.entry_cpf = ttk.Entry(self.master, width=20)
        self.entry_cpf.grid(row=0, column=1, padx=5, pady=5)
        
        # Entrada de nome
        self.label_name = ttk.Label(self.master, text="Nome")
        self.label_name.grid(row=1, column=0, padx=5, pady=5)

        self.entry_name = ttk.Entry(self.master, width=50)
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)

        # Entrada de idade
        self.label_age = ttk.Label(self.master, text="Idade")
        self.label_age.grid(row=2, column=0, padx=5, pady=5)

        self.entry_age = ttk.Entry(self.master, width=5)
        self.entry_age.grid(row=2, column=1, padx=5, pady=5)

        # Entrada de telefone
        self.label_phone = ttk.Label(self.master, text="Telefone")
        self.label_phone.grid(row=3, column=0, padx=5, pady=5)

        self.entry_phone = ttk.Entry(self.master, width=20)
        self.entry_phone.grid(row=3, column=1, padx=5, pady=5)

        # Botão de inserção
        self.button_insert = ttk.Button(self.master, text="Inserir/Atualizar", command=self.insert_person)
        self.button_insert.grid(row=4, column=0, padx=5, pady=5)

        # Botão de busca
        self.button_search = ttk.Button(self.master, text="Buscar", command=self.get_person)
        self.button_search.grid(row=0, column=2, padx=5, pady=5)
        
        # Botão de deleção
        self.button_insert = ttk.Button(self.master, text="Deletar", command=self.delete_person)
        self.button_insert.grid(row=5, column=0, padx=5, pady=5)

        # Botões de relatório
        self.button_report_age = ttk.Button(self.master, text="Relatório geral das idade", command=self.generate_report_on_peoples_age)
        self.button_report_age.grid(row=4, column=1, padx=5, pady=5)

        self.button_report_specific_age = ttk.Button(self.master, text="Relatório por idade específica", command=self.generate_report_on_how_many_people_are_of_a_specific_age)
        self.button_report_specific_age.grid(row=4, column=2, padx=5, pady=5)

    def insert_person(self) -> None:
        cpf = self.entry_cpf.get()
        name = self.entry_name.get()
        age = self.entry_age.get()
        phone = self.entry_phone.get()

        try:
            self.people_registry.insert_person(cpf, name, age, phone)
            messagebox.showinfo("Sucesso", "Pessoa inserida com sucesso.")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

        self.clear_entries()

    def clear_entries(self) -> None:
        self.entry_cpf.delete(0, 'end')
        self.entry_name.delete(0, 'end')
        self.entry_age.delete(0, 'end')
        self.entry_phone.delete(0, 'end')

    def get_person(self) -> None:
        cpf = self.entry_cpf.get()
        person = self.people_registry.get_person(cpf)
        if person is not None:
            self.clear_entries()
            self.insert_entries(person, cpf)
        else:
            messagebox.showerror("Erro", "Pessoa não encontrada.")
            self.entry_cpf.delete(0, 'end')

    def insert_entries(self, person:dict, cpf:int) -> None:
        self.entry_cpf.insert(0, cpf)
        self.entry_name.insert(0, person.nome)
        self.entry_age.insert(0, person.idade)
        self.entry_phone.insert(0, person.telefone)

    def delete_person(self) -> None:
        cpf = self.entry_cpf.get()
        try:
            self.people_registry.delete_person(cpf)
            messagebox.showinfo("Sucesso", "Pessoa deletada com sucesso.")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def generate_report_on_peoples_age(self) -> None:
        report = self.people_registry.generate_report_on_peoples_age()
        message = f"Mais novo: {report['mais_novo']['nome']} ({report['mais_novo']['idade']} anos)\n" \
                  f"Mais velho: {report['mais_velho']['nome']} ({report['mais_velho']['idade']} anos)\n" \
                  f"Média de idade: {report['media']:.2f}"

        messagebox.showinfo("Relatório de idade", message)

    def generate_report_on_how_many_people_are_of_a_specific_age(self) -> None:
        age = self.entry_age.get()
        try:
            report = self.people_registry.generate_report_on_how_many_people_are_of_a_specific_age(int(age))
            message = f"Há {report['pessoas']} pessoa(s) com {age} anos de idade. De um total de {report['total']} pessoa(s)."
            messagebox.showinfo("Relatório de idade específica", message)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

root = tk.Tk()
people_registry_gui = PeopleRegistryGUI(root)
root.mainloop()
