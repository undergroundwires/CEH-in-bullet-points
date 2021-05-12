# Sniffing attacks overview

- [Spoofing attacks](./spoofing-attacks.md)
- [ARP posioning](./arp-poisoning.md)

## MAC flooding

### MAC

- MAC address is a unique identifier of a network node.
- E.g. `52:54:00:e5:83:bb`
  - First three sets (`52:54:00`): Manufacturers signature
  - Last three sets is set in different ways depending on manufacturers
- Embedded in the device (firmware or some read-only part of the device)
- In a network, each device has its own MAC address
  - Associates the device with a physical port
- 🤗 If your MAC address is logged, police can use it to contact the manufacturer to ask who purchased the device.
  - Difficult to trace it if it was paid by cash.
- 💡🤗 You may have free WiFi forever if you can change your MAC address.
  - Usually checked in public places e.g. in an airport when they give you free WiFi.

#### Content Addressable Memory (CAM) table

- Used by switches
- Stores all available MAC addresses and their virtual LAN parameters for each port.
- Possible to sniff by flooding it.

### MAC flooding attack

- Flooding the switch with thousands of MAC address mappings such that it cannot keep up.
  - When the table can't keep up it starts sending every message out to every port.
  - I.e. switch is forced to behave as a hub.
- Allowed by the fixed size of the CAM table.
- Steps:
  1. Send large number of fake MAC addresses to the switch until CAM table becomes full
  2. Switch enters fail-open mode
     - where it broadcasts the incoming traffic to all ports on the network
  3. Attacker (with promiscuous mode) starts sniffing the traffic passing through the network.
- Can be followed up using [ARP spoofing](./arp-poisoning.md) to retain access to data after switches recover.
- See also [MAC spoofing](./spoofing-attacks.md#mac-spoofing)

## DHCP attacks

### DHCP introduction

- DHCP: Dynamic Host Configuration Protocol
- Client/server protocol
- Used by routers as they start a DHCP server
- Server provides following to DHCP-enabled clients:
  - IP addresses
  - Configuration information
  - Time period of the lease offer
- A possible way to drop connection of others in network is to brute-force DHCP server with "returning lease" messages.
  - It'll force everybody to lose connection and request IP addresses again

#### DHCP snooping

- Layer 2 security feature
- Built into operating system of a capable network switches
- Filters, rate-limits suspicious DHCP traffic
- Builds and maintains the **DHCP snooping binding database**
  - Also known as **DHCP snooping binding table**
  - Stores MAC + assigned IP + [VLAN](#vlan) and switch ports
  - Uses to validate subsequent requests from untrusted hosts.
- 📝 **Dynamic ARP Inspection (DAI)**
  - Defense against too many incoming ARP broadcasts.
  - Each port on VLAN is untrusted by default
  - Each IP to MAC conversion is validated using DHCP snooping binding database.

### DHCP starvation

- Exhaust all available addresses from the server
- Exploits that DHCP has a limited number of ip addresses to lease.
- A type of Denial of Service attack
- Flow
  1. Starve it, and no new clients will be able to connect
     1. Attacker broadcasts large number of DHCP REQUEST messages with spoofed source MAC addresses.
     2. Available IP addresses in the DHCP server scope becomes depleted.
     3. DHCP server becomes unable to allocate configurations to new clients and issue any IP addresses
  2. Set-up rogue (fake server) to respond to the discovery requests
     1. Attacker sets up a rogue DHCP server to respond to DHCP discovery requests.
     2. If a client accepts the rogue server as its DHCP server, then the attacker can listen to all traffic going from or to the client.
- **Tools**
  - [`yersinia`](https://linux.die.net/man/8/yersinia)
    - Start UI using `yersinia -G` then click on "Start attack"
  - [DHCPstarv](http://dhcpstarv.sourceforge.net/)

### DHCP starvation countermeasures

- Authentication
- Configure [DHCP snooping](#dhcp-snooping)
- Trusted sources
  - ❗Vulnerable to mimicing them

#### Port security

- Allows traffic from a specific MAC address to enter to a port
- Only allowing one MAC through a port
- Only one IP at a time can be requested
- ❗ Vulnerable to [spoofing MAC addresses](./spoofing-attacks.md#mac-spoofing)

## DNS poisoning

### DNS introduction

- Domain Name Server
- 📝 Protocol that resolves domain names into IP addresses using default port 53.
- Stores domain name and IP address pairs in a **DNS table**.

### DNS poisoning attack

- 📝 Also known as **DNS cache poisoning** and **DNS spoofing**
- 📝 Manipulating the DNS table by replacing a legitimate IP address with a malicious one
  - E.g. redirecting `cloudarchitecture.io` to attackers IP address.
- 🤗 Used for internet censorship in many countries.
- Flow
  1. Attacker makes DNS request to target
  2. DNS server asks the root name server for the entry
  3. Attacker floods the DNS server with a fake response for the targeted domain until legitimate response from root server is ignored
  4. The poisoned entry remains in cache for hours and even days
- Can be used after [ARP poisoning](./arp-poisoning.md) through **DNS spoof** plugin of [Ettercap](https://www.ettercap-project.org/).
- Can be followed up with e.g. • man-in-the-middle attacks • [website defacement](./../12-web-servers/web-server-threats-and-attacks.md#website-defacement) attacks

### DNS poisoning countermeasures

- **Active monitoring**
  - Monitor DNS data for new patterns such as new host
  - E.g. by using intrusion detection system (IDS)
- **Keep DNS servers up-to-date**
  - Updated versions have port randomization and cryptographically secure transaction IDs against attackers.
- **Randomize source and destination IP, query IDs, during name requests**
  - Makes harder for attackers to send spoofed responses as it'd be harder to guess the address and query ID.
- **Use HTTPS and/or TLS for securing the traffic**
  - Also known as **DNS over HTTPS (DoH)** and **DNS over TLS (DoT)**
  - SSL and TLS use certificates to verify the identity of the other party.
  - So although they do not protect against cache poisoning itself, the certificates help to protect against the results

#### DNSSEC (Domain Name System Security Extension)

- Developed by The Internet Engineering Task Force (IETF)
  - Open standards organization, which develops and promotes voluntary Internet standards
- Help verifying the true originator of DNS messaging
- 📝 Provides secure DNS data authentication by using digital signatures and encryption.
  - Adds cryptographic signatures to existing DNS records, stored in DNS name servers.
- Widely considered one of the greatest cache poisoning prevention tool as a defense
- Allows verifying that a requested DNS record comes from its authoritative name server and wasn't altered, opposed to a fake record injected in a man-in-the-middle attack.
- **Chain of trust**: E.g. `cloudarchitecture.io`'s signature is verified by `.io` signature that is verified by root certificate (signed by [IANA](https://www.cloudflare.com/en-gb/dns/dnssec/root-signing-ceremony/))
  - **IANA**: Centrally coordinates Internet for DNS Root, IP addressing, and other Internet protocol resources.

## VLAN hopping

### VLAN

- 📝 Allows multiple separate LANs/networks on same switch through logical grouping
- Provides network separation
  - Hosts one one VLAN does not see hosts on other one
- **Port-based VLAN**
  1. Designate set of ports on the switch
     - account department VLAN, shipping department VLAN..
  2. Connect devices to right ports each group is a VLAN
- **Tag-based VLAN** aka IEEE 802.1q VLANs
  - Basically a tags frames with which VLAN it belongs to
    - Frame = Primitive packet on layer 2
  - Tagged frame = IEEE 802.1q frame
  - Can tag/assign based on e.g. [802.1x](./../09-wireless-networks/wireless-networks-overview.md#ieee-8021x)
- **Trunk** (=802.1q link)
  - Allows sharing VLANs (VLAN IDs) between switches

### VLAN hopping attack

- Attacking host on a VLAN to gain access to traffic on other VLANs
- E.g. using [Frogger](https://github.com/nccgroup/vlan-hopping---frogger)
- **Switch spoofing**
  - Attacking host imitates a trunking switch
- **Double tagging**
  - Attacker prepends two VLAN tags to frames
  - Second tag is the target host
  - First switch removes first innocent VLAN tag and sends packet to second switch.
  - Allows bypassing security mechanisms and reaching the target hosts.
  - Replies are not forwarded to the attacker host

## OSPF attacks

- Forms a trusted relationship with the adjacent router
- Usually these attacks go undetected
- **Remote attacks**: caused by misconfigurations

### OSPF: Open Shortest Path First

- Most popular routing protocol for IP networks
- Dynamically discovers neighbors like RIPv2 and BPG (Border Gateway Protocol)
- Used by e.g. internet service providers (ISP) and cloud providers for hybrid communication

### Compromised router attacks

- Placing a rogue router in target network e.g. remote branch/headquarters
- Allows attacker to inject routes to redirect traffic for MITM attacks or DoS attacks.
- Attacker learns about that entire routing domain such network types, links etc

### OSPF attacks countermeasures

- 📝 Configure OSPF to authenticate every OSPF message
  - Routers must pass the authentication process before becoming OSPF neighbors.
- Monitor OSPF neighbors for eavesdropping through e.g. a SIEM
