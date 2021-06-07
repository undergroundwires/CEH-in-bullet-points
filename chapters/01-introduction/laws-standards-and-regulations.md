# Laws, standards, and regulations

## Legal systems

- Two main categories of legal systems in World. Many systems mix those:
  1. Common law
     - Unwritten laws based on legal precedents established by the courts.
     - E.g. USA, UK, India and Canada
     - Two main branches:
       - **Civil law (in common law)**
         - Between individuals, organizations, or between the two
         - Focuses on dispute resolution and victim compensation
       - **Criminal law**
         - Includes the punishment and rehabilitation
         - Proscribes conduct threatening, harmful, or otherwise endangering to the property, health, safety, and moral welfare of people inclusive of one's self
  2. Civil law
     - Codified statutes and legal codes predominate
     - E.g. majority of countries including Germany, France, Spain, Sweden, Turkey..

## PCI DSS

- Payment Card Industry Data Security Standard
- Applies to organizations that card payments and all entities involved in the process of card payment.
- Global data security standard
- Common sense steps presenting best security practices
- 📝 Requires tester to notify organization if cardholder data is accessed during a penetration test
  > "If cardholder data is accessed during the penetration test, it is important that the tester notify the organization immediately" [PCI DSS Guidance](https://www.pcisecuritystandards.org/documents/Penetration-Testing-Guidance-v1_1.pdf) recommends:
- See also the [official guide](https://www.pcisecuritystandards.org/documents/PCI_DSS_v3.pdf), or the [simpler version](https://www.pcisecuritystandards.org/documents/pci_ssc_quick_guide.pdf).

### PCI DSS Requirements

- Build and maintain a secure network
  - **(1)** Install and maintain a firewall
  - **(2)** Do not use vendor-supplied defaults for any security parameters (e.g. passwords)
- 📝 Protect cardholder data
  - **(3)** Protect stored data
    - Storing cardholder data is discouraged, but if stored it must be encrypted or hashed.
    - Never store sensitive data on the magnetic stripe or chip including PIN and CAV2 / CVC2 / CVV2 / CID.
  - **(4)** Encrypt transmission of cardholder data across public networks
- Maintain a vulnerability management program
  - **(5)** Use and regularly update anti-virus software
  - **(6)** Develop and maintain secure systems and applications
- 📝 Implement strong access control measures
  - **(7)** Restrict access to cardholder data by business need-to-know
  - **(8)** Assign a unique ID to each person with computer access
  - **(9)** Restrict physical access to cardholder data
    - Store media back-ups in a secure location, preferably off site.
    - Review and confirm that back-up media is secure at least annually.
- 📝 Regularly monitor and test networks
  - **(10)** Track and monitor all access to network resources and cardholder data
  - **(11)** Regularly test security systems and processes
    - **(11.1)** Test presence of wireless access points on a quarterly basis
    - **(11.2)** Network vulnerability scans at least quarterly and after any significant change
    - **(11.3)** Penetration testing at least once a year and after any significant change
- Maintain an information security policy
  - **(12)** Maintain a policy that addresses information security

## ISO/IEC 27000-series

- Set of worldwide information security standards
- Also known as ***ISMS Family of Standards*** or ***ISO27K***
- ISO/IEC stands for
  - "The International Standard for Standardization (ISO)"
  - and "The International Electrotechnical Commission (IEC)"

### ISO/IEC 27001:2013

- Titled as "Information technology - Security Techniques - Information security management systems — Requirements"
- Defines requirements for the organization's information security management system.
- Applies a risk management process
- Used
  - To create security requirements and objectives
  - To ensure the cost efficiency of managing the security risks
  - To ensure that laws and regulations are followed
  - For defining new information security processes
  - For identifying and clarifying existing information security processes.
  - For determining the status of information security management activities in an organization
  - For implementing business information security
  - For providing relevant security information to customers

### ISO/IEC 27002

- Titled as "Information technology – Security techniques – Code of practice for information security controls".
- Information security controls to enforce best-practices
- Includes controls for e.g. • Access Control • Cryptography • Access Control • Physical and environmental security...

## HIPAA

- Health Insurance Portability and Accountability Act
- 📝 Provides data privacy and protection of medical information.
- Specifies administrative, physical, and technical protection for all entities involved.
- 🤗 Initially created to protect people from losing their health insurance e.g. when changing jobs.
  - Extended to reduce costs and administrative burdens of healthcare transactions.

### HIPAA transactions

- **Healthcare transaction**
  - A transaction is an electronic exchange of information between two parties to carry out financial or administrative activities related to health care
  - Usually represented by claims and enrollment data
  - E.g. a health care provider will send a claim to a health plan to request payment for medical services.
- 📝 **Standard transactions**
  - Adopted standard by HSA (U.S. Health & Human Services) under HIPAA
  - Include • payment and remittance advice • claims status • eligibility • premium payment • enrollment and disenrollment • referrals and authorizations.

### HIPAA rules

- **Electronic transaction and code sets standards**
  - Every provider who performs electronic transactions needs to use the same health care transactions, codes, and identifiers.
- **Security rule**
  - Ensures the confidentiality, integrity, and security of health information
- **Enforcement rule**
  - Details provisions in regard to the compliance, investigations, violations, and hearing procedures.
- **Privacy rule**
  - Protects a person's health information and defines who has the access to the information.
  - Controls include
    - **Administrative safeguards** such as • performing risk analysis • employee training • security policies and procedures • business associate agreements
    - **Physical safeguards** such as • access controls • policies for workstations (e.g. laptops) • workstation security
    - **Technical safeguards** such as • access control • audit control • integrity control • transmission security
- 📝 **National identifier requirements**
  - **National Provider Identifier (NPI)**: A 10-digit number used for covered healthcare providers
  - **National Health Plan Identifier (NHI)**: An identifier that is used for identifying health plans.
  - **Employer Identifier Standard**: A number that identifies employers on standard transactions.

## FISMA

- Federal Information Security Management Act
- 📝 US legislation that regulates federal data security standards and guidelines.
- Protects government information, operations and assets against various threats.
- Provides
  - Standards for
    - categorizing information and information systems by mission impact
    - minimum security requirements for information and information systems
  - Guidance for
    - choosing appropriate security controls for information systems
    - assessing security controls in information systems
    - the security authorization of information systems

### NIST SP 800-53

- Shorthand for National Institute of Standards and Technology Special Publication 800-53
- 📝 Security and privacy controls for federal information systems and organization
- Guidelines to assist in [FISMA](#fisma) compliance

## Sarbanes-Oxley act

- Also known as **SOX** or **Sarbanes Oxley** act.
- US federal law
- Protect investors by making corporate disclosures more reliable and accurate
- Regulates what records organizations must keep and for how long
- E.g. banks need to save financial reports for a very long time
- The act contains 11 titles
  1. Public company accounting oversight board
  2. Auditor independence
  3. Corporate responsibility
  4. Enhanced financial disclosures
  5. Analyst conflicts of interest
  6. Commission resources and authority
  7. Studies and reports
  8. Corporate and criminal fraud accountability
  9. White-collar-crime penalty enhancement
  10. Corporate tax returns
  11. Corporate fraud accountability

## DMCA

- Digital Millennium Copyright Act
- Copyright laws in the USA
- Implements
  - WIPO (World Intellectual Property Organization) Copyright Treaty
  - WIPO Performances and Phonograms Treaty
- Against theft of intellectual property
- E.g. platforms must act as they can not benefit from what is yours, most platforms have copyright notice that you can issue.
- Act contains five titles:
  1. WIPO Treaty Implementation
  2. Online Copyright Infringement Liability Limitation
  3. Computer maintenance or repair
  4. Miscellaneous provisions
  5. Protection of certain original designs

## COBIT

- Framework created by ISACA for information technology (IT) management and IT governance.
- Helps companies follow law, be more agile and earn more.
- Links business and IT.
- Ties in with COSO, ITIL, BiSL, ISO 27000, CMMI, TOGAF and PMBOK.
- Defines processes for the management of IT
  1. Evaluate, Direct and Monitor (EDM)
  2. Align, Plan and Organize (APO)
  3. Build, Acquire and Implement (BAI)
  4. Deliver, Service and Support (DSS)
  5. Monitor, Evaluate and Assess (MEA)
- Components include
  - **Framework**: Link IT objective and best practices to business requirements.
  - **Process descriptions**: Process model to build common language for planning, building, running and monitoring.
  - **Control objectives**: High-level requirements to be considered by management.
  - **Management guidelines**: Helps assign responsibility, agree on objectives, measure performance, and illustrate interrelationship with other processes.
  - **Maturity models**: Assesses maturity and capability per process and helps to address gaps.

## EU Laws

### SCCs

- Standard Contractual Clauses
- Contract between an EU based data exporters and a non-EU-based data importers
- Protects personal data sent from the European Union (EU) to countries with lower level of data protection rights
- Ensures [GDPR](#gdpr) requirements in territories which are not considered to offer adequate protection to the rights and freedoms of data subjects

### EU–US Privacy Shield

- Also known as **PrivacyShield**
- Framework for regulating exchanges of personal data for commercial purposes between the European Union and the United States
- Enables US companies to more easily receive personal data from EU entities
- Became invalid in 16 July 2020 as it did not protect EU citizens on government snooping

### Safe Harbor

- Also known as **International Safe Harbor Privacy Principles**, **Safe Harbour Privacy Principles**, **Safe Harbour decision**
- Signed between US and EU to prevent customer data leakage from private organizations
- Seven principles include: notice, choice (can opt out), onward transfer (only share with compliant companies), security, data integrity, access (can be accessed and deleted by individuals), enforcement
- Abolished in October 2015 and replaced with [EU–US Privacy Shield](#euus-privacy-shield)

### GDPR

- Regulates data processing of EU citizens
- Applies in EU and outside of EU if personal data is collected from EU
- Requires consent to collect data
- **Privacy by design**: Enforces privacy and security measures
- Gives rights such as: • right to be informed • right of access • right to rectification • right to erasure (right to be forgotten) • right to restrict processing • right to data portability • right to object • right in relation to automated decision making and profiling.

### Common Criteria

- Also known as **ISO/IEC 15408**
- Standard for computer security certification
- Tests to evaluate vendor claims of security about its products
- Four aspects to the of evaluation
  - **TOE**: the system being tested
  - **ST** (security target): he documentation describing the TOE and requirements)
  - **PP** (protection profile)
    - The requirements for the type of product being tested)
    - The evaluation assurance level (EAL, the rating level, ranked from 1 to 7).

## Other laws, standards and regulations

- **RFC 1918**: Private IP Standard
- **RFC 3227**: Collecting and storing data
- **CAN-SPAM act**: Email marketing
- **GLBA**
  - Gramm-Leach-Bliley Act
  - Requires financial institutions to take steps to protect customer information
- **FERPA**: Education Records
