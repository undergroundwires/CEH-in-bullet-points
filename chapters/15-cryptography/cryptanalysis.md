# Cryptanalysis

- Process of decryption of ciphers and encrypted text
- Identifies vulnerabilities in cryptosystems

## Cryptanalytic techniques

### Linear cryptanalysis

- Known as **plaintext attack**
- Applicable to block ciphers and stream ciphers.
- Given enough pairs of plaintext and corresponding ciphertext, key can be obtained
- Discovered by By Matsui and Yamagishi in 1992
- Attacker identifies the linear relation between some bits of the plaintext, some bits of the ciphertext and some bits of the unknown key.

### Differential cryptanalysis

- Discovered by Israeli researchers Eli Biham and Adi Shamir in the late 1980s.
- Applicable primarily to block ciphers, but also to stream ciphers and cryptographic hash functions.
- Applicable to symmetric key algorithms
- Comparing differences in the inputs to how each one affects the outcome
- Working with chosen plaintext originally, also works with known plaintext and ciphertext

### Integral cryptanalysis

- Used on block ciphers
- Discovered by Lars Knudsen in 1997
- Input vs Output comparison same as differential, however, runs multiple computations of the same block size input
- Attacker analyzes outputs of encrypting sets of plaintexts where some of the content is held constant and some of the content is varied through all possibilities

## Code-breaking methodologies

- **Frequency analysis**
  - Study of the frequency of letters or groups of letters in a ciphertext
  - E.g. checking cipher chunks against in languages some letters or combination of letters are used more often
  - Can be used to crack a substitution cipher, like rotation cipher ROT13
- **Trickery and deceit**
  - Requires a high level of mathematical and cryptographic skills
  - Using [social engineering techniques](./../10-social-engineering/social-engineering-types.md) to trick someone to encrypt and send a known message
- **One-time pad**
  - A shared random key that has to be the same length or longer than the cipher text
  - Each individual bit or character of plaintext is encrypted by combining it with the corresponding bit or character from the pad using modular addition
  - Assuming to be unbreakable
  - **Drawback**
    - Key distribution becomes impracticable for large messages as key length is same as as the messages

## Cryptography attacks

### Chosen-key Attack

- 📝 Attacker knows keys that are used or can choose the secret key.
- May allow breaking the larger system which relies on that cipher

### Rubber-hose attack

- Also known as **rubber hose** or **rubberhose** attack.
- 📝 Extraction of cryptographic secrets (e.g. the password to an encrypted file) from a person by coercion or torture
- E.g. beating that person with a rubber hose until they give up the encryption key.

### Ciphertext-only attack (COA)

- Also known as **known ciphertext attack**
- 📝 Attacker has only access to cipher texts
- E.g. using frequency analysis to assume plain text
- Early ciphers (using pen-and-paper) were cracked this way
- Modern ciphers have strong protections against it
  - take years to separate statistical departure from random noise

### Known-plaintext attack (KPA)

- Also known as **known-plain-text attack**
- 📝 Attacker has access to parts of plaintext and corresponding ciphertext.
- Can be used to reveal secret keys, code books.
- Classical ciphers are typically vulnerable

#### Meet-in-the-middle attack

- Also known as **meet in the middle attack**.
- Attack over certain block ciphers by decomposing the problem in two halves and proceeds on each part separately
- Reduces the effort to perform a brute-force attack
- 📝 Reason why re-encrypting an ciphertext reduces its security
  - The reason that Triple DES or Double DES is considered weak and are no longer used.
- E.g. transforming an attack that requires `2exp128` time into one that takes `2exp64` time and `2exp64` space
- Type of known-plaintext attack

### Chosen-plaintext attack (CPA)

- 📝 Attacker can choose random plaintexts to be encrypted and obtain the corresponding ciphertexts
- 📝 Two forms
  - **Batch chosen-plaintext attack**
    - Cryptanalyst chooses all plaintexts before any of them are encrypted.
    - Not so effective
  - **Adaptive chosen-plaintext attack**
    - Cryptanalyst makes a series of interactive queries
    - Subsequent plaintexts are chosen based on the information from the previous encryptions.

### Chosen-ciphertext attack (CCA)

- Also known as **chosen ciphertext attack** or **chosen-cipher-text attack**.
- Attacker gathers information by obtaining the decryptions of chosen ciphertexts.
- Early versions of RSA padding used in the SSL protocol were vulnerable.
- Types
  - **Adaptive chosen-ciphertext (CCA2)**
    - Attacker uses the results from prior decryptions to inform their choices of which ciphertexts to have decrypted
  - **Non-adaptive chosen-ciphertext**
    - Attacker chooses the ciphertexts to have decrypted without seeing any of the resulting plaintexts
  - **Lunchtime attack** or **midnight attack**
    - Attacker can have access to system for only a limited amount of time, can access only few plaintext-ciphertext pairs

### Side-channel attacks

- Based on information gained from a computer, rather than weaknesses in the algorithm itself.
- Monitors environmental factors such as power consumption, sound, timing and delay.
- E.g. [RSA keys can be revealed by listening to CPU work](https://www.pcworld.com/article/2082200/listen-up-rsa-keys-snatched-by-recording-cpu-sounds-with-a-phone.html).

#### Timing attack

- Execution times are measured to learn more about the system
- Information to find can include e.g. key, CPU used, algorithms, input, implementation details etc.
- A type of side-channel attack

### Brute-force attack

- Also known as **brute force**
- Trying every possible combination of characters to break the encryption
- 📝 ❗️ Requires a lot of time and processing power.
- See also [Brute-force attack | Cracking passwords](./../06-system-hacking/cracking-passwords-overview.md#brute-force-attack)

#### Birthday Attack

- Type of [brute-force](#brute-force-attack) attack but faster that focuses on collisions
- Based on collisions where attacker uses own plain texts to match hashes (find collisions)
- Depends on the higher likelihood of collisions found between random attack attempts and a fixed degree of permutations
- Exploits [birthday problem](https://en.wikipedia.org/wiki/Birthday_problem) in probability theory
  - E.g. 23 people in room, chance of two having same birthday is not `23 / 365 = ≈6%` but it's 50%. For 75 people it's 99% chance.

#### Rainbow table attack

- 📝 Rainbow table contains precomputed hashes to try and find out passwords
- Faster than [brute-force](#brute-force-attack) however the trade-off is that it takes a lot of storage (sometimes Terabytes) to hold the Rainbow Tables themselves.
- Tools
  - [HashCalc](https://www.slavasoft.com/hashcalc/)
  - [MD5 Calculator](http://onlinemd5.com/)

### Dictionary attack

- Attacker creates and uses a dictionary of plaintext and its ciphertext.
- E.g. words in a dictionary
- E.g. previously used passwords, often from lists obtained from past security breaches
  - See also [Dictionary attacks | Cracking passwords](./../06-system-hacking/cracking-passwords-overview.md#dictionary-attack)

### Related-key attack

- Attacker observes the operation of a cipher under several different keys
- Some relationship connecting the keys is known to attacker while key values are unknown.
- E.g. attacker knows that last 80 bits of the keys are the same

### DUHK Attack (Don't Use Hard-Coded Keys)

- Allowing attackers to access keys and read communications in certain VPN implementations
- Based on vulnerability affecting devices using ANSI X9.31 Random Number Generator (RNG) with a hard-coded seed key

### Collision attack

- Also known as **hash collision attack**
- 📝 Tries to find two inputs resulting in same hash value, i.e. a hash collision.
  - Find two different messages `m1` and `m2` such that `hash(m1) = hash(m2)`.
- Extended by **chosen-prefix collision attack**
  - Given two different prefixes `p1`, `p2`
    - The attack finds two appendages `m1` and `m2` such that `hash(p1 ∥ m1) = hash(p2 ∥ m2)`
      - where `∥` is the concatenation operation.
  - More powerful
- 💡 The larger the hash value size, the less likely there are for collisions to occur and therefore the more [collision resistant](./hashing-algorithms.md#collision-resistance) the hash algorithm

## Cryptography attack tools

- [L0phtcrack](https://www.l0phtcrack.com/)
  - Password cracking tool
  - Used mainly against Windows [SAM files](./../06-system-hacking/microsoft-authentication.md)
- 📝 [John the Ripper](https://www.openwall.com/john/)
  - Password cracking tool
  - Can run against hashed/encrypted passwords of OSes, databases etc.
  - See also [John the Ripper | Password cracking tools](./../06-system-hacking/password-cracking-tools.md#john-the-ripper)
- [CrypTool](https://www.cryptool.org/en/)
  - Open-source program for for cryptography and cryptanalysis
  - GUI to experiment with cryptographic procedures and to animate their cascades
- [Cryptobench](http://www.addario.org/cryptobench/)
  - Encrypt, decrypt, hash using many algorithms
  - Helps in the cryptanalysis process of common cryptographic schemes
