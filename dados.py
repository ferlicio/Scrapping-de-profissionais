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


def _gerar_profissionais_teste():
    estados = ["SP", "RJ", "MG", "RS", "SC"]
    cidades = {
        "SP": ["Sao Paulo", "Campinas", "Santos"],
        "RJ": ["Rio de Janeiro", "Niteroi"],
        "MG": ["Belo Horizonte", "Uberlandia"],
        "RS": ["Porto Alegre", "Caxias do Sul"],
        "SC": ["Florianopolis", "Joinville"],
    }
    setores = ["Tecnologia", "Finanças", "Saúde", "Educação", "Jurídico"]
    senioridades = ["Estágio", "Júnior", "Pleno", "Sênior", "Lead"]
    titulos = [
        "Analista de Teste",
        "Desenvolvedor Backend",
        "Desenvolvedor Frontend",
        "Analista de Dados",
        "Designer",
    ]
    formacoes = [
        "Bacharelado",
        "Mestrado",
        "MBA",
        "Tecnólogo",
        "Especialização",
    ]
    certificacoes_opcoes = [
        [],
        ["AWS"],
        ["PMP"],
        ["Scrum Master"],
        ["ITIL"],
        ["CCNA"],
        ["Docker", "Kubernetes"],
        ["Azure"],
    ]

    for i in range(100):
        estado = estados[i % len(estados)]
        cidade = cidades[estado][i % len(cidades[estado])]
        PROFISSIONAIS.append(
            {
                "nome": f"Teste {i}",
                "titulo": titulos[i % len(titulos)],
                "pais": "Brasil",
                "estado": estado,
                "cidade": cidade,
                "setor": setores[i % len(setores)],
                "senioridade": senioridades[i % len(senioridades)],
                "skills": ["Teste", f"Skill{i}"],
                "empresa": f"Empresa Teste {i}",
                "formacao": formacoes[i % len(formacoes)],
                "certificacoes": certificacoes_opcoes[i % len(certificacoes_opcoes)],
            }
        )


_gerar_profissionais_teste()
