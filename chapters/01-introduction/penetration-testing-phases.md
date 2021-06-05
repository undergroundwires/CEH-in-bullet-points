# Penetration testing phases

## 1. Pre-Attack Phase

- Planning
- Preparation
- [Reconnaissance](./hacking-stages.md#1-reconnaissance)

### Contracts

- Ethical hackers proceed only after an agreement is in place—to protect both parties.
- **Non-disclosure agreement**
  - Also known as **NDA**
  - 📝 Prohibits you from sharing your findings
- **Penetration testing contract**
  - Should include all information and requirements that the penetration tester needs.
  - Ensures the tester won't be sued or prosecuted and can legally perform an attack.
    - as damage can incur during penetration testing
- 💡 Good idea to go through those with a lawyer.

#### Rules of Engagement (ROE)

- Formal document that gives permission to perform a penetration test.
- 📝 Guideline for testers and as such should clearly state what is and isn't allowed
- E.g. which IP addresses should be tested, which hosts are not to be tested, which techniques, time frame when test can take place etc.
. E.g. ok with SQL injection tests and brute force attacks but no DDoS attacks to not have service disruption or to not have network costs.
- 🤗 Used also by armies, e.g. US army cannot fire on somebody unless they're firing on them.

### Understanding the clients requirements

- Pen-tester needs to understand the client's requirements.
  - 💡 Also make sure client understands that themselves as well as they may not understand what they're asking you to do
- Important for testers reputation and clients satisfaction.
- 💡 Create checklists.
  - Make suggestions
  - Ensure everything is clear without loose ends
  - Best to be clear as changing something during testing is not good as it would postpone the deadline and cost more for the client.

### Defining the scope

- Ensures that requirements are fulfilled, and objectives are met.
- Objectives should be determined first e.g.
  - **Deliverables**: Different reports and often a final report where all results are placed and documented.
  - **Functionality**: Verifies the system you're pen-testing is working as intended
  - **Technical structure**: Design of the whole project
  - **Data definition**
- Defines areas/parts of the system that'll be tested e.g.:
  - Network security
    - E.g. check routers for faulty configurations, outdated operative systems.
  - System software security
  - Client-side application security
  - Client-side to server-side communication security
  - Server-side application security
  - Document security
  - Physical security
    - E.g. how are people tracked? How is access granted and controlled? How are the access policies enforced?
  - Application communication security
  - [Dumpster diving](./../10-social-engineering/social-engineering-types.md#dumpster-diving)
  - Insiders
  - Sabotage intruder confusion
  - Intrusion detection
  - Intrusion response
  - Social engineering

### Information gathering

- To goal is to gather as much information about the target as possible
- Information is used to map out the target's network and plan the attack.
- See also [Reconnaissance | Hacking stages](./hacking-stages.md#1-reconnaissance) and [Footprinting](./../02-footprinting/footprinting-overview.md)
- Information can include
  - **Physical and logical locations**
    - e.g. for servers
  - **Analog connections**
    - E.g. phones, GSM networks
    - 🤗 You can create your own cellphone tower and take over their connections as you'll have the strongest signal.
  - **Contact information**
    - E.g. sitting in a near coffee to take photos and take names. You can then look at their contact information in list of employees (if publicly available somewhere). They become suspectable to social engineering.
  - **Information about other organizations**
    - 🤗 E.g. You can come with a rack suit to fix air-conditioning devices and say "hey there's a problem in air conditioning on floor 14" or "regular maintenance" or "one of your devices is due.". A security personal mey escort you but he won't watch everything carefully, you can place a Raspberry Pie and connect it to electricity. Refer to the following video: [Sneaking in EVERYWHERE for FREE (Yellow Vest Experiment)](https://www.youtube.com/watch?v=GyvRamX1VyA)
      - Stupid and simple. Something too complex has higher risks of not working as the dumber it is, the simple it is, it'll probably work.

## 2. Attack phase

- Phase where target gets compromised.
- Information gathered in the previous one is used to carry out an attack.
- Steps
  1. [Penetrate the perimeter](#a-penetrating-the-perimeter)
  2. [Acquire target](#b-target-acquisition)
  3. [Escalate privileges](#c-privilege-escalation)
  4. [Execute, implant, retract](#d-execute-implant-retract)

### a. Penetrating the perimeter

- Trying to bypass IDS (Intrusion Detection System) and firewall
- A way is to use social engineering to test out the boundaries and find a way into the system.
- **Firewall testing** techniques include
  - ICMP probes
  - Checking access control
  - Evaluating protocol filtering rules
  - Evaluating IDS
- Probing allow you to see what the perimeter detects & drops & won't detect
  - You can craft own packets and see the reactions
    - e.g. by modifying source/destination IPs
  - E.g. check if certain port always drops, maybe port is open but only goes through the VPN where employees access network.
- Figure out what devices are running under perimeter to select as a target.
  - **Enumerate devices** collecting:
    - ID of the device
    - Description
    - Hostname
    - Physical location
    - IP and MAC address
      - 🤗 MAC address lets you know who the manufacturer is. Manufacturer information can give you idea of what kind of OS they run. You might get what devices they are running and how they are shipped. You can go to the distributor and put some physical keyloggers or sniffers e.g. a Raspberry Pi into a large router/switch.
  - By cross checking them later again, it is possible to identify unauthorized devices.

### b. Target acquisition

- Done after scanning and penetrating of the perimeter and selecting a target machine/device
- Involves vulnerability scans to find vulnerabilities which can be later exploited
- 📝 Includes:
  - **Active probing assaults**
    - Scanning the network and gathering more information
  - **Running vulnerability scans**
    - Completing vulnerability scans to see what vulnerabilities that the target has.
  - **Attempt to access services and obtain data**
    - Trusted systems and trusted process assessment
    - Trying to access the resources on the system using the credentials obtained during the information gathering process
      - E.g. using credentials that you have obtained through social engineering or general research of the company/system
    - You attempt to access and extract as much as data as you can
    - Pick-locking: try to unlock it in every possible way

### c. Privilege escalation

- 📝 Done once the access to the system is granted
- Goal is to grant elevated access.
- Techniques include
  - **Password crackers**
    - E.g. bruteforce, dictionary-based attack
  - **Exploit vulnerabilities in a code** e.g.
    - Poorly written security policies
    - False code in the code / applications
    - Web app version is not updated, there's a vulnerability in this version
    - Use flaws in a system e.g. older version of OS.
  - **[Trojans](./../07-malware/trojans.md)**
  - **[Social engineering](./../10-social-engineering/social-engineering-overview.md)**
    - E.g. you realized that there's no strict policy regarding e-mails. You send an e-mail for phishing scheme, gain more information when the person clicks on that link, you can then execute arbitrary code if e-mail client is old (unlikely).
    - E.g. phone-call and ask what you need: works way more than it should
- 🤗 A lot of companies have state-of-the-art perimeter
  - inside perimeter they have very old equipment and OS
  - they don't emphasize much on security interior as they do in external
    - once you pass the perimeter, you're more likely to find something inside
- Defenses include
  - Running services with the least privileged accounts
  - Implementing [multi-factor authentication/authorization](./identity-access-management-(iam).md#multi-factor-authentication-mfa)

### d. Execute, implant, retract

- Involves compromising the system with code.
- Techniques include
  - [DoS, DDoS attacks](./../13-web-applications/denial-of-service.md)
  - buffer overflows to execute arbitrary code.
  - using [viruses](./../07-malware/viruses.md), [trojans](./../07-malware/trojans.md), rootkits
  - installing [backdoor](./../07-malware/malware-overview.md#backdoor)s
- Retract means being able to exit without leaving any traces behind
  - Traces left behind can cause suspicions and in effect vulnerablities would be patched and you cannot gain access to the target machine back using the same method.
  - Delete all the logs that indicates you existed to ensure persistent remote access.
  - Good idea is to figure out their antiviruses, and test your execution in a VM with same antivirus and security measures to not get detected by a random scan.
  - If alarm is raised, you might be detected, put it in the report and result of whether the flag was investigated.

## 3. Post-attack phase

- The tester restores the system to the pretest state.
- ❗Don't leave your stuff be it accidentally or on purpose as it breaks the law either way.
  - Examples
    - Delete any malware/rootkit installed
    - Recover all files that were deleted
    - Reverse any elevated privileges.
    - Restore network settings to its original state
    - Remove created vulnerabilities and exploits
- Documentation / clear log of activities, results and security flaws.
