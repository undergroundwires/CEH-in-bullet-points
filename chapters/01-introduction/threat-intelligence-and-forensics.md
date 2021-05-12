# Threat intelligence and forensics

## Cyber kill chain

- Framework for identification and prevention of cyber intrusions activity.
- Developed by [Lockheed Martin](https://www.lockheedmartin.com/)
- Identifies what the adversaries must complete in order to achieve their objective.
- 🤗 Based on military kill chains, a concept consisting of • target identification • force dispatch to target decision • order to attack the target • the destruction of the target
- 🤗 Critiques states it only defends "perimeter" and isn't suitable model to insider threats.
- E.g. [A "Kill Chain" Analysis of the 2013 Target Data Breach](https://www.commerce.senate.gov/services/files/24d3c229-4f2f-405d-b8db-a3a67f183883)

### Cyber kill chain steps

- ❗ Not same in every organization as different organizations have constructed their own kill chains to try to model different threats

1. **Reconnaissance**
   - Collecting as much as information about the target.
   - E.g. harvesting email addresses, conferece information etc.
   - See also [footprinting](./../02-footprinting/footprinting-overview.md)
2. **Weaponization**
   - Analyzing collected data to identify and vulnerabilities to exploit to gain access
   - E.g. creating a [phishing](./../10-social-engineering/social-engineering-types.md#phishing) campaign based on collected data
3. **Delivery**
   - Weaponized bundle to the victim via email, web, USB, etc.
   - Key to measure the effectiveness of the defense strategies implemented by the target.
   - E.g. sending [phishing](./../10-social-engineering/social-engineering-types.md#phishing) emails
4. **Exploitation**
   - Execute code on victim's system.
   - E.g. arbitrary code execution, authentication and authorization attacks
5. **Installation**
   - Installing malware on the asset
   - E.g. [backdoor](./../07-malware/malware-overview.md#backdoor) to gain remote access and maintain access in the network
6. **Command and control**
   - Allows remote manipulation/exploation of victim
   - Done by establishing two-way communication between the victim and the attacker.
   - Evidence is usually hidden using [encryption techniques](./../15-cryptography/encryption-algorithms.md)
7. **Actions on objectives**
   - With hands-on access, intruders accomplish their original goals.
   - E.g. • distrupting network • gaining access to confidential data

### Defensive courses of action

1. **Detect**: determine whether an attacker is poking around
2. **Deny**: prevent information disclosure and unauthorized access
3. **Disrupt**: stop or change outbound traffic (to attacker)
4. **Degrade**: counter-attack command and control
5. **Deceive**: interfere with command and control
6. **Contain**: network segmentation changes

## Threat identification

### Tactics, Techniques, and Procedures (TTPs)

- Concept in terrorism and cyber security studies
- Identifies patterns of behavior of the threat actors (= bad guys)
- Aids in
  - counterintelligence for threat prediction and detection
  - implementing defenses
  - profiling threat actors e.g. [APT groups](security-threats-and-attacks.md#advanced-persistent-threats-apt)
- E.g. In [2020 United States federal government data breach](https://en.wikipedia.org/wiki/2020_United_States_federal_government_data_breach), used TTP were stealing SAML tokens to attack [SSO](identity-access-management-(iam).md#single-sign-on-sso) infrastructure according to [TTP analysis from NSA](https://media.defense.gov/2020/Dec/17/2002554125/-1/-1/0/AUTHENTICATION_MECHANISMS_CSA_U_OO_198854_20.PDF).
- Read more at [NIST Special Publication 800-159](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-150.pdf)

#### Tactics

- Also called **tools** in the acronym
- Highest-level description of the behavior
- Describes ways attacker attacks from start to end
- E.g.
  - Way of gathering information e.g. [open-source intelligence](./../02-footprinting/footprinting-overview.md#open-source-intelligence-osint), [social engineering](./../10-social-engineering/social-engineering-overview.md).
  - Way of initial compromise e.g. tools, zero-day vulnerabilities, obfuscation methods

#### Techniques

- Technical methods used by an attacker
- Gives a more detailed description of behavior in the context of a [tactic](#tactics).
- E.g.
  - [social engineering techniques](./../10-social-engineering/social-engineering-types.md) in early stages
  - exploit tools at middle stages
  - and software tools to clear logs to cover tracks at later stages.

#### Procedures

- Lower-level, highly detailed description in the context of a [technique](#techniques).
- Sequence of actions done by attackers
- E.g. an actor collects business e-mails of target company then launches a [spear phishing](./../10-social-engineering/social-engineering-types.md#spear-phishing) campaign

#### Adversary behaviors

- Method or techniques used by attacker to penetrate victim network.
- E.g. using PowerShell, [DNS Tunneling](../11-firewalls-ids-and-honeypots/evading-firewalls.md#dns-tunneling), [Web Shell](../06-system-hacking/escalating-privileges.md#privilege-escalation-techniques) etc.

#### Indicators of Compromise (IoCs)

- Artifacts observed that indicates computer intrusion with high confidence.
- 4 categories:
  - **Email indicators**
    - E.g. sender's email address, subject, attachment, links.
  - **Network indicators**
    - E.g. URLs, domain names, IP addresses, unusual DNS requests
  - **Host-based indicators**
    - E.g. filenames, file hashes, registry  keys, DDLs, mutex
  - **Behavioral indicators**
    - E.g. memory code injection, remote command execution, document execution PowerShell script.
