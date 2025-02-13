# Lab 01 - Network & Routing Basics

## 📖 Overview
This lab introduces fundamental networking concepts such as:
- IP & MAC Address identification (`ip addr`)
- Address Resolution Protocol (ARP) (`arp -a`)
- TCP Packet Analysis using `tcpdump`
- Basic Routing concepts (`route -n` & `ifconfig`)
- Network Address Translation (NAT)
- Packet Forwarding & DNS Configuration

---

## ⚙️ **Tools & Commands Used**
| Tool/Command   | Description |
|---------------|------------|
| `ip addr` | Displays IP and MAC addresses |
| `arp -a` | Shows the ARP table (IP-MAC mapping) |
| `tcpdump` | Captures and analyzes network traffic |
| `route -n` | Displays the routing table |
| `wget` | Used for testing internet connectivity |

---

## 📂 **Lab Tasks**
### 1️⃣ **Exploring Network Interfaces**
- Command: `ip addr`
- Output: Displays the IP and MAC address of the machine.
- **Screenshot:**
- ![image](https://github.com/user-attachments/assets/804028bc-daa8-421b-a9e5-aea15f5a4782)

### 2️⃣ **Analyzing ARP (Address Resolution Protocol)**
- Command: `arp -a`
- Explanation: Maps IP addresses to MAC addresses.

### 3️⃣ **Capturing TCP Packets with tcpdump**
- Command: `sudo tcpdump -vv -n -e -i eth0`
- Explanation: Used to analyze network packets.
- **Screenshot:** 
- ![image](https://github.com/user-attachments/assets/403f3cc0-137f-40ac-9296-f8bd3785abe6)


### 4️⃣ **Routing Table Exploration**
- Command: `route -n`
- Explanation: Shows the system’s routing table.
- **Screenshot:** 
- ![image](https://github.com/user-attachments/assets/010b7791-2ebb-4f36-b65e-1a9a3498b4f7)


### 5️⃣ **Network Address Translation (NAT)**
- Command: `sudo iptables -L -v -t nat`
- Explanation: Demonstrates NAT configurations.

---

## 🎯 **Key Takeaways**
✅ Learned how to inspect IP/MAC addresses  
✅ Understood ARP & how devices resolve MAC addresses  
✅ Captured and analyzed network traffic using `tcpdump`  
✅ Explored routing tables and added a default gateway  
✅ Configured NAT and verified packet forwarding  

---

## 🛠 **Additional Resources**
- [TCP/IP Model Explanation](https://www.imperva.com/learn/application-security/tcp-ip/)
- [Wireshark for Packet Analysis](https://www.wireshark.org/docs/)
- [Linux Routing Basics](https://www.linux.com/training-tutorials/linux-networking-routing-basics/)
