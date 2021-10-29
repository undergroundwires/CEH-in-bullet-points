# Cloud security

- Cloud providers implement
  - Limited access and access policies
  - Access logs
  - Ability to require access reason against repudiation

## Trusted Computing (TC)

- Attempts to resolve computer security problems through hardware enhancements
- **Roots of Trust (RoT)**: set of functions within TCM that are always trusted by the OS

## Cloud computing risks and threats

- **Stealing information from other cloud users**
  - Internal threats where employees copying company data with bad intentions e.g. to trade.
  - Most of those breaches are not published & advertised to media.
  - Information might include e.g. credit numbers, social security numbers
- **Data loss**
  - Deleting data stored on the cloud through viruses and malware
  - ❗ High impact if there are no back-ups
- **Attack on sensitive information**
  - Stealing information about other users e.g. financial data.
- Attacker utilization of cloud infrastructure e.g.
  - **Using compute power** to crack passwords with many password attempts per seconds
  - **DDoS** attacks using cloud computing
- **Shadow IT**
  - IT systems or solutions that are developed to handle an issue but aren't taken through proper approval chain
- **Abusing cloud services**
- **Insecure interfaces and APIs**
  - E.g. weak authentication
- **Insufficient due diligence**
  - Moving an application without knowing the security differences
- **Shared technology issues**
  - Multi-tenant environments that don't provide proper isolation
  - If the hypervisor is compromised, all hosts on that hypervisor are as well
- **Unknown risk profile**
  - Subscribers don't know what security provisions are made behind the scenes.
- **Inadequate infrastructure design and planning**
- **Conflicts between client hardening procedures and cloud environment**
- **Malicious insiders**
- **Illegal access to the cloud**
  - E.g. in US data breach in 2020 a compromised global administrator account has assigned credentials to cloud service principals that allowed malicious access to cloud systems [1]
- **Virtualization level attacks**
- **Privilege escalation via error**
- **Service termination and failure**
- **Hardware failure**
  - 💡 Can be mitigated by using more zones in cloud.
- **Natural disasters**
  - 💡 Can be mitigated by using more regions in cloud.
- **Weak authentication**
  - E.g. burden of managing identity both on-premises and on cloud
    - Allows compromise on on-premises systems to spread to cloud.
    - Allows adding a malicious certificate trust relationship in cloud for forging SAML tokens on-premises.
- **Compliance risks**
  - E.g. laws regarding data transfer across borders
- **Cloud cryptojacking**
  - 📝 Hijacking cloud resources to mine for cryptocurrency
  - Often targeted on IaaS platforms through malware

[1]: https://en.wikipedia.org/wiki/2020_United_States_federal_government_data_breach "2020 United States federal government data breach"

## Cloud computing attacks

- **[Social engineering attacks](./../10-social-engineering/social-engineering-overview.md)** e.g. password guessing
- **[Cross Site Scripting (XSS)](./../13-web-applications/owasp-top-10-threats.md#cross-site-scripting-xss)**
- **DNS attacks** e.g. DNS poisoning, domain hijacking
- **SQL injection** to to gain unauthorized access to a database.
- **Network sniffing** e.g. obtain credentials, cookies
- **Session hijacking** e.g. cookie stealing
- **Cryptanalysis attacks** e.g. weak encryption
- **DoS (Denial-of-service)**
- E.g. In 2020 United States federal government data breach [1]

[1]: https://en.wikipedia.org/wiki/2020_United_States_federal_government_data_breach "2020 United States federal government data breach"

### Wrapping attack

- Also known as **XML rewriting** attack
- Changes the content of the signed part without invalidating the signature.
- Intercepting a SOAP message and sending/replaying envelope with changed data.

### Session riding

- Happens when an attacker steals a user's cookie to use the application in the name of the user
- Simply [CSRF](./../13-web-applications/session-hijacking.md#cross-site-request-forgery-csrf) in cloud

### Side channel attacks

- Also known as • **cross-guest virtual machine breach** • **cross-guest VM breach**
- Attacker controls a VM on same physical host (by compromising one or placing own)
- Attacker can then take advantage of shared resources (processor cache, keys, ...)
- Can be installed by a malicious insider or an impersonated legitimate user

### Cloud Hopper attack

- 📝 Targets managed service providers (MSPs) and their users
- 📝 Initiated by delivering malware through [spear-phishing](./../10-social-engineering/social-engineering-types.md#spear-phishing) emails
- Goal is to compromise the accounts of staff or cloud service firms to obtain confidential information
- Flow [2]
  1. Infiltrate the service provider
  2. Once inside, find system administrator  who controls the company jump servers with connection to client networks
  3. Map victim network and identify sensitive data
  4. Encrypt and exfiltrate the data either through victim or the service provider
- 🤗 Named after attacks by Chinese cyber spies [2] to MSPs in countries such as UK, USA and Sweden [1]

[1]: https://en.wikipedia.org/wiki/Red_Apollo#2014_to_2017:_Operation_Cloud_Hopper "Operation Cloud Hopper | Wikipedia"
[2]: https://www.reuters.com/investigates/special-report/china-cyber-cloudhopper/ "Inside the West's failed fight against China's 'Cloud Hopper' hackers | Reuters"

### Cloudborne attack

- Done by exploiting a specific BMC  vulnerability
- 📝 Bare-metal / firmware level attack
  - Allows injecting code/backdoors
  - Affects IaaS providers that gives bare-metal access without access to the actual firmware
    - Impacting businesses that use bare metal cloud offerings
  - Survives client switches (customer customer re-assignments) performed by the provider
  - Targets baseboard management controller (BMC) firmware
    - BMC enables remote management of a server for initial provisioning, OS reinstall and troubleshooting [1] [2]
- Mitigated by IBM through factory firmware reset before re-provisioning hardware to other customers [2]
- Allows attacks such as
  - permanent denial-of-service (PDoS) on bare metal server
  - stealing data from application running on the server
  - ransomware attacks
- Revealed by Eclypsium (Firmware protection firm) in 2019 based on IBM SoftLayer cloud services [1]

[1]: https://eclypsium.com/2019/01/26/the-missing-security-primer-for-bare-metal-cloud-services/ "The Missing Security Primer for Bare Metal Cloud Services | eclypsium.com"
[2]: https://www.ibm.com/blogs/psirt/vulnerability-involving-ibm-cloud-baseboard-management-controller-bmc-firmware/ "Vulnerability involving IBM Cloud Baseboard Management Controller (BMC) Firmware | IBM"

### Man-In-The-Cloud (MITC) attack

- 📝 Done by using file synchronization services (e.g. Google Drive and Dropbox) as infrastructure
  - E.g. as command and control (C&C), data exfiltration, and remote access.
- Makes it hard to
  - distinguish malicious traffic from normal traffic
  - discover and analyze evidence due to not leaving footprint on endpoint devices
- E.g. Switcher malware [1]
  1. Installs attackers token and moves victim's real token into *sync folder* folder to be synced
  2. Victim device is synced to attackers attacker account
  3. Attacker uses original account token and erase malicious one
  4. Removes traces of the security breach

[1]: https://www.helpnetsecurity.com/2019/01/21/mitc-attack/ "Beware the man in the cloud: How to protect against a new breed of cyberattack | Help Net Security"

## Cloud security tools

- [CloudInspect](https://www.coresecurity.com/core-labs/open-source-tools/core-cloudinspect)
  - Penetration-testing as a service from Amazon Web Services for EC2 users
- [CloudPassage Halo](https://www.cloudpassage.com/cloud-computing-security/)
  - Automates cloud computing security and compliance controls
- [privacy.sexy](https://github.com/undergroundwires/privacy.sexy)
  - Open-source solution to increase privacy by reducing third party cloud-based data collection
  - Can also be used to harden virtual machine images and OSes that are talking to cloud services
