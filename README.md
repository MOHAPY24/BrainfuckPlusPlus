# 🌌 NOVAXIS — The New Axis of Esoteric Programming

                                                      

## 💡 What is Novaxis?

Novaxis is a **modern esoteric language** evolved from Brainfuck.  
It’s built for **control, precision, and raw minimalism** — where every symbol has weight and the tape is your entire universe.

The design goal is simple:  
> **Keep the soul of Brainfuck, but give it a 21st-century upgrade.**

That means:
- Extended instruction set.
- Cleaner control flow with direct cell jumps.
- Modern syntax rules for a structured feel.
- Infinite tape by design.

---

## ⚙️ Core Features

- **Direct Cell Jumps** — Use `{n` to jump to any cell instantly if the current cell isn’t zero.
- **Infinite Memory Tape** — Move as far left or right as needed.
- **Extended Arithmetic** — Square, add from neighbors, store and recall values.
- **Readable, Commentable Code** — `$.../` lets you annotate freely.
- **Structured File Format** — Must start with `&` and end with `,` for clarity and parsing safety.

---

## 🔠 Instruction Set

| Symbol | Description |
|--------|-------------|
| `+` | Increment current cell value |
| `-` | Decrement current cell value |
| `>` | Move pointer right |
| `<` | Move pointer left |
| `.` | Print current cell as ASCII |
| `@` | Print entire tape contents |
| `,` | End program (required) |
| ` straight line symbol ` | Save current cell value |
| `%` | Load saved value into current cell |
| `*` | Square current cell value |
| `#` | Add value from cell before into current cell |
| `'` | Move current cell value to cell 0 & jump pointer to cell 0 |
| `=` | Add value from cell ahead into current cell |
| `$.../` | Block comment |
| `^` | Take integer input & add to current cell |
| `:` | Print raw numeric value of current cell |
| `{n` | Jump to cell `n` if current cell is non-zero |
| `!` | Clear current cell |
| `?` | Clear all cells |
| `&` | Start of file marker |

---

## 📂 File Format

**Extensions:**  
`.nva`, `.nv`, `.nova`

**Structure Rules:**
- Program **must** start with `&`
- Program **must** end with `,`
- Code after `,` will be ignored
- Whitespace and newlines are ignored

---

## 🚀 Example Programs

**Hello World**
```nva
&++++++++++*++++.---.++++++..+++.>++++++*----.>++++++++++*+++++++++++++++++++.--------.+++.----------.--------.",
```
"Hi"
```
&++++++++++*++++.+.",
```
Useless Pointer Chaos
```
&+++-*>++:*{1>{2:++*>{1:",
```

---

## 🔧 Running Novaxis

```
git clone https://github.com/MOHAPY24/novaxis
cd novaxis
python3 interpreter.py urfile.nova
```

---

## 🧠 Philosophy

Novaxis keeps the low-level mental challenge of Brainfuck but removes arbitrary limitations.
It’s not about being the shortest — it’s about complete mastery over your tape.

If you want a pure, modern esolang experience that rewards skill and planning,
this is the new axis.


---

## 📜 License

MIT — Fork, modify, experiment, share.


---

### Novaxis — Where the tape becomes the universe.

