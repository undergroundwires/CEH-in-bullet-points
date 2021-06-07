# Social engineering overview

- 📝 Art of convincing people to reveal confidential information
- Exploits peoples
  - **unawareness** about importance of data or social engineering attacks
  - **careless** about protecting data
  - **trust**
  - **fear** of consequences of not providing the information
  - **greed** for promised gain for providing requested information
  - **moral obligation** sense
- Type of [footprinting](./../02-footprinting/footprinting-overview.md).
- 🤗 Well-known social engineering examples
  - [**RSA attack**](https://www.washingtonpost.com/blogs/post-tech/post/cyber-attack-on-rsa-cost-emc-66-million/2011/07/26/gIQA1ceKbI_blog.html): $66 million loss based on e-mail with attachment exploiting [zero day](./../01-introduction/information-security-overview.md#zero-day-attack) Flash vulnerability through an Excel macro.
  - [**Ubiquiti networks scam**](https://www.nbcnews.com/tech/security/ubiquiti-networks-says-it-was-victim-47-million-cyber-scam-n406201): $47 million stolen by impersonation of executives with requests to companies finance department.
  - [**US Department of Justice attack**](https://www.trendmicro.com/vinfo/pl/security/news/cyber-attacks/hackers-leak-information-of-30-000-fbi-and-dhs-employees): One employee e-mail was hacked, then hacker pretended to be a new employee and asked for all access codes, ended up with leak of 30.000 FBI and DHS employee data
  - [**Yahoo Customer Account Attack**](https://www.wsj.com/articles/yahoo-triples-estimate-of-breached-accounts-to-3-billion-1507062804): 3 billion users data was stolen and used for social engineering (e.g. if two people are connected)

## Steps of social engineering

1. **Research**
   - Gather enough information about the target company
   - Collected by e.g. [dumpster diving](./social-engineering-types.md#dumpster-diving), scanning, company tour, search on the internet...
2. **Select target**
   - Choose a target employee
   - Some employees are more vulnerable than others
     - Easy targets also known as **Rebecca** and **Jessica** mean a person who is an easy target for social engineering such as the receptionist of a company
     - E.g. receptionists, help-desk personnel, tech support, system administrators, clients.
   - A frustrated target is more willing to reveal information
3. **Relationship**
   - Earn the target employee's trust e.g. by creating a relationship
4. **Exploit**
   - Extract information from the target employee

## Identity theft

- Stealing someone elses personally identifiable information to pose as that person
  - E.g. name, credit card number, social security or driver license numbers
- Can be used to impersonate employees of a target

### Steps of stealing an identity

1. Gather targets information
   - Through e.g. bill from social networks, dumpster diving
   - Information include usually first and last name, date of birth, address, social security number, bank accounts, id card and passport numbers.
2. Fake identity proof: get fake IDs
   - Can be driving licence, ID card, etc...
   - E.g. using stolen bills you can claim the person lost driving license and get new one to an address you choose.
3. Fraud: spend money, unauthorized access, use ID for frauds, etc...
   - Can open new credit card accounts on the victim's name
   - Can sell identity information

### Identity theft countermeasures

- Check the credit card reports periodically
- Safeguarding personal information at home and in the workplace
- Verifying the legality of sources.

## Impersonation on social network sites

## Gaining information through social network sites

- Information is used for spear phishing, impersonation, and identity theft.
- Can e.g. create a fake user group "Employees of the company" in **Facebook**
  - Invite people to group and collect credentials such as birth date, employment/education backgrounds.
- Can scan profile pages in **LinkedIn** and **Twitter**.

### Steps of social media impersonation

1. Gather personal information from Internet including social network sites
   - E.g. full name, date of birth, email address, residential address.
2. Create an account that is exactly the same
3. Carry out social engineering attacks with the account e.g.:
   - Introduce it to targets friends in a convincing way to reveal information
   - Join the target organization's employee groups where they share personal and company information.

### Corporate threats from social network sites

- Social network has vulnerable authentication as it's not isolated like corporate network.
- The employee while communicating on social network may not take care of sensitive information.

## Physical security

- **Physical measures**
  - E.g. air quality, power concerns, humidity-control systems
- **Technical measures**
  - E.g. smart cards and biometrics
- **Operational measures**
  - E.g. policies and procedures to enforce a security-minded operation.
- **Access control**
  - **Biometrics**
    - Something you are
    - **False rejection rate (FRR)**
      - When a biometric rejects a valid user
    - **False acceptance rate (FAR)**
      - When a biometric accepts an invalid user
    - **Crossover error rate (CER)**
      - Combination of the FRR ad FAR; determines how good a system is
- **Environmental disasters**
  - E.g. hurricanes, tornadoes, floods.
- See also [Physical security | Information security controls](./../01-introduction/physical-security.md)

## The Social-Engineer Toolkit (SET)

- [Open-source tool](https://github.com/trustedsec/social-engineer-toolkit) for Linux and macOS
- Available in [Kali Linux](https://tools.kali.org/information-gathering/set)
- Templates and cloning for credential harvesting
- Functions such as website attack vectors, mass mailer attack, sms spoofing, QRCode generator, WAP attack...
