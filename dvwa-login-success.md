# How to Log In to DVWA
I'm not sure if this is an intentional feature of DVWA, but I found that I had to brute force my way in to the main login screen. Note that I cheated a bit by first seeding the users list with usernames I found in the DVWA [source code][2].

## Assumptions:
1. You have DVWA running and you're looking at the DVWA login page, e.g., `http://192.168.0.18/dvwa/login.php`
1. You have Burp Suite running.
1. You have Firefox or Chrome proxied through Burp.
1. You have a list of possible usernames. Mine is [here](http_default_users.txt).
1. You have a list of possible passwords. Mine is [here](john.txt).

Quora has a very straightforward [tutorial][1] on using Burp (even the free version) to brute force your way in to the login page for DVWA. It uses Burp's Intruder tab and the attack type is "Cluster Bomb". Some important notes:

* Pay close attention to the three screenshots showing the settings for the three different Payload Sets.
* I found that I didn't need the third Payload Set.
* Intruder tab -> Options tab -> all the way at the bottom are the Redirections settings. Set "Follow Redirections" to "Always". Also check the box for "Process cookies in redirections". If you don't do this you'll just get HTTP 302 Found but Burp won't follow the redirects even if it guesses the right username/password. You should see only 200 OK once this is set up right.
* In the attack window, sort the results tab by size. Any successful login will be of a different size than failed logins.

Here's a successful login, shown before the redirect.

```
POST /dvwa/login.php HTTP/1.1
Host: 192.168.0.18
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Referer: http://192.168.0.18/dvwa/login.php
Cookie: security=low; PHPSESSID=93l9ahf1120bkp79t5ehbkc0m4; acopendivids=swingset,jotto,phpbb2,redmine; acgroupswithpersist=nada
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 45

username=smithy&password=password&Login=Login
```


Here it s as a curl command, if you wanted to do that for some reason.

```shell
curl -i -s -k  -X $'POST' \
    -H $'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0' -H $'Referer: http://192.168.0.18/dvwa/login.php' -H $'Upgrade-Insecure-Requests: 1' -H $'Content-Type: application/x-www-form-urlencoded' \
    -b $'security=low; PHPSESSID=93l9ahf1120bkp79t5ehbkc0m4; acopendivids=swingset,jotto,phpbb2,redmine; acgroupswithpersist=nada' \
    --data-binary $'username=smithy&password=password&Login=Login' \
    $'http://192.168.0.18/dvwa/login.php'
```
[1]: https://www.quora.com/What-is-the-username-and-password-of-DVWA-web-pentesting-lab
[2]: https://github.com/ethicalhack3r/DVWA/tree/master/hackable/users
