# Denial of service

- Attacker overloads the target system with a lot of traffic
- Goal is to reduce, restrict or prevent accessibility of system resources to its legitimate users

## Botnets

- Bots are software applications that run-automated tasks over the internet
- A botnet is a huge network of compromised systems and can be used by an attacker to launch a DoS attack
- Controlled by **Command and Control server** owned by the attacker
- **Distributed Denial of Service (DDoS)**
  - Using botnets (compromised systems) to perform a DoS attack.
- DoS and DDoS attack tools: • [LOIC](#low-orbit-ion-cannon-loic) • [GoldenEye or Petya](https://en.wikipedia.org/wiki/Petya_(malware))
- See also [Botnet](./../01-introduction/security-threats-and-attacks.md#botnet) and [Botnet trojans](./../07-malware/trojans.md#botnet-trojans)

## Attack vectors

### Volumetric attacks

- Goal is to use up bandwidth of the target network or service.

#### Volumetric attacks types

- **Flood attacks**
  - Sending high volume traffic, can utilize zombies
- **Amplification attacks**
  - Sending magnified traffic, can utilize zombies

#### Volumetric attack techniques

- **UDP flood attack**
  - Flooding random ports of the target server with a huge number of spoofed UDP packets
  - Causes the server to continuously check for applications on the ports.
    - When not found, system responds with `ICMP Destination Unreachable` packet increasing its traffic.
- **ICMP flood attack** or **Ping flood**
  - Flooding with ICMP echo request packets.

##### Smurf attack

- 📝 Flooding a IP broadcast network with ICMP echo request packets with victim IP address as source
- Causes hosts in the network respond to received requests/responds targeting the victim.
- Leads to server overloads in victim caused by too many replies.
- The reason to attack broadcast address is to send so many ICMP requests going to the target that all its resources are taken up.
- Mitigated by either
  - configuring routers/hosts to not respond to ICMP broadcasts/requests
  - configuring routers to not forward packets directed to broadcast addresses
- See also [Broadcast ICMP ping](./../03-scanning-networks/scanning-techniques.md#broadcast-icmp-ping)

##### Ping of death attack

- 📝 Sending irregular or big packets using `ping` command
- Attacker fragments ICMP message to send to target.
- When the fragments are reassembled, the resultant ICMP packet is larger than max size and crashes the system

### Protocol attacks

- Also known as **state exhaustion flood attacks**
- Goal is to make target device reject new connections
- Targets connection state tables, that are present in e.g. load balancers, firewalls, app servers

#### Protocol attack techniques

##### SYN flood attack

- Also known as **SYN Attack** or **SYN ACK flood attack**
- Exploits a flaw in [TCP three-way handshake](./../03-scanning-networks/tcpip-basics.md#three-way-handshake)
- Floods SYN requests with fake source IPs
  - Target responds with a SYN ACK packet and waits for the sender to complete the session
  - Sender never completes the session as source IP is fake.
- OS kernels usually implements a backlog of open connections
  - So the attack does not attempt to overload memory or resources
  - It overloads backlog of half-open connections
  - Causes legitimate requests to be rejected

###### SYN flood countermeasures

- 🤗 Defined in [RFC 4987](https://tools.ietf.org/html/rfc4987)
- Same countermeasures also resists against IP spoofing
- **Filtering**
  - Packet filtering based on IP addresses
- **Increasing backlog**
  - Larger backlogs allow more connections
- **Reducing `SYN-RECEIVED` timer**
  - Shorter time will prevent half-open connections to persist in backlog
- **Recycling the oldest half-open TCP**
  - When backlog is full, overwrite the oldest half-open entry
- **SYN cache**
  - Not allocating full state to minimize space until connection has been established
- **SYN cookies**
  - Resists IP spoofing
  - Encodes SYN queue entry in sequence number sent in the `SYN+ACK` response
  - When server receives `ACK`, it reconstructs SYN entry from sequence number to establish the connection
- **Hybrid approaches**
  - Combining SYN cache and cookies
  - E.g. sending cookies when cache is full
- **Firewalls and proxies**
  - Firewalls/proxies sends connection to end host when connection is established
  - Moves away problem to firewalls/proxies

##### ACK flood attack

- Overloading a server with TCP ACK packets
- TCP ACK packet is any TCP packet with the ACK flag set in the header.
- ACK is short for "acknowledgement"
  - TCP protocol requires that connected devices acknowledge they have received all packets in order
  - E.g. when all packets for an image is sent, ACK packet is required otherwise image is sent again.

##### DNS query/NXDOMAIN floods

- Attackers send valid but spoofed DNS request packets at a very high packet rate
- Victim's DNS servers proceeds to respond to all requests

##### Fragmentation attack

- Flooding TCP/UDP fragmented packets with small packet rate to the system
- Exhausts the system through forcing it to reassembling packets.

###### TCP fragmentation attack

- Also known as ***teardrop attack***
- 📝 Type of DoS attack also known as **teardrop** attack.
- Sends invalid packets with overlapping, oversized payloads to the victim.
- Sends gigantic payloads to crash vulnerable systems:
  - Windows 3.1x, Windows 95 and Windows NT
  - Linux prior to versions 2.0.32 and 2.1.63

##### `RST` attack

- Also known as **TCP reset attack**
- Attacker sends TCP packets with the `RST` flag set to `1` to host A, host B, or both using spoofed IPs
  - Causes termination of valid TCP connection between the two hosts.
- Setting `RST` flag
  - Indicates that receiving computer should immediately kill the TCP connection
  - An real-life scenario
    1. Two computers (computer A and computer B) communicate with each other
    2. Computer B kills the communication without knowledge of computer A
       - E.g. computer B has crashed
    3. Computer A continues to send packets to computer B
    4. Computer B sends `RST` packet to computer A to kill the communication
  - See also: [TCP flags](./../03-scanning-networks/tcpip-basics.md#tcp-flags)
- 🤗 Used often for internet censorship e.g. • [The Great Firewall of China](https://en.wikipedia.org/wiki/Great_Firewall) • [Iranian Internet censors](https://en.wikipedia.org/wiki/Internet_censorship_in_Iran#Deep_packet_inspection).

### Application layer DoS attacks

- Send "legitimate" traffic to a web application than it can handle.
- Goal is to make target application reject new connections by creating new connections and keeping them open as long as possible.
- Flow
  1. Attacker opens multiple connections to the targeted server by sending partial HTTP request headers.
  2. Target opens a thread for each incoming request to close once connection is completed.
     - If connection takes too long, the server will timeout, freeing the thread up.
  3. Attacker sends partial request headers to prevent target from timing out

#### Application layer attack techniques

- **HTTP flooding attacks**
  - Goal is to make server hold on to connections waiting for the full requests which it never receives.
  - **HTTP GET attack**: Sending requests with time delayed HTTP headers
  - **HTTP POST attack**: Sending requests with incomplete bodies delayed HTTP headers
- **Slow-rate attacks**
  - Also known ass **low and slow attacks**
  - Apparently legitimate traffic arriving at a seemingly legitimate albeit slow
  - E.g. [Slowloris and R-U-Dead-Yet](#dos-tools)

### Other attack types

- **Multi-vector attack**
  - Combining volumetric, protocol, and application layer attacks into one and launching
  - Can be sequentially or in parallel
- **Peer-to-Peer Attack**
  - Caused by bugs in a peer-to-peer server
  - Instructs clients to disconnect and reconnect to a victims website.
- **Permanent DoS Attack (PDoS)** or **phlashing**
  - Does irreversible (without replacement or reinstalling) damage to the hardware or its firmware.
  - E.g. replacing firmware (e.g. through fake updates) with a corrupt one, also known as flashing.
- **Fraggle attack**
  - Similar to [Smurf](#smurf-attack) but uses UDP.
- **TCP state-exhaustion**
  - Attempts to consume connection state tables.  
  - Tergets load balancers, firewalls, and application servers

#### DRDoS

- Also known as ***distributed reflection denial of service (DRDoS) attack*** or ***spoofed attack***
- Multiple intermediary machines send the attack at the behest of the attacker is correct.
- Secondary systems carry out attacks so the attacker remains hidden.
- Attacker instructs zombie machines (called **secondary machines**) to send packets to uncompromised machines (called **secondary machines**)
  - Packets contain target's IP address as the source address
  - Secondary machines try to connect to the target.

### DoS Tools

- **Slowloris**
  - Floods HTTP with headers for each request without actually completing them.
  - 🤗 [Slowloris presentation](https://samsclass.info/seminars/slowloris.pdf)
- 📝 **[R-U-Dead-Yet](https://sourceforge.net/projects/r-u-dead-yet/)**
  - Also known as ***RUDY***, ***R.U.D.Y.*** or ***R U Dead yet***
  - Submits long form fields using HTTP posts to the target server.
  - Sends concurrenct small pakets at incredibly slow rate
  - Keeps connection open as long as possible
- **[HULK](https://github.com/grafov/hulk)**
  - HTTP DoS tool
- **[Metasploit](./../05-vulnerabilities/automated-penetration-testing-tools.md#metasploit)**
  - with modules for DoS e.g. [TCPSYNFlooder](https://www.rapid7.com/db/modules/auxiliary/dos/tcp/synflood/)
- [**Nmap**](./../03-scanning-networks/scanning-tools.md#nmap) with [DoS scripts](https://Nmap.org/nsedoc/categories/dos.html)
- **[DAVOSET](https://github.com/MustLive/DAVOSET)**
  - DAVOSET = DDoS attacks via other sites execution tool
  - DDoS attacks on the sites via Abuse of Functionality and XML External Entities vulnerabilities on other sites.
- **[High Orbit Ion Cannon (HOIC)](https://sourceforge.net/projects/highorbitioncannon/)**
  - High-speed multi-threaded HTTP flood
- Other tools include • Stacheldraht • Trinoo • TFN2k • WinTrinoo • T-Sight

#### Low Orbit Ion Cannon (LOIC)

- DoS attack tool (C#) using layer (TCP, UDP) and layer 7 (HTTP) packets
- Used for successful attacks to big companies by including Anonymous group.
- [Open-source](https://sourceforge.net/projects/loic/)
- Improved version: **[Tsunami](https://sourceforge.net/projects/tsunami-dos/)**

#### Mobile tools

- [LOIC](#low-orbit-ion-cannon-loic)
- AnDOSID

## Denial of Service countermeasures

### DoS analysis

- **Activity Profiling**: Detect Increases in activity levels, distinct clusters, average packet rate etc.
- **Changepoint detection**: Stores and presents graph of traffic flow rate vs time for each IP/port.
- **Wavelet-based signal analysis**: Divides incoming signal into various frequencies as spectral components.

### DoS prevention strategies

- Absorb the attack with additional resources e.g. through using a CDN.
- Degrade or shut down services (start with non-critical services)
- Deflect attacks using honeypots.
- Ingress filtering to enable originator be traced to its true source.
- Egress Filtering to ensure unauthorized or malicious traffic never leaves the internal network
- Load balancing and throttling

### DoS post-attack forensics

- Traffic patterns for new filtering techniques
- Router, firewall, and IDS logs
- Update load-balancing and throttling countermeasures
