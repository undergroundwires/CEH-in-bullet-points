# Data leakage, backup and recovery

## Data leakage

- Any sort of unauthorized disclosure of sensitive information from anyone/any system.
- Includes emails, malicious links, device theft etc.
- Data leakage leads to
  - loss of trust e.g. trust to governments decreased during late years
  - loss of profit e.g. Sony lost profit of their movies after [they were leaked](https://en.wikipedia.org/wiki/Sony_Pictures_hack) before publishing

### Data leakage threats

#### External threats

- Corporate espionage, phishing, malware
- Business partners, consultants when company outsources
  - Less surveillance than own employees.

#### Internal threats

- Also known as **insider threats**
- Dangers are greater than external threats as they'll have greater access to the company
- See also [insider attacks](./security-threats-and-attacks.md#insider-attacks)
- E.g. eavesdropping, shoulder surfing, [dumpster diving](./../10-social-engineering/social-engineering-types.md#dumpster-diving) can be used to acquire data.

## Data loss prevention

- Also known as **DLP**
- Identification and monitoring of important information that is not to be shared outside the organization.
- Can block, notify the sender or lets admins to analyze, react and report to sensitive data in transit.
- Important tool for enterprise message systems
- Uses different techniques of data access control
  - E.g. when e-mailing where content is scanned for fingerprints, classifications and bank account numbers.

## Data backup

- Process of making a duplicate copy of data that already exists.
- Protects against data loss and corruption as it can lead to great financial damages.
- No backup = Far more suspectable to all sorts of attacks, especially ransomware.

### Backup mediums

#### Magnetic tapes

- Oldest form, still used by many enterprises.
- Retention time: ≈30 years
- 📝 To pull anything off the tape, you have to fast-forward to wherever the correct file is stored
  - Good for restoring systems in one go.
  - Bad for incremental backups or storing a few files.
  - ❗ Only way to tell if backups are working is to fully restore from the tape and check if it's correctly restored.

#### Optical disks

- 2 to 3 times slower than hard drives
- Retention time: ≈25 years

#### Hard disks

- Cheaper, easily accessible
- Less stability than magnetic tapes
- Retention time: ≈9-20 years

#### SSD disks

- Includes also usb drives known as Flash storage or thumb-drive.
- Resistant to shock, temperature, being run through the washing machine
- Retention time: ≈10 years

#### Cloud storage

- Requires little infrastructure
- Depends on stable internet connection
- No retention time, high reliability

#### SD and micro-SD

- Little capacity and pricy.
- Retention time: ≈10 years

### Steps of data backup strategy

1. **Identify important data**
   - because backing-up everything is too costly and takes up much storage.
2. **Choose appropriate backup media**
   - Reliable, solid, preferably cheap
   - E.g. USBs or portable media for personal users, and HDD/SDDs for companies for more speed.
3. **Choose the appropriate backup strategy**
   - Check features such as scheduling, monitoring file changes to update back-ups, protocols, integrations...
   - Paid vs Free
     - Free requires more knowledge and work, training costs (one time)
       - E.g. in Linux, set cron job from point A to B
     - Paid versions has recurring license costs including training
4. **Choose appropriate RAID levels**
   - **RAID 1**
     - 2 disks
     - All that are written in disk A is also written to B, if one disk fails, other works
   - **RAID 5**
     - 3 disks
     - If A fails you can reconstruct based on data in B and C
   - RAIDing is not only for backups, can also use for faster read and writes
     - E.g. BIG = Everything is seen as one drive. File is written two all of them. Crazy write & read speeds. If single disk dies all data is gone.
5. **Choose the appropriate backup method**
   - **Cold backup**
     - Performed while system is not in use.
     - E.g. at nights, during weekends.
   - **Hot backup**
     - Performed when system is still used.
     - E.g. you type a document, power shortage happens but it's still saved.
   - **Warm backup**
     - Hybrid of the two.
     - Period backups while system is in use, but you might lose longer time period than hot backup.
6. **Choose the appropriate backup locations**
   - Three options:
     1. **On-site**: Same building / room
        - Susceptible to same types of problems like other servers.
        - If there's a breach, fire or earthquake = all data are gone
     2. **Off-site**: backup is performed at a remote location
     3. **Cloud**:
        - Most secure: most cost effective and safe where data won't be loss, no electricity, no hardware, no maintainable.
        - Can be replicated in same building, different buildings in same data center or different regions.
        - Can have privacy/trust issues: encrypt
7. **Choose the backup type**
   - **Full backup**: Costly, you back up everything
   - **Incremental backup**
     - Backs-up on each change of the previous back-up
     - When restoring, you need to restore everything from the first full back-up
   - **Differential backup**:
     - Back-ups on difference to the initial backup on each backup.s
     - Faster restoring time as you only need the last point and the initial full back-up
8. **Appropriate backup solution**: Combination of all of this
9. **Perform a recovery test**
   - Ensure you can recover a data that's lost with DR tests e.g. twice a year.
   - **Recovery drill**
     - Simulating data tier outage
     - Recovering
     - Validate application integrity post recovery

## Data recovery

- Recovering lost data
- Reasons
  - Accidental lost e.g. • natural disaster • corrupted data
  - Or can be intentionally destroyed
- DR stands for "Disaster Recovery"
- Most of data is recoverable but you can have recovery failure if backed up data becomes corrupt.
