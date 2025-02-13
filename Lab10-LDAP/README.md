
# Lab 10 - LDAP

📖 **Overview**  
In this lab, we explored the use of **LDAP** (Lightweight Directory Access Protocol) to authenticate users on Linux systems. We learned how to display the LDAP directory content, monitor protocol traffic, and add LDAP users. LDAP is commonly used for centralized authentication and directory services in enterprise environments.

⚙️ **Tools & Commands Used**  
| **Tool/Command**                | **Description**                                                   |
|----------------------------------|-------------------------------------------------------------------|
| `ldapsearch -x | less`           | Display the LDAP directory content                                |
| `tcpdump -i eth0 port 389 -w password.pcapng` | Capture LDAP protocol traffic and save it to a file             |
| `ssh mike@server2`               | SSH into server 2 using mike's credentials                       |
| `sudo useradd mary`              | Add a new LDAP user, "mary", to the LDAP directory               |
| `ssh mary@server2`               | SSH into server 2 using mary's credentials                       |

📂 **Lab Tasks**

### 1️⃣ **Exploring LDAP Directory**
- **Step 1**: Display the LDAP directory content:
  ```bash
  ldapsearch -x | less
  ```
- **Step 2**: Observe the entries in the directory.

### 2️⃣ **Viewing Protocol Traffic**
- **Step 1**: Apply a filter to capture LDAP traffic and save it as a `.pcapng` file:
  ```bash
  tcpdump -i eth0 port 389 -w password.pcapng
  ```
- **Step 2**: Inspect the captured traffic using Wireshark or any packet analysis tool.

### 3️⃣ **Using LDAP Credentials to Access a Server**
- **Step 1**: Use the credentials of "mike" to SSH into server 2:
  ```bash
  ssh mike@server2
  ```

### 4️⃣ **Adding an LDAP User**
- **Step 1**: Add a new user "mary" to the LDAP directory:
  ```bash
  sudo useradd mary
  ```
- **Step 2**: SSH into server 2 using "mary's" credentials:
  ```bash
  ssh mary@server2
  ```

🎯 **Key Takeaways**
- **LDAP** is a protocol used for directory services and centralizing authentication across multiple systems.
- **LDAP Search** allows users to query and view entries in the LDAP directory.
- **Packet Capture** can help observe the traffic between clients and LDAP servers to ensure secure communication.
- Adding new users to the LDAP directory streamlines user management and authentication across systems.

🛠 **Additional Resources**
- [Introduction to LDAP](https://www.openldap.org/doc/)
- [LDAP Search Command Guide](https://linux.die.net/man/1/ldapsearch)
