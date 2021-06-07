# Penetration Testing

- Simulating of an security attack to
  - discover vulnerabilities (and document)
  - evaluate the security
- Detailed analysis of weaknesses in design, technical flaws, and vulnerabilities in organizations information security.
- E.g. • [phishing](./../10-social-engineering/social-engineering-types.md#phishing) • [testing authentication](./../13-web-applications/hacking-web-applications.md#authentication-attacks) using [dictionaries](./../06-system-hacking/cracking-passwords-overview.md#dictionary-attack) • test if router is using an [obsolete OS](./security-threats-and-attacks.md#operating-system-attacks)

## Purpose

- Identify threats
- Reduce security expenses
  - E.g. you can recommend cheaper router and switches that'll be enough for their capacity and still secure.
  - **ROSI = Return on security investment**
    - E.g. you'll save company for 100% payback if they implement anti-junk system and junk e-mails cost more to the company.
- Provide complete security assessment
- Maintain industry standards and regulations
- Follow best practices
- Test security controls
- Improve current security infrastructure
- Pay particular attention to severe vulnerabilities
  - E.g. explain what one single vulnerability can lead to what kind of damage.
- Prepare steps for preventing exploitations
- Test network security devices

## Activities for a good penetration test

- Defining the penetration test parameters
  - States what pen-tester can do and cannot do.
  - Have both signed.
- Engaging skilled penetration testers
- Following non-disclosure agreement
  - Companies don't want to work with someone with bad reputation, e.g. who broke NDA before.
- Selecting appropriate tests
  - Done by the company and the pen-tester together
  - Find cost/benefit ratio of tests
- Using and following a [methodology](#security-testing-methodology)
  - 💡 Good to test for all known vulnerabilities to save time and make documentation easier.
- Documenting the results of the test
- Creating a final report

## Audit vs Vulnerability Assessment vs Penetration Test

### Security audit

- Compliance = Inspects if an organization is following security standards and policies.
- E.g. interviewing staff, vulnerability scans, reviewing access controls, analyzing physical access.
- Often [blue/red teaming](#blue-and-red-teaming) approach is used by penetration testers.

### Vulnerability assessment

- Finds the vulnerabilities in the network
- Will not state if they're exploitable, nor the potential harm

### Penetration test

- Includes both [security audit](#security-audit) + [vulnerability assessment](#vulnerability-assessment)
- Discovers vulnerabilities in a system and evaluates its security
- Demonstrates how attackers can exploit the identified vulnerabilities.
- Tells you what measures should be taken to prevent the vulnerabilities.

## Blue and red teaming

- Two teams in company, or sometimes outside of the company who battles against each other.
- Similar to capture the flag contest, red is aggressor, blue protects.
- More cost-efficient then hiring an external company to do full penetration testing.
- **Blue team**
  - Defender: Detects attackers (red team) and predict possible attacks.
  - Has full access to the system to analyze the security.
- **Red team**
  - Attacker: Finds vulnerabilities in the system and penetrates to examine what real attackers could do.
  - Has no access to the system
- **Purple team**
  - Both worlds
  - Both attacks and also repairs/suggests improvements

## Types of penetration testing

- Consists of [white box](#white-box-testing), [black box](#black-box-testing) and [grey box](#grey-box-testing) testing.
  - 💡 The darker the box is the more credible test results and the higher the costs are. As going from nothing to something as opposed to something to nothing would simulate real-world hacks but would take more time.
- 📝 Each type can be
  - Announced vs. Unannounced
    - **Announced testing**
      - IT team are aware of security being tested.
      - Often it occurs when testing a specific segment where IT admins give you access to test different components.
    - **Unannounced testing**
      - IT team is unaware of the security being tested
  - Internal vs External
    - **Internal**
      - Targets assets within an corporate network
    - **External**
      - Targets internet-facing assets such as web, mail and FTP servers.

### Black box testing

- Also called ***zero-knowledge Testing***, ***blackbox testing*** or ***black-box testing***
- 📝 Testers have very little information about the client's infrastructure.
- The goal is to simulate an external hacking or cyber warfare attack.
- provides a very realistic scenario for testing of the defenses
- Can be costlier as it takes much more time to conduct.

#### Blind testing

- Tester has little information to none about target.
- Target itself (e.g. system administrator) knows about the test and its scope.
- Demonstrates what a real attacker would do.

#### Double-blind testing

- Also called **zero-knowledge approach**
- Neither the pen-tester nor the target knows anything about each other.
- Good & reliable results
- Most difficult, time-consuming and expensive to perform.

### Grey box testing

- Also called ***greybox testing***, ***grey-box testing***, ***gray box testing***, ***graybox testing***, ***gray-box testing***
- 📝 Tester has partial knowledge i.e. knowledge of the internal workings is limited.
- Combination of black box and white box testing.
- Helps to reduce the cost of the test by gaining knowledge that would be harder to gain otherwise.

### White box testing

- Also called ***Complete-Knowledge Testing***, ***whitebox testing*** or ***white-box testing***
- 📝 Tester knows the company inside out
  - fully aware of the network, infrastructure policies.
  - e.g. ap of the subnets, ruling list of firewalls, intrusion detection system details.
- Cost-effective and can be good when testing a single component

## Security testing methodology

- Approach to attempt to find vulnerabilities in the system's security mechanisms.
- Used during e.g. [security audit](#security-audit), [vulnerability assessment](#vulnerability-assessment) and [penetration test](#penetration-test).
- 💡 Using a good security testing methodology provides a repeatable framework

### Proprietary methodologies

- Usually done by security companies who offer pen testing services and as such are kept confidential.
- Includes
  - **IBM**
    - Good for mid-sized companies
    - Gives fast result without much effort
  - **McAfee Foundstone**
    - Used mainly in enterprises.
    - Anything that's custom not generic has big chance of slipping through
  - **EC-Council LPT**
    - Auditing framework

### Open-source Methodologies

- Publicly available and can be used by anyone

#### OWASP (Open Web Application Security Project)

- Online community, produces freely-available articles, methodologies, documentation, tools, and technologies in the field of web application security
- Produces Top 10 lists of the most common vulnerabilities and how to fix them.
  - E.g. • [Web Application Top 10 threats](./../13-web-applications/owasp-top-10-threats.md) • [Docker Top 10](./../16-cloud-computing/container-security.md#owasp-docker-top-10) • [Top 10 Mobile Threats](./../17-mobile-platforms/mobile-attack-vectors.md#owasp-top-10-mobile-threats)
- Good for developers and system architects (anyone working with coding/application)

#### OSSTMM (Open Source Security Testing Methodology Manual)

- Open-source security testing methodology manual
- Standard set of penetration testing tests
  - Attempt to standardize pen-testing and making consistent
- Defines three types of compliance:
  - **Contractual**: requirements enforced by an industry or non-government group.
  - **Legislative**: regulations enforced by the government.
  - **Standards based**: actions that are recommended and must be adhered to in order to be certified by a group.

#### ISSAF (Information Systems Security Assessment Framework)

- Like an instruction manual "how to conduct a pen-test"

#### NIST (National Institute of Standards and Technology)

- Federal technology agency
- Applies a lot of standards to comply.
- They do much research and publish most.
- E.g. • [NIST SP 800-53](./laws-standards-and-regulations.md#nist-sp-800-53) • [NIST definition of cloud computing](../16-cloud-computing/cloud-computing.md#nist-definition-of-cloud-computing)
