# DNS enumeration

## DNS

- Stands for "Domain Name System"
- Hierarchical and decentralized naming system
- Used for resources connected to the Internet including computers and services
- Runs on TCP/UDP port 53

### DNS records

- Database record used to map a URL to an IP address
- Stored in zone files in DNS servers
  - A DNS server contains a "zone file" for each domain
  - Zone file is made up of "resource records" (RRs)
- Helps users connect their websites to the outside world.
- 📝 Common DNS records include
  - **`A`**
    - Points a domain to an IPv4 address, such as `11.22.33.44`.
  - **`AAAA`**
    - Points a domain to an IPv6 address, such as `FE80::0202:B3FF:FE1E:8329`.
  - **`MX`**
    - Mail eXchange records are used to direct emails sent to domain
    - See also [MX records | Whois, GeoIpLocation and DNS interrogation](./../02-footprinting/whois-geoiplocation-and-dns-interrogation.md#mx-records)
  - **`NS`**
    - Used to delegate a domain or subdomain to a set of name servers
  - **`SOA`**
    - Contains data to control the zone transfer.
    - Includes serial number, timestamps, mail address of zone responsible..
    - E.g.

      ```txt

        $TTL 86400
        @   IN  SOA     ns.icann.org. noc.dns.icann.org. (
                2020080302  ;Serial
                7200        ;Refresh
                3600        ;Retry
                1209600     ;Expire
                3600        ;Minimum TTL
        )

      ```

  - **`CNAME`**
    - Link a subdomain to a domain's existing A or AAAA record
    - E.g. `www.cloudarchitecture.io` to `cloudarchitecture.io`
  - **`PTR`**
    - Opposite of `A`, points an IP to domain
    - Commonly used for spam verification for e-mail programs
  - **`HINFO`**
    - System information including CPU and OS type.

## DNS enumeration techniques

- Check all NS Records for [zone transfers](#zone-transfers).
- Enumerate general [DNS records](#dns-records) for a given domain.
- Perform common SRV Record Enumeration.
  - Service records contain the hostname, port and priority of servers for a given service.
  - Enumerates e.g. • LDAP • Autodiscover for Exchange • Kerberos...
  - E.g. by `nmap --script dns-srv-enum --script-args "dns-srv-enum.domain='google.com'"`
- Brute force subdomain and host A and AAAA records discovery with given top domain and wordlist.
- DNS PTR lookup given a IP range CIDR range
  - Querying dns for PTR record of each IP in subnet
- See also [DNS interrogation](./../02-footprinting/whois-geoiplocation-and-dns-interrogation.md#dns-interrogation)

### DNS cache snooping

- Checks a DNS server cached records.
   Done by performing **non-recursive** (or also known as **iterative**) DNS queries
  - Also known as iterative query
  - Server returns either its own record or another DNS server that may know the answer.
  - As opposed to [recursive DNS lookup](../12-web-servers/web-server-threats-and-attacks.md#recursive-dns-lookup) where servers communicates with other DNS servers.
- **Tools**
  - Automated: [dnsrecon](#dnsrecon)
  - 📝 Manual:
    - `dig` with `+norecurse` flag
    - `nslookup` with `-norecurse` flag
    - `host` with `-r` flag

## Zone transfers

- DNS server passes a copy of part of it's database ("zone") to another DNS server
- There's one master DNS server, and one or more slave DNS servers
  - Slaves ask master for a copy of records
- Uses TCP port 53
- 📝 Uses **AXFR** (full) protocol or **IXFR** (incremental).
- The secondary server request a new copy if the primary SOA serial number is higher.
  - The primary increments the serial number every time the SOA changes
  - If the secondary checks in and the primary’s copy has a higher serial number

### DNS zone transfer attack

- Pretending to be a slave and ask for records
- Allows an attacker to obtain sensitive information about internal DNS records (network).
- 📝 Flow
  1. Get NS records (DNS servers that are responsible for resolving the queries)
     - Using `dig`: `dig ns zonetransfer.me` or `dig +short ns zonetransfer.me`
     - Using `nslookup`: `nslookup zonetransfer.me`
  2. Initiate AXFR request to get a copy of the zone from name server
     - Using `dig`: `dig axfr @<DNS you are querying> <target>`
       - E.g. `dig axfr @nsztm1.digi.ninja zonetransfer.me`
     - Using `nslookup`
       - `nslookup -ls -d nsztm1.digi.ninja`
         - `-d`: list all records for DNS domain
         - Sends AXFR query to the remote nameserver
         - Initiates zone transfer if and only if the remote nameserver is dumb enough to respond to unsolicited, unauthorized AXFRs originating from random machines on the Internet.
       - Or using interactive mode with specified a DNS server:

       ```txt
         $ nslookup
         > server <DNS you are querying>
         > set type=any
         > ls -d <target>
       ```

     - Or `nslookup -query=AXFR <target> <DNS you are querying>`
     - Using `host`: `host -l nsztm1.digi.ninja`
- 🤗 In June 2017 the registrar responsible for Russian top-level-domains accidentally enabled DNS zone transfers via AXFR which led to 5.6 million records being accidentally exposed | [source](https://securitytrails.com/blog/russian-tlds)

### Zone transfers countermeasures

- Do not allow or restrict zone transfers
- Use [split DNS](#split-dns)

#### Split DNS

- Also known as ***split-horizon DNS***, ***split-view DNS***, ***split-brain DNS*** or ***split DNS***
- 📝 Separation of internal network (intranet) DNS and public network (Internet) DNS
- Provides different answers to DNS queries based on the source address of the DNS request.
- Can be accomplished with hardware or software solutions

## DNS enumeration tools

### dnsrecon

- [Open source](https://github.com/darkoperator/dnsrecon) python script
- E.g. `./dnsrecon.py -d cloudarchitecture.io`
- Enumerates DNS records and more

### nslookup

- Limited: Depends on existence of DNS reverse lookup zone.
- Forward lookup (normal): Here's name give me IP
- Reverse lookup: Here's IP give me back the name

### dig

- *Nix tool for querying DNS
- E.g. `dig cloudarchitecture.io any`
  - `any` argument (optional): all records it can find
- `dig axfr cloudarchitecture.io`

### `host`

- On Unix-like operating systems, the `host` command is a DNS lookup utility
- Using e.g. `host <target-domain>` to see all records.
- 📝 You can also set type `-t` to see specific records e.g.
  - `host -t a <target-domain>` to see A records
  - `host -t ns <target-domain>` to see NS records
  - ...
