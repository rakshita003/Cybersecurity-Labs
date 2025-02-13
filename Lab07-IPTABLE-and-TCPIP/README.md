
# Lab 07 - IPTables & TCP/IP Attacks  

## 📖 Overview  
- Configuring IPTables to allow only SSH and HTTP traffic  
- Scanning open ports on a target system using Nmap  
- Understanding TCP-based attacks: SYN Flood, TCP Reset, and TCP Session Hijacking  

---

## ⚙️ **Tools & Commands Used**  
| Tool/Command   | Description |
|---------------|------------|
| `iptables` | Firewall utility for managing packet filtering |
| `iptables -A FORWARD -p tcp --dport 22 -j ACCEPT` | Allows SSH traffic |
| `iptables -A FORWARD -p tcp --dport 80 -j ACCEPT` | Allows HTTP traffic |
| `iptables -A FORWARD -j DROP` | Blocks all other forwarded traffic |
| `nmap -n <IP>` | Scans open ports on a target machine |
| `hping3` | Tool for crafting TCP packets and launching attacks |
| `ettercap` | Used for ARP poisoning & TCP session hijacking |
| `tcpdump` | Captures network traffic for analysis |

---

## 📂 **Lab Tasks**  

### 1️⃣ **Configuring a Firewall with IPTables**  
- Set up IPTables to allow only SSH (22) and HTTP (80)  
- Verified firewall rules by scanning the server using Nmap  

### 2️⃣ **TCP/IP Attacks & Security Considerations**  

#### 🔹 **SYN Flood Attack**  
- Sends numerous SYN packets to exhaust server connections  
- Command:  
  ```bash
  hping3 -S --flood -p 80 172.25.0.3
  ```
- Prevention: Rate limiting and SYN cookies  

#### 🔹 **TCP Reset Attack**  
- Sends forged RST packets to terminate active TCP sessions  
- Command:  
  ```bash
  hping3 -R -p 22 172.25.0.3
  ```
- Prevention: Firewall rules and TCP filtering  

#### 🔹 **TCP Session Hijacking**  
- Intercepts and manipulates an existing TCP session  
- Commands:  
  ```bash
  ettercap -T -M arp /<target_IP>/ /<gateway_IP>/
  tcpdump -i eth0 -A port 23
  ```
- Prevention: Use encrypted protocols, ARP spoofing detection, and firewall rules  

---

## 🎯 **Key Takeaways**  
- IPTables controls access to network services  
- Firewalls should block unnecessary ports  
- TCP attacks exploit insecure configurations  
- Security best practices include using SSH instead of Telnet, enabling SYN cookies, and blocking unauthorized traffic  

---

## 🛠 **Additional Resources**  
- [IPTables Firewall Guide](https://www.digitalocean.com/community/tutorials/iptables-essentials-common-firewall-rules-and-commands)  
- [Understanding SYN Flood Attacks](https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack/)  
- [How TCP Session Hijacking Works](https://owasp.org/www-community/attacks/Session_hijacking_attack)  
```
