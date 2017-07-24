## String SQL Injection in WebGoat

This lesson is very straightforward. You just have to inect this:
```
Smith' or 1=1;--
```
Specifically,
1. `Smith'` closes the single quote that we presume precedes the username string you type in.
1. ` or 1=1` allows us to add an always-true condition to the query, so that it will match all rows of the table being queried.
1. `;--` does two things.
     1. The `;` character terminates the SQL query. Note that the semicolon is not actually required. It is an optional SQL statement terminator which is really only needed if you're trying to add more than one SQL statement.
     1. The `--` characters comment out the abandoned single quote, and any other fragment of SQL that we have left stranded on the right side of the original SQL statement that we're injecting into.

Note that another successful injection string for this lesson is this:
```
smith' or 'a'='a
```
In this case we're accomplishing two things by using `or 'a'='a`:
1. It adds an always-true condition to the query, so that it will match all rows of the table being queried.
1. It nicely balances out the last single quote character, so that we don't get a syntax error.
