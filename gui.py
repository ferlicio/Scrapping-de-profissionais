import tkinter as tk
from tkinter import ttk, messagebox
from difflib import SequenceMatcher

# Dados de exemplo para demonstracao com informacoes adicionais
PROFISSIONAIS = [
    {
        "nome": "Fulano",
        "titulo": "Desenvolvedor Python",
        "pais": "Brasil",
        "estado": "SP",
        "cidade": "Sao Paulo",
        "setor": "Tecnologia",
        "senioridade": "Sênior",
        "skills": ["Python", "Django", "AWS"],
        "empresa": "Empresa X",
        "formacao": "Bacharelado",
        "certificacoes": ["AWS"],
    },
    {
        "nome": "Beltrano",
        "titulo": "Product Manager",
        "pais": "Brasil",
        "estado": "RJ",
        "cidade": "Rio de Janeiro",
        "setor": "Tecnologia",
        "senioridade": "Pleno",
        "skills": ["Agile", "Scrum"],
        "empresa": "Empresa Y",
        "formacao": "MBA",
        "certificacoes": ["PMP"],
    },
    {
        "nome": "Sicrano",
        "titulo": "Advogado",
        "pais": "Brasil",
        "estado": "MG",
        "cidade": "Belo Horizonte",
        "setor": "Jurídico",
        "senioridade": "Sênior",
        "skills": ["Direito", "Contratos"],
        "empresa": "Escritorio Z",
        "formacao": "Mestrado",
        "certificacoes": [],
    },
    {
        "nome": "Maria",
        "titulo": "Engenheira de Software",
        "pais": "Brasil",
        "estado": "MG",
        "cidade": "Belo Horizonte",
        "setor": "Tecnologia",
        "senioridade": "Júnior",
        "skills": ["Python", "UX"],
        "empresa": "Empresa K",
        "formacao": "Bacharelado",
        "certificacoes": [],
    },
]


def _parse_lista(valor: str):
    """Converte uma string separada por virgula em lista."""
    return [v.strip() for v in valor.split(',') if v.strip()]


def _similaridade(a: str, b: str) -> float:
    """Retorna a similaridade entre duas strings (0 a 1)."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def buscar_profissionais(
    titulo: str,
    pais: str,
    estado: str,
    cidade: str,
    setor: str,
    senioridades,
    palavras,
    excluir,
    empresa: str,
    formacao: str,
    certificacoes,
    hard_flags,
):
    """Filtra e rankeia os profissionais conforme os filtros informados."""
    resultados = []
    for p in PROFISSIONAIS:
        score = 0
        soft = 0

        if titulo:
            if hard_flags.get("titulo"):
                if titulo.lower() not in p["titulo"].lower():
                    continue
            else:
                r = _similaridade(titulo, p["titulo"])
                if r == 0:
                    continue
                score += r
                soft += 1

        if pais:
            if hard_flags.get("pais"):
                if pais.lower() not in p["pais"].lower():
                    continue
            else:
                r = _similaridade(pais, p["pais"])
                if r == 0:
                    continue
                score += r
                soft += 1

        if estado:
            if hard_flags.get("estado"):
                if estado.lower() not in p["estado"].lower():
                    continue
            else:
                r = _similaridade(estado, p["estado"])
                if r == 0:
                    continue
                score += r
                soft += 1

        if cidade:
            if hard_flags.get("cidade"):
                if cidade.lower() not in p["cidade"].lower():
                    continue
            else:
                r = _similaridade(cidade, p["cidade"])
                if r == 0:
                    continue
                score += r
                soft += 1

        if setor:
            if hard_flags.get("setor"):
                if setor != p["setor"]:
                    continue
            else:
                r = _similaridade(setor, p["setor"])
                if r == 0:
                    continue
                score += r
                soft += 1

        if senioridades:
            if hard_flags.get("senioridade"):
                if p["senioridade"].lower() not in [s.lower() for s in senioridades]:
                    continue
            else:
                r = 1.0 if p["senioridade"].lower() in [s.lower() for s in senioridades] else 0
                if r == 0:
                    continue
                score += r
                soft += 1

        if empresa:
            if hard_flags.get("empresa"):
                if empresa.lower() not in p["empresa"].lower():
                    continue
            else:
                r = _similaridade(empresa, p["empresa"])
                if r == 0:
                    continue
                score += r
                soft += 1

        if formacao:
            if hard_flags.get("formacao"):
                if formacao.lower() not in p["formacao"].lower():
                    continue
            else:
                r = _similaridade(formacao, p["formacao"])
                if r == 0:
                    continue
                score += r
                soft += 1

        if certificacoes:
            if hard_flags.get("certificacoes"):
                if not all(c.lower() in map(str.lower, p["certificacoes"]) for c in certificacoes):
                    continue
            else:
                found = sum(1 for c in certificacoes if c.lower() in map(str.lower, p["certificacoes"]))
                r = found / len(certificacoes)
                if r == 0:
                    continue
                score += r
                soft += 1

        if palavras:
            if hard_flags.get("palavras"):
                if not all(any(k.lower() in skill.lower() for skill in p["skills"]) for k in palavras):
                    continue
            else:
                matches = sum(1 for k in palavras if any(k.lower() in skill.lower() for skill in p["skills"]))
                r = matches / len(palavras)
                if r == 0:
                    continue
                score += r
                soft += 1

        if excluir:
            texto = p["titulo"].lower() + " " + " ".join(p["skills"]).lower()
            if hard_flags.get("excluir"):
                if any(e.lower() in texto for e in excluir):
                    continue
            else:
                if any(e.lower() in texto for e in excluir):
                    continue

        media = score / soft if soft else 1.0
        resultados.append((media, p))

    resultados.sort(key=lambda x: x[0], reverse=True)
    return [p for _, p in resultados]


def exibir_resultados(resultados, lista):
    lista.delete(*lista.get_children())
    if not resultados:
        messagebox.showinfo(
            "Profissionais não encontrados",
            "Nenhum profissional foi encontrado com os parâmetros informados.",
        )
        return
    for profissional in resultados:
        lista.insert("", tk.END, values=(
            profissional["nome"],
            profissional["titulo"],
            f"{profissional['cidade']}/{profissional['estado']}",
        ))


def pesquisar(campos, lista, hard_vars):
    titulo = campos["titulo"].get()
    pais = campos["pais"].get()
    estado = campos["estado"].get()
    cidade = campos["cidade"].get()
    setor = campos["setor"].get()
    senioridade = campos["senioridade"].get()
    senioridades = [senioridade] if senioridade else []
    palavras = _parse_lista(campos["palavras"].get())
    excluir = _parse_lista(campos["excluir"].get())
    empresa = campos["empresa"].get()
    formacao = campos["formacao"].get()
    certs = _parse_lista(campos["certificacoes"].get())
    resultados = buscar_profissionais(
        titulo,
        pais,
        estado,
        cidade,
        setor,
        senioridades,
        palavras,
        excluir,
        empresa,
        formacao,
        certs,
        hard_vars,
    )
    exibir_resultados(resultados, lista)


def criar_interface():
    root = tk.Tk()
    root.title("Busca de Profissionais")

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    campos = {}
    hard_vars = {}

    ttk.Label(frm, text="Cargo/Título:").grid(column=0, row=0, sticky="w")
    campos["titulo"] = ttk.Entry(frm)
    campos["titulo"].grid(column=1, row=0, padx=5, pady=2)
    hard_vars["titulo"] = tk.BooleanVar(value=True)
    ttk.Checkbutton(frm, text="Hard", variable=hard_vars["titulo"]).grid(column=2, row=0, sticky="w")

    ttk.Label(frm, text="País:").grid(column=0, row=1, sticky="w")
    campos["pais"] = ttk.Entry(frm)
    campos["pais"].grid(column=1, row=1, padx=5, pady=2)
    hard_vars["pais"] = tk.BooleanVar(value=True)
    ttk.Checkbutton(frm, text="Hard", variable=hard_vars["pais"]).grid(column=2, row=1, sticky="w")

    ttk.Label(frm, text="Estado:").grid(column=0, row=2, sticky="w")
    campos["estado"] = ttk.Entry(frm)
    campos["estado"].grid(column=1, row=2, padx=5, pady=2)
    hard_vars["estado"] = tk.BooleanVar(value=True)
    ttk.Checkbutton(frm, text="Hard", variable=hard_vars["estado"]).grid(column=2, row=2, sticky="w")

    ttk.Label(frm, text="Cidade:").grid(column=0, row=3, sticky="w")
    campos["cidade"] = ttk.Entry(frm)
    campos["cidade"].grid(column=1, row=3, padx=5, pady=2)
    hard_vars["cidade"] = tk.BooleanVar(value=True)
    ttk.Checkbutton(frm, text="Hard", variable=hard_vars["cidade"]).grid(column=2, row=3, sticky="w")

    ttk.Label(frm, text="Setor/Indústria:").grid(column=0, row=4, sticky="w")
    campos["setor"] = ttk.Combobox(frm, values=["", "Tecnologia", "Finanças", "Saúde", "Educação", "Jurídico"])
    campos["setor"].grid(column=1, row=4, padx=5, pady=2)
    hard_vars["setor"] = tk.BooleanVar(value=True)
    ttk.Checkbutton(frm, text="Hard", variable=hard_vars["setor"]).grid(column=2, row=4, sticky="w")

    ttk.Label(frm, text="Nível de Senioridade:").grid(column=0, row=5, sticky="w")
    campos["senioridade"] = ttk.Combobox(
        frm,
        values=["", "Estágio", "Júnior", "Pleno", "Sênior", "Lead", "Especialista"],
    )
    campos["senioridade"].grid(column=1, row=5, padx=5, pady=2, sticky="w")
    hard_vars["senioridade"] = tk.BooleanVar(value=True)
    ttk.Checkbutton(frm, text="Hard", variable=hard_vars["senioridade"]).grid(column=2, row=5, sticky="w")

    ttk.Label(frm, text="Palavras-chave extras:").grid(column=0, row=6, sticky="w")
    campos["palavras"] = ttk.Entry(frm)
    campos["palavras"].grid(column=1, row=6, padx=5, pady=2)
    hard_vars["palavras"] = tk.BooleanVar(value=True)
    ttk.Checkbutton(frm, text="Hard", variable=hard_vars["palavras"]).grid(column=2, row=6, sticky="w")

    ttk.Label(frm, text="Filtro excludente:").grid(column=0, row=7, sticky="w")
    campos["excluir"] = ttk.Entry(frm)
    campos["excluir"].grid(column=1, row=7, padx=5, pady=2)
    hard_vars["excluir"] = tk.BooleanVar(value=True)
    ttk.Checkbutton(frm, text="Hard", variable=hard_vars["excluir"]).grid(column=2, row=7, sticky="w")

    ttk.Label(frm, text="Empresa:").grid(column=0, row=8, sticky="w")
    campos["empresa"] = ttk.Entry(frm)
    campos["empresa"].grid(column=1, row=8, padx=5, pady=2)
    hard_vars["empresa"] = tk.BooleanVar(value=True)
    ttk.Checkbutton(frm, text="Hard", variable=hard_vars["empresa"]).grid(column=2, row=8, sticky="w")

    ttk.Label(frm, text="Formação:").grid(column=0, row=9, sticky="w")
    campos["formacao"] = ttk.Entry(frm)
    campos["formacao"].grid(column=1, row=9, padx=5, pady=2)
    hard_vars["formacao"] = tk.BooleanVar(value=True)
    ttk.Checkbutton(frm, text="Hard", variable=hard_vars["formacao"]).grid(column=2, row=9, sticky="w")

    ttk.Label(frm, text="Certificações:").grid(column=0, row=10, sticky="w")
    campos["certificacoes"] = ttk.Entry(frm)
    campos["certificacoes"].grid(column=1, row=10, padx=5, pady=2)
    hard_vars["certificacoes"] = tk.BooleanVar(value=True)
    ttk.Checkbutton(frm, text="Hard", variable=hard_vars["certificacoes"]).grid(column=2, row=10, sticky="w")

    cols = ("Nome", "Título", "Local")
    lista = ttk.Treeview(frm, columns=cols, show="headings")
    for col in cols:
        lista.heading(col, text=col)
    lista.grid(column=0, row=13, columnspan=3, pady=5)

    botao = ttk.Button(
        frm,
        text="Buscar",
        command=lambda: pesquisar(campos, lista, hard_vars),
    )
    botao.grid(column=0, row=12, columnspan=3, pady=5)

    root.mainloop()


if __name__ == "__main__":
    criar_interface()
