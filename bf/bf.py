# brainfuck_interpreter.py

def interpret_brainfuck(code):
    tape = [0] * 30000      # memória de 30.000 células, todas iniciadas em 0
    ptr = 0                 # ponteiro para a posição atual na fita
    i = 0                   # índice do comando atual no código
    loop_stack = []         # pilha para guardar posições de '['

    while i < len(code):
        command = code[i]

        if command == '>':
            ptr += 1
            if ptr >= len(tape):
                ptr = 0  # comportamento circular opcional

        elif command == '<':
            ptr -= 1
            if ptr < 0:
                ptr = len(tape) - 1  # comportamento circular opcional

        elif command == '+':
            tape[ptr] = (tape[ptr] + 1) % 256  # wrap-around de 0 a 255

        elif command == '-':
            tape[ptr] = (tape[ptr] - 1) % 256  # wrap-around de 0 a 255

        elif command == '.':
            print(chr(tape[ptr]), end='')

        elif command == ',':
            try:
                user_input = input("Entrada: ")[0]
                tape[ptr] = ord(user_input)
            except IndexError:
                tape[ptr] = 0  # se nada for digitado

        elif command == '[':
            if tape[ptr] == 0:
                # pula até o comando depois do ']'
                open_brackets = 1
                while open_brackets > 0:
                    i += 1
                    if i >= len(code):
                        raise SyntaxError("Loop '[' sem fechamento")
                    if code[i] == '[':
                        open_brackets += 1
                    elif code[i] == ']':
                        open_brackets -= 1
            else:
                loop_stack.append(i)

        elif command == ']':
            if tape[ptr] != 0:
                i = loop_stack[-1]  # volta para o começo do loop
            else:
                loop_stack.pop()

        i += 1

# ===== EXECUÇÃO DIRETA =====
if __name__ == '__main__':
    print("Digite o código Brainfuck:")
    codigo = input(">>> ")
    print("\nSaída do programa:\n")
    interpret_brainfuck(codigo)
    print("\n\n[Fim da execução]")

