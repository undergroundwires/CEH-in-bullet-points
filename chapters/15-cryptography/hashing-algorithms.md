# Hashing algorithms

- Also known as **one-way functions**, **hash functions** or **message-digest-functions**
- Calculates unique fixed-size representation of a block of information.
- Cannot be reversed.
- 📝 Used for
  - integrity e.g. when downloading a file in internet, you can compare downloaded files hash with hash given on the website to ensure the right file is downloaded
  - storing passwords in a database by e.g. operating systems
- **Checksum**
  - Number created by a message digest.

## Collision resistance

- Property of a hash function
- 📝 [Computationally infeasible](cryptography-overview.md#computational-infeasibility) to find two colliding inputs
- See also [Collision attack | Cryptanalysis](./cryptanalysis.md#collision-attack)

## Hash functions

### MD5

- 📝 Most popular message digest algorithm.
- Takes any length of input and produces a 128-bit hash
- Considered very insecure as it is easy to reverse with current processing power
- Still used commonly in integrity checking e.g. file download verification

### SHA

- Secure Hashing Algorithms
- 📝 Generates a cryptographically secure message digest.
- Published by NIST (National Institute of Standards and Technology)
- Generations
  - **SHA-0**
    - Withdrawn shortly after publication due to a flaw and replaced with revised SHA-1
  - 📝 **SHA-1**
    - Produces 160-bit digests
    - Designated by NSA
  - **SHA-2**
    - Primarily SHA-256 (32-bit block words), SHA-512 (64-bit block words)
    - Truncated versions: SHA-224, SHA-384, SHA-512/224 and SHA-512/256
    - Designated by NSA
  - **SHA-3**
    - Chosen after competition by non-NSA designers
    - Supports same hash lengths as SHA-2
    - Internal structure differs significantly from the rest of the SHA family.

### RIPEMD (RACE Integrity Primitives Evaluation Message Digest)

- 160-bit hash algorithm
- Working through 80 stages made up of 6 blocks that executes 16 times each
- Using modulo 32 addition

## HMAC

- Expands either as
  - Keyed-hash message authentication code
  - Hash-based message authentication code
- Uses a combination of a cryptographic key and hash function such as SHA-1 or MD5.
- Used for authentication and integrity checks.
- E.g. `HMAC_SHA256("key", "The quick brown fox jumps over the lazy dog") = f7bc83f430538424b13298e6aa6fb143ef4d59a14946175997479dbc2d1a3cd8`
- Uses **keyed hashing** to generate hashed-based MACs (HMAC).  
  - Involves hashing a message with a • hash function and • a secret key.
  - Message authentication codes (MACs)
    - Cryptographic checksums
    - Used to detect when an attacker has tampered with a message
  - Keyed hashing vs [salted hashes](#salted-hash)
    - Keyed hashing is against tampering, hash salting is against brute-force attacks.
    - Salts are not assumed to be secret but keys are.
- HMAC can provide digital signatures without PKI infrastructure
  - Delegates the key exchange to the communicating parties
  - Parties are responsible for establishing and using a trusted channel to agree on the key prior to communication

## Hash function attacks

- [Collision](./cryptanalysis.md#collision-attack)
- [Birthday attack](./cryptanalysis.md#birthday-attack)
- [Rainbow tables](./cryptanalysis.md#rainbow-table-attack)
- [Brute-force attack](./cryptanalysis.md#brute-force-attack)

### Hash function attack countermeasures

#### Salted hash

- 📝 Hash is used with salt (collection of random bits) to obscure the hash.
- Goal is to increase protection against dictionary and brute-force attacks.
- Usually the salt is stored along with the hash of e.g. password.
- See also [Password cracking countermeasures](./../06-system-hacking/cracking-passwords-overview.md#password-cracking-countermeasures)

#### Key stretching

- Converting a key (e.g. password) to a longer and more random key to e.g. use as encryption.
- Makes encryption stronger as it increases the time and resources for brute-force attacks.
- Usually done by re-hashing multiple (e.g. a few million) times
- E.g. using slow key derivation functions such as PBKDF2
