import random as rn
import time as tm
import math
import os
import sys

file_extensions = [".nv", ".nva", ".nova"]
tape = [0] 
pointer = 0
code = ""
loop_stack = []
variables = {}
ver = "1.1.3"
pc = 0


if file_extensions[0] in sys.argv[1] or file_extensions[1] in sys.argv[1]:
    with open(sys.argv[1], "r") as fl:
        print(sys.argv[1] + f", novaxis version {ver}")
        code = fl.read()
        global comment_mode
        global saveval
        saveval = 0
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
                    tape.append(0)
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
                    tape.append(0)
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
            elif "'" in line:
                if comment_mode == True:
                    continue
                else:
                    save = tape[pointer]
                    pointer = 0
                    tape[pointer] = save


            elif "," in line:
                if comment_mode == True:
                    continue
                else:
                    x = 0
                    for i in tape:
                        if i == 0:
                            x += 1
                    if x > 3:
                        raise MemoryError("over 3 inactive cells remain at EOF, excessive garbage load")
                    else:
                        print("exitied with 0 errors.")
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
                    saveval = tape[pointer]
                    tape.append(0)

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
                    tape = [0] * len(tape)

            elif "_" in line:
                continue

            elif "^" in line:
                if comment_mode == True:
                    continue
                else:
                    i = int(input(": "))
                    tape[pointer] += i
                    tape.append(0)
                    continue
            elif "#" in line:
                if comment_mode == True:
                    continue
                else:
                    save = tape[pointer - 1]
                    tape[pointer] += save
                    tape.append(0)
            
            elif "*" in line:
                if comment_mode == True:
                    continue
                else:
                    tape[pointer] = tape[pointer] * tape[pointer]
                    tape.append(0)

            elif ":" in line:
                if comment_mode == True:
                    continue
                else:
                    print(tape[pointer])

            elif "=" in line:
                if comment_mode == True:
                    tape[pointer] += tape[pointer + 1]



            elif "{" in line:
                cll = int(code[code.index(line) + 1])
                if tape[pointer] == 0:
                    if cll > len(tape):
                        while cll > len(tape):
                            tape.append(0)

                    tape.append(0)
                    pointer = cll

            else:
                if "&" in line:
                    continue

                elif isinstance(int(line), int) == True:
                    continue

                else:
                    raise SyntaxError(f"Character {line} is not defined or a valid argument.")
            




elif sys.argv[1] is not file_extensions[1] or sys.argv[1] is not file_extensions[0]:
    raise RuntimeError("No file found.")