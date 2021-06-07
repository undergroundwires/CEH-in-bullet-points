# Evading IDS

- See also [SQL evasion](./../14-sql-injection/sql-injection-overview.md#sql-evasion)
- See also [bypassing IDS and firewall when scanning](../03-scanning-networks/bypassing-ids-and-firewall.md), [evading firewalls](evading-firewalls.md)

## Obfuscation

### Path obfuscation

| Type | Clear-text | Obfuscated-text |
| -- | -- | -- |
| Self-referencing directories | `/etc/passwd` | `/etc/./passwd` |
| Double slashes | `/etc//passwd` | `/etc/passwd` |
| Path traversal | `/etc/passwd` | `/etc/dummy/../passwd` |
| Windows folder separator | `../../cmd.exe` | `..\..\cmd.exe` |
| IFS (Unix shells) | `/etc/passwd` | `CMD=X/bin/catX/etc/passwd;eval$CMD` |

### URL encoding

- E.g. `http://cloudarchitecture.io/paynow.php?p=attack` becomes `http://cloudarchitecture.io/paynow.php?p=%61%74%74%61%63%6B`
- **Null-byte attacks**
  - Evasion technique and attack at the same time (to get unauthorized access to server files)
  - Effective against applications
    - developed using C-based languages
    - using native file manipulation
  - Can be done by appending `%00`

### Unicode encoding

#### Unicode

- Provides unique identifier for every character in every language
- Facilitates uniform computer representation of the world's languages
- Each character can be represented by U+xxxx where x is a hexadecimal digit.

#### Unicode encoding attack

- Also known as **UTF-8 encoding**
- Presenting information in an unusual way to confuse the signature-based IDS
- 📝 A very common way to evade IDS
- E.g. instead of `http://vulneapplication/../../appusers.txt` using `http://vulneapplication/%C0AE%C0AE%C0AF%C0AE%C0AE%C0AFappusers.txt`

### Encryption

- 📝 Most effective evasion attack
- IDS becomes unable to analyze packets going through these encrypted communications
- E.g. [SSH](./../15-cryptography/tunneling-protocols.md#ssh-secure-shell), [SSL](./../15-cryptography/encrypting-communication.md#ssl-secure-sockets-layer)/[TLS](./../15-cryptography/encrypting-communication.md#tls-transport-layer-security), or [OpenVPN](./../15-cryptography/tunneling-protocols.md#openvpn) tunnel

### Polymorphism

- Using polymorphic shellcode to create unique network patterns to evade signature detection
- E.g. by encoding payload by XORing and putting the decoder in the start of the payload where the target runs the decoder when it executes the code
- Tools include [ADMMutate](https://github.com/K2/ADMMutate): A shellcode mutation engine, can evade NIDS

## Denial of service

- If IDS fails, it allows the traffic to go through
- Passive IDSes are vulnerable as they are fail-open.
- E.g.
  - by exploiting a bug in the IDS, consuming all of the computational resources on the IDS
  - deliberately triggering a large number of alerts to disguise the actual attack.

## False positive generation

- Also known as ***flooding*** or ***false-positive generation***
- 📝 Designed to create a great deal of log noise in an attempt to blend real attacks with the false
- Attackers craft packets known to trigger alerts within the IDS, forcing it to generate a large number of false reports
- Similar to the DoS method is to generate a large amount of alert data that must be logged
- Make is difficult legitimate attacks and false positives by looking at logs
- Can even generate false positives specific to an IDS if attacker has knowledge of IDS used.
- Tools include [inundator](http://inundator.sourceforge.net/): intrusion detection false positives generator.

## Insertion attack

- Exploited by sending packets to an end-system that it will reject but IDS will think are valid.
- By doing this the attacker is ***inserting*** data into the IDS
- Allows attacker to defeat signature analysis and to slip attacks past an IDS.
- An IDS can accept a packet that an end-system rejects.
  - also misbelieving that the end-system has accepted and processed the packet
- As signature analysis use pattern-matching in a stream of data to detect strings.
  - E.g. IDS can easily detect `phf` in HTTP request.
    - But the attacker insert data and make it look like e.g. `pleasdontdetectthisforme` where only `phf` part is sent to the original stream.
- A countermeasure would be making IDS as strict as an end-system to minimize this attacks
  - however it then allows for evasion attacks.

## Session splicing

- Splits the attack traffic in to many packets such that no single packet triggers the IDS.
- Network level attack
- ❗ Not the same as [IP fragmentation](../03-scanning-networks/bypassing-ids-and-firewall.md#packet-fragmentation)
  - Session splicing concerns just HTTP payload in chunks to prevent string matches by IDS.
- Send parts of the request in different packets
  - E.g. `"GET / HTTP/1.0"` may be split across multiple packets to be
    - `"GE"`, `"T "`, `"/"`, `" H"`, `"T"`, `"TP"`, `"/1"`, `".0"`
- Tools include [Nessus](./../05-vulnerabilities/vulnerability-analysis.md#nessus) or [Whisker](#whisker)

## Tools

- [`fragroute`](https://tools.kali.org/information-gathering/fragroute) for [packet fragmentation](../03-scanning-networks/bypassing-ids-and-firewall.md#packet-fragmentation)
- Different scanners such as `nmap` has also [options to evade IDS](https://Nmap.org/book/subvert-ids.html#avoid-ids).
- Also many web vulnerability scanners can be used such as [Nikto](./../05-vulnerabilities/vulnerability-analysis.md#nikto)], [Whisker](#whisker) and [Nessus](./../05-vulnerabilities/vulnerability-analysis.md#nessus)

### Whisker

- Also known as `libwhisker`
- Open-source [perl module](https://sourceforge.net/projects/whisker/) for HTTP-related functions, including vulnerability scanning and exploitation.
- 📝 Helps also to evade IDS with [session splicing](#session-splicing) and tactics including:

  | Name | Explanation/Example |
  | ---- | ------------------ |
  | Method matching | GET -> HEAD |
  | URL encoding | HEX %xx notation |
  | Double slashes | `/` -> `//` |
  | Reverse traversal | `/dir/blahblah/../` |
  | Self-reference directories | `/dir/./././././ == /dir/` |
  | Premature request ending | stop at the first `HTTP/1.?\r\n` |
  | Parameter hiding | `%3f` -> `?` |
  | HTTP mis-formatting | `%20` -> `%09 (TAB)` |
  | Long Urls | `GET /<random>/../dir/a.cgi` |
  | DOS/Win directory syntax | `'/'` -> `\` |
  | NULL method processing | `GET\0` |
  | Case sensitivity | `'abc' -> 'ABC` |
