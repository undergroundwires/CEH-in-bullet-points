# Cracking passwords overview

- Recovering passwords from the transmitted or stored data on computer systems.
- See also [Password cracking techniques | Web server threats and attacks](./../12-web-servers/web-server-threats-and-attacks.md)

## Password attack types

### Non-electronic attacks

- Do not require the attacker to have any technical knowledge about cracking passwords.
- [**Dumpster diving**](./../10-social-engineering/social-engineering-types.md#dumpster-diving)
  - Looking for notes or anything that can help in cracking the password.
- **Shoulder surfing**
  - Observing the target while they type in their passwords
  - E.G. looking at their keyboard or screen
- **[Social engineering](./../10-social-engineering/social-engineering-overview.md)**
  - Interacting with the target to trick them into revealing their passwords.

### Active online attacks

- Require the attacker to communicate with the target machine in order to crack the password.
- E.g. trying to login with username password combination on an online login page.
- ❗ Limitations
  - Network communication to server over internet takes long time
  - There are rate limits e.g. get locked after 5 minutes, then 10 then 15
  - If server becomes suspicious that it's a bot then it might shut you off directly
  - Offline attack can perform millions/billions a second
    - Online attack, e.g. every 5 seconds, if you fail 5 times you might get locked out.

#### Dictionary attack

- 📝 Dictionary = file containing list of passwords
- Steps
  1. Load a dictionary file into a password cracking program.
  2. The program checks the passwords against user accounts.
- Helps to test against
  - Default passwords
  - Common / weak passwords
  - Leaks downloaded from internet
- ❗ Limitations
  - Can get too big
  - No guarantee to find the password
- See also [Dictionary attacks | Cryptanalysis](./../15-cryptography/cryptanalysis.md#dictionary-attack)

#### Brute-force attack

- Running every combination of characters until the password is cracked.
- Slowest technique (can take years) but comprehensive.
  - 💡 Should be used in combination with [rule-based attack](#rule-based-attack) to increase the speed.
- See also [Brute force attack | Cryptanalysis](./../15-cryptography/cryptanalysis.md#brute-force-attack)

#### Hybrid attack

- 📝 [Dictionary attack](#dictionary-attack) + [brute force attack](#brute-force-attack)  
- Taking a dictionary and expanding it with guesses using brute-force.
- It prepends, appends or substitutes characters in words.
- E.g. using [`hashcat`](https://hashcat.net/wiki/doku.php?id=hybrid_attack)
  - Say an `example.dict` contains: `password` and `hello`
  - `... -a 6 example.dict ?d?d` would generate from `password00` and `hello00` to `password99` and `hello99`

#### Rule-based Attack

- Used when the attacker has some information about the password
  - such as the length, if there are any digits, and similar.
- Attacker combines several other attacks to crack the password.
  - E.g. brute force, dictionary, and syllable attack.
- Can e.g. record people, or use other [non-electronic attacks](#non-electronic-attacks) to get some portions of the password to build rules.

#### Password guessing

- Guess passwords either by humans or by automated tools using dictionaries
- Requires the attacker to manually attempt to log into the target's machine.
- E.g.
  1. Find the target's username
  2. Create a password dictionary list
     - 💡 Good to add default passwords from manufacturers.
  3. Sort the passwords by the probability
  4. Try each password

#### Trojan/spyware/keylogger

- Installed in target machine to get the target's passwords and usernames.
- They run in the background and sometimes are difficult to detect.
- **Trojans**
  - Design to collect information or harm the system.
  - Allow attackers to remotely access the machine and perform malicious activities.
- **Spyware** are designed to collect secret information.
- **[Keyloggers](./executing-applications.md#keylogger)** to send key strokes to the attacker.

#### Hash injection

- Attack on systems that use hash functions for the user authentication.
- Steps:
  1. Retrieve the hashes which are stored in a databases
  2. Find the hash that belongs to the user
  3. Use that hash to create an authenticated session.

#### LLMNR/NBT-NS poisoning

- LLMNR = Link Local Multicast Name Resolution
- NBT-NS = NetBIOS Name Service
- Two main Windows OS elements that perform host name resolution.
- **Vulnerability**
  - When DNS fails to resolve name queries, the host sends a UDP broadcast message to other hosts asking them to authenticate themselves
  - Allows an attacker to listen for such broadcast messages and tricks the host into establishing a connection.
  - Once the connection is established, the host sends its username and NTLMv2 hash, which the attacker can attempt to crack and in such a way discover the password.

### Passive online attacks

- Grabbing data in-transit e.g. a key, password hash
- Without communicating with the target machine.
- Attacker
  1. Monitors the communication channel
  2. Records the traffic data
  3. Uses the data to break into the system.

#### Wire sniffing

- Attackers sniff credentials by capturing packets that are being transmitted
- During the packet transmission, attackers
  - capture packets
  - extract sensitive information such as passwords and emails
    - uses them to  gain access to the target system.

#### Man-in-the-middle (MITM) attack

- Attacker gains access to the communication channel between the target and server.
- Attacker then extracts information and data they need to gain unauthorized access.

#### Replay attack

- Involves using a sniffer to capture packets and authentication tokens.
- Need access to raw network data using e.g.
  - Network tap to physically copy everything that goes through in network.
  - Man in the middle attack using e.g. ARP poisoning.
  - Malware on victims computer
- Attacker replay information using e.g. extracted authentication token or hashed password.
- **Countermeasure**
  - Using Session ID for each user session on server side
  - Expire session ID in short time intervals so replay attack cannot use same session ID

### Offline attacks

- Cracking efforts on a separate system
- Attacker never attempts to login to the application server that can be logged.
- ❗ Does not mean disconnected from internet.
- Usually the attacker tries to guess a password from a hash dump.
  - E.g. SAM file on Windows or `/etc/shadow` on Linux.

#### Distributed network attack (DNA)

- Uses the power of machines across the network to decrypt passwords.
- Used for recovering passwords from hashes
- DNA manager is installed on a central location
  - Coordinates the attack by allocating portions of the key search to machines which are on the network.

#### Hash attacks

- [Rainbow table attack](../15-cryptography/cryptanalysis.md#rainbow-table-attack)
- [Collision](../15-cryptography/cryptanalysis.md#collision-attack)
- [Birthday attack](../15-cryptography/cryptanalysis.md#birthday-attack)
- [Brute-force attack](../15-cryptography/cryptanalysis.md#brute-force-attack)

#### Password cracking countermeasures

- 📝 Use [**password salting**](./../15-cryptography/hashing-algorithms.md#salted-hash)
  - The longer the random string, the harder it becomes to break or crack the password
  - Generates different hashes for the same password
  - Protects against [rainbow tables](../15-cryptography/cryptanalysis.md#rainbow-table-attack) as it would cause the table to include salts making it much bigger.
- Use [key stretching](./../15-cryptography/hashing-algorithms.md#key-stretching) to derive stronger passwords to use in encryption.

## Linux passwords

- 📝 Linux hashed passwords lies in `/etc/shadow/` so you can attack on that.
- Linux usually use SHA512, you can find method in `/etc/login.defs`
- In older systems password information was stored in `/etc/passwd`, now it holds only user account information.
