# Automated penetration testing tools

- [CANVAS](https://immunityinc.com/products/canvas/) (proprietary)
  - Exploit gallery and development framework
- [Core Impact](https://www.coresecurity.com/products/core-impact) (proprietary)
  - All-inclusive automated testing framework
- Nmap with custom scripts
  - Can used for • [footprinting](./../02-footprinting/network-footprinting.md#nmap) • [scanning](./../03-scanning-networks/scanning-tools.md#nmap) • [vulnerability analysis](./vulnerability-analysis.md#nmap)
  - Also to carry out attacks e.g. as [DoS tool](./../13-web-applications/denial-of-service.md#dos-tools)

## Automated vs manual penetration testing

- Automated testing cannot fully replace manual testing but as it has its own advantages and disadvantages
- **Automated testing advantages**
  - Help the initial analysis to understand where potential vulnerabilities exist
  - Enable the testers to build efficient exploit strategies to confirm the security vulnerabilities and weaknesses.
  - Same pen test multiple times from different entry points
  - Reduces costs
- **Automated testing disadvantages**
  - It can miss unforeseen instances
  - Usually works from "inside" of the network
  - Fails to work in complex scenarios
  - Usually does not exploit the vulnerabilities
  - Not as creative as humans (yet 😉) in e.g. social engineering

## Metasploit

- 📝 Framework for building and performing exploit attacks against targets.
- [Source code](https://github.com/rapid7/metasploit-framework) | [Website](https://www.metasploit.com/)
- Modular architecture allowing code re-use instead of copying or re-implement on a per-exploit basis

### Free version

- Developing and executing exploit code against a remote target machine.
- Database of vulnerabilities and platform to execute different exploits for them.
- [Fuzzing](./../14-sql-injection/sql-injection-overview.md#fuzz-testing) tools to discover vulnerabilities
- Automated exploitation of known vulnerabilities such as weak passwords for e.g. Telnet, SSH, HTTP.
- Manual exploitation and manual brute forcing
- Zenmap (Nmap GUI)

### Paid (Pro) version

- Web application testing (OWASP Top 10)
- Dynamic payloads for anti-virus evasion
- Has web interface
  - 💡📝 A free alternative is [**Armitage**](http://www.fastandeasyhacking.com/) that's [open-source](https://github.com/rsmudge/armitage) GUI.

### Metasploit interfaces

#### `meterpreter`

- 📝 Payload that provides control over an exploited target system
- Runs as a DLL loaded inside of any process on a target machine
- Resides entirely in memory and writes nothing to disk

#### `msfvenom`

- Generates stand-alone payload
- 📝 Combines
  - Payload generation (old tool: `msfpayload`)
    - `-p <payload-name>` e.g. `-p windows/meterpreter/bind_tcp`
    - `-f <format>` e.g. `-f exe` or `-f raw` (shellcode)
  - Encoding (old tool: `msfencode`)
    - Used to avoid antivirus detection
    - Done by `-b` or `-e` flags
    - `-i <number>` allows encoding multiple times for more stealth
- E.g. `msfvenom -a x86 --platform Windows -p windows/shell/bind_tcp -e x86/shikata_ga_nai -b '\x00' -f python`
- See also [msfvenom | Hiding files](../06-system-hacking/hiding-files.md#msfvenom)

#### `msfconsole`

- All-in-one centralized console for all of the options available in the MSF
- Contains the most features and is the most stable MSF interface
- E.g. flow for using unreal exploit:
  1. Run `msfconsole`
  2. You can search for a service e.g. `unrealirc`
     - ❗Disclosure date is not same as when vulnerability found, it can be before but not published.
  3. Use with `use exploit/unix/irc/unreal_ircd_3281_backdoor`
     - There can be multiple payloads, check with `show payload` and then set with `set PAYLOAD <name>`
     - Set required options (`show options` to list) and `set <option-name> <option-value>`to set
  4. Run exploit using `exploit`
     - Hopefully you'll end up in terminal session as root :)
