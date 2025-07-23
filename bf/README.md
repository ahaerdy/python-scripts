# Introdução à Linguagem Brainfuck

Brainfuck é uma linguagem de programação esotérica criada por Urban Müller em 1993. Seu objetivo é ser minimalista, com apenas 8 comandos. Apesar de sua simplicidade, é Turing completa — ou seja, capaz de expressar qualquer algoritmo.

# Sintaxe: Os 8 Comandos da Linguagem

Brainfuck opera sobre uma "fita" (array) de células (valores inteiros de 0 a 255), um ponteiro de posição e um conjunto mínimo de instruções:

| Comando | Significado                                                              |
| ------- | ------------------------------------------------------------------------ |
| `>`     | Move o ponteiro para a **direita**                                       |
| `<`     | Move o ponteiro para a **esquerda**                                      |
| `+`     | Incrementa o valor da **célula atual**                                   |
| `-`     | Decrementa o valor da **célula atual**                                   |
| `.`     | Imprime o **caractere ASCII** da célula atual                            |
| `,`     | Lê um caractere da entrada e armazena na célula atual                    |
| `[`     | Início de um **loop**: se o valor da célula atual for 0, pula até o `]`  |
| `]`     | Fim do loop: se o valor da célula atual for diferente de 0, volta ao `[` |

# Como o Interpretador Funciona (Explicação do Script em Python)

Aqui está o funcionamento passo a passo do script [bf.py](https://github.com/ahaerdy/python-scripts/blob/main/bf/bf.py):

## 1. Incicialização

```
tape = [0] * 30000
ptr = 0
i = 0
loop_stack = []

```

- Cria uma "fita" com 30.000 células (como um array de memória).
- O ponteiro ptr começa na primeira célula.
- A variável i percorre o código Brainfuck.
- A loop_stack guarda as posições de colchetes [ para controle de loops aninhados.

## 2. Interpretação comando a comando

```
while i < len(code):
    command = code[i]
```

A cada iteração, o script analisa um caractere do código Brainfuck.

## 3. Comandos principais

> e < → movem o ponteiro

