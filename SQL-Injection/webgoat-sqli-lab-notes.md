## Download & Run WebGoat on OS X
*Note that I'm running WebGoat on a non-default port, `8081`. This is because I've already got Burp Suite's proxy listening on the default port, `8080`. Also, my browser is already configured to use Burp's proxy.*

### Requirements
* Java
* Burp Suite
* Python (to de-obfuscate the solutions to this lab)

I'm running WebGoat on OS X Yosemite 10.10.5. The quickest and least complicated way to get WebGoat running is to download the `.jar` file and launch it from the command line.

1. **Downlaod:** Go to the [WebGoat Repository](https://github.com/WebGoat/WebGoat/releases/latest), scroll to the bottom of the page, to the "Downloads" section of the page. Download the `.jar` file.

1. **Disconnect:** After the download finishes, disconnect your computer from WiFi and Ethernet. You're about to open up many security holes.

1. **Execute WebGoat:**

   ```shell
   $ mv ~/Downloads/webgoat-container-7.1-exec.jar /Applications/
   $ cd /Applications
   $ java -jar webgoat-container-7.1-exec.jar -httpPort=8081
   ```

   Wait for the java output to say this:

   ```
   INFO: Starting ProtocolHandler ["http-bio-8081"]
   ```

1. **Open WebGoat in your browser:** http://localhost:8081/WebGoat

## The 'Command Injection' Lesson
From the [WebGoat home page][3], click on 'Injection Flaws' to get a drop-down tree of the lesson modules. Start at the top, 'Command Injection'.

### Where To Inject

The `HelpFile` parameter is vulnerable to OS command injection.

### The Injected Payload
Run this in a Python 2 or Python 3 shell to see the attack string I injected to complete this lesson:

```Python
$ python
>>> import base64
>>> print(base64.b64decode('IiA7IG5ldHN0YXQgLWFuIDsgRk9PPSIx').decode())
```

### The Raw Request body
Run this in a Python 2 or Python 3 shell to see the raw request body, including the injection:

```Python
$ python
>>> import base64
>>> print(base64.b64decode('SGVscEZpbGU9Q1NSRi5oZWxwIiA7IG5ldHN0YXQgLWFuIDsgRk9PPSIxJlNVQk1JVD1WaWV3').decode())
```

### Beware The Orphaned Double-Quote
Note that I also had to close the orphaned `"` character at the end of the shell command. In the documentation and in solution videos on YouTube, I didn't see anyone having to close the orphaned `"` character. All their examples and demos just show successful injections using things like:

`" ; netstat -an`

But I was never successful until I figured out a way to close up the left-over `"` character.

## Screenshot

![Screen shot of Burp Repeater successfully injecting an operating system command against WebGoat][screenshot_1]

The image above is a screenshot of Burp Repeater successfully injecting an operating system command against WebGoat. In this screenshot the underlying OS was Ubuntu and the target app was WebGoat v5.4.

[screenshot_1]: https://raw.githubusercontent.com/tcpiplab/Web-App-Hacking-Notes/master/SQL-Injection/burp-webgoat-command-injection.png "Screen shot of Burp Repeater successfully injecting an operating system command against WebGoat"



[3]: http://localhost:8081/WebGoat/attack
