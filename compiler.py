import random as rn
import time as tm
import math
import os
import sys

ver = "1.1.3"
print(f"compiling file, '{sys.argv[1]}'")


with open(sys.argv[1], "r") as f:
	code = f.read()
	code = code.strip()
	compiled_code = "\n"
	if code.startswith("&") != True:
		raise SyntaxError("SOF Identifier '&' not found at SOF.")
	else:
		compiled_code += "tape = [0] * 3000 \npointer = 0 \n"
		compiled_code += f"\nprint(f'novaxis ver: {ver}')\n"
	if code.endswith(",") != True:
		raise SyntaxError("EOF Identifier ',' not found at EOF")
	compiled_code += f"code = '{code}'\n"


	for line in code:
		compiled_code += f"\nline = '{line}'\n"
		if "+" in line:
			compiled_code += "tape[pointer] += 1 \n"
		if "-" in line:
			compiled_code += "tape[pointer] -= 1 \n"
		if ">" in line:
			compiled_code += "pointer += 1 \n"
		if "<" in line:
			compiled_code += "pointer -= 1 \n"
		if "." in line:
			compiled_code += "\nprint(chr(tape[pointer]));\n"
		if "*" in line:
			compiled_code += "tape[pointer] = tape[pointer] * tape[pointer] \n"
		if ":" in line:
			compiled_code += "print(tape[pointer]); \n"
		if "|" in line:
			compiled_code += "a = tape[pointer] \n"
		if "%" in line:
			compiled_code += "tape[pointer] += a \n"
		if "$" in line:
			compiled_code += '\n"""'
		if "/" in line:
			compiled_code += '""" \n'
		if line.isalpha() == True:
			compiled_code += line + ""
		if "^" in line:
			compiled_code += "\ni = int(input(': '')) \ntape[pointer] += i \n"
		if "#" in line:
			compiled_code += "\nsave = tape[pointer - 1] \ntape[pointer] += save \n"
		if "," in line:
			compiled_code += "quit('executed with 0 errors.')"
		if "@" in line:
			compiled_code += "print(tape)"
		if "r" in line:
			compiled_code += "save = tape[pointer] \npointer = 0 \ntape[pointer] = rsave\n"
		if "!" in line:
			compiled_code += "tape[pointer] = 0 \n"
		if "?" in line:
			compiled_code += "tape = [0] * 3000 \n"
		if "_" in line:
			continue
		if "=" in line:
			compiled_code += "tape[pointer] += tape[pointer + 1] \n"
		if "{" in line:
			compiled_code += """
			\n
cll = int(code[code.index(line) + 1])
if tape[pointer] == 0:
    if cll > len(tape):
    	while cll > len(tape):
        	tape.append(0)
        	tape.append(0)
        	pointer = cll
\n
"""

with open("compiled.py", "w") as fl:
	fl.write(compiled_code)
	print("compiled with 0 errors")

