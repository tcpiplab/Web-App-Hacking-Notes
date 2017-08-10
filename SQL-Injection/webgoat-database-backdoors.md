## WebGoat SQL Injection Notes: Database Backdoors

### Stage 1: Execute more than one SQL statement
The goal here was to inject an entire second, arbitrary SQL command after the numeric value you're setting. The second command should increase your salary. This requires two things:
1. A semi-colon `;` to terminate the original SQL `SELECT` statement.
1. An SQL [`UPDATE`](https://www.w3schools.com/sql/sql_update.asp) statement.

In the Hints, the third hint tells you to just use this command:
```
101 or 1=1; update employee set salary=100000
```
But this ends up setting everyone's salary to $100,000. This mistake was easy to catch because we appended ` or 1=1` to the first SQL statement; it shows everyone's salary. That's convenient, so I left it in the injection string.

But the `UPDATE` statement needs to be more precise. I started the lesson over by clicking the Restart Lesson button. Then I injected this string, which includes a more precise `UPDATE` statement.
```
101 or 1=1; update employee set salary=100001 where userid=101
```
Also note that I changed the `salary` value to visually distinguish it from the other rows.

### Stage 2: Inject a backdoor

>Stage 2: Use String SQL Injection to inject a backdoor. The second stage of this lesson is to teach you how to use a vulneable fields to inject the DB work or the backdoor. Now inject a trigger that would act as SQL backdoor. **Note that nothing will actually be executed because the current underlying DB doesn't support triggers.**

I like the following definition from [Microsoft](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-trigger-transact-sql):
> A trigger is a special kind of stored procedure that automatically executes when an event occurs in the database server.

I get the idea that the syntax, permissions, and availability of database triggers differs depending on the database vendor. Here are links to documentation: [Oracle](https://docs.oracle.com/cd/B19306_01/server.102/b14200/statements_7004.htm), [SQLite](https://sqlite.org/lang_createtrigger.html), [PostgreSQL](https://www.postgresql.org/docs/9.1/static/sql-createtrigger.html), and [MySQL](https://dev.mysql.com/doc/refman/5.7/en/create-trigger.html).

Here is the solution to this exercise:
```
101; CREATE TRIGGER myBackDoor BEFORE INSERT ON employee FOR EACH ROW BEGIN UPDATE employee SET email='john@hackme.com' WHERE userid = NEW.userid
```

Here is the same SQL code, for prettified a bit:

```
101;
CREATE TRIGGER myBackDoor BEFORE INSERT ON employee
FOR EACH ROW
BEGIN
    UPDATE employee SET email='john@hackme.com'WHERE userid = NEW.userid
```

WebGoat uses [MongoDB]() as the underlying database. MongoDB does not support triggers. Hence the warning on the final page:
> Error generating org.owasp.webgoat.lessons.BackDoors

Incidentally, [here is a StackOverflow answer](https://stackoverflow.com/questions/9691316/how-to-listen-for-changes-to-a-mongodb-collection) explaining how to approximate trigger functionality in MongoDB.
