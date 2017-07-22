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
