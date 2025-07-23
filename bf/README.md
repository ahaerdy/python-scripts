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



