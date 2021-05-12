# Microsoft authentication

- Windows stores passwords in hashed form using either:
  - **Security Accounts Manager (SAM) Database**
    - A file stored at `%SystemRoot%/system32/config/SAM`
    - Locked by Windows kernel to prevent copying/moving
      - Usually stolen through bootable CD/USBs.
  - **Active Directory Database**
    - Stored on a domain controller in a database
    - Located in either `%SystemRoot%\NTDS\Ntds.dit` or `%SystemRoot%\System32\Ntds.dit`

## NTLM authentication

- New Technology (NT) LAN Manager (LM)
- Security protocols, default authentication scheme
- 📝 Consists of LM and NTLM authentication protocols
  - Challenge-response authentication protocols
  - Each stores user passwords in SAM database using different hash methodologies
  - 💡 Try all as many systems still keep older authentication for backwards compatibility.
- 💡 Insecure, can be disabled through GPO (Group Policy Object) with [privacy.sexy](https://privacy.sexy)

### LM vs NTLM

#### LM

- LM is the oldest password protocol dating back to OS/2 in 1980's
- **LM Hash**
  - E.g. `aad3c435b514a4eeaad3b935b51304f`
  - 📝 **Flow**
    1. Convert all lower case to upper case (case-insensitive)
    2. Pad password to 14 characters with NULL characters
    3. Split the password to two 7 character chunks
    4. Create two DES keys from each 7 character chunk
    5. DES encrypt the string "`KGS!@#$%`" with these two chunks
    6. Concatenate the two DES encrypted strings = LM hash.
- **Authentication flow**
  1. Client ends authentication request
  2. Server response with a challenge
  3. Client responds with DES encrypted LM hash with challenge as key
- **Weaknesses**
  - No salting allowing MITM attacks (through [pass the hash](#pass-the-hash-attack) and rainbow tables).
  - If password is less than 7 characters second half is always `0xAAD3B435B51404EE`
  - Maximum allowed length is 14 characters
  - Case insensitive: PassWord, PaSsWoRd, PASSword and other similar combinations are same as PASSWORD.
  - 💡 Turned off as default since Windows Vista/Server 2008 as it's weak
- **Cracking**

  ```txt
    john --format=lm hash.txt
    hashcat -m 3000 -a 3 hash.txt
  ```

#### NTLM

- Also known as ***NT LAN Manager***
- Uses DES with MD4 hash, used in Windows NT until SP3
- **NTLM Hash**
  - Also known as ***NTLM hash***, ***NTHash***, ***NT hash**'.
  - Algorithm: `MD4(UTF-16-LE(password))`
    - UTF-16-LE is the little endian UTF-16
  - E.g. `B4B9B02E6F09A9BD760F388B67351E2B`
  - **Cracking**
    1. Can be extracted using e.g. SAM database or [mimikatz](https://github.com/gentilkiwi/mimikatz)
    2. Then

    ```txt
      john --format=netntlm hash.txt
      hashcat -m 5500 -a 3 hash.txt
    ```

##### NTLMv1

- Also known as ***Net-NTLMv1***
- Uses both the NT and LM hash, depending on configuration and what is available.
- Deprecated, but still used in some old systems on the network.
- E.g.  

  ```txt
    u4-netntlm::kNS:338d08f8e26de93300000000000000000000000000000000:9526fb8c23a90751cdd619b6cea564742e1e4bf33006ba41:cb8086049ec4736c
  ```

- **Authentication flow**
  1. `C = 8-byte server challenge, random`
     - Server sends sending an 8-byte random number, the challenge
  2. `K1 | K2 | K3 = NTLM-Hash | 5-bytes-0`
     - Five zeroes are added to the hash to achieve 21 bytes
     - 21 bytes is split into three 7 byte parts
  3. `response = DES(K1,C) | DES(K2,C) | DES(K3,C)`
     - Each part is used as key in DES
     - Three encryptions are reunited to form the 24-byte response
- **Cracking**
  - 💡 Easy to crack as it lacks salting
  1. Can be captured using [Responder](https://github.com/lgandx/Responder)
  2. Then

  ```txt
    john --format=netntlm hash.txt
    hashcat -m 5500 -a 3 hash.txt
  ```

##### NTLM v2

- Also known as ***Net-NTLMv2***
- Uses MD5
- Introduced in Windows NT 4.0 SP1 (Windows 2000)
- E.g.

  ```txt
    admin::N46iSNekpT:08ca45b7d7ea58ee:88dcbe4446168966a153a0064958dac6:5c7830315c7830310000000000000b45c67103d07d7b95acd12ffa11230e0000000052920b85f78d013c31cdb3b92f5d765c783030
  ```

- Replaces NTLM with
  - stronger cryptography against spoofing attacks
  - ability to authenticate the client
- **Authentication flow**
  1. `SC = 8-byte server challenge, random`
     - Server sends sending an 8-byte random number, the challenge
  2. `CC = 8-byte client challenge, random`
     - 8-byte random value for the challenge
  3. `CC* = (X, time, CC2, domain name)`
     - `time`: the current time in NT Time format
     - `CC2`: an 8-byte random value
     - `X`: fixed contents of a formatting field.
  4. `v2-Hash = HMAC-MD5(NT-Hash, user name, domain name)`
     - HMAC-MD5 hash of users password and domain name with other identifying information
  5. `LMv2 = HMAC-MD5(v2-Hash, SC, CC)`
  6. `NTv2 = HMAC-MD5(v2-Hash, SC, CC*)`
  7. `response = LMv2 | CC | NTv2 | CC*`
- Cracking it
  1. Can be captured using [Responder](https://github.com/lgandx/Responder)
  2. Then:

  ```txt
    john --format=netntlmv2 hash.txt
    hashcat -m 5600 -a 3 hash.txt
  ```

### Pass the hash attack

- Also known as **pass-the-hash**
- Allows gaining access to systems without accessing password in plaintext
- Can be used on any systems using LM or NTLM authentication
- Exploits static hash that's shared between sessions in authentication protocol
- Helps to hack Windows user name, domain name, and password hashes
- Can dump hashes
  - from compromised machines by e.g. [Windows Credentials Editor](https://www.ampliasecurity.com/research/wcefaq.html) and [Pass-the-Hash Toolkit](https://en.wikipedia.org/wiki/Pass_the_hash)
  - or sniff the network
- Allows privilege escalation as domain administrators connected to machine also leaves their hashes.

## Kerberos authentication

- Network authentication protocol for client/server applications
- Protects against replay attacks and eavesdropping
- Uses both symmetric and asymmetric encryption
- Uses TCP/UDP port 88
- **Mutual authentication**
  - Both parties verifies each others identity using tickets.

### Kerberos authentication components

- Requires **Key Distribution Center (KDC)** that consists of:
  - **Authentication server (AS)**
  - **Ticket Granting Server (TGS)**
- **Ticket Granting Ticket (TGT)**
  - Small, encrypted file with limited validity
  - Protects users from MITM attacks
  - Includes session key, its expiration date, and the user's IP address

### Kerberos authentication flow

1. Client asks KDC (who has AS and TGS) for ticket to authenticate throughout the network.
   - This request is in clear text.
2. Server responds with secret key.
   - Hashed by the password copy kept on AD server (TGT).
3. TGT sent back to server requesting TGS if user decrypts.
4. Server responds with ticket, and client can log on and access network resources.

### Pass the ticket attacks

- Also known as **pass-the-ticket**
- Authentication Method using Kerberos tickets without having access to an account's password.
- Kerberos tickets are retrieved e.g. from memory on a system
- Tools include [mimikatz](https://github.com/gentilkiwi/mimikatz) and [Rubeus](https://github.com/GhostPack/Rubeus)
