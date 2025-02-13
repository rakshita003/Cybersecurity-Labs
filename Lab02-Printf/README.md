
# Lab 02 - Printf Vulnerabilities & Memory Exploration

## 📖 Overview
This lab focuses on the **printf function** and how it interacts with memory, exploring:
- How **format specifiers** reference memory
- Understanding **calling conventions** in `gdb`
- Examining the **stack** and **disassembly of printf**
- Identifying potential **security vulnerabilities** in format strings
- **Screenshots provided in the lab report.**
---

## ⚙️ **Tools & Commands Used**
| Tool/Command   | Description |
|---------------|------------|
| `labtainer printf` | Starts the lab environment |
| `vim printTest.c` | Opens the source code for review |
| `gdb printTest` | Debugging tool for analyzing the program |
| `mkit` | Compiles the C program |
| `nexti` | Steps through the program execution |
| `x/20xw $esp` | Examines the stack memory in hexadecimal |

---

## 📂 **Lab Tasks**
### 1️⃣ **Reviewing `printTest.c`**
- Opened the `printTest.c` program:
  ```bash
  vim printTest.c
  ```
- Observed how `printf` handles format specifiers and variable references.

### 2️⃣ **Compiling & Running `printTest.c`**
- Compiled the program:
  ```bash
  ./mkit
  ```
- Executed the program:
  ```bash
  ./printTest
  ```


### 3️⃣ **Analyzing `printf` with `gdb`**
- Loaded the program into `gdb`:
  ```bash
  gdb printTest
  ```
- Listed program instructions:
  ```bash
  list
  ```
- Set a breakpoint before the first `printf` statement:
  ```bash
  break <line_number>
  ```
- Started execution:
  ```bash
  run
  ```


### 4️⃣ **Exploring the Stack**
- Disassembled current instructions:
  ```bash
  display/i $pc
  ```
- Stepped through execution:
  ```bash
  nexti
  ```
- Examined 20 words on the stack:
  ```bash
  x/20xw $esp
  ```


### 5️⃣ **Testing User Input in Format Strings**
- Ran `printTest` with a format string attack:
  ```bash
  ./printTest
  ```
- Entered:
  ```
  AAAA%8x.%8x.%8x.%8x.%8x.%8x.%8x.%8x.%8x.%8x.
  ```
- Observed how user input manipulated memory.


### 6️⃣ **Checking Work**
- Verified lab completion:
  ```bash
  checkwork
  ```

---

## 🎯 **Key Takeaways**
✅ **Learned how `printf` interacts with memory**  
✅ **Examined calling conventions & stack operations**  
✅ **Identified format string vulnerabilities**  
✅ **Understood how attackers can exploit printf to leak memory**  

---

## 🛠 **Additional Resources**
- [Format String Vulnerabilities](https://owasp.org/www-community/attacks/Format_string_attack)
- [GDB Debugging Commands](https://sourceware.org/gdb/current/onlinedocs/gdb/)
- [Understanding Stack Frames](https://en.wikipedia.org/wiki/Call_stack)

---
