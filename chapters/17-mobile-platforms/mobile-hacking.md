# Mobile hacking

## Motivations

- **Surveillance**: • Audio • Camera • Call logs • Location • SMS messages
- **Financial**: • sending high rate SMS • stealing transaction authentication numbers (TANs) • extortion via ransomware • fake antivirus • making expensive calls
- **Data theft**: • Account details • Contacts • Call logs • phone number • stealing IMEI
- **Botnet activity**: • launching DDoS attacks • click fraud • sending SMS
- **Impersonation**: • SMS redirection, sending e-mail messages, posting to social media

## Attack vectors

- Malware
- Data exfiltration
- Data tampering
- Data loss

## Vulnerabilities and risks

- Malicious apps in stores
- Mobile malware
- App sandboxing vulnerabilities
- Weak device and app encryption
- OS and app update issues
- Jailbreaking and rooting
- Mobile application vulnerabilities
- Privacy issues (Geolocation)
- Weak data security
- Excessive permissions
- Weak communication security
- Physical attacks
- Insufficient code obfuscation
- Insufficient transport layer security
- Insufficient session expiration

## Security issues from App Stores

- Used to distribute malware/malicious apps
- App: Software that runs on mobile devices
- App Store: Distribution platform
  - Can be from owners of the OS e.g. Apple, Google play, Microsoft.
  - Or third parties e.g. Amazon Appstore, GetJar, and APKMirror.
- Can be distributed through
  - legitimate app stores
    - because of insufficient or no vetting of apps
  - unofficial app stores
    - user is social engineered to download and execute

## Sandboxing

- App sandboxing
  - Limits resources available to an app
  - Isolates one from another
  - ❗ A vulnerable one can still be exploited

## Mobile spam

- Also known as SMS spam, text spam, or m-spam
- Advertisements or malicious links
- E.g. you've won a prize, click here to claim it.

## SMiShing

- SMS phishing
- Acquire personal information through SMS with malicious links
- Effective as
  - Easy through e.g. using prepaid SMS card using fake identity
  - Usually not checked by antiviruses
  - Users are not familiar
- E.g. "PayPal - your account has been locked"

## Pairing

- Pairing with malicious devices may enable e.g. [BlueSnarfing](./../09-wireless-networks/bluetooth.md#bluesnarfing) and [BlueBugging](./../09-wireless-networks/bluetooth.md#bluebugging)
