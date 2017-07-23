## WebGoat Log Spoofing Notes

This is a simple lesson. Just remember to use percent-encoding for the injected newline:

```html
username=guest%250d%250aLogin+succeeded+for+username%3A+admin&password=foo&SUBMIT=Login
```
Also note that in a real world attack you'd need to inject a timestamp because the web application probably prepends log entries with a timestamp. But you'd have to know the correct format, as well as any other fields that precede the log message.
