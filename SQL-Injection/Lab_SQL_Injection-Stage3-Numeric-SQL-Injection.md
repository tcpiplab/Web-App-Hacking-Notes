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

![Screen shot showing Larry's profile][screenshot_1]

The image above shows Larry's profile.

[screenshot_1]: https://raw.githubusercontent.com/tcpiplab/Web-App-Hacking-Notes/master/SQL-Injection/larry.png "Screen shot showing Larry's profile"

Here's why. Consider the HTML `POST` payload that we're tampering with:
```
employee_id=101&action=ViewProfile
```
You'll always get Larry's profile if you set the value of the `employee_id` parameter to any of these values:
```
101
101 OR 1=1
101 OR 1=1 order by ccn asc
```
I think what's going on here is that the *default* sort for this page's data is by credit card number, in ascending order. And Larry has the numerically lowest credit card number.

That's why, unless you re-sort the data, the page will keep looking like you are still only allowed to see Larry's profile.

But now how can we reach our goal of viewing Neville's profile? Trial and error (and this [YouTube video by William Tavares](https://www.youtube.com/watch?v=M2Xqqkyf5gw)) will show that Neville, in fact, has the highest salary in the database. So we can view his row of data in the web page with this injection:
```
101 OR 1=1 order by salary desc

```
The `POST` payload will look like this:
```
employee_id=101 OR 1=1 order by salary desc&action=ViewProfile
```
![Screen shot showing Neville's profile][screenshot_2]

The image above shows Neville's profile. If you've been staring at Larry's profile while you tried dozens of variations of SQLi attacks, you might miss the fact that the actual data on the page has changed to that of Neville. You might be tricked by the blue "Larry" above the name "Neville".

[screenshot_2]: https://raw.githubusercontent.com/tcpiplab/Web-App-Hacking-Notes/master/SQL-Injection/neville.png "Screen shot showing Neville's profile"


### Lessons Learned
This lesson has some quirks that could cause you to waste a lot of time, even though you'd already successfully injected SQL code into the database's SQL interpreter. But I think this may have been the intention of the creators.

Don't conclude that an input field is **not** vulnerable to SQLi just because the returned data doesn't change. You could be, coincidentally, looking at the default sort order.

This matters because, in this lesson at least, the web page for viewing a user's profile only displays one database row at a time. If a successful SQLi returns multiple database rows, you'll only be shown the first or last record, depending on how the query was sorted and depending on how the web application was written.
