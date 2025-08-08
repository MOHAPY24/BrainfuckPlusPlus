# 🧠 Brainfuck++ (BF++) Interpreter

A lightweight, modernized esolang interpreter for **Brainfuck++**, the chaotic-genius cousin of the classic Brainfuck. Designed for experimenters, masochists, and bored geniuses who want to bend the very rules of logic into tape-based ASCII spaghetti.

**Current Version:** `v1.1.2`  
**Interpreter Language:** Python 3  
**Tape Size:** 3000 cells  
**File Extensions Supported:** `.bfpp`, `.bfa`

---

## 💡 What is Brainfuck++?

BF++ is a low-level esoteric programming language with extended functionality over the classic Brainfuck. It’s not meant to be practical. It’s meant to be *fun*, *chaotic*, and surprisingly powerful if you hate yourself enough.

### 👾 BF++ 1.1.1-1.1.2 Adds:

- ASCII character printing via `.`
- Raw value printing via `:`
- Cell clearing, full tape wiping, and selective assignment
- Cell-saving & restoring
- Interactivity with user input (`^`)
- SOF Identifier `&`
- And more!

---

## 🔧 How to Use

```bash
python3 interpreter.py your_file.bfpp
```

Make sure your file ends with a `,` (end-of-file marker) and starts with a `&` (start-of-file marker) or the interpreter will yeet an error.


---

## 🧠 BF++ Syntax Cheatsheet

Symbol Function

"+" Increment current cell

"-" Decrement current cell

">" Move pointer right

"<" Move pointer left

"." Print ASCII of current cell

":" Print raw value of current cell

"," End the program

"@" Print entire tape (does not clear cells)

"!" Clear current cell

"?" Clear all cells

"%" Load saved value into current cell

"#" Copy value from previous cell into current

" ' " Move current cell’s value to cell 0 (unsafe)

"=" Copy value from next cell into current cell

"_" Null command (does nothing)

"&" Start the program

"^" Take integer input into current cell

"$ ... /" Comments



---

## 🚨 Error Handling

Errors are now handled professionally using Python’s built-in error types:

SyntaxError for missing EOF, SOF or incorrect syntax and markers

RuntimeError for improper cell manipulations

FileNotFoundError if no valid .bfpp file is found

IndexError if pointer tries to go out of bounds



---

📦 DevLog Highlights (v1.1.1-1.1.2)

✅ Added proper ASCII support

✅ Removed sassy legacy errors (RIP Despair++)

✅ Interactivity support with `^`

✅ Improved error handling

✅ Increased tape size to 3000 cells

✅ Added null `_`, input `^`, and nextval `=`

✅ added an SOF marker `&`



---

❗ Known Quirks

Still no loop support. It’s intentional for now.

Tape is 1-indexed for ASCII operations—don’t forget that 😤

Use only .bfpp or .bfa extensions or it’ll yell at you.



---

🧠 Example Program

Print Hello:

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
,


---

🤘 Created By

> 🧠 Momo (age 13 but smarter than half the devs on GitHub)
🧪 Author of Despair++, Leaf@Root, Custogotchi, and more
🎓 100% certified tape-based language enthusiast




---

📜 License

MIT License. Do whatever.


---

🌐 Final Thoughts

> You will basically never need this, but it exists.



Welcome to the BF++ Institute.
