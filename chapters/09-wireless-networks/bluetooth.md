# Bluetooth

- Range is typically less than 10m
- Operates on the 2.4 GHz
- Discovery feature can control the visibility of the device
- **Bluetooth Low Energy (BLE)**: Bluetooth >= 4.0
- **Bluetooth Classic (BC)**: Bluetooth < 4.0
- Uses WPAN (wireless personal area network)
- Utilize the Gaussian Frequency Shift Keying (FSK) to exchange information in the basic rate (BR) of usually 1 mbps.

## Bluetooth security

- Standard provides three basic security services:
  - **Authentication**
    - To verify the identity of communicating devices
  - **Confidentiality**
    - To prevent the compromise of information and ensure that only
    authorized devices can access and view data.
  - **Authorization**
    - To allow the control of resources by ensuring that a device is
    authorized to use a service before permitting it to do so.
- ❗ Standard does not address address other security services such as audit and non-repudiation.
- Four security modes (levels):
  1. **Mode 1**: No authentication/encryption.
  2. **Mode 2**: Authorization with access control policies.
  3. **Mode 3**: Mandate authentication and encryption using secret key with paired devices
  4. **Mode 4**: Secure Simple Pairing using [Elliptic-Curve Diffie-Hellman (ECDH)](./../15-cryptography/encryption-algorithms.md#elliptic-curve-diffiehellman) for key exchange and link key generation

## Bluetooth device discovery

- [BlueScanner](https://sourceforge.net/projects/bluescanner/): Finds devices around and displays information
- [BT Browser](http://www.bluejackingtools.com/java/bt-browser-20/): Find and enumerate nearby devices

## Bluetooth attacks

### BlueSmacking

- 📝 DoS attack using echo.

### BlueJacking

- 📝 Sending unsolicited data to bluetooth devices
- Allows spamming for bluetooth also known as **BlueSpamming**
- ❗ Not related to hijacking

### BluePrinting

- 📝 Extracting information about the device

### BlueSnarfing

- 📝 Stealing data from target device
- E.g. calendars, contact lists, emails and text messages

### BlackJacking

- 📝 Exploits a blackberry device to attack corporate LAN directly
- Compromises blackberry then proxies between corporate servers and attacker.

#### BBProxy

- 📝 Bluejacking tool
- Included in [BlackBerry Attack Toolkit](https://sourceforge.net/projects/bbat/)
- Announced by [DefCon](https://www.defcon.org/images/defcon-14/dc-14-presentations/DC-14-X30n.pdf)

### BlueBugging

- Also known as **bluebug-attack**
- Create a [backdoor attack](./../07-malware/malware-overview.md#backdoor) before returning control of the phone to its owner
- Extends [BlueJacking](#bluejacking) and [BlueSnarfing](#bluesnarfing) (allows attacker to access data)
- E.g. by pretending to be a headset to receive phone calls
- Not so common as vulnerabilities are generally patched

#### Bloover

- A proof-of-concept [tool](https://trifinite.org/trifinite_stuff_blooover.html)
- 📝 Exploits bluebugging targeting J2ME (Java micro edition) enabled phones such as Nokia
- [Bloover II](https://trifinite.org/trifinite_stuff_bloooverii.html): Exploits bluebug and also helomoto, bluesnarf and OBEX object push attacks

## Bluetooth attacks countermeasures

- Check paired devices
- Turn off visibility / turn off Bluetooth if not used
- Use strong PIN
- Use encryption
- Use the strongest security mode available
- Don't accept unknown requests
- Use [bluetooth security tools](#bluetooth-security-tools)

## Bluetooth security tools

- [Bluetooth firewall](http://www.fruitmobile.com/bt_firewall.html)
  - Mobile app for logging and monitoring Bluetooth connections
  - Radar feature allows you to scan nearby bluetooth devices
  - Scan feature lists apps that can perform bluetooth actions
- [Bluediving](https://github.com/balle/bluediving)
  - Bluetooth penetration suite
  - Exploits BlueBug, BlueSnarf, BlueSnarf++ and BlueSmack
- [Bluelog](https://github.com/MS3FGX/Bluelog)
  - Linux Bluetooth scanner
- [btscanner](https://packages.debian.org/unstable/btscanner)
  - Debian tool to extract information from a Bluetooth device without the requirement to pair.
- [BlueRanger](https://tools.kali.org/wireless-attacks/blueranger)
  - Simple Bash script which uses Link Quality to locate Bluetooth device radios
