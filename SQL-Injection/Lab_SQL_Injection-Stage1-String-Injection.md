## **WebGoat LAB:** SQL Injection -> Stage 1: String SQL Injection

The goal of this injection is to log in as `Neville`, who has admin privileges.
This is best accomplished by running your browser through a proxy like Burp or ZAP.

1. Using the pull down menu, select `Neville Bartholomew (admin)`. Put in any password and click the `Login` button. You don't need to look through the `HTML`. But just for reference, here is the menu item:
```
<option value="112">Neville Bartholomew (admin)</option>
```

1. Now look at Burp's Proxy Tab, then the HTTP History tab.
Find the `POST` you just sent. The parameters are in the body of the request:
```
employee_id=112&password=ddddddd&action=Login
```
1. Right-click that `POST` and send it to the Repeater.
1. Decide where to attempt injection. I couldn't easily figure out how to inject into the `employee_id` field. This is probably because it's a numeric value, so there is no pair of single quotes for me to inject into. Instead I injected into the password field because I knew it would be a string between single quotes.
1. Type any string for the password, and append `' OR 1=1;--` to it. Click the Burp Repeater's `Go` button. Here is the full body of the edited `POST` you're sending:
```
employee_id=112&password=ddddddd' OR 1=1;--&action=Login
```
1. In the right half of the Repeater window, click the Render tab. You'll see "Welcome Back Neville".

Note that, instead of using Burp Repeater, you could just as easily have done it with the intercept proxy and edited the password value before forwarding the POST to the web server. I found that, while either of these works, it was not possible to accomplish through the browser. I suspect that some Javascript is sanitizing the password field value before it gets sent. I searched all the scripts, but couldn't find the code. Moving on.
