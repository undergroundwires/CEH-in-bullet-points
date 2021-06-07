# Mobile attacks

## Mobile threats

- Takes advantage of the lack of security control in smartphones
- Can also be caused by a malicious app
- Older OS versions have known vulnerabilities
  - Patched in newer versions but users may not update them.
  - Vendors may not update phones after a while, maybe before warranty period.
- Vendors having own modified version of Android increases security risks
- Data transmission threats through [Bluetooth](./../09-wireless-networks/bluetooth.md), [WiFi](./../09-wireless-networks/wireless-threats-and-attacks.md), 3G/4G/5G or wired connection to a computer.

## Attack vectors

## Attacks on the device

- **Malicious code signing**
  - Obtaining a code-signing key from the code signing service to create a malicious application
- **JAD File Exploit**
  - Attacker crafts a `.jad` file with spoofed information
  - Java Application Description (`.jad`) contains attributes of Java application

### Browser-based attacks

- **Framing**
  - Integrating another page through `iframe` element of HTML
  - Enables clickjacking to steal information
- **Man-in-the-Mobile**
  - Also known as • **MitMo** • **Man-in-the-Phone**
  - Malware to spy on e.g. SMS OTPs (one-time passwords) or voice calls and relay them back to the hackers
- **Buffer Overflow**
  - Caused by not truncating input data when it's longer than the reserved space and leads to overwriting other data in memory.
  - 📝 Both iOS and Android are vulnerable as they use C/C++ in their kernels
- **Data caching**
  - Inspected to gain sensitive information stored in them
- [Clickjacking](./../13-web-applications/hacking-web-applications.md#clickjacking)

#### Phishing

- Redirecting uses to legitimate looking malicious sites through e.g. pop-ups, emails
- Mobile users are more vulnerable due to smaller size of the browsers, URLs, warnings etc.
- See also [Phishing | Social Engineering](../10-social-engineering/social-engineering-types.md#phishing)

### Phone/SMS-based attacks

- **Baseband Attacks**
  - Exploits GSM/3GPP processor (exchanges radio signals with cell towers)
- See [Mobile-based social engineering | Social engineering types](./../10-social-engineering/social-engineering-types.md#mobile-based-social-engineering) including e.g. • SMS phishing (SMSiShing) • Fake security apps • Repackaging legitimate apps • Malicious apps

### Application-based attacks

- Sensitive data storage
- No encryption / weak encryption
- Improper SSL validation
- Configuration manipulation
  - E.g. through external configuration files
- Dynamic runtime injection
  - E.g. stealing data in memory
- Unintended permissions
- Escalated privileges
- Access to device and User info
- Third-party code
- Intent hijacking
- Zip directory traversal
- Side channel attack
- UI overlay/pin stealing
- Intent hijacking
- Clipboard data
- URL schemes
- GPS spoofing
- Weak / no local authentication
- Integrity / tampering / repackaging
- Unprotected app signing key
- App transport security

### System attacks

- Malware
  - Attacks the underlying system
- No passcode / weak passcode
- iOS jailbreaking
- Android rooting
- OS data caching
- Accessible passwords and data
- Carrier-loaded software
  - Through e.g. bloatware
- No encryption / weak encryption
- User-initiated Code
- Zero-day exploits
- Device lockout
- Kernel driver vulnerabilities
- Confused deputy attack
- TEE/secure enclave processor
- Side-channel leakage
- Multimedia/file format parsers
- Kernel driver vulnerabilities
- Resource DoS
- GPS spoofing

## Network attacks

- [Wi-Fi](./../09-wireless-networks/wireless-threats-and-attacks.md)
  - E.g. no-encryption or weak encryption
- Rogue Access Point
- [Packet sniffing](./../08-sniffing/sniffing-attacks-overview.md)
- Man-in-the-Middle (MITM)
  - **SSLStrip**: websites are downgrades to use HTTP
  - **Fake SSL certificates** issued by attacker
- [Session hijacking](./../13-web-applications/session-hijacking.md)
- [DNS poisoning](./../08-sniffing/sniffing-attacks-overview.md#dns-poisoning)
- BGP hijacking
- [HTTP proxies](./../03-scanning-networks/bypassing-ids-and-firewall.md#proxy-servers)
- **Sidejacking**
  - Listening to traffic to steal exchanged cookies to extract session IDs

## Data center/cloud attacks

### Web server attacks

- Platform vulnerabilities in OS and server software
- Server misconfiguration
- [**Cross-site scripting (XSS)**](./../13-web-applications/owasp-top-10-threats.md#cross-site-scripting-xss)
- Cross-site forgery (XSRF)
- Weak input validation
- [Brute force attacks](../15-cryptography/cryptanalysis.md#brute-force-attack)
- Cross Origin Resource Sharing
- [Side channel attack](./../16-cloud-computing/cloud-security.md#side-channel-attacks)
- Hypervisor attack
- VPN

### Database attacks

- [SQL injection](./../14-sql-injection/sql-injection-overview.md)
- [Privilege escalation](./../06-system-hacking/escalating-privileges.md)
- Data dumping
- OS command execution
