# Cryptography overview

- Process of hiding information
- Can protect e.g. emails, files, and other sensitive data.

## Cryptography terms

- **Cipher**: an algorithm performing encryption and decryption
- **Clear text / plaintext**: unencrypted data
- **Cipher text**: encrypted data
- **Key**: specifies the transformation of data for encryption / decryption

## Cipher types

- **Cipher**: algorithm performing encryption and decryption.

## Classical ciphers

- Used historically but no longer used for the most part.
  
### Substitution cipher

- Every character is substituted with another one
- E.g. [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher) (100 BC)

  ```txt
    Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
    Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
    Key: right shift of 3
  ```

### Polyalphabetic cipher

- Based on substitution
- Uses multiple substitution alphabets
- E.g. [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) from 1467
  - Has cipher has several Caesar ciphers in sequence with different shift values.

### Transposition cipher

- Plain text is repositioned (shifted) to create a ciphertext
- Also called a **zigzag cipher**
- E.g. [Rail fence cipher](https://en.wikipedia.org/wiki/Rail_fence) (invented by ancient Greeks)

  ```txt
    Clear text: WE ARE DISCOVERED. FLEE AT ONCE

    W . . . E . . . C . . . R . . . L . . . T . . . E
    . E . R . D . S . O . E . E . F . E . A . O . C .
    . . A . . . I . . . V . . . D . . . E . . . N . .

    Ciphertext: WECRLTEERDSOEEFEAOCAIVDEN
  ```

## Modern ciphers

### Computational infeasibility

- Modern cryptographic systems are built on problems which are assumed to be **computationally infeasible**
- A computation which although computable would take far too many resources to actually compute.
- Cryptography tries to ensure an infeasible computation's cost is greater than the reward obtained by computing it
- "Secure" because it's "too slow" to achieve by computers.

### Key-based ciphers

#### Symmetric encryption

- One (same) key to encrypt and decrypt
  - Known as **single key** or **shared key**.
- Either uses stream cipher or block cipher
- E.g. [AES](./encryption-algorithms.md#aes-advanced-encryption-standard), [DES](./encryption-algorithms.md#des-data-encryption-standard)
- Problems include key distribution and management
- Suitable for large amounts of data
- Harder for groups of people because more keys are needed as group increases
- Doing nothing for non-repudiation, only performs confidentiality

#### Asymmetric encryption

- Also known as **public key cryptography**
- 📝 Different keys to encrypt and decrypt
  - **Public key** to encrypt
    - Known by everyone
    - Can be issued by [Public Key Infrastructure (PKI)](./encrypting-communication.md#public-key-infrastructure-pki)
  - **Private key** to decrypt
    - Only known by the owner, secret to the public.
- It's slower than [symmetric encryption](#symmetric-encryption)
  - 📝 **Hybrid encryption**
    - Combining
      - public-key cryptography for ease of secure key exchange
      - symmetric-key cryptography for speed
    - E.g. SSL/TLS uses asymmetric encryption to create a key that's later used for encrypting/decrypting packets.
- 📝 Used in • [digital certificates](./encrypting-communication.md#digital-certificate) • [PKI](./encrypting-communication.md#public-key-infrastructure-pki) • [SSH](./tunneling-protocols.md#ssh-secure-shell) • [PGP](./encrypting-communication.md#pgp-pretty-good-privacy) • [IPSec](./tunneling-protocols.md#ipsec)
- Algorithms include • [RSA](./encryption-algorithms.md#rsa-rivestshamiradleman) • [DSA](./encryption-algorithms.md#dsa-digital-signature-algorithm) • [Diffie-Hellman](./encryption-algorithms.md#diffiehellman)

##### Forward secrecy

- Also known as **perfect forward secrecy**
- Property of cryptographic systems ensuring future disclosure of encryption keys cannot be used to decrypt communications in past.
- Ensures that a session key derived from a set of public and private keys will not be compromised if one of the private keys is compromised in the future
- E.g. web traffic cannot be decrypted with only server's private key through a court order.

### Input-based ciphers

#### Block cipher

- 📝 Fixed-size blocks of data using a symmetric key
- Data bits are split up into blocks and fed into the cipher
- Each block of data (usually 64 bits) is encrypted with key and algorithm
- Simpler and slower than stream ciphers
- Key chosen for cipher must have a length larger than the data, if not, it is vulnerable to frequency attacks

#### Stream cipher

- 📝 One bit at a time using a symmetric key
- Combines each bit with a pseudorandom cipher digit stream (keystream)
- Works at a high rate of speed
- Usually done by an combining [XOR](#xor-cipher) with random generated key.

##### XOR cipher

- Also known as • **exclusive OR** • **modulus 2** (addition/subtraction).
- 📝 If the inputs match, the output is a 0; otherwise, it is a 1.

  | A | B | Output |
  |:-:|:-:|:------:|
  | 0 | 0 | 0 |
  | 0 | 1 | 1 |
  | 1 | 0 | 1 |
  | 1 | 1 | 0 |

- ❗ If the key chosen is actually smaller than the data, the cipher will be vulnerable to frequency attacks
- Uses "⊕" that denotes the exclusive disjunction (XOR) operation
- Applying XOR operator at every character encrypts, re-applying it decrypts.
