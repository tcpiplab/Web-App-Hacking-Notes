Web Hacking 101,
How to Make Money Hacking Ethicallyby Peter Yaworski

Notes from Ch. 19 Getting Started


HIS SUMMARY:

1. Enumerate all sub domains (if they are in scope) using KnockPy, enumall Recon-ng script and IPV4info.com```bashknockpy example.com -w domain/sorted_knock_dnsrecon_fierce_recon-ng.txt```2. Start ZAP proxy, visit the main target site and perform a Forced Browse to discover files and directories3. Map technologies used with Wappalyzer and Burp Suite (or ZAP) proxy4. Explore and understand available functionality, noting areas that correspond tovulnerability types5. Begin testing functionality mapping vulnerability types to functionality provided6. Automate EyeWitness and Nmap scans from the KnockPy and enumall scans7. Review mobile application vulnerabilities8. Test the API layer, if available, including otherwise inaccessible functionality9. Look for private information in GitHub repos with GitRob10. Subscribe to the site and pay for the additional functionality to test


MY SUMMARY:

Enumerate sub domains
 - knockpy
 - enumall

Crawl the main site
 - Burp Suite
 - ZAP Proxy

Manually explore the main site to figure out the site's stack
 - Wappalyzer plug-in
 - Burp Suite
 - If it has a front-end JS library which interact with a back-end API
 - - Find out if it has known vulnerabilities
 - - Do API calls return sensitive data which is not rendered?
 - Check proxy to see:
 - - Where files are being served from
 - - JS files hosted elsewhere?
 - - Calls to 3rd party services?
 - Look for JSON files
 - Attempt passing unauthorized file IDs

Map functionality to vulnerability types
 - Set up accounts
 - OAuth?
 - 2fA?
 - Multiple users per account? Complex permissions model?
 - Inter-user messaging allowed?
 - Sensitive documents stored or allowed to be uploaded?
 - Profile pictures allowed?
 - HTML allowed, or WSISYG editor?
 - Bulk importer accepting XML/XXE document?

Application testing
 - Create content, users, teams, etc.
 - Inject payloads everywhere
 - - E.g., <img src=”x” onerror=alert(1)>
 - - Inject exploit code to vulnerable JS framework
 - - How is my content rendered?
 - - - Are special characters encoded?
 - - - Are attributes stripped? (What does this one mean? URL params?)
 - - - Does XSS image payload execute?
 - Test each area
 - Analyze HTTP requests and responses
 - - Enumerate or access URLs to sensitive files as anonymous user?
 - - If WYSIWYG, add HTML to POST requests
 - - CSRF tokens present in HTTP requests that change data? Tokens validated? (CSRF)
 - - Can manipulate ID parameters?  (Application Logic)
 - - Can repeat requests across two separate user accounts? (Application Logic)
 - - Any XML upload fields (XXE)?
 - - Notice any URL patterns containing record IDs?  (Application Logic, HPP)
 - - Any URLs with redirect related parameter? (Open Redirect)
 - - Any requests which echo URL parameters in the response? (CRLF, XSS, Open Redirect)
 - - Server information disclosed? Find unpatched vulnerabilities
 - - Did ZAP discover anything interesting like .htpasswd or config files?
 - - Did Burp discover anything interesting?

Digging deeper
 - Combine sub-domain lists from KnockPy and enumall scans as input to EyeWitness for screenshots
 - - Accessible web panels?
 - - Continuous integration servers?
 - - Administrative consoles?
 - Pass KnockPy list of IPs and pass it to Nmap (namp -sSV -oA OUTPUTFILE -T4 -iL IPS.csv)
 - - Open ports?
 - - Vulnerable services?

Mobile applications
 - Proxy your phone traffic through Burp while using the mobile app (if no SSL pinning)
 - Explore API endpoints
 - Mobile Security Framework
 - JD-GUI

APIs (mobile or not)
 - Review developer documentation looking for abnormalities
 - Does API sanitize input?

Public leaks
 - GitRob
 - - Passwords?
 - - Config files?
 - - Keys?
 - Google search (site:example.com .bash_history, etc.)

Paywalls
 - Explore paid functionality, which most other hackers likely avoid
