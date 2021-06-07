# Hacking web servers

## Web server

- System used for storing, processing, and delivering websites
- Hosts web applications, allowing clients to access those applications
- Implements client-server model architecture where client can be e.g. a browser or an API.

### Web server concepts

- **Document root**
  - Root directory of servable documents
  - E.g. HTML, JS, image files...
- **Server root**
  - Root directory of all the code that implements the server.
  - Stores configuration, log, and executable files
- **Virtual document tree**
  - Used when the original disk becomes full
  - Located sometimes on different disk, possibly on a different machine
- **Virtual hosting** is multiple sites on a single server
- **Web proxy**
  - Also known as **HTTP proxy**
  - Server placed between the client and server
  - All requests coming from the client go through the proxy to the server
    - instead of directly going to the server
- **Open-source Web Server Architecture**
  - Typically uses
    - **Linux** as an OS
    - **Apache** as a web server
    - **MySQL** as a database
    - **PHP (LAMP)** as principal components.
- **Internet Information Service (IIS)**
  - Web server application developed for Windows Server

## Web server hacking methodology

1. **Information gathering** e.g.:
   - Acquiring `robots.txt` to see directories/files that are hidden from web crawlers.
   - Internet searches, WHOIS
   - 📝 Testing HTTP methods
     - Checks for `GET`, `HEAD`, `POST`, `OPTIONS`, `DELETE`, `PUT`, `CONNECT`, `TRACE`
     - Risky methods are `DELETE`, `PUT`, `CONNECT`, `TRACE` and should be [disabled](https://wiki.owasp.org/index.php/Test_HTTP_Methods_(OTG-CONFIG-006))
     - `nmap --script http-methods <target>`
2. **Footprinting**
   - E.g.
     - List email addresses: `nmap --script http-google-email`
     - Enumerate common web apps `nmap --script http-enum -p80`
   - Tools: [Netcraft](./../02-footprinting/search-engines-and-online-resources.md#netcraft), HTTPRecon, ID Serve, HTTPrint, [Nmap](./../03-scanning-networks/scanning-tools.md#nmap)
   - See also [Banner grabbing](./../03-scanning-networks/banner-grabbing.md)
3. **Mirror** the target website to browse it offline
   - Tools: • Wget • [BlackWidow](http://softbytelabs.com/wp/blackwidow/) • HTTrack • WebCopier Pro • Web Ripper • SurfOffline
4. Discover vulnerabilities using e.g.:
   - 📝 **[Nikto](https://github.com/sullo/nikto)**
     - Web-server scanner focusing on • misconfigurations • outdated/insecure files
     - Read more in [Vulnerability analysis | Nikto](../05-vulnerabilities/vulnerability-analysis.md#nikto)
   - **[Metasploit](./../05-vulnerabilities/automated-penetration-testing-tools.md#metasploit)**
     - Find, exploit and validate vulnerabilities
5. Perform [**session hijacking**](./../13-web-applications/session-hijacking.md) and [**password cracking**](./../06-system-hacking/cracking-passwords-overview.md) attacks

## Web server hacking tools

- [Wfetch](https://support.microsoft.com/en-us/help/284285/how-to-use-wfetch-exe-to-troubleshoot-http-connections): Microsoft tool to customize and send HTTP requests
- [THC Hydra](https://github.com/vanhauser-thc/thc-hydra): login cracker which supports numerous protocols to attack
- [HULK DoS](https://github.com/grafov/hulk): DoSer
- [w3af](http://w3af.org): web application security scanner
- [Metasploit](./../05-vulnerabilities/automated-penetration-testing-tools.md#metasploit): Penetration testing suit

## Web server hacking countermeasures

- Patch and update server regularly
- Encrypt the traffic.
  - See also [Encrypting communication | Cryptography](./../15-cryptography/encrypting-communication.md)
- Enforce code access security policy
- Monitor logs
- Use website change detection system
  - Check server files with hash comparison and alert if any modifications has happened.
- Filter traffic to [SSH](./../15-cryptography/tunneling-protocols.md#ssh-secure-shell) server
- Default passwords and unused default accounts should be changed and disabled respectively.

### Place web servers securely

- Place web servers in separate secure server security segment on network
- Recommend to have three layered web application network: Internet, DMZ, internal
  - See also [Multi-tier architecture | Hacking web applications](./../13-web-applications/hacking-web-applications.md#multi-tier-architecture)
- Place web servers in DMZ zone isolated from public network as well as internal network.
  - See also [Network security zoning | Network security](./../01-introduction/network-security.md#network-security-zoning)
- Each layer should have its own firewalls
  - See also • [Zone-based firewall | Firewall](./../11-firewalls-ids-and-honeypots/firewall-overview.md#zone-based-firewall) • [Screened subnet firewalls | Firewall](./../11-firewalls-ids-and-honeypots/firewall-overview.md#screened-subnet-firewalls)

### Securing ports

- Audit the ports regularly
- Disabling insecure and unnecessary ports.
- Use Port 443 HTTPS over port 80 HTTP.

### Using certificates

- Ensure validity of certificate data ranges and certificate's public key
- See also [Digital certificate | Cryptography](./../15-cryptography/encrypting-communication.md#digital-certificate)

### Securing IIS

- [Securing your web server | Microsoft docs](https://docs.microsoft.com/en-us/previous-versions/msp-n-p/ff648653(v=pandp.10))
  - `Machine.config`
    - Disable tracing (`<trace enable="false"/>`)
    - Turn off debug compiles.
  - 📝 Remove unnecessary ISAPI extensions and filters
    - Allows custom Web Request handling
    - Exploited heavily by attackers in the past.
