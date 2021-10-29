# Security threats and attacks

- The more valuable information is the higher the threats and chances for an attack are.

## Security threats

- 📝 **Threat** means anything that has potential of causing damage to the system.

### Types of threats

#### Network threats

- **Network** is the set of devices that are connected through communication channels where data exchange happens between devices
- Attacker may break into the channel and steal the information that is being exchanged.
- E.g. • [denial of service attacks (DoS)](./../13-web-applications/denial-of-service.md) • [password-based attacks](./../06-system-hacking/cracking-passwords-overview.md) • compromised-key attacks, firewall and IDS attacks • DNS and ARP poisoning • man in the middle (MITM) attack • spoofing • [session hijacking](./../13-web-applications/session-hijacking.md) • information gathering • sniffing...

#### Host threats

- Attack that tries to gain access to information from a system
- E.g. • [password attacks](./../06-system-hacking/cracking-passwords-overview.md) • unauthorized access • profiling • [malware attacks](./../07-malware/malware-overview.md) • [footprinting](./../02-footprinting/footprinting-overview.md) • [denial of service attacks (DoS)](./../13-web-applications/denial-of-service.md) • arbitrary code execution • privilege escalation • [backdoor attacks](./../07-malware/malware-overview.md#backdoor) • [physical security](./physical-security.md) threats

#### Application threats

- Exploitation of vulnerabilities that exists in the application itself
  - Caused by e.g. bad coding practices
  - Rushed programs has mistakes e.g. lack of validation of input data
- Can be found through reverse engineering, or trial and error
- Large codes that are difficult to maintain has more vulnerabilities.
- Mostly because of improper input validation.
- E.g. • [SQL injection](./../14-sql-injection/sql-injection-overview.md) • cross-site scripting • [session hijacking](./../13-web-applications/session-hijacking.md) • identity spoofing • improper input validation • security misconfiguration • information disclosure • [hidden-field manipulation](./../13-web-applications/hacking-web-applications.md#hidden-field-manipulation) • broken session management • [cryptography attacks](./../15-cryptography/cryptanalysis.md#cryptography-attacks) • [buffer overflow attacks](./../12-web-servers/web-server-threats-and-attacks.md#buffer-overflow-attacks) • [phishing](./../10-social-engineering/social-engineering-types.md#phishing)

## Security attacks

- Or **cyber attack**
- Attempt to gain unauthorized access to a system or network.
- Actualization of a threat

### Motives

- Attack = Motive + Vulnerability + Method (exploit)
- General core of every motives is access to the valuable information
- Common motives:
  - Interrupting the flow of business activities and processes
  - Stealing valuable information
  - Data manipulation
  - Stealing money and important financial information
  - Revenge
  - Ransom

### Types of attacks

- You need to find vulnerability in a system to have an attack
- You can never prove that's its not vulnerable, but can prove it's vulnerable.
  - or You can never prove that a system is secure, but can prove it's insecure.

#### Operating system attacks

- ❗ If OS is taken over protecting applications won't matter.
- Vulnerabilities include
  - Bugs (as it's a big codebase)
  - Buffer overflow
  - Unpatched operating systems
    - Can lead to successful leads using already known vulnerabilities
    - 🤗 E.g. Microsoft had already patched the [EternalBlue vulnerability](https://en.wikipedia.org/wiki/EternalBlue) that NSA developed before it was leaked to public. However, many systems still remained unpatched due to users not updating their systems. So the same vulnerability on unpatched systems were still successfuly exploited by first [WannaCry ransomware](https://en.wikipedia.org/wiki/WannaCry_ransomware) that compromised hundreds of thousands computers, and then by [NotPetya malware](https://en.wikipedia.org/wiki/Petya_(malware)). [1]
- Attacks include
  - Exploiting network protocol implementations
  - [Authentication attacks](./../13-web-applications/hacking-web-applications.md#authentication-attacks)
  - [Cracking passwords](./../06-system-hacking/cracking-passwords-overview.md)
  - Breaking filesystem security
- 💡 Secure OS is an OS that's updated, monitored, regulated as frequently as possible.
- See also [banner grabbing](./../03-scanning-networks/banner-grabbing.md)

[1]: https://en.wikipedia.org/wiki/EternalBlue

#### Misconfiguration attacks

- Hacker gains access to the system that has poorly configured security.
- Can affect works, databases, web servers, etc.
- E.g. • using default accounts (passwords) • forgetting Apache server online to allow proxy requests enabling DDoS attacks
- 💡 Detected mostly by automated scanners

#### Application-level attacks

- Similar to OS attacks but far less damaging as their scope is far narrower.
- Caused by lack of testing as developers rush development of applications and miss something.
- E.g. • sensitive information disclosure • buffer overflow attack • SQL injection v cross-site scripting • session hijacking denial of service • man in the middle • phishing
- 🤗 E.g. Transmission torrent client (macOS)
  - The store where it was downloaded was compromised
  - They substituted torrent download link to their own application
  - See [Transmission is hacked to spread malware](https://blog.malwarebytes.com/threat-analysis/2016/09/transmission-hijacked-again-to-spread-malware/)

#### Shrink-wrap code attacks

- Attacks on libraries and frameworks that the software is depended on.
- Finding vulnerabilities in libraries allows re-using same exploits on more than single application
- 💡 Use libraries: older, more mature, maintained, updated actively with proven track record.
- E.g.
  - A bug is fixed in library but application uses older version.
  - Application uses libraries in debug mode or with default configurations.

### Attack vectors

- Attack vector = Means by which hackers deliver a payload to systems and networks
- [Cloud computing threats](./../16-cloud-computing/cloud-security.md#cloud-computing-risks-and-threats) such as data breach and loss.
- [IoT threats](./../18-iot-and-ot/iot-security.md#iot-threats) usually caused by insecure devices and hardware constraints (battery, memory, CPU etc.)
- [Ransomware](../07-malware/malware-overview.md#ransomware): Restricts access to your files and requires payment to be granted access
- [Mobile threats](./../17-mobile-platforms/mobile-attacks.md#mobile-threats)

#### Advanced Persistent Threats (APT)

- 📝 Stealthy threat actor with continuous attacks targeting a specific entity.
- APT groups include:
  - [APT 10 - Red Apollo @China](https://en.wikipedia.org/wiki/Double_Dragon_(hacking_organization))
  - [Equation Group @USA](https://en.wikipedia.org/wiki/Equation_Group)
  - [APT 29 - Cozy Bear @Russia](https://en.wikipedia.org/wiki/Cozy_Bear)
  - and [many more](https://en.wikipedia.org/wiki/Advanced_persistent_threat#APT_groups)...
- **Advanced**
  - Uses special malware, often crafted for specific organizations
    - Usually a modified version of common malware used in botnets
  - Sophisticated techniques against target not generic
- **Persistent**
  - Long-term presence with external command and control
  - Extracting data
    - Usually ***low-and-slow*** to avoid detection
    - E.g. instead of sending big data, it breaks data to chunks and sends each chunk whenever a user is connected to the internet
- **Threat**
  - Targets high value organizations and information
  - E.g. governments and big companies
- 🤗 E.g.
  - [Sony Pictures hack](https://en.wikipedia.org/wiki/Sony_Pictures_hack) where sensitive data from Sony, e.g. unreleased movies was published as torrents.
  - [2020 United States federal government data breach](https://en.wikipedia.org/wiki/2020_United_States_federal_government_data_breach) where more than 18.000 US companies and government agencies where hacked.
- Common steps
  1. Create a breach e.g. through spear phishing
  2. Exploit inner system vulnerabilities
  3. Control of the system or its segments
  4. Data exfiltration (= unauthorized data transfer)

#### Viruses and worms

- Both can replicates themselves throughout the system in files, documents.
- Have capabilities to infect systems and networks in a quick time.
- [Virus](./../07-malware/viruses.md): Requires user action to be activated e.g. running a file that has a virus embedded.
- [Worm](./../07-malware/malware-overview.md#worm): can spread independently without any user action i.e. self-replicating

#### Botnet

- 📝 Used by hackers to control the infected machines e.g. phones, PC, IoT
- Hackers perform malicious activities from the machines on which bots run eg. DDoS attacks.
- Main problem is lack of security software or proper updates on devices.
- See also [Botnet trojans](./../07-malware/trojans.md#botnet-trojans) and [Botnets | Denial of Service](./../13-web-applications/denial-of-service.md#botnets)

#### Insider attacks

- Performed by a person from within the organization who has authorized access.
  - E.g. disgruntled employee, employee paid by a third-party
- Presents one of the greatest potential of risk and most difficult attacks to defend against.
- See also [Insider attacks | Social engineering types](./../10-social-engineering/social-engineering-types.md#insider-attacks).

##### Insider threat types

- **Pure insider**
  - Inside employee with normal access rights
- **Elevated pure insider**
  - Insider with elevated access
- **Insider associate**
  - Insider with limited authorized access (e.g. guard, cleaning person)
- **Insider affiliate**
  - Spouse, friend, or client of an employee that uses employee's credentials.
- **Outsider affiliate**
  - Unknown and untrusted person from outside the organization.
  - Uses an open access channel or stolen credentials to gain unauthorized access.

##### Insider attack countermeasures

- Restricting access
- Logging to know who access what at what point of time
- Active monitoring of employees with elevated privileges
- Trying to not have disgruntled employees
- Separation of duties
  - Also known as **segregation of duties**
  - Concept of having more than one person required to complete a task.
  - See also [Separation of duties | Cloud computing](./../16-cloud-computing/cloud-computing.md#separation-of-duties)

#### Phishing

- See [Phishing | Social Engineering Types](./../10-social-engineering/social-engineering-types.md#phishing)

#### Web application threats

- Takes advantage of poorly written code and lack of proper validation of input and output data.
- E.g. buffer overflows, SQL injections, cross-site scripting
- 💡 There are many online scanning tools to detect those.

## Modern age information warfare

- Use of information and communication technologies for competitive advantages over an opponent
- Weapons include • viruses • worms • trojan horses • logic bombs • trap doors • nano machines and microbes • electronic jamming • penetration exploits and tools.
- E.g.
  - Corporations spy on each other to use each others technology secrets and patents
    - 🤗 Also known as [Industrial espionage](https://en.wikipedia.org/wiki/Industrial_espionage)
  - Governments spy on other governments by using hackers as proxies to gain information about e.g. defense systems.
  - Intellectual property thefts with reverse engineering to create products without investing in R&D
- Categories include:
  - **Command and control (C2) warfare**
    - Taking down the command center may protect the headquarters but may interfere with their mobility
  - **Intelligence-based warfare**
    - Sensor-based technology to disrupt systems
  - **Electronic warfare**
    - Enhance, degrade, or intercept the flow of information
  - **Psychological warfare**
    - "Capture their minds and their hearts and souls will follow"
    - E.g. propaganda or terror
  - **Hacker warfare**
    - Acquire information about subject A, sell it to subject B.
  - **Economic information warfare**
    - Channeling or blocking information to pursue economic dominance
  - **Cyber warfare**: use of information systems against virtual personas
- Each category can have:
  - **Offensive strategy**
    - Attacks against an opponent
    - E.g. web application attacks, malware attacks, system hacking..
  - **Defensive strategy**
    - Actions taken against attacks.
    - E.g. monitoring, alerts, response, detection, prevention systems
- See also [Information Warfare website](http://www.iwar.org.uk)
