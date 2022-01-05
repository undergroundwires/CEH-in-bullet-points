# Search engines and online resources

- For e.g. information about the target organization's employees, intranet, login pages...
- Sources include • social networking sites • people search services • alerting services • financial services • job sites showing target infrastructure details, physical location, and employee details • deep and dark web

## Google hacking

- Involves using a set of search operators (**dorks**) and building complex queries.
- 📝 Form of [passive reconnaissance](./footprinting-overview.md#passive-footprinting)
- Common dorks:

  | Dork | Definition | Example |
  | ---- | ---------- | ------- |
  | **`site`** | Only from the specified domain | `azure site:cloudarchitecture.io` |
  | **`inurl`** | Only pages that has the query in its URL. | `inurl: cloudarchitecture` |
  | **`intitle`** | Only pages that has the query in its title. | `intitle: cloud architecture` |
  | **`cache`** | Cached versions of the queried page | `cache:cloudarchitecture.io` |
  | **`link`** | Only pages that contain the queried URL. Discontinued. | `link:cloudarchitecture.io` |
  | **`filetype`** | Only results for the given filetype | `filetype:sql` |

- 📝 Usual to combine `filetype` and `site` dorks as see in [metagoofil](#metagoofil)
- Google logical query operators

  | Operator | Definition | Example |
  | ---- | ---------- | ------- |
  | **`OR`**, **`|`** | X or Y but not both | `jobs OR gates`, `jobs | gates` |
  | **`AND`** | Results related to both X and Y, google default. | `jobs AND gates` |
  | **`-`** | Exclude a term or phrase | `jobs ‑apple` |
  | **`*`** | Wildcard that will match any word or phrase. | `"Google * my life"` > google changed my life, google runs my life... |
  | **`(`**, **`)`** | Group multiple terms | `(iPad OR iPhone) apple` |

- E.g. finding passwords: `intext:"please change your" password | code | login file:pdf | doc | txt | docx -github`
  - **`intext`**: in the text of the website
  - **`"please change your" password"`**: Placing something in quote marks  means it must contain the text as whole, not parts of it.
  - **`file:pdf`**: specify what kind of file you want.
  - **`-github`**: minus + word tells to exclude results containing that word(s).
- For complex searches use:
  - [Google Advanced Search](https://www.google.com/advanced_search) (no need for dorks)
  - [Google Advanced Image Search](https://www.google.com/advanced_image_search)
- 💡 Easier way may be using [Google Advanced Search](https://www.google.com/advanced_search) or [Advanced Image Search](https://www.google.com/advanced_image_search)

### Google hacking tools

- [**Google hack honeypot**](http://ghh.sourceforge.net)
  - Logs google hacking queries against your resources
- [**Google hacking database**](https://www.exploit-db.com/google-hacking-database)
  - Helps you with
    - finding various types of files, including those that contain usernames and passwords.
    - VoIP footprinting using e.g. `intitle:"D-Link VoIP Router" "Welcome"` to find pages containing D-Link login portals
    - VPN footprinting using e.g. `filetype:pcf "cisco" "GroupPwd"` to find Cisco VPN files with passwords
  - 💡 Once you find password lists and you can guess similar ones as people usually have similar passwords.

#### metagoofil

- [Open-source](https://github.com/laramies/metagoofil) tool to extract metadata of public documents (pdf,doc,xls,ppt,etc) available in the target websites
- Also helps with [website footprinting](./website-footprinting.md)
- Flow
  1. Queries Google for different filetypes that may have metadata
     - Combining `site:` and `filetype` dorks
  2. Downloads the documents to disk and extracts the metadata of the file
  3. Parses files using different libraries for metadata (e.g. Hachoir, pdfminer)

## Online services

- Searching domain gives you some data about e.g. IP address, server, geolocation.
  - ❗Careful, can be fairly inaccurate, Generic results = No guarantee.
    - Far better to do your own search
    - Generic results = No guarantee
- [Website Watcher](https://www.aignes.com/) to get notified if a web page is changed.

### Reverse image search

- Allows tracking original source of an image
- E.g. • Google Image Search • TinEye Reverse Image Search • Yahoo Image Search

### Video search engines

- Search video related to target and extract video information
- E.g. • YouTube • Google Videos
- Video analysis tools include • YouTube DataViewer • EZGif • VideoReverser.com,

### Meta data engines

- Uses other search engines to build meta data of Internet
- Can give more information such as images, videos, blogs, news, articles about target
- E.g. • Startpage • MetaGer

### FTP search engines

- Search files on FTP servers
- E.g. • NAPALM FTP Indexer • Global FTP Search Engine
- Can help to find tax documents, business strategies etc.

### IoT search engines

- Can allow finding e.g. manufacturer details, geographical location, IP address, hostname, open ports
- E.g. [Shodan](#shodan), Censys, and Thingful
- See [Information Gathering | IoT security](./../18-iot-and-ot/iot-security.md#information-gathering)

#### Shodan

- Online [search engine](https://shodan.io)
- Finds specific types of IoT (webcams, routers, servers, etc.) connected to the internet using a variety of filters.
- 📝 You can e.g. search for open ports `port: 1433`

#### Censys

- Online [censys](https://censys.io/)
- 📝 Provides internet asset discovery i.e. scanning for unknown internet resources.
- Available on [search.censys.io](https://search.censys.io/)

### Netcraft

- Allows you search web by domain (DNS) through [search DNS](https://searchdns.netcraft.com/) service.
- Reports more information such as
  - If it uses HTML5 or flash (flash has many vulnerabilities)
  - `X-Frame-Options`: Do not allow this site to be rendered in an iframe
    - If it's allowed it allows for a phishing scheme such as [clickjacking](./../13-web-applications/hacking-web-applications.md#clickjacking)

### [CrimeFlare](http://www.crimeflare.org:82/cfs.html)

- Helps you find IP addresses behind a CDN (e.g. CloudFlare)
- **CDN**: Protects against DDoS, geolocation of servers by having different IP address.
- People often use real IP addresses before CDN, you can then look at past DNS records to find it.
