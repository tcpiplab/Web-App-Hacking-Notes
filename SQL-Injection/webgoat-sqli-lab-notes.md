## Download & Run WebGoat on OS X
*Note that I'm running WebGoat on a non-default port, `8081`. This is because I've already got Burp Suite's proxy listening on the default port, `8080`. Also, my browser is already configured to use Burp's proxy.*

Go to the [WebGoat Repository](https://github.com/WebGoat/WebGoat/releases/latest), scroll to the bottom of the page, to the "Downloads" section of the page. Download the `.jar` file. After the download finishes, do this:

```shell
$ mv ~/Downloads/webgoat-container-7.1-exec.jar /Applications/
$ cd /Applications
$ java -jar webgoat-container-7.1-exec.jar -httpPort=8081
```

Wait for the java output to say this:

```
INFO: Starting ProtocolHandler ["http-bio-8081"]
```
Now point your browser at: http://localhost:8081/WebGoat

## The 'Command Injection' Lesson
From the [WebGoat home page][3], click on 'Injection Flaws' to get a drop-down tree of the lesson modules. Start at the top, 'Command Injection'.

The `HelpFile` is vulnerable to OS command injection.

The payload I injected was:

`" ; netstat -an ; FOO="1`

After injection, here is the raw request body:

`HelpFile=CSRF.help" ; netstat -an ; FOO="1&SUBMIT=View`

I'm running this on OS X Yosemite 10.10.5. Note that I had to append `; FOO="1` in order to close the orphaned `"` character at the end of the shell command. In the documentation and in solution videos on YouTube, I didn't see anyone having to close the orphaned `"` character. All their examples and demos just show successful injections using things like:

`" ; netstat -an`

But I was never successful until I figured out a way to close up the left-over `"` character.

[3]: http://localhost:8081/WebGoat/attack
