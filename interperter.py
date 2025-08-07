import random as rn
import time as tm
import math
import os
import sys

file_extensions = [".bfpp", ".bfa"]
tape = [0] * 3000
pointer = 0
code = ""
variables = {}
ver = 1.1.1


if file_extensions[0] in sys.argv[1] or file_extensions[1] in sys.argv[1]:
    with open(sys.argv[1], "r") as fl:
        print(sys.argv[1] + f", version {ver}")
        content = fl.read()
        global comment_mode
        comment_mode = False
        content = content.strip()
        code = content
        pc = 0
        loop_stack = []

        def bfpp_gen(text):
            out = ""
            for char in text:
                out += "+" * ord(char) + ".>"
            return out[:-1] + ","


        for line in code:
            line = line.strip()

            if "$" in line:
                comment_mode = True
                continue
            elif "/" in line:
                comment_mode = False
            elif ">" in line:
                if comment_mode == True:
                    continue
                else:
                    pointer += 1
            elif "<" in line:
                if comment_mode == True:
                    continue
                else:
                    pointer -= 1
            elif "." in line:
                if comment_mode == True:
                    continue
                else:
                    print(chr(tape[pointer]), end='')
            elif "+" in line:
                if comment_mode == True:
                    continue
                else:
                    tape[pointer] += 1
            elif "-" in line:
                if comment_mode == True:
                    continue
                else:
                    tape[pointer] -= 1
            elif "@" in line:
                if comment_mode == True:
                    continue
                else:
                    print(tape)
            elif "," in line:
                if comment_mode == True:
                    continue
                else:
                    break
            elif "," not in code:
                raise SyntaxError("SyntaxError: file closer , not found at EOF")
            elif "'" in line:
                if comment_mode == True:
                    continue
                else:
                    if tape[0] > 1:
                        raise RuntimeError("RuntimeError: Cell 0 has information while trying to use function '")
                    else:
                        save = tape[pointer]
                        pointer = 0
                        tape[pointer] = save
            elif "|" in line:
                if comment_mode == True:
                    continue
                else:
                    global savepoint
                    global saveval
                    saveval = tape[pointer] 
            elif "%" in line: 
                if comment_mode == True:
                    continue
                else:
                    tape[pointer] += saveval
            elif "!" in line:
                if comment_mode == True:
                    continue
                else:
                    tape[pointer] = 0

            elif "?" in line:
                if comment_mode == True:
                    continue
                else:
                    tape.clear()
                    tape[0] * 3000

            elif "_" in line:
                continue

            elif "^" in line:
                if comment_mode == True:
                    continue
                else:
                    i = input(": ")
                    if int(i) is int:
                        tape[pointer] += i
                    else:
                        raise ValueError(f"Argument {i} is not a valid inttype.")

            elif "#" in line:
                if comment_mode == True:
                    continue
                else:
                    save = tape[pointer - 1]
                    tape[pointer] += save
            
            elif "*" in line:
                if comment_mode == True:
                    continue
                else:
                    tape[pointer] = tape[pointer] * tape[pointer]

            elif ":" in line:
                if comment_mode == True:
                    print(tape[pointer])

            elif "=" in line:
                if comment_mode == True:
                    tape[pointer] += tape[pointer + 1]

            elif pointer > 3000:
                raise MemoryError("Pointer has exceeded tape maximum size.")

            else:
               raise SyntaxError(f"Character {line} is not defined or a valid argument.")




else:
    Exception("RuntimeError: No file found.")
