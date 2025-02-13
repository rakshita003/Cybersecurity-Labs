
# Lab 09 - Format Strings & Buffer Overflow

📖 **Overview**  
In this lab, we explored two common vulnerabilities in software: **Format Strings** and **Buffer Overflow**. Format string vulnerabilities allow an attacker to manipulate data by controlling the format specifiers in input, leading to information disclosure or modification. Buffer overflow exploits occur when data overflows into adjacent memory, potentially allowing for control of execution flow.

⚙️ **Tools & Commands Used**  
| **Tool/Command**                             | **Description**                                                               |
|---------------------------------------------|-------------------------------------------------------------------------------|
| `sudo sysctl -w kernel.randomize_va_space=2` | Enable Address Space Layout Randomization (ASLR)                              |
| `gcc -z execstack -fno-stack-protector -o vul_prog vul_prog.c` | Compile vulnerable program                                                     |
| `cat vul_prog.c`                            | Display vulnerable program code                                                |
| `./vul_prog`                                | Run the compiled vulnerable program                                            |
| `python -c 'print("A"*1000)' > badfile`      | Create a "badfile" for buffer overflow test                                    |
| `chmod +x vul_prog`                         | Make the program executable                                                    |

📂 **Lab Tasks**

### 1️⃣ **Format Strings Exploitation**  
- **Step 1**: Enable ASLR:
  ```bash
  sudo sysctl -w kernel.randomize_va_space=2
  ```
- **Step 2**: Compile vulnerable code:
  ```bash
  gcc -z execstack -fno-stack-protector -o vul_prog vul_prog.c
  ```
- **Step 3**: Exploit the Format String vulnerability to print a secret value and its location.
- **Step 4**: Modify the value at a specific memory location (e.g., `0x4a`).

### 2️⃣ **Buffer Overflow Exploitation**  
- **Step 1**: Disable ASLR (Set randomizer to 0):
  ```bash
  sudo sysctl -w kernel.randomize_va_space=0
  ```
- **Step 2**: Compile vulnerable code:
  ```bash
  gcc -z execstack -fno-stack-protector -o vul_prog vul_prog.c
  ```
- **Step 3**: Change file permissions:
  ```bash
  chmod +x vul_prog
  ```
- **Step 4**: Create a "badfile" to overflow the buffer:
  ```bash
  python -c 'print("A"*1000)' > badfile
  ```
- **Step 5**: Run the vulnerable program with the badfile.

🎯 **Key Takeaways**
- **Format String Vulnerabilities**: Can lead to memory corruption and information leakage if unchecked. By manipulating format specifiers, attackers can gain access to sensitive data or control execution.
- **Buffer Overflow Vulnerabilities**: Exploited by overflowing a buffer with more data than it can handle, causing adjacent memory corruption and allowing attackers to inject malicious code.
- **Protection**: Use techniques like ASLR, stack canaries, and proper bounds checking to mitigate these vulnerabilities.

🛠 **Additional Resources**
- [Format String Exploitation](https://www.exploit-db.com/docs/12156)
- [Buffer Overflow Protection](https://www.securityfocus.com/infocus/1760)
