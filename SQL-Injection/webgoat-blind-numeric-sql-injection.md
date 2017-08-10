
## Blind Numeric SQL Injection

This lesson shows us how to use very little feedback to determine the value of a particular row of a table. Regardless of the input, the web page only returns one of these two messages:

1. Account number is valid.
1. Invalid account number.

But we can use these as a TRUE/FALSE boolean test.

```
101 AND ((SELECT pin FROM pins WHERE cc_number='1111222233334444') = 2364 );
```
