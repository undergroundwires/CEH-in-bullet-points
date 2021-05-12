# Covering tracks

- Attempt to hide attackers presence on the system so the system appears uncompromised.
- To avoid detection the attacker needs to
  - modify the system logs and delete their activity during the attack.
  - ensure that future activities are not logged
- You can mitigate damage by reducing footprint by e.g. making your access disguise a legit process.
- 💡 Have an exit strategy prior to breaking in by getting to know OS type, log types, policies (e.g. log altered alarms) and applications running on it.
  - E.g. if you know OS you can know where in general the OS keeps logs (e.g. `/var/log/`)
  - ❗ There's no universal way to figure out where all the logs are in a system
- Log file permissions
  - Common and big mistake: bad permissions on log files
    - Allows access from a lot of users that shouldn't
  - E.g. to read system messages you need to become root `sudo tail /var/log/messages`
- Terminal history
  - Might leave footprints here for commands you run.
  - Good place to learn about the user (they sometimes write passwords by mistake).
  - You can run `history` to get the history.
    - In (fedora) saved in `home/<username>/.bash_history`

## Security logs

### Windows security logs

- Event logs for are stored in `C:\Windows\System32\winevt\Logs`
- Can use OS tool "Windows Event Viewer" to navigate the logs
- Logs are categorized as application, security and system.

### Linux security logs

- Centralized repository of log files are in `/var/log` directory.
  - See also [Linux folders | Linux basics](./linux-basics.md#linux-folders)
- 📝 Log folders include
  - `/var/log/messages` | `/var/log/syslog` (debian-based)
    - Generic system activity logs
  - `/var/log/auth.log` (Debian and Ubuntu) | `/var/log/secure` (RedHat and CentOS)
    - Authentication/authorization related events
    - E.g. [SSH](./../15-cryptography/tunneling-protocols.md#ssh-secure-shell) logs
  - • `/var/log/utmp` • `/var/log/wtmp` • `/var/log/btmp` | `/var/log/faillog`
    - Login/logout events
  - `/var/log/lastlog`
    - Display information about a user's last login time
  - `/var/log/cron`
    - Cron service logs
    - Can include failed authorizations
  - `/var/log/secure`
    - Authentication and authorization privileges.
    - E.g. sshd logs including unsuccessful login.

## Techniques of covering tracks

- **Disabling auditing**
  - Disabling auditing features of the system
  - Disabling logging is difficult
    - Hard to know what kind of logs are being collected
    - Can include OS logs, additional security mechanisms logs, side applications logs..
    - Usually requires system restart for disabling of logs
      - E.g. if you use SELinux (can check with `getenforce`) it has different modes: • permissive (just logs) • enforcing and • disabled state
        - Setting its state to disabled requires a restart.
- **Clearing logs**
  - Deleting the attacker's logged activities
  - ❗Suspicious if all logs are deleted may raise alarms.
- **Manipulating logs**:
  - Changing the logs to prevent detection
  - E.g. search and replace your IP
- To cover tracks on network, attackers use

### Covering tracks on network

- **Reverse shell**
  - Target system sends a request to the remote system to act on the response.
  - **Reverse HTTP shells**
    - Asks the master system for commands to execute on the target machine
  - **Reverse ICMP tunnels**
    - Accessing the system by using ICMP echo and reply packets as carriers of TCP payload
- **DNS tunneling**
  - Adding data payload to the target's DNS server to create a back channel to steal information
- **TCP parameters**
  - Using TCP parameters for payload distribution.
  - Fields in which data can be hidden are e.g.
    - IP identification field, TCP acknowledgement number, and TCP initial sequence number.

### Tools for covering tracks

- [Privacy.sexy](https://privacy.sexy): Online/offline nad open source tool that can cleanup logs and personal activities.
- [Auditpol](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol): Microsoft tool to manipulate audit policies.
- [MRU-blaster](https://www.brightfort.com/mrublaster.html): Find and remove 30,000 MRU lists.
