import tkinter as tk
from tkinter import ttk

# Dados de exemplo para demonstracao
PROFISSIONAIS = [
    {"nome": "Fulano", "profissao": "Medico", "localizacao": "Sao Paulo"},
    {"nome": "Beltrano", "profissao": "Advogado", "localizacao": "Rio de Janeiro"},
    {"nome": "Sicrano", "profissao": "Engenheiro", "localizacao": "Belo Horizonte"},
    {"nome": "Maria", "profissao": "Medico", "localizacao": "Belo Horizonte"},
]

def buscar_profissionais(profissao: str, localizacao: str):
    """Filtra os profissionais de acordo com a profissao e localizacao."""
    resultados = []
    for p in PROFISSIONAIS:
        if profissao and profissao.lower() not in p["profissao"].lower():
            continue
        if localizacao and localizacao.lower() not in p["localizacao"].lower():
            continue
        resultados.append(p)
    return resultados


def exibir_resultados(resultados, lista):
    lista.delete(*lista.get_children())
    for profissional in resultados:
        lista.insert("", tk.END, values=(
            profissional["nome"],
            profissional["profissao"],
            profissional["localizacao"],
        ))


def pesquisar(entry_prof, entry_loc, lista):
    profissao = entry_prof.get()
    localizacao = entry_loc.get()
    resultados = buscar_profissionais(profissao, localizacao)
    exibir_resultados(resultados, lista)


def criar_interface():
    root = tk.Tk()
    root.title("Busca de Profissionais")

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    ttk.Label(frm, text="Profissao:").grid(column=0, row=0, sticky="w")
    entry_prof = ttk.Entry(frm)
    entry_prof.grid(column=1, row=0, padx=5, pady=2)

    ttk.Label(frm, text="Localizacao:").grid(column=0, row=1, sticky="w")
    entry_loc = ttk.Entry(frm)
    entry_loc.grid(column=1, row=1, padx=5, pady=2)

    cols = ("Nome", "Profissao", "Localizacao")
    lista = ttk.Treeview(frm, columns=cols, show="headings")
    for col in cols:
        lista.heading(col, text=col)
    lista.grid(column=0, row=3, columnspan=2, pady=5)

    botao = ttk.Button(
        frm,
        text="Buscar",
        command=lambda: pesquisar(entry_prof, entry_loc, lista),
    )
    botao.grid(column=0, row=2, columnspan=2, pady=5)

    root.mainloop()


if __name__ == "__main__":
    criar_interface()
