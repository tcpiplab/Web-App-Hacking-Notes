## WebGoat XPATH Injection Notes

The language in the Plan and Hints seems to have left something out, probably because it should be obvious to some people. But it wasn't obvious to me. However, in total,
I think this lesson is teaching these concepts:

1. The method for XPATH injection is (usually?) identical to a SQLi.
1. When doing SQL injections, you may in fact be attempting to inject into an XPATH query, not into a SQL query.

The injection vulnerability is in the Java source code for this page, which you'd never see in a blackbox pentest. The vulnerable line of code is this:
```
String username = s.getParser().getRawParameter(USERNAME, "");
```
The variable `username`, having never been sanitized, is injected as-is into this line of Java:
```
String expression = "/employees/employee[loginID/text()='" + username + "' and passwd/text()='" + password
+ "']";
```
Then an XPATH query is executed, with your input appended, just like in an SQL injection. For brevity, I'm not going to explain the adjacent lines of Java code that execute the XPATH query.

### The Solution
The successful injection string is:
```
Smith' or 1=1 or 'a'='a
```
Here is why this string works:
1. `Smith'` just needs to be any string, appended with a single quote. This single quote closes the first opening single quote in the vulnerable line of Java: `/employees/employee[loginID/text()='`. The variable `expression` is now, so far anyway, this:
```
/employees/employee[loginID/text()='Smith'
```
1. ` or 1=1 ` (including the leading and trailing space) is required to make the resulting query match all rows, because it is always true that 1 equals 1. Appending this to the query string we're building results in this:
```
/employees/employee[loginID/text()='Smith' or 1=1
```
1. `or 'a'='a` is required so that we can close the closing single quote that we've been essentially pushing over to the right of the query we're building. The query would fail if we didn't provide an opening single quote to match up with that closing quote mark.
```
/employees/employee[loginID/text()='Smith' or 1=1 or 'a'='a' and passwd/text()='
```
1. There are two remaining pieces of the Java string concatenation. The first is whatever value you typed in as the password. For clarity, I've used the password `wR0ngP@ssw0rd`. But it doesn't matter what password value you supply because the injection will take place whether or not authentication succeeds. With the password value automatically appended to the query, we now have:
```
/employees/employee[loginID/text()='Smith' or 1=1 or 'a'='a' and passwd/text()='wR0ngP@ssw0rd
```
1. The final piece of Java, `']`, is also automatically appended to the query we're building. This finally closes the last pair of single quotes. Now the query is free of syntax errors:
```
/employees/employee[loginID/text()='Smith' or 1=1 or 'a'='a' and passwd/text()='wR0ngP@ssw0rd']
```

![Screen shot of WebGoat returning all rows of a table after a successful XPATH injection attack][screenshot_1]

The image above is a screenshot of WebGoat returning all rows of a table after a successful XPATH injection attack.

[screenshot_1]: https://raw.githubusercontent.com/tcpiplab/Web-App-Hacking-Notes/master/SQL-Injection/xpath-screenshot.png "Screen shot of WebGoat returning all rows of a table after a successful XPATH injection attack"
