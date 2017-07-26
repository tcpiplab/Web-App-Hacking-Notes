## **WebGoat LAB:** SQL Injection -> Stage 3: Numeric SQL Injection

The goal of this lesson was to view Neville's profile. But there are a couple of ways that you can get tricked into thinking that you have not yet succeeded.

This is a great opportunity to learn an important lesson: a successful SQL injection might return a web page that looks nearly identical to the "unsuccessful" page you've grown accustomed to looking at while you're trying to figure out a successful attack string.

### The Solution
You'll have to be running this through an intercept proxy (Burp, ZAP, etc.) so you can edit the input parameters before they're sent to the web server.

It looks to me like the vulnerable line of Java is this:
```
String query = "SELECT * FROM employee WHERE userid = " + subjectUserId;
```
So you would think that a simple `101 OR 1=1` would be successful. And you'd be correct. But if you try that attack string you'll get the exact same page that you get without doing any attack: In both cases you get the page showing Larry's profile.

--------------
![Screen shot showing Larry's profile][screenshot_1]

The image above shows Larry's profile.

[screenshot_1]: https://raw.githubusercontent.com/tcpiplab/Web-App-Hacking-Notes/master/SQL-Injection/larry.png "Screen shot showing Larry's profile"


-----------------
1. Inject ``
1.
But I think this may have been the intention of the creators.
