# Notes from Jason Haddix's beginning [tutorial][1]

Run Burp Suite with 2 GB RAM, which is more than the default:
```bash
java -jar -Xmx2g Burp\ Suite\ Free\ Edition.app/Contents/java/app/burpsuite_free.jar
```
[1]: https://www.youtube.com/watch?v=N-IKHmGjf2c

Cipher Suite problem:
```
Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (0xc02f)

Cipher Suite: TLS_RSA_WITH_AES_128_GCM_SHA256 (0x009c)

Cipher Suite: TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (0xc030)
```
Solved with these two pages:

http://cybergibbons.com/security-2/burp-suite/missing-tls-ciphers-when-running-burp-suite/

http://stackoverflow.com/questions/37741142/how-to-install-unlimited-strength-jce-for-java-8-in-os-x
