# Common vulnerabilities

## Shellshock

- Also known as ***bashdoor*** or ***bash bug***
- Privilege escalation vulnerability enabling arbitrary commands execution
- 📝 Caused by family of security bugs in the Unix Bash shell
- Related CVE entries include: • *CVE-[2014-6271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6271)*, *CVE-[2014-6277](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6277)* • *CVE-[2014-6278](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2014-6278)*, *CVE-[2014-7169](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-7169)* • *CVE-[2014-7186](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-7186)*, *CVE-[2014-7187](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-7187)*
- Achieved by manipulating the environment variable list and then cause Bash to run
- Upon startup Bash parser executes scripts saved as environment variables
- E.g. `$ env x='() { :;}; echo vulnerable' bash -c "echo this is a test"`
  - Prints first `vulnerable` then `this is a test`
- To exploit there needs to be away to talk to Bash.
- Often exploits websites using CGI
  - CGI stands for "Common Gateway Interface"
  - In Apache it's done using [mod_cgi](https://httpd.apache.org/docs/2.4/mod/mod_cgi.html)
    - Way to let Apache execute script files and send the output to the client
    - Apache passes information to CGI scripts using environment variables
  - E.g. if you you have a HTTP header named `Sike` in your request, you will have an
environment variable named `HTTP_SIKE` available in your CGI.
- Big impact
  - Thousands of attacks were reported when the bug was revealed including botnets against [United States Department of Defense](https://en.wikipedia.org/wiki/Shellshock_(software_bug)#cite_note-IT-20140926-JS-10).
  - > "Shellshock makes Heartbleed look insignificant" - [ZDNet](https://www.zdnet.com/shellshock-makes-heartbleed-look-insignificant-7000034143/)

### Detecting Shellshock using Nmap

- Can use [Shellshock script](https://Nmap.org/nsedoc/scripts/http-shellshock.html) with Nmap scripting engine.
- `nmap -sV -p 80 --script http-shellshock --script-args uri=/cgi-bin/blabla.sh,cmd=ls 192.168.122.17.8`
  - `-sV`: detect services and versions
  - `-p`: port 80, you can also do -p- to scan for entire port range
  - `--script`: You can test different scripts / vulnerabilities, choose anything from [scripts page](https://Nmap.org/nsedoc/scripts)
  - `--script-args`: optional, 2 args, uri and cmd

## SSL/TLS Vulnerabilities

### Heartbleed

- 📝 Bug in [OpenSSL](https://www.openssl.org/) library a widely used implementation of TLS.
- Introduced and patched in April 2014.
- Results from improper input validation (no boundary check) in TLS heartbeat extension
- Causing server to send more data in the memory than it allowed
  - Classified as **buffer over-read**
- Flow
  - TLS/DTLS Heartbeat flow:
    - Client: `Send me 4 letter word: "bird"` -> Server: `"bird"`
  - Malicious Heartbeat flow:
    - Client: `Send me 500 letter word: "bird"` -> Server: `bird. Server master key is 3131531535. User Carol wants to change password to "password 1 2 3"...`
- **Reverse Heartbleed**
  - Malicious server exploiting Heartbleed to read from client memory.
- Millions of webpages were affected, still there are IoT devices are vulnerable (see [shodan search](https://www.shodan.io/report/0Wew7Zq7))
- Had big impact, some known ones are [stealing of millions of patient records](http://time.com/3148773/report-devastating-heartbleed-flaw-was-used-in-hospital-hack/), [hijacking accounts CEO impersonation](https://www.bbc.co.uk/news/technology-27028101) ....
  - > "Heartbleed is the worst vulnerability found" - [Forbes](https://www.forbes.com/sites/josephsteinberg/2014/04/10/massive-internet-security-vulnerability-you-are-at-risk-what-you-need-to-do/)
- Can be exploited
  - Using Nmap: `nmap -p 443 --script ssl-heartbleed <target>`
    - Will return "State: NOT VULNERABLE" if not vulnerable.
  - Using Metasploit: [openssl_heartbleed](https://github.com/rapid7/metasploit-framework/blob/master/documentation/modules/auxiliary/scanner/ssl/openssl_heartbleed.md) module

### POODLE

- POODLE stands for "Padding Oracle On Downgraded Legacy Encryption"
- 📝 Forcing a degradation to a vulnerable SSL/TLS version
  - TLS handshakes are walked down the connection until a usable/vulnerable one is found
  - Exploits backwards compatibility
- Man-in-the-middle exploit
- Affects both SSL and TLS
  - Vulnerability was disclosed in October 2014 for SSL.
  - A variation used to attack TLS was disclosed in December 2014.
- **POODLE attack against SSL**
  - Takes advantage of Internet and security software clients' fallback to SSL 3.0.
  - Attackers make 256 SSL 3.0 request on average to reveal a single byte.
- **POODLE attack against TLS**
  - Caused by some implementation not following the TLS specifications.
  - Exploits CBC encryption mode in the TLS 1.0 - 1.2 protocols

### FREAK

- Stands for "Factoring RSA Export Keys"
- Man-in-the-middle attack forcing downgrade of RSA key to a weaker length
- Enables successful brute-force attacks.
- Exploits cryptographic weakness in the SSL/TLS protocols

### SSL/TLS Renegotiation

- 📝 Leads to plaintext injection attacks against SSL 3.0 and all current versions of TLS
- **Background**
  - Marsh Ray and Steve Dispensa release a document discussing a vulnerability in the design of TLS – November 4, 2009
  - Turkish grad student, Anil Kurmus, exploits the vulnerability to steal Twitter login credentials – November 10, 2009
- **Mitigation**
  - Quick fix was the renegotiation
  - Proposed standard ([RFC 5746](https://tools.ietf.org/html/rfc5746)) is to verify previous renegotiation handshakes between client and server.
- **Testing**
  - Use `open_ssl s_client -connect <website>:443`
  - Then type `R` for renegotiate and `[ENTER]`

### DROWN

- Stands for "Decrypting RSA with Obsolete and Weakened eNcryption"
- Exploits modern SSL/TLS suites by exploiting their obsolete SSLv2 protocol support.
- The only viable countermeasure is to disable SSLv2 on all servers
