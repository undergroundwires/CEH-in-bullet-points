   # Network footprinting

- Collecting network range information to use the information to map the target's network
- Gives insights into how the network is structured and which machines belong to the network.

## Nmap

- Used for network discovery
- Uses raw IP packets to determine e.g.
  - the available hosts on the network
  - the services offered by those hosts
  - operating systems they are
  - firewall types that are being used
  - and more...
- Not only used for malicious purposes but also for checking something is working as intended
  - e.g. check why a port is open and confirm it's closed
- E.g. `nmap -v -p 0-2000 -O -sV 178.128.203.1`
  - `-v`: verbose, more output than usual
    - `-d` prints even more.
  - `-p`: for port
    - default: 0-1024
    - the higher the ranges is the longer it takes.
  - `-O`: os detection (best guess)
  - `-sV`: versions of all detected services (best guess)
    - 💡 Allows you to check for vulnerabilities of a specific version of that services e.g. through [exploit database](https://www.exploit-db.com/)
  - `178.128.203.1`: can also specify subnet also e.g. `/24`
- 🤗 In UK and Germany it's illegal to conduct a scan on a network, more [Nmap | legal issues](https://Nmap.org/book/legal-issues.html)
- Read more about Nmap in [Nmap | Scanning Tools](./../03-scanning-networks/scanning-tools.md#nmap)

## Traceroute

- 📝 Programs used for discovering routers that are on the path to the target host.
- You always go through multiple hops before you reach target
  - E.g. first hop being your router, then routers & switches ISP provider and the router that sends traffic out of the country...
- Helps hacker to collect information about
  - network topology
  - trusted routers
  - firewall locations
- Can use protocols such as `ICMP` (often), `TCP`, `UDP`, `DCPP`..
- ❗ There can be hops that are invisible/undetectable
  - 💡 You can craft special packets to detect them with custom time to lives, their failure
- Uses TTL field in the IP header to discover the route.
  - Starts by setting TTL to 1
  - Stops at each hop on the way to the destination and providing information to the sender about that hop
  - The TTL is incremented by 1 for each hop discovered
- Used to create network diagrams and plan attacks.
- Helps with e.g. man-in-the-middle attacks.
- It records IP addresses and DNS names of discovered routers.
- Commands
  - Unix tool: `traceroute 178.128.203.1` (uses UDP)
  - Using Nmap: `nmap traceroute --script traceroute-geolocation 178.128.203.1 -d`
  - Using hping: `hping3 –traceroute -S {target ip}`
  - Windows tool: `tracert 178.128.203.1` (uses ICMP)
