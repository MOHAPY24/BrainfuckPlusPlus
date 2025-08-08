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
ver = "1.1.2"


if file_extensions[0] in sys.argv[1] or file_extensions[1] in sys.argv[1]:
    with open(sys.argv[1], "r") as fl:
        print(sys.argv[1] + f", version {ver}")
        code = fl.read()
        global comment_mode
        comment_mode = False
        code = code.strip()


        def bfpp_gen(text):
            out = "&"
            for char in text:
               out += "+" * ord(char) + ".>"
               return out[:-1] + ","

        if code.startswith("&") != True:
            raise SyntaxError("SOF identifier '&' not located in file.")

        #with open(sys.argv[1], "w") as f:
            #f.write(bfpp_gen(input(": ")))
            #f.close()

        for line in code:

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
                    print(chr(tape[pointer]))
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
                raise SyntaxError("file closer , not found at EOF")
            elif "'" in line:
                if comment_mode == True:
                    continue
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

            elif line.isspace():
                continue

            elif "?" in line:
                if comment_mode == True:
                    continue
                else:
                    tape.clear()
                    tape = [0] * 3000

            elif "_" in line:
                continue

            elif "^" in line:
                if comment_mode == True:
                    continue
                else:
                    i = int(input(": "))
                    tape[pointer] += i
                    continue
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
                    continue
                else:
                    print(tape[pointer])

            elif "=" in line:
                if comment_mode == True:
                    tape[pointer] += tape[pointer + 1]

            elif pointer > 2999:
                raise MemoryError("Pointer has exceeded tape maximum size.")

            else:
                if "&" in line:
                    continue
                else:
                    raise SyntaxError(f"Character {line} is not defined or a valid argument.")




elif sys.argv[1] is not file_extensions[1] or sys.argv[1] is not file_extensions[0]:
    raise RuntimeError("No file found.")