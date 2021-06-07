# Sniffing overview

- Capturing data packets on a network using a program or a device.

## Networking concepts

### Network adapter

- Can enable Wi-Fi (wireless, WLAN) and Ethernet (wired, LAN) connection.
- Can be a **NIC** (Network interface card)
  - Physical card that connects to an expansion slot in a computer
- Modern systems has usually an integrated network adapter (e.g. on motherboard).
- As default it discards messages that's not destined to it
  - See [promiscuous mode](#promiscuous-mode) for the opposite behavior.

#### Promiscuous mode

- Allows sniffing the packets after connecting to an access point
- 📝 Network interface controller pass all traffic it receives, rather than only destined ones.
- Works on both wired and wireless connections
- See also • [libpcap | Sniffing tools](./sniffing-tools.md#libpcap) • [Turning on promiscuous mode | Wireshark](./sniffing-tools.md#turning-on-promiscuous-mode)

#### Monitor mode

- Allows sniffing the packets in the air without connecting (associating) with any access point.
- ❗ Wireless connection only

## Sniffing types

### Passive sniffing

- Does not require any packets to be sent
- Monitors and captures incoming packets
- Used in networks which use hubs i.e. shared ethernets
  - A **hub** forwards every frame to all ports but the sources filters

### Active sniffing

- Require a packet to have a source and destination addresses in order to be sent to its destination
- Used in networks which use switches i.e. switched ethernets
  - A **switch** maps MAC addresses into ports, based on source addresses
  - A switch operates at data link layer (2) to forward data to MAC addresses
    - Some switches can run on network layer (3) with additional routing functionality.
      - Also known as layer-3 switches, or multilayer switches.
- E.g.
  - [Port mirroring](#port-mirroring) where each packet is also sent to a port that attacker listens to
  - Lawful interception where electronic surveillance on a target is authorized by a judicial or administrative order.

#### Port mirroring

- Used on a network switch
- Sends copy of network packets seen on one switch port (or an entire VLAN) to another port
- Often used in [Intrusion Detection System](./../11-firewalls-ids-and-honeypots/intrusion-detection-system-(ids)-overview.md)s.
- Also known as **span port**
  - In Cisco system, it's commonly referred as Switched Port Analyzer (SPAN)
- See also [STP attack](./spoofing-attacks.md#stp-spoofing-attack) for an exploitation

## Sniffer

- Packet sniffing programs
- Designed to capture packets that contain information such as passwords, router configuration, traffic.
- 📝 Works at data link layer (2) of the OSI model where MAC addresses work
  - It may then translate frames to higher level packets.
- Allows attackers to access the network traffic from a single point.
- Turns the network adapter into [promiscuous mode](#promiscuous-mode) or [monitor mode](#monitor-mode)

## Wiretapping

- Also known as **telephone tapping** or **wire tapping**
- Monitoring of telephone and Internet-based conversations by a third party.
- Legal wiretapping by a government agency is also called **lawful interception (LI)**
- **Active wiretapping**: Alters communication by e.g. interjecting something.
- **Passive wiretapping**: Only monitors or records the traffic.
- 🤗 NSA wiretaps Internet going through using out-of-band signaling with their tool called [PRISM](https://www.zdnet.com/article/prism-heres-how-the-nsa-wiretapped-the-internet/)
- **Out-of-band vs In-band signaling**
  - **In-Band signaling**: Method where signalling is sent over the voice/data circuit.
  - **Out-of-band signaling**: Data transmission through different channels (or frequencies) than normal ones.

## Sniffing countermeasures

- Restrict the physical access to the network media
- 📝 Encryption is, by far, the best option.
  - E.g. • [SSH](./../15-cryptography/tunneling-protocols.md#ssh-secure-shell) instead of Telnet • [Secure Copy (SCP)](./../15-cryptography/tunneling-protocols.md#ssh-secure-shell) instead of FTP • [SSL](./../15-cryptography/encrypting-communication.md#ssl-secure-sockets-layer) for email connection • HTTPS instead of HTTP • [SFTP](./../15-cryptography/encrypting-communication.md#securing-ftp) instead of FTP • [WPA2](./../09-wireless-networks/wireless-networks-overview.md#wpa2) or [WPA3](./../09-wireless-networks/wireless-networks-overview.md#wpa3) for wireless traffic
  - See also [encrypting communication](./../15-cryptography/encrypting-communication.md)
- 📝 Use [Access Control Lists (ACLs)](./../11-firewalls-ids-and-honeypots/firewall-overview.md#access-control-lists-acls) on router/firewall to only allow authorized devices/IP ranges.
- Permanently add the MAC address of the gateway to the ARP cache.
- Use static IP addresses and static ARP tables
- Use switch instead of hub as switch delivers data only to the intended recipient.
- Use • [PGP](./../15-cryptography/encrypting-communication.md#pgp-pretty-good-privacy) and S/MIPE • VPN • [IPSec](./../15-cryptography/tunneling-protocols.md#ipsec) • [SSL/TLS](./../15-cryptography/encrypting-communication.md#ssltls) • [Secure Shell (SSH)](./../15-cryptography/tunneling-protocols.md#ssh-secure-shell) • [One-time passwords (OTP)](./../01-introduction/identity-access-management-(iam).md#one-time-password-otp).
- Retrieve MAC directly from NIC instead of OS to prevent MAC address spoofing.
- Use tools to determine if any NICs are running in the promiscuous mode.
