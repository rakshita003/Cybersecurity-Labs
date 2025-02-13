
# Lab 04 - Wireshark & PCAP Analysis  

## 📖 Overview  
This lab focuses on **packet capturing and analysis** using Wireshark and Tshark. It demonstrates:  
- **Capturing network packets** using PCAP files  
- **Analyzing captured packets** for sensitive data extraction  
- **Using Wireshark filters** to locate specific traffic  
- **Interpreting Telnet packet data** in a PCAP file  

---

## ⚙️ **Tools & Commands Used**  
| Tool/Command   | Description |
|---------------|------------|
| `tshark` | Command-line tool for network packet analysis |
| `man tshark` | Displays the manual for Tshark |
| `tshark -T fields -e frame.number -e frame.time -e telnet.data -r telnet.pcap` | Extracts specific fields from a PCAP file |
| `tshark -T fields -e frame.number -e frame.time -e telnet.data -r telnet.pcap -Y frame.number==181` | Filters packets based on frame number |
| `ls` | Lists directory contents |
| `file telnet.pcap` | Checks details of the PCAP file |
| `Wireshark` | GUI-based tool for packet capture and analysis |

---

## 📂 **Lab Tasks**  

### 1️⃣ **PCAP Analysis Using Tshark**  
- Opened the **manual** for `tshark`:  
  ```bash
  man tshark
  ```
- Displayed specific fields from the captured **Telnet session**:  
  ```bash
  tshark -T fields -e frame.number -e frame.time -e telnet.data -r telnet.pcap
  ```
- **Identified a specific packet** containing an invalid "admin" password:  
  ```bash
  tshark -T fields -e frame.number -e frame.time -e telnet.data -r telnet.pcap -Y frame.number==181
  ```
- Used `checkwork` to verify completion.  
- **Screenshot in the attached PDF.**  

---

### 2️⃣ **Wireshark Introduction & PCAP Analysis**  
- Listed files in the working directory:  
  ```bash
  ls
  ```
- Identified the **PCAP file** for analysis:  
  ```bash
  file telnet.pcap
  ```
- Opened **Wireshark** and located the Telnet traffic.  
- Applied filters to find the **correct packet**.  
- Selected and exported the **suspicious packet**.  
- Used **"Follow TCP Stream"** to view the **full Telnet session data**.  
- **Screenshot in the attached PDF.**  

---

## 🎯 **Key Takeaways**  
✅ **PCAP files** store captured network packets.  
✅ **Tshark and Wireshark** allow deep packet analysis.  
✅ **Sensitive data (like passwords) can be retrieved from unencrypted traffic**.  
✅ **Filtering packets helps quickly locate relevant data** in large network captures.  

---

## 🛠 **Additional Resources**  
- [Wireshark Packet Analysis](https://www.wireshark.org/docs/)  
- [Using Tshark for PCAP Analysis](https://www.wireshark.org/docs/man-pages/tshark.html)  
- [Packet Filtering Techniques](https://www.networkcomputing.com/networking/how-use-wireshark-network-packet-analysis)  

---
