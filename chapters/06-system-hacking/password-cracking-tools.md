# Password cracking tools

- See also [Web server password cracking tools | Web server threats and attacks](./../12-web-servers/web-server-threats-and-attacks.md#web-server-password-cracking-tools)

## `crunch`

- Generates password dictionaries.
- E.g. `crunch <min-length> <max-length> <character-pool> -o <file-name>`
- Difficulty/time grows exponentially not linearly
  - Takes much longer when you e.g. increase total chars in a password.
  - E.g. `crunch 4 16 abcekfeafkapeo434@*.` generates thousands of petabytes.

## John the Ripper

- Also known as • ***JtR*** or ***`john`***
- 📝 Auto-detects OS password based on dictionary or brute-force attacks.
- Tries different passwords and compares their hashes to OS password
- Supports Windows, Linux and macOS.
- 📝 Usage:
  1. Dump OS password to a file.
     - E.g. on Linux, John has `unshadow` tool that can be used.: `unshadow /etc/passwd /etc/shadow > mypasswd`
  2. Crack password file using default order: `john mypasswd`
     - Passwords are saved in `$JOHN/john.pot`
     - You can also run `john --show mypasswd` to see the passwords

## Hydra

- Parallelized login cracker for different network protocols such as HTTP, Cisco, MySQl.
- 💡 You can use [DVWA: damn vulnerable web app](http://www.dvwa.co.uk/) for educational purposes & learning pen-testing
- E.g. `hydra -L usernamelist.txt -P passlist.txt -e ns -F -t 1 -w 10 <host-ip-address> http-form-post "/login.php:username=^USER^&password=^PASS^&Login=Login:Login failed" -v`
  - `-e ns`: e additional options
    - `n`: try null (for empty password)
    - `s`: try also same password as a user name
  - `-t 1`: number of tasks (based on threads), default is 16
    - ❗ Careful. Too many connections and too quick = Detected immediately
  - `-w 10`: waiting time of 10 ms
  - `<host-ip-address>`
    - Usually people go to the target using proxies and examine results in proxies.
      - E.g. [burp suite](./../05-vulnerabilities/vulnerability-analysis.md#burp-suite)
  - `http-form-post "/login.php:username=^USER^&password=^PASS^&Login=Login:Login failed`
    - Posts data to server as the HTML does
    - `Login failed`: text to search in result page to determine whether the login has failed.

## Hashcat

- Very fast, GPU-based password cracker with in-kernel rule engine
- Can do dictionary hash attack, brute force hash, role based attack and more
- [Website](https://hashcat.net/hashcat/) | [source code](https://github.com/hashcat/hashcat)
- 💡 Good idea to use in cloud to get more compute power.
- Proper drivers are required for e.g. AMD and Intel and NVIDIA
- E.g. cracking Linux OS password
  - `./hashcat64.bin -a 3 -m 1800 ?u?l?l?l?d?d?d`
    - `-m 1800`: Hash mode `sha512crypt $6$, SHA512 (Unix)`
    - `-a 3 ?u?l?l?l?d?d?d`: Mask attack
      - Brute-force on user specified character sets
      - `?u?l?l?l?d?d?d`= uppercase + lowercase + lowercase + lowercase + number + number + number
      - 💡 Do certain assumptions or it might take until the next big bang to crack the password.
      - E.g. usually passwords start with capital letter and continues with lowercase letters

## Password recovery tools

- [Elcomsoft Distributed Password Recovery](https://www.elcomsoft.com/edpr.html)
  - Data recovery and password recovery services
  - Runs on Windows
  - For forensic and government agencies
  - Can crack systems passwords for Windows, Unix and Mac OS and many more other passwords.
- [Passware Kit Forensic](https://www.passware.com/kit-forensic/)
  - Tool for encrypted electronic evidence discovery and decryption
  - Can crack systems passwords for Windows, Unix and Mac OS and [many more other passwords](https://www.passware.com/kit-forensic/filetypes/).

### Windows password reset tools

- Resets Windows login passwords.
- Often can run from a bootable USB or CD/DVD.
- Include • [Stellar Password Recovery](https://www.stellarinfo.com/password-recovery/password-recovery-software.php) • [Windows Password Recovery Pro ISeePassword](https://www.iseepassword.com/windows-password-recovery.html) • [Windows Password Recovery Tool](https://www.windowspasswordsrecovery.com/) • [Windows Password Refixer](https://www.isumsoft.com/windows-password-refixer/) • [PCUnlocker](http://www.pcunlocker.com/)

#### chntpw

- Also known as [Offline NT Password & Registry Editor](http://www.chntpw.com/)
- 📝 Linux utility used for resetting or blanking local passwords used by Windows.
