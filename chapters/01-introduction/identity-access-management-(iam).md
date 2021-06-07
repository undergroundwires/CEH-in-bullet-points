# Identity and access management (IAM)

- Ensures right users have access to right resources at right time
- Framework of best-practices used by organizations
- Main modules:
  1. **Access Management Module**: • Authentication • Authorization.
  2. **Identity Management Module**: Management of users and enterprise directory service components of IAM.

## IAM components

### Access management

#### Authentication

- Session Management
- Password Service

##### Single sign-on (SSO)

- Also known as ***single sign on***
- 📝 Allows one set of login credentials to be used to access multiple applications
- Centralized session and user authentication service
- Easier administration
- Benefits for users including remembering one password instead of many
- Many user authentication problems can be resolved at a central location at SSO point.

##### Multi-factor authentication (MFA)

- Authentication method that requires the user to provide two or more verification factors to gain access to a resource
- **Two-factor authentication (2FA)** is subset of MFA using two different factors
- 📝 Authentication factors include
  - **Knowledge** - something only the user knows
    - E.g. password or PIN
    - Vulnerable to recording user screen, e.g. [attack against PayPal](https://www.welivesecurity.com/2018/12/11/android-trojan-steals-money-paypal-accounts-2fa/)
  - **Possession** - something only the user has
    - E.g. smart cards, security token
    - Vulnerable to be cloned/copied
  - **Inherence** - something only the user is
    - E.g. biometrics (• fingerprint, face, voice, iris, retinal recognition • behavioral: keystroke dynamics)
      - **Retina**: Sending an intrusive close light to compare blood vessels
      - **Iris**: Mapping structures of iris using a camera.
    - Vulnerable to manually prompting users, e.g. [touch ID scams that targeted Apple devices](https://www.wired.com/story/iphone-touch-id-scam-apps/)
  - **Location**: somewhere the user is
    - E.g. based on network, known country
    - Vulnerable to proxies

##### One-time password (OTP)

- A password that's only used once and only valid for a limited of time-
- Enforces strong password authentication as it protects against someone getting access to password.
- Usually used when authenticating to VPN, and online Internet banking systems.

###### OTP Token

- Tool used to generate one-time passwords
- Can be a hardware device or software token installed on the computer or phone.
- Authenticating server use the same algorithm as token to be able to validate the code.
- 📝 **Token types**
  - **Synchronous Tokens**
    - **Clock-based tokens**
      - Also known as **Time-based tokens**
      - Tokens have same time configuration as the authenticating server.
      - Both use algorithms that are based on a time and a shared secret key.
    - **Counter-based tokens**
      - Both the token and the authenticating server maintain a counter.
      - Code consists of the value from the counter and a shared secret key.
      - Requires one or more actions from users (e.g. powering on or PIN number) to increment the counter.
  - **Asynchronous Tokens**
    - Also known as • **challenge-response tokens** • **challenge/response tokens**
    - Server sends a challenge (random value) to user and expects user to enter it.
    - Protects against replay attacks

#### Authorization

- Rule-based Authorization
- Attribute-based Authorization
- Remote Authorization

##### Role-based authorization

- Restricting system access to authorized users
- Can implement
  - **Mandatory access control** (MAC)
    - OS-enforced access control based on subject's clearance and object's labels
    - Assigns sensitivity labels to data and controls access by matching the user's security level to the resource label.
    - E.g. traditional Unix system of users, groups, and read-write-execute permissions
  - **Discretionary access control** (DAC)
    - Restricting access to objects based on the identity of subjects and/or groups to which they belong
    - Allows the data owner to set security permissions for the object
    - E.g. unix file mode which represent write, read, and execute in each of the 3 bits for each of User, Group and Others
    - E.g. on Windows, you can set sharing and permissions on files/folders you create
- RBAC vs MAC vs DAC
  | Access Control | User rights | Popular |
  | -------------- | ------------ | ------ |
  | **Discretionary** | Full control | OS file systems |
  | **Mandatory** | No control, policies are predefined by root/admin | OS file systems |
  | **Role based access** | No control, policies are predefined by root/admin | Cloud computing |

### Identity management

#### User management

- Delegated administration
- User and Role Management
- Provisioning
- Password Management
- Self-service
- **Compliance Auditing**
  - Conduct security audit for company to be compliant with policies/regulations

#### Enterprise directory service

- Central repository where all others components gets their data
- Includes
  - Directory service
  - Data synchronization
  - Metadirectory
  - Virtual directory
