# Lab 04 – Strings

**Disciplina:** Laboratório de Algoritmos e Lógica de Programação  
**Curso:** Análise e Desenvolvimento de Sistemas – IFPB  
**Pontuação total:** 100 pontos  

---

## Objetivo

Praticar a manipulação de **strings** em Python: **percorrer** um texto caractere
por caractere, acessar posições por **índice**, usar **fatias** (`texto[i:j]`),
o operador **`in`**, **`len()`** e os métodos vistos em aula (`upper()`,
`lower()`, `isupper()`, `replace()`, `count()`, `find()`, `isdigit()`, `isalpha()`...).

---

## Como entregar

1. Aceite o laboratório com `gh student accept ifpb-soledade-ads lalp-2026-2 lab04-string`
   (ou pelo link disponibilizado pelo professor).
2. Clone o repositório gerado para você e entre na pasta.
3. Edite **apenas** o arquivo `src/solucao.py`.
4. Envie sua solução com `gh student submit` (ou `git add`, `git commit` e `git push`).
5. Após o envio, acesse as abas **Actions** e **Releases** do seu repositório para ver o
   resultado da correção automática.

>  **Não modifique** nenhum outro arquivo do repositório.

> **Não use `import` nem listas** (nem métodos que geram listas, como `split()`).
> Tudo neste laboratório se resolve com `for`/`while`, índices, fatias e os
> métodos de string vistos em aula.

> **As funções recebem o texto como parâmetro.** Não use `input()` dentro delas.

> **Para testar no seu computador**, rode `python src/solucao.py` e coloque as
> chamadas das funções **somente** dentro do bloco `if __name__ == "__main__":`
> que já está no fim do arquivo. Chamadas (ou `input()`) fora desse bloco quebram
> a correção automática e **zeram a nota do laboratório inteiro**.

---

## Questões

### Q1 – Detector de grito no chat `(25 pontos)`

Na internet, escrever EM MAIÚSCULAS é como gritar. O moderador do grupo da
turma quer um programa que ajude a identificar mensagens "gritadas".

Implemente `contar_maiusculas(mensagem: str) -> int` que recebe uma
**mensagem** e retorna **quantas letras maiúsculas** ela tem.

- Letras minúsculas, espaços, números e sinais **não** contam.
- Letras maiúsculas **acentuadas também contam** (`É`, `Ã`, `Ç`...).

| Chamada                                   | Retorno |
|-------------------------------------------|---------|
| `contar_maiusculas("Oi TUDO bem?")`       | `5`     |
| `contar_maiusculas("IFPB Soledade")`      | `5`     |
| `contar_maiusculas("ÉGUA, QUE PROVA!")`   | `12`    |
| `contar_maiusculas("ADS 2026!!!")`        | `3`     |
| `contar_maiusculas("bom dia")`            | `0`     |

> Dica: percorra a mensagem com `for letra in mensagem:` e use um **contador**.
> O método `isupper()` ajuda.

---

### Q2 – Mascarando o cartão de crédito `(25 pontos)`

Lojas virtuais nunca mostram o número completo do cartão do cliente: só os
**4 últimos dígitos** ficam visíveis, o resto vira `*`.

Implemente `mascarar_cartao(numero: str) -> str` que recebe o número de um
cartão e retorna o número **mascarado**:

- Todos os **dígitos** viram `*`, **menos os 4 últimos dígitos**.
- Os separadores (**espaços** e **hífens**) ficam **como estão**, no mesmo lugar.
- Se o número tiver **4 dígitos ou menos**, nada é mascarado.

| Chamada                                    | Retorno                    |
|--------------------------------------------|----------------------------|
| `mascarar_cartao("1234 5678 9012 3456")`   | `"**** **** **** 3456"`    |
| `mascarar_cartao("1234567890123456")`      | `"************3456"`       |
| `mascarar_cartao("1234-5678-9012-3456")`   | `"****-****-****-3456"`    |
| `mascarar_cartao("3782 822463 10005")`     | `"**** ****** *0005"`      |
| `mascarar_cartao("1234")`                  | `"1234"`                   |

> Atenção ao último exemplo: os 4 últimos **dígitos** são `0005`, e não o
> último grupo (`10005`). Os separadores não contam como dígito.

> Dica: primeiro **conte** quantos dígitos o número tem. Depois percorra o
> texto de novo montando o resultado (`resultado = ""`) e decida, para cada
> dígito, se ele é um dos 4 últimos.

---

### Q3 – Nível de segurança da senha `(25 pontos)`

Implemente `nivel_senha(senha: str) -> str` que diz o nível de segurança de uma
senha, de acordo com os tipos de caracteres que ela contém:

| Retorno          | Quando                                                         |
|------------------|----------------------------------------------------------------|
| `"Nível 1"`      | a senha contém **apenas letras**                               |
| `"Nível 2"`      | a senha contém **letras e números** (e nada mais)              |
| `"Nível 3"`      | a senha contém **letras, números e caracteres especiais**      |
| `"Senha inválida"` | qualquer outro caso (veja abaixo)                            |

Considere:

- **Letras:** maiúsculas ou minúsculas.
- **Números:** os dígitos de `0` a `9`.
- **Caracteres especiais:** somente `!`, `#`, `*` e `@`.

A senha é **inválida** quando não se encaixa em nenhum nível, por exemplo:

- é vazia (`""`);
- tem só números (`"123456"`);
- tem letras e especiais, mas **nenhum número** (`"abc@#"`);
- tem algum caractere que não é letra, número nem especial (espaço, `$`, `.`...).

| Chamada                    | Retorno            |
|----------------------------|--------------------|
| `nivel_senha("Soledade")`  | `"Nível 1"`        |
| `nivel_senha("ifpb2026")`  | `"Nível 2"`        |
| `nivel_senha("Ifpb@2026")` | `"Nível 3"`        |
| `nivel_senha("123456")`    | `"Senha inválida"` |
| `nivel_senha("abc 123")`   | `"Senha inválida"` |

> Dica: percorra a senha e use variáveis como `tem_letra`, `tem_numero`,
> `tem_especial` (começando em `False`). Depois do laço, decida o nível com
> `if`/`elif`. Os métodos `isalpha()` e `isdigit()` ajudam.

---

### Q4 – Verifica CPF `(25 pontos)`

Implemente `validar_cpf(cpf: str) -> str` que recebe um CPF no formato
**`xxx.xxx.xxx-xx`** e retorna `"CPF válido"` ou `"CPF inválido"`.

Um CPF é **válido** quando passa pelas **três** verificações abaixo.

**1. Formato.** O texto tem exatamente **14 caracteres**, com `.` nas posições
`3` e `7`, `-` na posição `11` e **dígitos** em todas as outras posições.

```
posição: 0 1 2 3 4 5 6 7 8 9 10 11 12 13
         5 2 9 . 9 8 2 . 2 4 7  -  2  5
```

**2. Dígitos repetidos.** CPFs com os 11 dígitos iguais (`111.111.111-11`,
`000.000.000-00`...) são **inválidos**.

**3. Dígitos verificadores.** Os dois últimos dígitos são calculados a partir
dos nove primeiros. Exemplo com `529.982.247-25`:

*Primeiro dígito verificador:* multiplique os 9 primeiros dígitos pelos pesos
`10, 9, 8, 7, 6, 5, 4, 3, 2` e some:

```
dígitos:  5   2   9   9   8   2   2   4   7
pesos:   10   9   8   7   6   5   4   3   2
         50 + 18 + 72 + 63 + 48 + 10 + 8 + 12 + 14 = 295
```

Calcule o resto da divisão por 11: `295 % 11 = 9`.

- Se o resto for **menor que 2**, o dígito é `0`;
- senão, o dígito é `11 - resto` → `11 - 9 = 2` ✔ (bate com o 10º dígito).

*Segundo dígito verificador:* faça o mesmo com os **10** primeiros dígitos
(incluindo o primeiro verificador) e os pesos `11, 10, 9, 8, 7, 6, 5, 4, 3, 2`:

```
dígitos:  5   2   9   9   8   2   2   4   7   2
pesos:   11  10   9   8   7   6   5   4   3   2
         55 + 20 + 81 + 72 + 56 + 12 + 10 + 16 + 21 + 4 = 347
```

Calcule o resto da divisão por 11: `347 % 11 = 6`.

- Se o resto for **menor que 2**, o dígito é `0`;
- senão, o dígito é `11 - resto` → `11 - 6 = 5` ✔ (bate com o 11º dígito).

Os dois dígitos verificadores bateram: CPF válido!

| Chamada                          | Retorno          |
|----------------------------------|------------------|
| `validar_cpf("529.982.247-25")`  | `"CPF válido"`   |
| `validar_cpf("529.982.247-26")`  | `"CPF inválido"` |
| `validar_cpf("52998224725")`     | `"CPF inválido"` |
| `validar_cpf("111.111.111-11")`  | `"CPF inválido"` |

> Dica: depois de validar o formato, use `replace()` para tirar os pontos e o
> hífen: `digitos = cpf.replace(".", "").replace("-", "")` deixa uma string só
> com os 11 dígitos (`"52998224725"`). Cada `digitos[i]` é um **caractere**
> (`'5'`), então converta com `int(digitos[i])` antes de multiplicar pelo peso.
> Sem o `int()`, `'5' * 10` repete o texto (`'5555555555'`) em vez de dar `50`.

---

## Critérios de avaliação

Cada questão é avaliada por testes automatizados que rodam após o seu envio
(você não tem acesso a eles diretamente). A nota é proporcional ao número de
testes que passam dentro de cada questão (25 pts cada).

Além da correção automática, o professor pode revisar o código fonte para
verificar boas práticas e o uso correto dos recursos de string.

---

*Bons estudos!* 
