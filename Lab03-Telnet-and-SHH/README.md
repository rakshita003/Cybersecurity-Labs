
# Lab 03 - Telnet & SSH: Secure & Insecure Remote Access

## 📖 Overview
This lab explores **Telnet and SSH**, two protocols used for remote server access. 
It demonstrates:
- **Telnet**: Insecure remote access with plaintext password transmission.
- **SSH**: Secure remote access using authentication keys and encryption.
- **Network traffic analysis**: Observing plaintext passwords in Telnet.

---

## ⚙️ **Tools & Commands Used**
| Tool/Command   | Description |
|---------------|------------|
| `ssh-keygen -t rsa` | Generates RSA authentication keys for SSH |
| `ssh-copy-id -i ~/.ssh/id_rsa.pub` | Copies SSH public key to the server |
| `ssh <server-ip>` | Connects securely to the server |
| `telnet <server-ip>` | Connects to the server using Telnet |
| `tcpdump -i eth0 -X tcp` | Captures network traffic to analyze plaintext passwords |
| `cat filetoview.txt` | Displays a file from the server |
| `exit` | Closes the connection |

---

## 📂 **Lab Tasks**
### 1️⃣ **SSH Authentication Setup**
- Generated SSH keys on the client:
  ```bash
  ssh-keygen -t rsa
  ```
- Copied the public key to the server:
  ```bash
  ssh-copy-id -i ~/.ssh/id_rsa.pub 172.20.0.3
  ```
- **Key Benefit:** SSH authentication avoids password-based logins.

### 2️⃣ **Secure SSH Connection**
- Connected securely to the server:
  ```bash
  ssh 172.20.0.3
  ```
- Displayed a file:
  ```bash
  cat filetoview.txt
  ```
- **Screenshot in the attached PDF.**

### 3️⃣ **Telnet - Insecure Connection**
- Identified the server IP address:
  ```bash
  ifconfig
  ```
- Logged in via Telnet:
  ```bash
  telnet 172.20.0.3
  ```
- Viewed a file:
  ```bash
  cat filetoview.txt
  ```
- **Key Issue:** Telnet transmits passwords in plaintext.

### 4️⃣ **Intercepting Plaintext Passwords**
- Captured network traffic using `tcpdump`:
  ```bash
  sudo tcpdump -i eth0 -X tcp
  ```
- Observed **plaintext** passwords from Telnet connections.
- **Screenshot in the attached PDF.**

### 5️⃣ **Protecting Communications with SSH**
- Verified that SSH encrypts traffic:
  ```bash
  ssh 172.20.0.3
  ```
- Used `tcpdump` again—no plaintext credentials visible.

---

## 🎯 **Key Takeaways**
✅ **Telnet is insecure** – passwords are transmitted in plaintext.  
✅ **SSH provides secure authentication & encryption**.  
✅ **Packet sniffing** can expose Telnet credentials but not SSH.  
✅ **Using SSH keys improves security** over password-based authentication.  

---

## 🛠 **Additional Resources**
- [Why Telnet is Insecure](https://www.techtarget.com/whatis/definition/Telnet)
- [SSH Key Authentication Guide](https://www.ssh.com/academy/ssh/keygen)
- [How `tcpdump` Works](https://www.tcpdump.org/manpages/tcpdump.1.html)

---
 Screenshots for this lab are included in the attached PDF.
```

