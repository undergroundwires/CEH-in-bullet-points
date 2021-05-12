# Cloud security

- Cloud providers implement
  - Limited access and access policies
  - Access logs
  - Ability to require access reason against repudiation

## Trusted Computing (TC)

- Attempts to resolve computer security problems through hardware enhancements
- **Roots of Trust (RoT)**: set of functions within TCM that are always trusted by the OS

## Cloud computing threats

- **Stealing information from other cloud users**
  - Internal threats where employees copying company data with bad intentions e.g. to trade.
  - Most of those breaches are not published & advertised to media.
  - Information might include e.g. credit numbers, social security numbers
- **Data loss**
  - Deleting data stored on the cloud through viruses and malware
  - ❗High impact if there are no back-ups
- **Attack on sensitive information**
  - Stealing information about other users e.g. financial data.
- **A hacker can utilize computer power** to e.g.
  - crack passwords with many password attempts per seconds
  - DDoS attacks
- **Shadow IT**
  - IT systems or solutions that are developed to handle an issue but aren't taken through proper approval chain
- **Abusing cloud services**
- **Insecure interfaces and APIs** e.g. weak authentication
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
  - E.g. in [2020 United States federal government data breach](https://en.wikipedia.org/wiki/2020_United_States_federal_government_data_breach) a compromised global administrator account has assigned credentials to cloud service principals that allowed malicious access to cloud systems.
- **Virtualization level attacks**
- **Privilege escalation via error**
- **Service termination and failure**
- **Hardware failure**: can be mitigated by using more zones in cloud.
- **Natural disasters**: can be mitigated by using more regions in cloud.
- **Weak authentication**
  - E.g. burden of managing identity both on-premises and on cloud
    - Allows compromise on on-premises systems to spread to cloud.
    - Allows adding a malicious certificate trust relationship in cloud for forging SAML tokens on-premises.
- **DDoS** attacks using cloud computing.
- **Compliance risks** e.g. laws regarding data transfer across borders

## Cloud computing attacks

- **[Social engineering attacks](./../10-social-engineering/social-engineering-overview.md)** e.g. password guessing
- **[Cross Site Scripting (XSS)](./../13-web-applications/owasp-top-10-threats.md#cross-site-scripting-xss)**
- **DNS attacks** e.g. DNS poisoning, domain hijacking
- **SQL injection** to to gain unauthorized access to a database.
- **Network sniffing** e.g. obtain credentials, cookies
- **Session hijacking** e.g. cookie stealing
- **Cryptanalysis attacks** e.g. weak encryption
- **DoS (Denial-of-service)**
- E.g. In [2020 United States federal government data breach](https://en.wikipedia.org/wiki/2020_United_States_federal_government_data_breach), used TTP were stealing SAML tokens to attack [SSO](./../01-introduction/identity-access-management-(iam).md#single-sign-on-sso) infrastructure according to [TTP analysis from NSA](https://media.defense.gov/2020/Dec/17/2002554125/-1/-1/0/AUTHENTICATION_MECHANISMS_CSA_U_OO_198854_20.PDF).

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

## Cloud security tools

- [CloudInspect](https://www.coresecurity.com/core-labs/open-source-tools/core-cloudinspect)
  - Penetration-testing as a service from Amazon Web Services for EC2 users
- [CloudPassage Halo](https://www.cloudpassage.com/cloud-computing-security/)
  - Automates cloud computing security and compliance controls
