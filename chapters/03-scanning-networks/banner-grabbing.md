# Banner grabbing

- **Banner information** = name + version
- 📝 Used to gain banner information about
  - a computer (e.g. OS information)
  - the services running on its open ports (e.g. nginx server)
- Allows attackers to exploit known vulnerabilities and form an attack plan.
- Can be prevented by disabling banners and by hiding web page extensions.

## Passive banner grabbing

- Uses sniffing to determine the operating system.
- E.g. analyzing error messages, sniffing the traffic on the network, and examining page extensions.

## Active banner grabbing

- Sending a packet to the OS and then analyzing the responses.
- E.g. each OS have different TCP/IP stack implementations.
  - Values of TTL (time to live) and TCP window size in the IP header of the first packet are different in each OS.
- HTTP (80), FTP (21), SMTP (25) are common ports.
- Tools include `telnet`, [`nmap`](./scanning-tools.md#nmap), [`zgrap`](https://github.com/zmap/zgrab2) and `netcat`.

### Banner grabbing tools

- `nmap -O` for OS automatic fingerprinting, see also [`-O`: OS fingerprinting | Scanning tools](./scanning-tools.md#-o-os-fingerprinting)

#### Netcat

- Networking utility for reading from and writing to network connections using TCP or UDP
- 🤗 Also known as TCP/IP swiss army knife
- **FTP**
  - `nc 178.128.203.1 21`: Checks FTP port 21
    - 💡 You can use `nmap 178.128.203.1` to find out open ports.
  - Usual for FTP servers to return something like `Welcome to XXX FTP Server`
    - gives you insights about the owner and that it's a FTP server
- **HTTP**
  - E.g.
    1. `nc 178.128.203.1 80`
    2. Type e.g. `GET /index.html HTTP 1.0` or `HEAD / HTTP/1.1`
    3. Press `[ENTER]`
  - And also usually useful headers such as `Server: Apache/2.4.6 (CentOS)`
- [CryptCat](http://cryptcat.sourceforge.net/) is the encrypted version of netcat

#### Telnet

- Application protocol for bidirectional interactive text-oriented communication using a virtual terminal connection
- Historically used to access to a command-line interface on a remote host but now replaced with [SSH](./../15-cryptography/tunneling-protocols.md#ssh-secure-shell) as it's unsecure.
- Built into many operative systems as default
- Runs on port 23 so `telnet <target>` sends TCP to targets port 23.
  - You can send to different ports using `telnet`
- If port is open a banner response received looking like:
  - `Server: Microsoft-IIS/5.0 Date: Fri, 14 Aug 2009 1:14:42 GMT Content-Length:340 Content-Type: text/html`
