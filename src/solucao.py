# ============================================================
#  LAB 04 – Strings
#  Disciplina: Laboratório de Algoritmos e Lógica de Programação
#  Curso: Análise e Desenvolvimento de Sistemas – IFPB
# ============================================================
#
#  INSTRUÇÕES:
#  - Implemente cada função conforme descrito no enunciado.
#  - NÃO altere os nomes das funções nem os parâmetros.
#  - As funções recebem o texto como PARÂMETRO: NÃO use input().
#  - NÃO use import nem listas (nem split()). Use for/while,
#    índices, fatias e os métodos de string vistos em aula.
#  - Após implementar, faça commit e push para o seu repositório.
#
# ============================================================


def contar_maiusculas(mensagem: str) -> int:
    """
    Retorna quantas letras maiúsculas a mensagem possui.
    Minúsculas, espaços, números e sinais NÃO contam.
    Maiúsculas acentuadas (É, Ã, Ç...) contam.
    Ex.: contar_maiusculas("Oi TUDO bem?") → 5
    """
    # TODO: implemente aqui
    pass


def mascarar_cartao(numero: str) -> str:
    """
    Troca por "*" todos os dígitos do cartão, MENOS os 4 últimos dígitos.
    Espaços e hífens ficam como estão.
    Com 4 dígitos ou menos, nada é mascarado.
    Ex.: mascarar_cartao("1234 5678 9012 3456") → "**** **** **** 3456"
    """
    # TODO: implemente aqui
    pass


def nivel_senha(senha: str) -> str:
    """
    Retorna o nível de segurança da senha:
      "Nível 1"        → apenas letras
      "Nível 2"        → letras e números
      "Nível 3"        → letras, números e especiais (! # * @)
      "Senha inválida" → qualquer outro caso (vazia, só números,
                         sem número, caractere não permitido...)
    """
    # TODO: implemente aqui
    pass


def validar_cpf(cpf: str) -> str:
    """
    Recebe um CPF no formato "xxx.xxx.xxx-xx" e retorna
    "CPF válido" ou "CPF inválido".
    Verifique: o formato, se os 11 dígitos não são todos iguais
    e os dois dígitos verificadores (veja o README).
    Ex.: validar_cpf("529.982.247-25") → "CPF válido"
    """
    # TODO: implemente aqui
    pass


# ============================================================
#  Use o bloco abaixo para testar suas funções no seu computador.
#  Ele NÃO é executado na correção automática.
#  Coloque chamadas de teste SOMENTE aqui dentro (indentadas):
#  chamadas fora deste bloco quebram a correção e zeram a nota.
# ============================================================
if __name__ == "__main__":
    print(contar_maiusculas("Oi TUDO bem?"))
    print(mascarar_cartao("1234 5678 9012 3456"))
    print(nivel_senha("Ifpb@2026"))
    print(validar_cpf("529.982.247-25"))
