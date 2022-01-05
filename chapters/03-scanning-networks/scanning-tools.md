# Scanning tools

## Nmap

- Scans network by sending specially crafted packets
- Allows finding hosts on network with service, OS and firewall information
- Allows custom scripts written in LUA using **NSE (Nmap Scripting Engine)**
  - 💡 Can be used to detect and/or exploit vulnerabilities
  - E.g. can [detect shellshock using nmap scripting engine](./../05-vulnerabilities/common-vulnerabilities.md#detecting-shellshock-using-nmap)
- Includes
  - [Ncat](https://Nmap.org/ncat/): reads and writes data across networks from the command
  - [`ndiff`](https://Nmap.org/ndiff/): compares scan results
  - [`nping`](https://Nmap.org/nping/): generates packets and analyzes responses
- 🤗 Used often in movies including Matrix Reloaded, see [the list](https://nmap.org/movies/)
- See also [Nmap | Network footprinting](./../02-footprinting/network-footprinting.md#nmap) and [Nmap | Vulnerability analysis](./../05-vulnerabilities/vulnerability-analysis.md#nmap).

### [Phases of an Nmap scan](https://Nmap.org/book/Nmap-phases.html)

1. **Script pre-scanning**: Runs NSE scripts that are run once per execution for each targets, e.g. `dhcp-discover`.
2. **Target enumeration**: Resolves DNS names, CIDR network notations etc. to list of IPv4 or IPv6 addresses
3. **Host discovery (ping scanning)**: Checking if a host (or which hosts are) is alive before deeper investigation
4. **Reverse-DNS resolution**: Provides IP numbers for hosts that are alive
5. **Port scanning**: Probes are sent and remote port states are classified as `open`, `closed`, `filtered`
6. **Version detection**: Determines what server software is running on remote system
7. **OS detection**: Determines OS that's running on the port
8. **Traceroute**: Usually involves another round of reverse-DNS resolution for intermediate hosts.
9. **Script scanning**: Runs most of the scripts rather than pre-scan and post-scan phases.
10. **Output**: Prints results using different options e.g. XML
11. **Script post-scanning**: Runs scripts that process results and deliver final reports and statistics

### Common Nmap options

- 📝 All options are important for a security tester to be able to use Nmap.
- `-n` (no resolution): Skips DNS resolution and scanning for DNS addresses
- `-A`: Enable • OS detection • version detection • script scanning • traceroute
- `--traceroute`: Enables trace routing
- `--script` or `-SC`: Activates custom script scanning

#### `-s*`: port scan options

- Uses [ICMP echo request](./scanning-techniques.md#scanning-icmp), [TCP SYN](./scanning-techniques.md#syn-scanning) to port 443, [TCP ACK to port 80](./scanning-techniques.md#ack-scanning), and an ICMP timestamp request.
- `-sn`
  - Also known as ***ping scan*** or ***host discovery***
  - Skips port scanning
- Common commands include:
  - TCP port scanning: `-sS` ([SYN](./scanning-techniques.md#syn-scanning)), `-sT` ([connect](./scanning-techniques.md#tcp-connect)), `-sN` ([NULL](./scanning-techniques.md#null-scan)), `-sF` ([FIN](./scanning-techniques.md#fin-scan)), `-sX` ([XMAS](./scanning-techniques.md#xmas-scan))
  - UDP port scanning: `-sU` ([UDP](./scanning-techniques.md#udp-scanning))
  - `-sV`: service/version detection scan
  - `-sO`
    - IP protocol scan
    - Not really a port scan
    - Lists supported IP protocols (TCP, ICMP, IGMP etc.) by target system.

#### `-P*`: ping (host discovery) options

- `-P*` options are used to select different ping methods
- User with `-sn` to skip port scanning and do host discovery only.
- Common commands include:
  - TCP: `-PS`, ([SYN](./scanning-techniques.md#syn-scanning)), `-PA` ([ACK](./scanning-techniques.md#ack-scanning))
  - Others: `-PR` ([ARP](./scanning-techniques.md#arp-scan)), `-PO` (IP protocol ping), `-PE` [ICMP](./scanning-techniques.md#icmp-ping-sweep) `PU` ([UDP](./scanning-techniques.md#udp-scanning))
  - **`-Pn` (no ping)**
    - Also known as ***pingless scan*** or ***port scan***
    - Skips host discovery and treats all hosts as online

#### Specifying ports

- `-p-` to scan all ports (`1-65535`)
- `-p`: only scan specified ports
  - E.g. `-p U:53,111,137,T:21-25,80,139,8080`
- `-r`: Scan ports consecutively - don't randomize

#### `-O`: OS fingerprinting

- `-O` is used for operating system fingerprinting
- It's Far more effective if at least one open and one closed TCP port are found.
  - Flag with `--osscan-limit` and Nmap will not try OS detection against hosts that do not meet this criteria.
- `--fuzzy` or `--osscan-guess` switch: Nmap will guess more aggressively
- ❗Requires `sudo` privileges
- See also [banner grabbing](./banner-grabbing.md)

#### `-o*`: output options

- `-oX` for XML output.
- `-oG` for `grep`able output to be able to use linux [`grep` command](../06-system-hacking/linux-basics.md) to search in text
- ❗ Not to be confused with `-O` (OS fingerprinting)

#### Faster scans

- `-T*`: Timing template
  - From slowest to fastest: `-T0` (paranoid), `-T1` (sneaky), `-T2` (polite), `-T3` (normal | default), `-T4` (aggressive) or `-T5` (insane)
- `-F`: Fast (limited port) scan
  - Nmap as default most common 1000 ports, `-F` reduces it to 100
- ❗ If the scan is too fast the system can drop the packets
  - Risky because the system can cancel the whole scan when it detects for the first time.

#### Target specification

- `nmap <target>`
- Everything that isn't an option (or option argument) is treated as a target host specification
- Target can be IP address(es) or hostname(s) (resolved via DNS)
- Target can be specify single or multiple hosts:
  - Scanning single host:
    - E.g. `nmap 192.168.10.0` (IP address) or `nmap localhost` (hostname)
  - Scanning many hosts:
    - CIDR style addressing
      - E.g. `192.168.10.0/24` would scan the 256 hosts
    - Octet range addressing (more flexible)
      - E.g. `192.168.0-255.1-254`
      - Full octet scan: `192.168.0.*`
    - Using target list: `nmap -iL targets`
    - Scan multiple addresses using `nmap <target-1>, <target-2> ...`
      - E.g. `nmap privacy.sexy cloudarchitecture.io`

## Hping

- [Open-source](http://www.hping.org/) port scanner
- Sends custom ICMP, UDP, or TCP packets and then displays any replies

### Hping vs Nmap

- `nmap` can scan a range of IP addresses
  - `hping` can only port scan one individual IP address
- `hping` is more lower level and stealthier than `nmap`
- `hping` does not support IPv6 while `nmap` does.

### Common hping commands

- `--tcp-timestamp`
  - Enables TCP timestamps
  - Tries to guess the timestamp update frequency and the remote system uptime.
  - ❗ Many firewalls drop packets without timestamp.
- `-Q` or `--seqnum`
  - Collects sequence numbers generated by target host
  - Useful when you need to analyze whether TCP sequence number is predictable.
- Setting flags using
  - `-F` (`FIN`), `-S` (`SYN`), `-R` (`RST`), `-P` (`PUSH`), `-A` (`ACK`), `-U` (`URG`)
- Scanning entire subnet: `hping3 -1 10.0.1.x`
- Listen to traffic (e.g. to sniff): `hping3 -9 HTTP -I eth0`
- See also its [man page](https://linux.die.net/man/8/hping3)

## Mobile tools

- [IP Scanner](https://10base-t.com) for IOS
- [Fing](https://www.fing.io) for IOS and Android
