# Evading firewalls

- See also • [Bypassing IDS and firewall | Scanning Networks](../03-scanning-networks/bypassing-ids-and-firewall.md) • [Evading IDS](evading-ids.md)

## Firewall evasion techniques

- [Source routing](../03-scanning-networks/bypassing-ids-and-firewall.md#source-routing) to avoid the route of the firewall

### Using fragmented packets

- The idea is to split up the TCP header over several packets to make it harder
- E.g. `-f` command in `nmap`: `nmap -f 192.168.1.12`
  - utilizes 16 bytes per fragment which diminishes the number of fragments
  - to specify own offset size: `nmap --mtu 16 192.168.1.12`
- ❗ Most modern firewall and IDS detect fragmented packets.

### Firewalking

- 📝 Discovers firewall rules using traceroute-like technique with IP TTL expiration
- Works by sending out TCP or UDP packets with a TTL one greater than the targeted gateway
  - Tests if gateway allows the traffic to find firewalls
- Requires knowledge of:
  1. Known gateway (can be firewall) before the host (serves as waypoint)
  2. IP address of a host located behind the firewall.
- ❗ If a host on the other side of the firewall cannot be targeted then firewalking will not be successful
- Also known as ***port knocking***
  - Externally opening ports on a firewall by generating a connection attempt on a set of prespecified closed ports
- **Tools**
  - [`firewall` script](https://Nmap.org/nsedoc/scripts/firewalk.html) in `nmap`: e.g. `nmap --traceroute --script=firewalk --script-args=firewalk.max-probed-ports=-1 192.168.3.11`
  - [Firewall tool](http://packetfactory.openwall.net/projects/firewalk/index.html) e.g. `firewalk 192.168.1.2 192.168.3.11`
    - Responses can be interpreted as:
      - **`ICMP_TIME_EXCEEDED`**: Gateway forwards packets to next hop where they're expired.
      - **No response**: Port is probably blocked
- **Countermeasures**
  - Use Network Address Translation to hide the addresses on your internal networks
  - Block all outgoing TTL Exceeded in Transit packets in the firewall

### HTTP and ICMP tunneling

- Can be used to bypass firewalls rules through obfuscation of the actual traffic
- Works by injecting arbitrary data into packets sent to a remote computer
- Hard to detect without proper deep packet inspection or log review
- HTTP tunneling (port 80) is almost never filtered by a firewall.

### DNS tunneling

- Also known as **TCP over DNS**
- Provides a TCP tunnel through the standard DNS protocol
- Used to evade firewalls as most firewalls allow DNS traffic to freely pass into and out of the network.
- 🤗💡 May browsing internet in coffee shops for free
- Tools include • [iodine](https://github.com/yarrick/iodine) • [ThunderDNS](https://github.com/fbkcs/ThunderDNS)

## Banner grabbing

- Used to identify firewalls.
- Tools
  - Using [Nmap banner script](https://Nmap.org/nsedoc/scripts/banner.html) `nmap -sV --script=banner <target-ip>`
  - Using [`netcat`](./../03-scanning-networks/banner-grabbing.md#netcat): `nc -v -n 192.168.51.129 21`
