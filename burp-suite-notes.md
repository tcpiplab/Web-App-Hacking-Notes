# Notes from [Jason Haddix's][2] Excellent [Hacking with Burp Suite - Tutorial 1][1] Video
## Run Burp Suite with More RAM

Run Burp Suite with 2 GB RAM, which is more than the default:

```code
java -jar -Xmx2g Burp\ Suite\ Free\ Edition.app/Contents/java/app/burpsuite_free.jar
```

## Fix the Cipher Suite problem:
This is not actually from his video. But, after successfully installing Burp Suite, I encountered browser HTTPS errors because the Burp proxy and the target website (yahoo.com) could not agree on a cipher suite. Here's some packet detail that I grabbed with [Wireshark][3]. It shows yahoo's webserver offering my browser (which was actually the Burp proxy) a reasonable choice of three strong cipher suites. But Burp wasn't able to support any of them. I'm guessing this was due to the US government's well-known restrictions on exporting cryptographic technology.

```
Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (0xc02f)

Cipher Suite: TLS_RSA_WITH_AES_128_GCM_SHA256 (0x009c)

Cipher Suite: TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (0xc030)
```

I easily solved the problem by downloading Oracle's [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 8][4], as suggested on these two pages:

http://cybergibbons.com/security-2/burp-suite/missing-tls-ciphers-when-running-burp-suite/

http://stackoverflow.com/questions/37741142/how-to-install-unlimited-strength-jce-for-java-8-in-os-x

After installing the JCE and restarting Burp, the problem was gone.

[1]: https://www.youtube.com/watch?v=N-IKHmGjf2c
[2]: https://twitter.com/Jhaddix
[3]: https://www.wireshark.org/
[4]: http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html
