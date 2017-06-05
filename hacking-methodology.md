# My Notes from Reading [Web Hacking 101][1],


Web Hacking 101 was written by [Peter Yaworski][2]. These are my notes from Ch. 19, "Getting Started".


### HIS SUMMARY:

1.
   1. Enumerate all sub domains (if they are in scope) using [KnockPy](https://github.com/guelfoweb/knock).

   ```bash
   knockpy example.com -w domain/sorted_knock_dnsrecon_fierce_recon-ng.txt
   ```
   OR
   ```
   knockpy example.com -c -w SecLists/Discovery/DNS/subdomains-top1mil-110000.txt
   ```
   1. Jason Haddix's `enumall` [script](https://github.com/jhaddix/domain), which requires `Recon-ng`. Note that, if you're running Kali Linux, [Recon-ng](https://bitbucket.org/LaNMaSteR53/recon-ng) is probably already installed. Also, `recon-ng` can call `altdns`. But installing  [altdns](https://github.com/infosec-au/altdns) is optional.
   ```
   enumall.py example.com -a -w SecLists/Discovery/DNS/sorted_knock_dnsrecon_fierce_recon-ng.txt
   ```
      * Note that to get `recon-ng` set up with API keys you'll need the very helpful info at [Raikia's Hub](https://raikia.com/recon-ng-api-key-creation/). You'll also need to watch a YouTube video called [Recon-ng:. How to add API keys](https://www.youtube.com/watch?v=EhYNCisebIc).
   1. `whois` or IPV4info.com.
2. Start ZAP proxy, visit the main target site and perform a Forced Browse to discover files and directories
3. Map technologies used with Wappalyzer and Burp Suite (or ZAP) proxy
4. Explore and understand available functionality, noting areas that correspond to vulnerability types
5. Begin testing functionality mapping vulnerability types to functionality provided
6. Automate EyeWitness and Nmap scans from the KnockPy and enumall scans
   ```
   sudo nmap -sS -A -PN --script=http-title -iL example.com.targets -oA example.com.nmap
   ```
   * Note that the `example.com.targets` file is a sorted, uniq-ed list of hostnames from the subdomain enumeration scans described above.
7. Review mobile application vulnerabilities
8. Test the API layer, if available, including otherwise inaccessible functionality
9. Look for private information in GitHub repos with GitRob
10. Subscribe to the site and pay for the additional functionality to test


## MY SUMMARY:

### Enumerate sub domains
 * [knockpy][3]
 * [enumall.py][4] From [Jason Haddix][5]

### Crawl the main site
 * Burp Suite
 * ZAP Proxy

### Manually explore the main site to figure out the site's stack
 1. Wappalyzer plug-in
 1. Burp Suite
 1. If it has a front-end JS library which interact with a back-end API
   1. Find out if it has known vulnerabilities
   1. Do API calls return sensitive data which is not rendered?
 1. Check proxy to see:
   1. Where files are being served from
   1. JS files hosted elsewhere?
   1. Calls to 3rd party services?
 1. Look for JSON files
 1. Attempt passing unauthorized file IDs

### Map functionality to vulnerability types
1. Set up accounts
OAuth?
1. 2fA?
1. Multiple users per account? Complex permissions model?
1. Inter-user messaging allowed?
1. Sensitive documents stored or allowed to be uploaded?
1. Profile pictures allowed?
1. HTML allowed, or WSISYG editor?
1. Bulk importer accepting XML/XXE document?

### Application testing
1. Create content, users, teams, etc.
1. Inject payloads everywhere
  * E.g., `<img src=”x” onerror=alert(1)>`
1. Inject exploit code to vulnerable JS framework
1. How is my content rendered?
  1. Are special characters encoded?
  1. Are attributes stripped? (What does this one mean? URL params?)
  1. Does XSS image payload execute?
1. Test each area
1. Analyze HTTP requests and responses
1. Enumerate or access URLs to sensitive files as anonymous user?
1. If WYSIWYG, add HTML to POST requests
1. CSRF tokens present in HTTP requests that change data? Tokens validated? (CSRF)
1. Can manipulate ID parameters?  (Application Logic)
1. Can repeat requests across two separate user accounts? (Application Logic)
1. Any XML upload fields (XXE)?
1. Notice any URL patterns containing record IDs?  (Application Logic, HPP)
1. Any URLs with redirect related parameter? (Open Redirect)
1. Any requests which echo URL parameters in the response? (CRLF, XSS, Open Redirect)
1. Server information disclosed? Find unpatched vulnerabilities
1. Did ZAP discover anything interesting like .htpasswd or config files?
1. Did Burp discover anything interesting?

### Digging deeper
1. Combine sub-domain lists from KnockPy and enumall scans as input to EyeWitness for screenshots
1. Accessible web panels?
1. Continuous integration servers?
1. Administrative consoles?
1. Pass KnockPy list of IPs and pass it to `nmap`:
  ```shell
  namp -sSV -oA OUTPUTFILE -T4 -iL IPS.csv
  ```
1. Open ports?
1. Vulnerable services?

### Mobile applications
1. Proxy your phone traffic through Burp while using the mobile app (if no SSL pinning)
1. Explore API endpoints
1. Mobile Security Framework
1. JD-GUI

### APIs (mobile or not)
1. Review developer documentation looking for abnormalities
1. Does API sanitize input?

### Look for Public Leaks
1. GitRob
1. Passwords?
1. Config files?
1. Keys?
1. Google search:
  ```
  site:example.com .bash_history
  ```

### Paywalls
* Explore paid functionality, which most other hackers likely avoid.

[1]: https://leanpub.com/web-hacking-101
[2]: https://leanpub.com/u/peteryaworski
[3]: https://github.com/guelfoweb/knock
[4]: https://github.com/jhaddix/domain
[5]: https://twitter.com/Jhaddix
