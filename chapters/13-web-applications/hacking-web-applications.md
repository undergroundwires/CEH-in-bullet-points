# Hacking web applications

- Web Application: UI to interact with web servers

## Web application architecture

### Service-oriented architecture

- Also known as • **SOA** • **service oriented architecture**
- Architecture-driven software design
- Software components deliver information to other components usually over a network.
- E.g. a company might develop an API that provides software programming access to a specific database, which would then let other developers build applications that could leverage the API to query or upload data.

### Multi-tier architecture

- Also known as • **multitier architecture** • **n-tier architecture** • **multilayered architecture**
- Each layer is developed and maintained as independent modules
- Every layer can exist without the layers above it, and requires the layers below it to function.

#### Three-tier architecture

1. 📝 **Client/presentation layer** e.g. HTML, CSS, JavaScript...
   - GUI to interact with users
   - 💡 Place in DMZ layer
2. 📝 **Business layer** e.g. C#, Java, Python, C++...
   - Also known as **logic layer**, **middle layer**, **business logic layer** or **domain layer**
   - Handles requests and response (return data from browser)
   - Includes **application layer**
     - Encapsulates the API definition surfacing the supported business functionality
     - ❗ In some conventions such as Domain Driven Design it's a separate layer above domain layer, making the architecture 4-tier.
   - 💡 Place in internal network
3. 📝 **Database layer** database server e.g. MySQL, Oracle, MongoDB
   - Also known as **data access layer**, **data**, **infrastructure** or **persistance** layer
   - 💡 Place in internal network

## Web 2.0

- **Web 1.0** (around 1991 - 2004)
  - Static pages instead of dynamic HTML
  - Data provided from filesystem instead of a database
  - Guestbooks
  - GIF buttons
  - HTML forms sent via email
- **Web 2.0** (> 2004)
  - Rich user experience: dynamic and responsive content
  - User participation: users create user-generated content for other users to see
  - Software-as-a-Service: APIs to allow automated usage
  - Mass participation: Near-universal web access instead of hackers and computer hobbyists as in Web 1.0.
  - **Facilitates**
    - Interoperability: • Blogs • Gaming • Dynamic • RSS
    - User-centered design: • Social networking • Mash-ups (emails, payments) • WIKIs • Location services
    - Collaboration: • Cloud computing • Interactive encyclopedias and dictionaries • Online office software

### Vulnerability stack

- Each [OSI layer](./../03-scanning-networks/tcpip-basics.md#osi-model) contains sensitive data that can help the attacker.
- 📝 Vulnerabilities in one layer is independent of vulnerabilities in another layer.
- Layers

  | Layer | Web element / service | Description |
  | ----- | ------------- | --------------- |
  | Layer 7 | Web application | Business logic flaws, technical vulnerabilities |
  | Layer 6 | Third party applications | Open source or commercial |
  | Layer 5 | Web server | E.g. • Apache • IIS |
  | Layer 4 | Database | E.g. • MySql • Oracle |
  | Layer 3 | OS | E,g, • Linux • Windows • macOS |
  | Layer 2 | Network | • Router • Switch |
  | Layer 1 | Security | • IPS / IDS |

## Web application hacking methodology

1. Web infrastructure footprinting
   - Server discovery: servers, location, ports
   - Hidden content discovery e.g. through web crawling
   - E.g. using telnet
     1. `telnet <target-url-or-ip> 80` to create a telnet connection
     2. Press "ESC" to get some information
   - 📝 E.g. using OpenSSL (TLS/SSL toolkit & library) with `s_client` (SSL/TLS client)
     - E.g. to get cipher used:
       - `openssl s_client -connect <target website> -port 443`
       - or `openssl s_client -connect <target website>:443`
2. Web server attack to exploit identified vulnerabilities
   - Client-side controls evasion e.g. [attacking hidden form fields](#hidden-field-manipulation)
   - Launch web server attack to exploit identified vulnerabilities, launch DoS

## Web application threats

- [**OWASP Top 10 Threats**](./owasp-top-10-threats.md)
  - • Injection • Broken authentication • Sensitive data exposure • XML External Entities (XXE) • Broken Access Control • Security misconfiguration • Cross-Site Scripting (XSS) • Insecure deserialization • Using components with known vulnerabilities • Insufficient logging and monitoring
- [**Web-server threats**](../../chapters/12-web-servers/web-server-threats-and-attacks.md)
  - • Denial-of-Service (DoS) • Buffer Overflow
- **Obfuscation application**: Obfuscated attacks using e.g. different encodings.
- **Broken account management**
  - Vulnerabilities in e.g. account update, password reset/recovery and other functions.
- **Platform Exploits**
  - Platforms that websites are built with/built on might have vulnerabilities

## Web application attacks

- **Web services Attack**
  - Exploiting an application integrated with vulnerable web services
- Authentication Hijacking
- **CAPTCHA Attacks**
  - CAPTCHA
    - Challenge–response test used in computing to determine whether or not the user is human
    - 🤗 Also known as **reverse Turing test**.
  - Attacks includes e.g. using deep learning to break semantic image
- **Network access attacks**
  - Allows access that HTTP protocol does not allow
- Application logic vulnerabilities such as poor coding

### DMZ protocol attacks

- By compromising a system that allows DMZ protocols, attacker can reach other DMZs and internal systems.
- Can lead to • compromising application and data • [website defacement](./../12-web-servers/web-server-threats-and-attacks.md#website-defacement) • unauthorized access to other internal systems.

### Hidden field manipulation

- Also known as • **hidden form values attack** • **hidden-field manipulation**
- Allows attacker to manipulate hidden values in forms such as product prices.
- Mostly against e-commerce websites

### Database connection (data connectivity) attacks

- Connection string injection
  - Appends to connection string with `;`
- Connection String Parameter Pollution (CSPP) Attacks
  - Overwrite parameter values in application where values are provided dynamically based on user input.
- Connection Pool DoS by injecting a large SQL query.

### Unvalidated redirects and forwards

- Attacker tricks victim into clicking legitimate-looking but malicious links.
- **Unvalidated redirect**
  - E.g. user sees `cloudarchitecture.io` but as the link is `cloudarchitecture.io/?redirect=evilsite.com` the user ends up on `evilsite.com`
  - **Watering Hole Attack**
    - 📝 Infecting website that's frequently visited by target with malware to attack the victim.
    - Usually website checks IP and only infects the target.
    - Websites are often infected through zero-day vulnerabilities on browsers or other software
    - Type of unvalidated redirect attack as it redirects the victim to the malware download.
    - 🤗 Named as watering hole since the attacker waits for the victim to fall into the trap, similar to a lion waiting for its prey to arrive at waterhole to drink water
- **Unvalidated forward**
  - E.g. appending `?forward=admin` ends up on admin page without validation.
- Can lead to attacks including • Session Fixation Attack • Security Management Exploits • Failure to Restrict URL Access • Malicious File Execution

### Web parameter tampering

- Attacker manipulates parameters to modify data
- 📝 Common types
  - **Changing a value in a hidden tag** e.g.
    - `<input type="hidden" name="price" value="59.90">`
  - **Adding a non-existing value to a combobox** e.g.
    - `<select name="accounts"><option value="755">755</option></select>`
    - Only one account is selectable but attacker changes HTML to add a new option.
  - **Changing parameter in an URL** e.g.
    - Legitimate URL is `https://cloudarchitecture.io/transfer?account=12345&amount=1`
    - Attacker changes is sto `https://cloudarchitecture.io/transfer?account=67890&amount=9999`
  - **Adding a new parameter to grant unauthorized**
    - Legitimate URL is `https://cloudarchitecture.io/getpage.asp?id=77492&mode=readonly`
    - Attacker removes `&mode=readonly` parameter.
- Read more on [OWASP](https://owasp.org/www-community/attacks/Web_Parameter_Tampering)

### Authentication attacks

- Username enumeration
- Poisoning (tampering)
- Sniffing replay
- [Exploiting cookies](#cookie-attacks) to bypass authentication.
- Session attacks: • Session prediction • brute forcing • poisoning
- Password attacks: • Guessing • brute force
- Verbose failure messages
- Predictable user names

### Authorization attacks

- Finds legitimate accounts then slowly escalates privileges
- Sources include URI, POST data, HTTP headers, cookies, hidden tags

### Session management attacks

- Goal is to impersonate targets
- Attacks include
  - session token prediction
  - session token tampering
  - session token sniffing
- Can be done through [cookie attacks](#cookie-attacks) as session token is often stored as a cookie.
- Gaining token allows • MITM • session hijacking • session replay.

### Cookie attacks

- **Cookie poisoning**
  - Also known as **cookie tampering**
  - E.g. a **cookie parameter tampering** would be changing `isAdmin: false` to `isAdmin: true`
- 📝 **Cookie sniffing**
  - Capturing cookies sent over a wired or wireless connection
  - Usually used to login as user to bypass authentication
- **Cookie snooping**
  - Looking inside cookies for valuable data, such as weakly encrypted logon credentials.
  - Can be used to reveal user surfing patterns and sold by e.g. spywares

#### Cookie

- An HTTP cookie is information stored on users computer by browser as instructed by website.
- **Session cookie**
  - Also known as an • **in-memory cookie** • **transient cookie** • **non-persistent cookie**.
  - A cookie that does not contain an expiration date.
  - Stored in memory and never written on disk
  - Browsers normally delete session cookies when the user closes the browser.
- A countermeasure is to disable cookies on the browser.
- Some poorly written applications may store password/username in a cookie.

#### Cookie exploitation tools

- [OWASP Zed Attack Proxy](https://github.com/zaproxy/zaproxy): Can use cookie for attacks.
- [Burp Suite](./../05-vulnerabilities/vulnerability-analysis.md#burp-suite): Can use cookie for attacks through burp proxy.
- [XSSer](https://github.com/epsylon/xsser): For cookie injection (XSS)

### Clickjacking

- Also known as ***user interface redress attack***, ***UI redress attack***, ***UI redressing***
- 📝 Tricks user to clicking something different from what they perceive
- `X-Frame-Options` header in web applications provides protection against it.
- E.g. showing app on top another app to give away sensitive information
