# Disk encryption

- Encryption of all data stored on a disk.
- Data-at-rest protection
- Protect the data stored in the disk and ensure its confidentiality
- 📝 Protects against someone who gains physical access to your device
  - ❗ But does not protect from malware or from being attacked by hackers over the internet

## Full Disk Encryption (FDE)

- Encrypting every bit of data stored on a disk or a disk volume
- Working similar to text-message encryption and protects data even OS is not active
- Protects system folders, files, and MBR until valid credentials are provided at pre-boot

## Disk encryption tools

- [VeraCrypt](https://www.veracrypt.fr/)
- [Symantec Drive Encryption](https://help.symantec.com/cs/SEE11.3_MS/SEEMS/v98749288_v130891549/Configuring-the-Drive-Encryption---Encryption-policy-options)
- [BitLocker Drive Encryption](https://en.wikipedia.org/wiki/BitLocker)
- [cryptsetup](https://gitlab.com/cryptsetup/cryptsetup)
  - Open-source disk encryption utility tool
  - Supports [LUKS (Linux Unified Key Setup)](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup), TrueCrypt, VeraCrypt, BitLocker, loop-AES, dm-crypt...
  - Encrypt
    1. `sudo yum install cryptsetup`
    2. Find mapped disk folder to encrypt using `sudo fdisk -l`
    3. `sudo cryptsetup -y -v luksFormat /dev/<mapped-folder>`
  - Decrypt
    - `sudo cryptsetup luksOpen /dev/<mapped-folder> <new-name>`
      - Will map unencrypted device to `/dev/mapper/<new-name>` (check `fdisk -l`)
    - More information about encryption method etc:
      - `sudo cryptsetup status <new-name>`
      - or `sudo cryptsetup luksDump /dev/<mapped-folder>`
    - Reformat device:
      - Clear: `sudo dd if=/dev/zero of=/dev/mapper/<mapped-folder> bs=128`
      - Create file system: `sudo mkfs.ext4 /dev/mapper/<mapped-folder>`
    - Mount: `sudo mount /dev/mapper/<mapped-folder> <mountad-name>/`
