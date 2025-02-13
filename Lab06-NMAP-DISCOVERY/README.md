
# Lab 06 - Nmap Network Discovery  

## 📖 Overview  
This lab explores **Nmap**, a powerful network scanning tool, to:  
- Discover **active hosts** on a network  
- Identify **open and closed ports**  
- Perform **service discovery** on a given machine  
- Use **SSH to connect to a discovered host**  

---

## ⚙️ **Tools & Commands Used**  
| Tool/Command   | Description |
|---------------|------------|
| `man nmap` | Displays the Nmap manual |
| `nmap -sP <network>` | Scans the network for active hosts |
| `nmap -o <port-range> <IP>` | Scans a specific range of ports |
| `ssh -p <port> <IP>` | Connects to a remote machine using SSH |
| `ls` | Lists files in a directory |
| `cat <filename>` | Displays the contents of a file |
| `checkwork` | Verifies lab completion |
| `stoplab` | Ends the lab session |

---

## 📂 **Lab Tasks**  

### 1️⃣ **Exploring Nmap Commands**  
- Opened the **Nmap manual** to view available options:  
  ```bash
  man nmap
  ```
- **Screenshot in the attached PDF.**  

---

### 2️⃣ **Discovering Active Hosts on the Network**  
- Used Nmap to scan the network for **active IP addresses**:  
  ```bash
  nmap -sP 172.24.0.0/24
  ```
- Identified a host with the IP address **172.25.0.2**.  

---

### 3️⃣ **Scanning for Open Ports**  
- Scanned ports from **2000 to 3000** on the target machine:  
  ```bash
  sudo nmap -o 2000-3000 172.25.0.5
  ```
- Found **1000 closed ports** and **one open port (2115)**.  
- **Inference:** Port **2115** is likely being used for SSH access.  

---

### 4️⃣ **Connecting to the Target Machine via SSH**  
- Established an SSH connection using the discovered port:  
  ```bash
  ssh -p 2115 user@172.25.0.5
  ```
- Listed available files:  
  ```bash
  ls
  ```
- Viewed a file’s content:  
  ```bash
  cat <filename>
  ```
- **Screenshot in the attached PDF.**  


---

## 🎯 **Key Takeaways**  
✅ **Nmap efficiently discovers active devices & open ports**.  
✅ **SSH allows secure access to discovered hosts**.  
✅ **Scanning for open ports helps identify vulnerable services**.  
✅ **Proper network security measures can mitigate unauthorized scanning attempts**.  

---

## 🛠 **Additional Resources**  
- [Nmap Cheat Sheet](https://hackertarget.com/nmap-cheatsheet/)  
- [How to Scan Networks with Nmap](https://nmap.org/book/man.html)  
- [Understanding Open & Closed Ports](https://www.varonis.com/blog/open-ports-security)  
