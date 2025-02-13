
# Lab 05 - Set-UID & Environment Variables  

## 📖 Overview  
This lab explores **how environment variables affect system behavior** and **the security implications of Set-UID programs**.  
It covers:  
- **Manipulating environment variables** (`printenv`, `export`, `unset`)  
- **How environment variables are inherited** by child and parent processes  
- **Interaction between environment variables and system functions** (`execve()`, `system()`)  
- **Security risks of Set-UID programs**  
- **Privilege escalation vulnerabilities using `LD_PRELOAD`**  

---

## ⚙️ **Tools & Commands Used**  
| Tool/Command   | Description |
|---------------|------------|
| `printenv` / `env` | Prints all environment variables |
| `export VAR=value` | Sets an environment variable |
| `unset VAR` | Unsets an environment variable |
| `gcc` | Compiles C programs (`printenv.c`, `execve.c`, `printall.c`) |
| `execve()` | Executes a program with environment variables |
| `system()` | Executes shell commands within a C program |
| `setuid()` | Changes the effective user ID of a process |
| `sudo chown root:root a.out` | Changes ownership of a file to root |
| `sudo chmod a+s a.out` | Makes a file a Set-UID program |
| `export PATH=~/:$PATH` | Modifies the execution path for security testing |
| `export LD_PRELOAD=<library>` | Loads a custom shared library before any other |

---

## 📂 **Lab Tasks**  

### 1️⃣ **Manipulating Environment Variables**  
- Displayed current environment variables:  
  ```bash
  printenv
  env
  ```
- Set and unset variables:  
  ```bash
  export TEST_VAR="Cybersecurity"
  unset TEST_VAR
  ```
- **Screenshot in the attached PDF.**  

---

### 2️⃣ **Inheritance of Environment Variables**  
- Compiled and ran `printenv.c` to examine inheritance.  
- Modified `printenv()` behavior in **child vs. parent process**.  
- Saved output to files and compared differences using `diff`:  
  ```bash
  diff parent_output.txt child_output.txt
  ```
- **Observation:** Child processes do not always inherit all variables from parents.  

---

### 3️⃣ **Environment Variables & `execve()`**  
- Compiled and ran `execve.c` to examine its effect on environment variables.  
- Modified how `execve()` calls `/usr/bin/env`:  
  ```c
  execve("/usr/bin/env", argv, environ);
  ```
- Observed that `execve()` inherits the caller’s environment variables.  

---

### 4️⃣ **Environment Variables & `system()`**  
- Examined how `system()` calls `/bin/sh`:  
  ```c
  system("echo $PATH");
  ```
- Noted that `system()` **inherits the environment variables**, which can be exploited for privilege escalation.  

---

### 5️⃣ **Understanding Set-UID & Security Risks**  
- **Compiled & set up a Set-UID program (`printall.c`)**:  
  ```bash
  sudo chown root:root a.out
  sudo chmod a+s a.out
  ```
- Ran the program as a normal user and observed **privilege escalation** risks.  

---

### 6️⃣ **Exploiting Set-UID & `system()`**  
- Modified `PATH` to execute a malicious script before legitimate binaries:  
  ```bash
  export PATH=~/:$PATH
  ```
- Observed how this **tricked Set-UID programs into running unintended commands**.  

---

### 7️⃣ **Exploiting `LD_PRELOAD` in Set-UID Programs**  
- Ran `myprog` normally and as a Set-UID program.  
- Exploited `LD_PRELOAD` to inject malicious shared libraries:  
  ```bash
  export LD_PRELOAD=/path/to/malicious.so
  ```
- Observed how this could **bypass security and execute arbitrary code**.  

---

### 8️⃣ **Understanding Capability Leaking**  
- Explored how `setuid()` prevents privilege retention:  
  ```c
  setuid(1000); // Drops privileges to a normal user
  ```
- **Key Insight:** Set-UID programs should explicitly drop privileges to prevent abuse.  

---

## 🎯 **Key Takeaways**  
✅ **Environment variables can affect program execution & security**.  
✅ **Set-UID programs run with elevated privileges and must be secured**.  
✅ **Modifying `PATH` or using `LD_PRELOAD` can exploit poorly secured programs**.  
✅ **Proper use of `setuid()` prevents privilege retention vulnerabilities**.  

---

## 🛠 **Additional Resources**  
- [Understanding Set-UID in Unix](https://www.redhat.com/sysadmin/setuid-linux)  
- [Security Risks of Environment Variables](https://owasp.org/www-community/vulnerabilities/Environment_Variable_Injection)  
- [How `LD_PRELOAD` Can Be Exploited](https://blog.hartleybrody.com/ld-preload/)  

---

Screenshots for this lab are included in the attached PDF.
```

