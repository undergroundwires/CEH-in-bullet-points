# Intrusion detection system (IDS) overview

- Detects intrusions in real time and alerts
- Can filter the traffic and alert the security personnel
  - Also known as ***intrusion detection and prevention systems (IDPS)*** or ***intrusion prevention systems (IPS)***
- Inspects both incoming (inbound) and outgoing (outbound) traffic
- Can be a software or hardware
- Usually placed near the firewall
  - Inside or outside depending on which traffic is being monitoring
  - 💡 Good to deploy on both places (before and after DMZ) for layered defense

## Intrusion types

- **Filesystem intrusion**
  - Unexpected creation/deletion/modification of files or file attributes (e.g. permissions)
- **Network intrusion**
  - Increase in bandwidth consumption
  - Unexpected incoming connections e.g. attempted logins
  - Sudden increase of logs can be caused by DoS/DDoS
- **System intrusion**
  - Missing/modified for log, system or configuration files
  - Degradation in system performance
  - Unfamiliar processes, system reboots, crashes

## IDS types

### Network-based vs Host-based IDS

- Comparison

  | | [NIDS](#network-based-intrusion-detection-systems-nidss) | [HIDS](#host-based-intrusion-detection-systems-hidss) |
  |-|----|----|
  | Strength | Sensing attacks from outside | Sensing attacks from inside that NIDS cannot examine |
  | Packet headers | Examines | Does not understand |
  | Host | Independent | Dependent |
  | Bandwidth | In need of | Does not require |
  | Performance | Slows down networks where it's installed | Slow down hosts where it's installed |
  | Attack types | Senses network attacks as payload is analyzed | Senses local attacks before they hit the network |
  | False positive rate | High | Low |
  
- See also [WIDS (Wireless Intrusion Detection system)](./../09-wireless-networks/wireless-security-tools.md#wireless-intrusion-detection-systems-wids)

#### Network-based intrusion detection systems (NIDSs)

- Also known as ***network-based IDS***
- Inspects each incoming packet for anomalies and suspicious patterns.
- Can detect DoS attacks, port scans, or break-in attempts.

##### Network tap

- Typically a hardware device, which provides a way to access the data flowing across a computer network.
- Provide IDS visibility into the traffic flowing over the network
- E.g. a hub connected on the segment or a network appliance created specifically for the task

##### Snort

- [Open-source](https://www.snort.org) NIDS that's most widely deployed
- Rule-based IPS to detect and stop packages
- Can block expressions such as
  - ` /(\%27)|(\')|(\-\-)|(\%23)|(#)/ix`
  - `/((\%27)|(\'))union/ix`

###### Snort configurations

- Alerts are defined in Snort configuration file
  - Configuration file is at `/etc/snort`, or `C:\Snort\etc`
- Can be configured to use as:
  - packet sniffer
    - E.g. `snort -vde`
  - packet logger
    - E.g. `./snort -dev -l ./log`
  - Network intrusion detection system by
    - Does not drop packets
    - Evaluates packets to check all alert rules, logging the matches.
    - E.g. `./snort -dev -l ./log -h 192.168.1.0/24 -c snort.conf`
  - Network intrusion protection System

###### Snort rules

- All rules are checked for each packet
- If multiple matches are found:
  - Alerts the most unique (specific) rule ignoring the more generic one.
- 📝 **Syntax**
  - Action protocol address port -> address port (option:value;option:value)
  - E.g. `alert tcp 10.0.0.1 25 -> 10.0.0.2 25 (msg:"Sample Alert"; sid:1000;)`

#### Host-Based intrusion detection systems (HIDSs)

- Also known as ***host-based IDS***
- 📝 Analyzes behavior and events on a particular host e.g. a desktop PC or a server.
- Can detect both anomalies and unauthorized changes in the filesystem.
- Log file monitoring (LFM): Monitoring logs files for malicious events.
- **File integrity checking**
  - Checking for modified files e.g. [ossec-hids](https://github.com/ossec/ossec-hids)
  - Compares the current hash value of the file against its known-good hash value.
- E.g. [Windows Defender](https://www.microsoft.com/en-us/windows/comprehensive-security), [Norton Internet Security](https://us.norton.com/internet-security)..

### Active vs passive IDS

#### Active IDS

- Also known as **Intrusion Detection and Prevention System (IDPS)** or **Intrusion Protection Systems (IPS)**
- Configured to automatically block suspected attacks without any intervention required by an operator

#### Passive IDS

- Configured to only monitor and analyze network traffic activity and alert
- Does not perform any protective or corrective functions on its own

### Signature-based vs Anomaly-based IDS

- 💡 Recent systems uses both (hybrid approach) to cover each others flaws

#### Signature recognition

- Also known as ***misuse detection***, ***signature based IDS*** or ***signature-based IDS***
- 📝 Compares incoming and outgoing traffic to the signatures of already known attacks
- Based on a database of previous attack signatures and known system vulnerabilities.
- A signature is a recorded evidence of an intrusion or attack
- 📝 **Pros**
  - Little false positives
  - No need for a training phase, starts working out of the box
- 📝 **Cons**
  - Vulnerable to unique attacks, easy to fool
  - High dependency of latest updates, constant maintenance
  - Signature data consumes traffic

#### Anomaly detection

- Also known as ***not-use detection***, ***behavior based IDS*** or ***behavior-based IDS***.
- 📝 Analyzes characteristics of the system's users and components and looks for deviations.
- Learns pattern of normal system activity to identify active intrusion attempts.
- Deviations from this baseline or pattern cause an alarm to be triggered.
- Can use artificial intelligence or can be based on heuristics or rules
- 📝 **Pros**
  - More suitable for blocking future unknown attacks
  - Low dependency of latest updates, constant maintenance
- 📝 **Cons**
  - Higher false positive alarm rates
  - Challenging to construct a model thoroughly on a regular network.

##### Protocol anomaly detection

- Identifies anomalies specific to a protocol
- Uses a model of the different ways vendors deploy the TCP/IP protocol.

## IDS alerts

- 📝 **IDS alert types**
  - **True positive**: Attack + Alert
  - **False positive**: No attack + Alert
  - **True negative**: No attack + No alert
  - **False negative**: Attack + No alert
  - 💡 False negatives are considered far worse than false positives
- 📝 **IDS alert thresholding**
  - Also known as ***alert throttling*** or ***event filtering***.
  - Reducing the volume of repeated alerts
  - E.g. ignore alerts after nth times during X minutes

## Firewall vs IPS vs IDS

| | [Firewall](./firewall-overview.md) | IPS | IDS |
| --------- | ------- | ------ |
| **Abbreviation for** | - | Intrusion Prevention System | Intrusion Detection System |
| **Firewall** | Filters incoming and outgoing network traffic based on predetermined rules | Inspects traffic, detects it, classifies and then proactively stops malicious traffic from attack. | Monitors a traffic for malicious activity or policy violations and sends alert on detection. |
| **Working principle** | Filters traffic based on IP address and port numbers (layer 3), state of the connection (layer 4), or contents of packet (layer 7) | Inspects real time traffic and looks for traffic patterns or signatures of attack and then prevents the attacks on detection | Detects real time traffic and looks for traffic patterns or signatures of attack and them generates alerts |
| **Configuration mode** | Layer 2 to 7 | Layer 3 and 4 |  Layer 2 to 7 |
| **Usual placement** | First line of defense | After firewall | After firewall |
| **Action on unauthorized traffic detection** | Block the traffic | Block the traffic |  Alerts/alarms |
