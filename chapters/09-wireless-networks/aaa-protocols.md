# AAA protocols

- AAA stands for (Authentication, Authorization, Accounting)
- Family of protocols that mediate network access.
- Sometimes these protocols are used in combination with
  - [Point-to-Point Protocol (PPP)](./../15-cryptography/tunneling-protocols.md#ppp-point-to-point-protocol)
  - [Extensible Authentication Protocol (EAP)](#extensible-authentication-protocol-eap)
  - Protected Extensible Authentication Protocol (PEAP)
  - [Lightweight Directory Access Protocol (LDAP)](./../04-enumeration/enumeration-overview.md#ldap)
- Most commonly used protocol is [RADIUS](#radius) and then [Diameter](#diameter), meanwhile older systems use [TACACS](#tacacs) and [TACACS+](#tacacs-tacacs-plus)

## RADIUS

- Stands for **R**emote **A**uthentication **D**ial **I**n **U**ser **S**ervice
- 📝 Commonly used by ISPs (Internet Service Providers) and corporations for access control
- Primarily used to manage access to the internet or other networks
  - Networks can employ a variety of networking technologies, including analog modems, DSL, wireless local area networks (WLANs), and VPNs.
- Based on UDP (User Datagram Protocol)
- Flexible and extensible offering a variety of ways to authenticate the user
- Requires setting-up a RADIUS back-end server.
  - Usually integrated with AD (active directory)

### Extensible Authentication Protocol (EAP)

- Authentication framework used by [Enterprise WPA operation mode](./wireless-networks-overview.md#enterprise).
- Strong when used with TLS (EAP-TLS)
  - Higher security when client-side certificates are hosted in smart cards.
- Extends and replaces [Point-to-Point Protocol (PPP)](./../15-cryptography/tunneling-protocols.md#ppp-point-to-point-protocol).

#### EAP Transport Layer Security (EAP-TLS)

- Secure standard using TLS protocol
- Requires mutual authentication
  - Where the client-side certificate can be stored in e.g. smart cards.

## Diameter

- Successor to RADIUS
- Not directly backwards compatible
- Security is provided by [IPsec](./../15-cryptography/tunneling-protocols.md#ipsec) or [TLS](./../15-cryptography/encrypting-communication.md#tls-transport-layer-security) and privacy protocols.

## TACACS

- Terminal Access Controller Access-Control System
- Remote authentication protocol
- Commonly used in networks of UNIX systems

## TACACS+ (TACACS plus)

- Terminal Access Controller Access-Control System Plus
- Provides access control for routers, network access servers, and other
networked computing devices via one or more centralized servers.
- Based on TACACS but an entirely new protocol (incompatible with TACACS)
- Runs on older systems but generally replaced by [RADIUS](#radius)
