# Security policies

- Rules and requirements that the system has to have to achieve information assurance.
- Defines everything about your layout for the employees
- Written documents including
  - Lists of allowed hardware and software
  - Locations for related policies and procedures
  - Exceptions i.e. exemption rules
  - Sanctions for noncompliance e.g. disciplinary actions/punishment/termination
  - ...
- Types
  - **Technical policies**: define the system configuration
  - **Administrative policies**: define the behavior of employees
- Mitigates risks, prevents something costly from happening.
- E.g. a good policy is NDA, distributed and cannot be repudiated (signed)

## Policy types for risk tolerance

- 📝 From most permissive to most strict
  1. [Promiscuous](#promiscuous-policy): No restrictions
  2. [Permissive](#permissive-policy): If something is malicious it's blocked.
  3. [Prudent](#prudent-policy): Restrictive
  4. [Paranoid](#paranoid-policy): Highest restrictions

### Promiscuous policy

- No restrictions on system resources.
- Do whatever you want
- 💡 Only good when you have bunch of highly trained & well-informed people with proven track record working in a team because otherwise policies would slow them down

### Permissive policy

- Begins as wide-open, can do anything
- When it knows something is malicious, it'll be blocked

### Prudent policy

- Provides maximum amount of security
- Allows only safe stuff
- Very restrictive
- A lot of things are locked up

### Paranoid policy

- Something of such high importance, not worth to take smallest of risks, e.g. government data regarding to citizens
  - E.g. access only from police station, they need to submit why they access, lethal data
- 🤗 In Linux firewall there's a command called panic that's equivalent to this: Drops all traffic

## Sub-policies

- Policy types are not limited to the listed.

### Password policy

- Guidelines for using strong password protection on available resources.
- E.g.
  - At least 8 characters in length
  - Must include upper/letter/number/symbols

### User account policy

- 📝 Defines the account creation process, authority, rights and responsibility of user accounts.
- E.g.
  - Put users in groups and decides what the groups can do.
  - What needs to be done during account creation

### Information protection policy

- 📝 Guidelines to users on the processing, storage and transmission of sensitive information
- Goal is to ensure information is appropriately protected from modification or disclosure
- E.g.
  - Setting level of sensitivity to information
  - Dictates who has access to information
  - Determines how information is stored and transmitted
  - Describes how information should be deleted from storage media

### Special access policy

- Custom rulings for specific scenarios for specific individuals and services
- The terms and conditions of granting special access to system resources.

### Email security policy

- Governs the proper usage of corporate email.
- E.g.
  - Verify proper signature
  - Never click on links, because they'll never be sent

### Acceptable use policy

- Same as **Terms of Service** or **Terms of Use**
- 📝 Description of what constitutes acceptable and unacceptable use of the Internet
- Code of conduct governing the behavior of a user whilst connected to the network/Internet.
- E.g.
  - ISP providers allows you to use unlimited bandwidth
    - In contract you see it says it's about "fair use"
    - Fair use can be e.g. to not exceed 50% maximum potential bandwidth that could be used with that bandwidth
  - Prohibiting port scanning or security scanning
  - Never revealing a password

### Access control policy

- 📝 Governs resources being protected and the rules that control access to them
- Who can access what (humans <-> services)
  - E.g. limited access to routers and switches on top floor
  - E.g. regulating electric socket placement as someone can connect a Raspberry Pi that can be listening
- What can access what (services <-> services)

### Remote access policy

- 📝 Defines acceptable methods of remotely connecting to the internal network
- Applies to both who and what
- E.g. enforcing VPN, strong passphrases, defining vendor access and requiring monitoring

### Firewall management policy

- Governs access, management and monitoring of firewalls in an organization.
- Who'll monitor? How will it be monitored?
- What kind of firewall that'll be used?

### Network connection policy

- Defines who can install new resources on the network, approve the installation of new devices, document network changes etc.
- Protects both yourself and the company
- E.g. must always use VPN if not working from office

### Network security policy

- 📝 Outlines rules for computer network access, determines how policies are enforced
- Governs e.g. • data access • web-browsing habits • use of passwords and encryption • email attachments.

### Encryption policy

- Dictates which encryption to use
- Goal is to avoid weak and obsolete algorithms
- Easier if everyone uses same algorithm
- Used by e.g. cloud providers, ISP providers

### Authentication policy

- Limits ability to be authenticated under some conditions
- E.g. no coffee shop wireless, only through VPN and using [MFA](identity-access-management-(iam).md#multi-factor-authentication-mfa)

## Implementation

- Steps
  1. Perform a [risk assessment](./risk-management.md#risk-assessment)
  2. Utilize standard guidelines
  3. Include senior management
  4. Define sanctions
  5. Distribute the final version
  6. Ensure that employees have read the policy
  7. Enforce policies
  8. Educate and train employees
  9. Review and update the policy
- Human Resource department has the responsibility to
  - educate and train employees in practices defined by the company's security policies
  - monitor the implementation of the policies
  - enforce penalties

### Top-down vs Bottom-up

- **Top-down**
  - Begins with management establishing a framework for initiating and implementing security practices in the enterprise.¨
  - Most important way to ensure employees across an organization will support and follow the policies
- **Bottom-up**
  - Occurs when the system administrators and security personnel try to establish a security program on their own without senior management support and enforcement.
