# brainfuck_interpreter_v2.py

def interpret_brainfuck_verbose(code):
    tape = [0] * 1000
    ptr = 0
    i = 0
    loop_stack = []
    output = ""

    with open("saida.txt", "w") as debug_file:

        def print_debug(i, command, ptr, tape, output):
            tape_window = tape[ptr-3:ptr] + ['[' + str(tape[ptr]) + ']'] + tape[ptr+1:ptr+4]
            tape_str = ' '.join(str(cell).rjust(3) if isinstance(cell, int) else cell for cell in tape_window)
            debug_file.write(f"Cmd #{i:<4} '{command}'\tPtr: {ptr:<5}\tTape: {tape_str}\tOutput: {output}\n")

        while i < len(code):
            command = code[i]
            print_debug(i, command, ptr, tape, output)

            if command == '>':
                ptr += 1
                if ptr >= len(tape):
                    ptr = 0

            elif command == '<':
                ptr -= 1
                if ptr < 0:
                    ptr = len(tape) - 1

            elif command == '+':
                tape[ptr] = (tape[ptr] + 1) % 256

            elif command == '-':
                tape[ptr] = (tape[ptr] - 1) % 256

            elif command == '.':
                output += chr(tape[ptr])
                print_debug(i, command, ptr, tape, output)

            elif command == ',':
                try:
                    user_input = input("Entrada: ")[0]
                    tape[ptr] = ord(user_input)
                except IndexError:
                    tape[ptr] = 0

            elif command == '[':
                if tape[ptr] == 0:
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
                    i = loop_stack[-1]
                    continue
                else:
                    loop_stack.pop()

            i += 1

    print(f"{output}\n")


# ===== EXECUÇÃO DIRETA =====
if __name__ == '__main__':
    print("Digite o código Brainfuck:")
    codigo = input(">>> ")
    print("\nSaída:\n")
    interpret_brainfuck_verbose(codigo)
