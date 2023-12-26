def ocultar_nome_usuario(email):
    partes = email.split("@")
    nome_usuario = partes[0]

    # Mantenha os dois primeiros e os três últimos caracteres visíveis
    caracteres_visiveis_inicio = min(3, len(nome_usuario))
    caracteres_visiveis_fim = min(4, len(nome_usuario) - caracteres_visiveis_inicio)

    nome_usuario_oculto = (
        nome_usuario[:caracteres_visiveis_inicio]
        + "*"
        * (len(nome_usuario) - caracteres_visiveis_inicio - caracteres_visiveis_fim)
        + nome_usuario[-caracteres_visiveis_fim:]
    )
    parte_oculta = nome_usuario_oculto + "@" + partes[1]

    return parte_oculta


"""# Exemplo de uso
email_original = "brunovidal27.19@gmail.com"
email_oculto = ocultar_nome_usuario(email_original)
print(email_oculto)
"""
