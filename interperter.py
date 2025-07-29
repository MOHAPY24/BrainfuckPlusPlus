import random as rn
import time as tm
import math
import os
import sys

file_extensions = [".bfpp", ".bfa"]
tape = [0] * 500
pointer = 0
code = ""
variables = {}


if file_extensions[0] in sys.argv[1] or file_extensions[1] in sys.argv[1]:
    with open(sys.argv[1], "r") as fl:
        print(sys.argv[1])
        content = fl.read()
        global comment_mode
        comment_mode = False
        content = content.strip()
        code = content
        for line in code:
            line.strip()
            if "$" in line:
                comment_mode = True
                continue
            if "/" in line:
                comment_mode = False
            if ">" in line:
                if comment_mode == True:
                    continue
                else:
                    pointer += 1
            if "<" in line:
                if comment_mode == True:
                    continue
                else:
                    pointer -= 1
            if "." in line:
                if comment_mode == True:
                    continue
                else:
                    print(tape[pointer])
            if "+" in line:
                if comment_mode == True:
                    continue
                else:
                    tape[pointer] += 1
            if "-" in line:
                if comment_mode == True:
                    continue
                else:
                    tape[pointer] -= 1
            if "@" in line:
                if comment_mode == True:
                    continue
                else:
                    print(tape)
                    tape.clear()
                    tape = [""] * 250
            if "," in line:
                if comment_mode == True:
                    continue
                else:
                    quit()
            if "," not in code:
                raise Exception("SyntaxError: file closer , not found at EOF")
            if "'" in line:
                if comment_mode == True:
                    continue
                else:
                    if tape[0] > 1:
                        Exception("RuntimeError: Cell 0 has information while trying to use function '")
                    else:
                        save = tape[pointer]
                        pointer = 0
                        tape[pointer] = save
            if "|" in line:
                if comment_mode == True:
                    continue
                else:
                    global savepoint
                    global saveval
                    saveval = tape[pointer] 
            if "%" in line: 
                if comment_mode == True:
                    continue
                else:
                    tape[pointer] = saveval


            if "#" in line:
                if comment_mode == True:
                    continue
                else:
                    save = tape[pointer - 1]
                    tape[pointer] = save
            
            if "*" in line:
                if comment_mode == True:
                    continue
                else:
                    tape[pointer] = tape[pointer] * tape[pointer]

else:
    Exception("RuntimeError: No file found.")