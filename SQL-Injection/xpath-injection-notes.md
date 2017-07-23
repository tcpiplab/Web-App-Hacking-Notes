## WebGoat XPATH Injection Notes

The language in the Plan and Hints seems to have left something out, probably because it should be obvious to some people. But it wasn't obvious to me. However, in total,
I think this lesson is teaching these concepts:

1. The method for XPATH injection is (usually?) identical to a SQLi.
1. You when doing SQL injections, you may in fact be attempting to inject into an XPATH query, not into a SQL query.

The injection vulnerability is in the Java source code for this page, which you'd never see in a blackbox pentest. The vulnerable line of code is this:
```
String username = s.getParser().getRawParameter(USERNAME, "");
```
The variable `username`, having never been sanitized, is injected as-is into this line of Java:
```
String expression = "/employees/employee[loginID/text()='" + username + "' and passwd/text()='" + password
+ "']";
```
Then, presumably, an XPATH query is executed, with your input appended, just like in an SQL injection.
