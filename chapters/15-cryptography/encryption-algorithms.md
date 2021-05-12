# Encryption algorithms and techniques

- **Algorithm**: step-by-step method of solving a problem
- **Encryption algorithms**: mathematical formulas used to encrypt and decrypt data
- Keys should still change on a regular basis even though they may be "unhackable"
- 📝 In terms of speed
  - Symmetric encryption algorithms are faster than asymmetric algorithms
  - Stream ciphers (including AES in CTR) are [usually faster](https://crypto.stackexchange.com/a/31281) than [hash functions](./hashing-algorithms.md#hash-functions)

## Encryption types per OSI layer

| [OSI layer](./../03-scanning-networks/tcpip-basics.md#osi-model) | Encryption type | Description |
|:---------:| --------------- | ----------- |
| 2 | Link encryption | Everything including original headers is encrypted |
| 3 | Network encryption | Everything in the packet is encrypted |
| 4 | Protocol encryption | Specific protocols are entirely encrypted e.g. [SSL](./encrypting-communication.md#ssl-secure-sockets-layer) |
| 5 | Service based encryption | Encryption for specific services on specific hosts |
| 6 | Data encryption | |
| 7 | Application based information encryption | |

## Symmetric algorithms

- Both ends of the transmission must use the same key.
  - Requires to find a secondary secure channel to send the symmetric key to the recipient to ensure security.

### DES (Data Encryption Standard)

- Block cipher, 56-bit key, 64-bit block size
- Developed in the early 1970s at IBM
- Was a standard set by NSA but was withdrawn, quickly outdated
- Used in initial implementation of Kerberos but later deprecated
- Considered insecure, has been superseded by the [Advanced Encryption Standard (AES)](#aes-advanced-encryption-standard)

### 3DES (Triple Data Encryption Standard)

- Block cipher, 168-bit key
- More effective than DES but much slower
- 3 keys are used:
  1. Used to encrypt the plain text
  2. Used to decrypt ciphertext resulting from the first round of encryption
  3. Used to encrypt the ciphertext that resulted from the decryption with the 2nd key

### AES (Advanced Encryption Standard)

- Iterated block cipher, 128, 192 or 256 bit key, 128-bit block size
- Original name is **Rijndael**, named to AES after [Advanced Encryption Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard_process) contest.
- Symmetric-key algorithm
- Performs same operation multiple size
- Approved and used by NSA
- Much faster than DES and 3DES for bulk data encryption.

### RC (Rivest Cipher)

- 📝 Symmetric-key algorithm.
- Lost to [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard_process) in [Advanced Encryption Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard_process) contest.

#### RC4

- Variable length key algorithm
- Uses random permutations
- Stream cipher

#### RC5

- Parameterized algorithm
- Block cipher (slower)
- Variable
  - block size: can be 32, 64, or 128 bits
  - key size: between 0 and 2048 bits
  - number of rounds: between 0 and 255

#### RC6

- Extends RC5 with two features
  1. integer multiplication
  2. 4-bit registers (RC5 uses 2-bit registers)

### Blowfish

- Fast symmetric block cipher, 64-bit block size, 32 to 448 bits key
- Considered public domain
- Insecure

### Twofish

- Symmetric-key block cipher
- Uses 128-bit blocks
- Key size can range between 0 and 256 bits.
- Lost to [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard_process) as finalist in [Advanced Encryption Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard_process) contest.

## Asymmetric algorithms

### RSA (Rivest–Shamir–Adleman)

- One of the common used encryption standards for data transmission.
- 📝 Achieving strong encryption through the use of two large prime numbers
- **Solves**
  - I want anybody to be able to encrypt a message, but I'm the only one who can decrypt it. I don't want to share decryption keys with anybody.
- There are no published methods to defeat the system if a large enough key is used.
- Wide usage, e.g. SSH for public key authentication
  - A lot safer than password authentication (should be disabled after copying keys)
  - Steps
    1. `ssh-gen -t rsa` creates private and public keys in `.ssh` folder
    2. Copy the key to server to be connected
       - Can run e.g. `ssh-copy-id user@192.168.122.37` with ssh password
       - Or just copy `~/.ssh/id_rsa.pub` to the server manually.
- 💡 In RSA crypto, when you generate a key pair, it's completely arbitrary which one you choose to be the public key, and which is the private key.
  - If you encrypt with one, you can decrypt with the other - it works in both directions.
  - When encrypting, private key is used to decrypt and public key to decrypt
    - "I want to be able to encrypt certain information and use it as a product key for my software."
  - When signing, private key is used to encrypt and public key to decrypt
    - "I want to use my private key to generate messages so only I can possibly be the sender."
- Recommended key size is 2048 bits or higher.
- 🤗 [RSA Factoring Challenge](https://en.wikipedia.org/wiki/RSA_Factoring_Challenge)
  - Held between 1991 and 2007 with price awards
  - Goal was to factoring prime numbers used by RSA
  - Shows cryptanalytic strength of RSA

### Diffie–Hellman

- Also known as **Diffie Hellman** or **DH**
- Used for generating a shared key between two entities over an insecure channel.
- One of the first public-key protocols
- 📝 Used in • [SSL](./encrypting-communication.md#ssl-secure-sockets-layer) • [IKE (Internet Key Exchange) | IPsec](./tunneling-protocols.md#ike-internet-key-exchange)
- ❗ If digital signatures are waived, vulnerable to MITM attacks
- Enables two parties to encrypt their traffic with a shared key.
- **Solves**: We have a symmetric encryption scheme and want to communicate. We don't want anybody else to have the key, so we can't say it out loud (or over a wire).

#### Diffie–Hellman groups

- Determines the strength of the key used in the Diffie-Hellman key exchange process.
- Higher Diffie-Hellman Group numbers are more secure, but requires more computation power.
- • Group 1 (768-bit) • Group 2 (1024-bit) • Group 5 (1536-bit) • Group 14 (2048-bit) • Group 15 (3072-bit) • Group 19 (256-bit elliptic curve) • Group 20 (384-bit elliptic curve) • Group 21 (521-bit elliptic curve) • Group 24 (2048-bit, 256 bit subgroup)

#### Elliptic-curve Diffie–Hellman

- Also known as • **ECDH** • **Elliptic curve Diffie Hellman**
- Variant of the Diffie–Hellman protocol using [elliptic-curve cryptography](#ecc-elliptic-curve-cryptography)
- 📝 Used in • [SSH](./tunneling-protocols.md#ssh-secure-shell) • [TLS 1.3](./encrypting-communication.md#tls-transport-layer-security)

### ECC (Elliptic-curve cryptography)

- Also known as **elliptic curve cryptosystem**
- Using points on elliptical curve along with logarithmic problems
- Using less processing power, smaller keys, good for mobile devices

### DSA (Digital Signature Algorithm)

- Asymmetric algorithm
  - Private key tells who signed the message
  - Public key verifies the digital signature
- In the message exchange, each entity creates a public and private key.
- Per [FIPS 186-5](https://doi.org/10.6028/NIST.FIPS.186-5-draft), it's not recommended for signature generation but approved for signature verification.

## Symmetric vs asymmetric algorithms

| Differentiator | Symmetric Key Encryption | Asymmetric Key Encryption |
| -------------- | ------------------------ | ------------------------- |
| **Key** | Only one key (symmetric key) is used to encrypt and decrypt | Two different cryptographic keys (asymmetric keys), called the public and the private keys, are used to encrypt and decrypt |
| **Complexity and Speed of Execution** | Simple technique, fast encryption | More complicated process, slower |
| **Length of key** | Smaller, usually 128, 256 and 512 bits | Much larger, e.g. recommended RSA key size is 2048 bits or higher |
| **Common usage** | When large chunks of data need to be transferred. | Smaller transactions, primarily to authenticate and establish a secure communication channel prior to the actual data transfer. |
| **Security** | The secret key is shared. Consequently, the risk of compromise is higher. | The private key is not shared, and the overall process is more secure as compared to symmetric encryption. |
