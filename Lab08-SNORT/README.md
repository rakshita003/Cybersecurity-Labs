# Lab 08 - Snort: Intrusion Detection System

📖 **Overview**  
In this lab, we explored Snort, an open-source intrusion detection system (IDS) used to monitor network traffic for suspicious activities and provide alerts. We focused on the configuration, rule creation, and real-time monitoring of traffic using Snort within a Linux environment.

🔐 **Key Concepts Covered:**
- Installation and setup of Snort
- Writing custom Snort rules to detect specific traffic patterns
- Understanding the effects of encryption on IDS
- Analyzing internal and external network traffic

⚙️ **Tools & Commands Used**  
| **Tool/Command**                       | **Description**                                                         |
|---------------------------------------|-------------------------------------------------------------------------|
| **snort**                              | Open-source network IDS used for detecting and preventing intrusions    |
| **./start_snort.sh**                   | Starts the Snort IDS system                                             |
| **nmap**                               | Scans open ports on a target machine to identify vulnerable services    |
| **nano**                               | Text editor used to create and edit Snort rule files                    |
| **iptables**                           | Configures firewall rules to route traffic for Snort monitoring         |
| **cat**                                | Displays the content of files (used to check Snort rule files)         |

📂 **Lab Tasks**

1️⃣ **Starting and Stopping Snort**  
   - **Action**: Initiated Snort using the `./start_snort.sh` command on the Snort machine.  
   - **Verification**: Ran `nmap www.example.com` to ensure Snort was up and generating alerts.

2️⃣ **Pre-configured Snort Rules**  
   - **Action**: Reviewed the pre-configured rules in the `/etc/snort/rules/` directory.  
   - **Verification**: Opened and examined the `icmp.rules` file to understand the default settings.

3️⃣ **Creating a Simple (Bad) Rule**  
   - **Action**: Added a poorly configured rule in the `local.rules` file using the `sudo nano /etc/snort/rules/local.rules` command.  
   - **Result**: The rule generated excessive alerts when visiting any webpage, demonstrating ineffective rule design.  
   - **Command**: `cat /etc/snort/rules/local.rules` (to check the rule content)

4️⃣ **Creating a Custom Rule for Confidential Traffic**  
   - **Action**: Designed a custom Snort rule to detect the word "CONFIDENTIAL" within the traffic and alert the system.  
   - **Verification**: After saving the rule and restarting Snort, we visited a webpage containing confidential information, triggering an alert in Snort.  
   - **Command**: `cat /etc/snort/rules/local.rules` (to check the rule content)

5️⃣ **Effects of Encryption on Snort Detection**  
   - **Action**: Tested Snort's ability to detect traffic after switching from HTTP to HTTPS (encrypted traffic).  
   - **Result**: Snort did not generate alerts for HTTPS traffic as it is encrypted and cannot be analyzed by Snort.

6️⃣ **Watching Internal and External Traffic**  
   - **Action**: Used `nmap www.example.com` to scan the network and watched Snort generate alerts. Then, modified routing to examine Snort's response to external traffic.  
   - **Verification**: The Snort system showed more detailed alerts after routing traffic through an external gateway with the command:  
     `iptables -t mangle -A PREROUTING -i $lan2 -j TEE --gateway 192.168.3.1`

7️⃣ **Distinguishing Traffic by Address**  
   - **Action**: Configured Snort to fire alerts only for external network traffic by specifying the gateway IP address in the Snort rule.  
   - **Verification**: The rule generated alerts when accessed from an external network but did not trigger when accessed from the local network.

🎯 **Key Takeaways**
- Snort can be used to monitor and detect suspicious network traffic by creating custom rules.
- Rule creation requires careful consideration to avoid generating unnecessary alerts (like in the "bad" rule example).
- Encrypted traffic (HTTPS) cannot be inspected by Snort, which is important for understanding its limitations.
- Snort can be configured to differentiate between internal and external traffic for more targeted monitoring.

🛠 **Additional Resources**
- [Snort User Manual](https://www.snort.org/documents)
- [How to Write Snort Rules](https://www.snort.org/faq/how-do-i-write-snort-rules)
