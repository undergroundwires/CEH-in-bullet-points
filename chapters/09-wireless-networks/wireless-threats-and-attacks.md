# Wireless threats and attacks

## Wireless threats

- **Access control attacks**
  - Evading access control measures such as Access Point MAC filters, port access control
- **Integrity attacks**
  - Sending forged frames
  - E.g. data frame injection, bit-flipping.
- **Confidentiality attacks**
  - Intercepting confidential information transmitted over the network
  - E.g. traffic analysis, session hijacking, MITM, etc...
- **Availability attacks**
  - Attempting to prevent users from accessing WLAN resources.
  - E.g. flooding, ARP poisoning, De-Authentication attacks
- **Authentication attacks**
  - Steal identity information or impersonating clients
  - E.g. password cracking, identity theft, password guessing
  - See also [Authentication attacks | Hacking Web Applications](./../13-web-applications/hacking-web-applications.md#authentication-attacks)
- **Misconfigured access point attack**
  - Accidents for configurations that you can exploit
- **AD Hoc connection attack**
  - Connecting directly to another device via ad-hoc network.
  - Not very successful as the other user has to accept connection
- **Honeyspot access point attack**
  - Using multiple WLANs in area and use same SID.
- **AP MAC spoofing**
  - MAC spoofing to mask an authorized client
- **Jamming signal attack**
  - Jamming or blocking the wireless communication, causing a denial of service

### De-authentication attack

- Also known as **deauthentication attack**
- Used to capture the handshake traffic.
- Can also be used to DoS the client by continuously de-authenticating the device.

### Evil twin attack

- Also known as **client mis-association**
- 📝 A rogue access point outside the place with the legitimate one
- E.g. can lure the employees of the organization to connect with it
- Can be done using [Airsnarf](http://airsnarf.shmoo.com/)

#### Honeyspot attack

- Faking a well-known hotspot on a rogue AP
- E.g. as McDonald's or Starbucks free Wi-Fi spot

### Rogue Access Point Attack

- Fake AP with same SSID as legitimate one.
- Allows hijacking connections and acting as a middle man sniffing
- Differs from [evil twin attack](#evil-twin-attack) as it focuses on MITM instead of WiFi passwords.

### Sinkhole attack

- Compromised node tries to attract network traffic by advertise its fake routing update.
- Allows traffic to be directed away from its target.
- Can be used to launch other attacks like dropping or altering routing information.

#### DNS sinkhole

- Also known as a ***sinkhole server***, ***Internet sinkhole***, or ***Blackhole DNS***
- DNS server that gives out a false result for a domain name.
- Used to attack on sensor/IoT device networks
- Can be prevented by owning own DNS server or hardcoding IP addresses.
- E.g. [WannaCry malware was stopped](https://en.wikipedia.org/wiki/WannaCry_ransomware_attack#Defensive_response) spreading as a worm by Marcus Hutchins who discovered kill switch in the malware and Registering a domain name for a DNS sinkhole.

## Wireless hacking methodology

1. **[Wi-Fi Discovery](#wireless-discovery)**
   - find wireless networks
2. **GPS mapping**
   - List of discovered Wi-Fi networks
3. **Wireless Traffic Analysis**
   - Capture the packets to reveal any information (SSID, authentication method, ...)
4. **Launch Attacks**
   - E.g. ARP poisoning, MAC spoofing, De-Authentication, Rogue access point, MITM.

### Wireless discovery

- Also known as Wi-Fi discovery
- **Wardriving**: Using a mobile vehicle to detect WiFi networks
  - 📝 E.g. [T.J. Maxx Data Theft](https://www.informationweek.com/tj-maxx-data-theft-likely-due-to-wireless-wardriving/d/d-id/1054964?) where 45 million credit/debit card data was stolen because of weak WEP encryption.
  - Also used: warbiking, warcycling, warwalking.
  - **Warchalking**: drawing of symbols in public places to advertise an open Wi-Fi network.
- Tools such as WiFiExplorer, WiFiFoFum, OpenSignalMaps, WiFinder
  - WIGLE: map for wireless networks
  - [NetStumbler](http://www.netstumbler.com/downloads/): Windows tool to find networks
  - [Kismet](./../08-sniffing/sniffing-tools.md#kismet)
    - Wireless network detector, sniffer, and intrusion detection system.
    - Works without sending any packets (passively)
  - [NetSurveyor](http://nutsaboutnets.com/archives/netsurveyor-wifi-scanner/): Windows tool similar to NetStumbler and Kismet
  - [Silica](https://www.immunityinc.com/products/silica/): Discovers and shows vulnerabilities

## Wireless encryption attacks

### WEP cracking

- Weak IV (Initialization Vectors)
  - Small
  - Get reused frequently
  - Are sent in clear text during transmission
- Can take a few seconds to discover the shared secret key.
- The goal is to collect as many IVs as possible
  - 💡 Inject packets to speed it up
- 📝 Can be cracked using Aircrack-ng:
  1. Listen to the traffic
     - Start a compatible adapter with injection and sniffing capabilities
     - `airmon-ng start <interface-name>`
  2. Start a sniffer to capture packets
     - `airodump-ng --bssid <AP-MAC-address> -c 11 -w <output-file> <interface-name>`
  3. Create more packets to escalate the process to collect more IV
     - Inject ARP traffic: `aireplay-ng -3 -b 00::09:58:6F:64:1E -h 44:60:57:c8:58:A0 mon0`
  4. Run a cracking tool to extract encryption keys from the collected IVs
     - `aircrack-ng <output-file>.cap`
     - Default method is PTW (Pyshkin, Tews, Weinmann), other (older) supported methods include:
       - FMS (Fluhrer, Mantin, Shamir) attacks: statistical techniques
       - Korek attacks: statistical techniques
       - Brute force
- Using separate tools for sniffing and cracking:
  1. Gathering packets through e.g. Wireshark or Prismdump
  2. Crack using e.g. [WEPCrack](http://wepcrack.sourceforge.net/), [AirSnort](https://sourceforge.net/projects/airsnort/), [Aircrack-ng](https://www.aircrack-ng.org/), and [WEPLab](https://linux.die.net/man/1/weplab)

### WPA/WPA2 cracking

- Much more difficult than WEP
- Uses a constantly changing temporal key and user-defined password
- **Key Reinstallation Attack (KRACK)**
  - Replay attack that uses third handshake of another device's session
- Most other attacks are simply brute-forcing the password that take a lof time.

#### Sniffing 4-way handshake

- 4-way handshake is the ceremony between AP and the device
- Vulnerability in WPA and WPA-Personal (WPA-PSK, pre-shared key)
- During WPA handshake, password is shared in encrypted form (called **PMK (pairwise master key)**)
- Flow:
  1. Client tries to connect to an AP (access point)
     - If the client is already connected then [deauthentication attack](#de-authentication-attack) can be used to disconnect the client and sniff when client is reconnecting.
  2. Grab packets while client goes through a 4-step process of authentication
  3. Crack WPA keys from recorded packets
     - Can be an offline attack e.g. utilizing a cloud virtual machine.
     - E.g. using `hashcat`
- Steps
  1. Recording and deauthenticating using **[`aircrack-ng`](https://www.aircrack-ng.org/)**
     - 🤗 Used often in movies as it looks cool
     - `airmon-ng start <interface-name>` to create a new interface and enable monitor mode
     - `airmon-ng <interface-name>` to list access points with BSSID, encryption (WPA2 etc.) and more.
     - `airmon-ng -c2 -w capture -d <BSSID> <interface-name>` to listen
       - Shows each client MAC and logs their traffics notifying handshakes.
     - `airplay-ng -deauth 100 -a <BSSID> -c <client-MAC> <interface-name>` to inject packets to de-authenticate the client
  2. Crack the password using `hashcat`
     - Convert log files from `airmon-ng` from `.cap` to `.hccapx` using e.g. an [online tool](https://hashcat.net/cap2hccap/)
     - Run `hashcat.bin -a 3 -m 2500 converted-file.hccapx ?d?d?d?d?d`
       - `-m 2500`: hash mode for `WPA-EAPOL-PBKDF2`
       - `-a 3 ?d?d?d?d?d`: attack mode: bruteforce with mask telling 5 any characters.

### WPA3

- More secure against sniffing, brute force and WPS attacks.
- However has implementation bugs that can be exploited using:
  - [potential side channel attacks](https://w1.fi/security/2019-2/eap-pwd-side-channel-attack.txt)
  - [DoS attacks](https://w1.fi/security/2019-3/sae-confirm-missing-state-validation.txt)

### Tools for wireless encryption attacks

#### Aircrack-ng

- 📝 Sniffer, detector, traffic analysis tool and a password cracker
- [Official webpage](https://www.aircrack-ng.org/) | [Source code](https://github.com/aircrack-ng/aircrack-ng)
- Uses dictionary attacks for WPA and WPA2.
  - Other attacks are for WEP only

#### Cain and Abel

- Also known as **Cain & Abel** or **Cain**
- 📝 Windows tool to sniff packets and crack passwords
- Relies on statistical measures and the PTW technique to break WEP
- See also • [Cain and Abel | Web server threats and attacks](./../12-web-servers/web-server-threats-and-attacks.md#cain-and-abel) • [Cain and Abel | Sniffing tools](./../08-sniffing/sniffing-tools.md#cain-and-abel)
