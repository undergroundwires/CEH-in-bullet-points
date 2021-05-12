# Honeypots

- Designed as a trap for attackers who try to access the network.
- Any interaction with a honeypot points to a malicious activity.
- E.g. free proxy servers, VPNs, WiFis...
- Can be used by law enforcements to e.g. get IP of attackers, or malicious people to blackmail you.
- IDP (intrusion detection prevention) systems or admins can redirect intruders to a virtual machine as honeypot.

## Honeypot types

- **Low-interaction honeypots**
  - Mimic small number of applications and services that run on a system or network.
  - Capture information about network probes and worms.
- **Medium-interaction honeypots**
  - Mimic real operating system, applications and services
  - Capture more data compared to low-interaction honeypots
- **High-interaction honeypots**
  - Run real operating systems and applications
  - Gather information about the techniques and tools used in the attack.
- **Production honeypots**
  - Mimic the organizations real production network allowing more attacks
  - Helps network admins to take preventive measures to reduce the probability of an attack
  - Differs from high-interaction honeypots as they do not run real operating systems or applications.
- **Research honeypots**
  - High-interaction honeypots
  - Mainly used by security analysis and researchers
  - Goal is to understand how the attack was performed

## Evading honeypots

- Goal is to avoid being trapped in a honeypot
- Tools are used to detect honeypots that are installed on the network.
- Well configured honeypot is nearly impossible to detect.
- Best to target specific IPs known ahead of time to be valid machines.
- Some giveaways (see [discussions](https://security.stackexchange.com/questions/90642/is-it-possible-to-detect-a-honeypot), [paper](https://ro.ecu.edu.au/cgi/viewcontent.cgi?referer=&httpsredir=1&article=1027&context=adf)):
  - They can be to good too obviously insecure e.g. sitting near DMZ.
  - No network traffic
  - Unrealistic configurations e.g. IIS server on Linux, file names, drivers (e.g. VMWare defaults) etc.
  - Attacker can detect if it's running in a VM, disrupt the VM.
  - Performance degradation or fails under a sustained attack because of e.g. insufficient bandwidth.
  - Logging instructions affects total execution time of hacker commands.
- There are some attempts to automate such as [Honeypot Hunter](https://send-safe-honeypot-hunter.apponic.com/) (commercial scanner) or using [machine learning](https://www.hindawi.com/journals/scn/2019/2627608/).

## Setting up a proxy server as honeypot

- 🤗 This walkthrough is out of scope to to get better understanding, unrelated to exam.
- Setup the honeypot
  - Install [`squid`](http://www.squid-cache.org/) the proxy server: `yum install squid`
  - Start `squid`: `systemctl start quid`
  - Start automatically on reboot (good for cloud machines): `systemctl enable quid`
  - Configure in `vim /etc/squid/squid.conf`:
    - Has ACL (access list) rules to e.g. allow source ip ranges and ports for access
  - People can now use the proxy server with its public ip and port `3128` as default.
  - It will be detected by automated crawlers on internet that's looking for e.g. vulnerabilities.
- Monitor the traffic using sniffing tools such as [`tcpdump`](./../08-sniffing/sniffing-tools.md#tcpdump) or [Wireshark](./../08-sniffing/sniffing-tools.md#wireshark)
  - Create a named pipe (aka FIFO) file: `mkfifo myPipe.fifo`
  - Redirect proxy server logs to a local file
    `ssh root@<proxy-server-ip> "tcpdump -s 0 -U -n -w - -i eth0 not port 22" > myPipe.fifo`
    - `-s 0`: sets snapshots length to default `262144` bytes to take
    - `-U`: unbuffered, dump anything
    - `-n`: don't convert addresses to names
    - `-w`: write file instead of parsing and printing them out.
      - `-`: means standard output, so it writes to standard output.
    - `-i eth0`: capture traffic on `eth0` interface
    - `not port 22`: filter out own connection to the server
  - Run `wireshark-gtk -k -i myPipe.fifo` to start wireshark
- You can now use proxy using e.g. Firefox and see the traffic.
