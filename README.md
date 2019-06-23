# XSS Fun!
A mock website for mocking XSS attacks.

## What's the idea?
This is a very simple chat filled with XSS attacks design flaws. It basically prints anything that the user texts to all the other chat participant's screens. This is bad because HTML can be ran on other clients without having the server noticing anything unusual.

## How do I run?
If you have Python installed, which most likely you do, run:
```bash
python server.py
```
Then, go to `localhost:8080` on your browser.<b>
You can run this on another machine, as long it's connected with the same network as you, by going on `<IP-ADDRESS-OF-THE-MACHINE-THATS-RUNNING-SERVER.PY>:8080`. Then, chat away!

## How does script.js works?
Very naively takes what's in the textarea and submits it to the server. It's worth mentioning that it does some encoding, just so that some characters are rendered properly ('<' or '>', for instance.). Notice that `password` is stored in this code, too.

## How does server.py works?
It uses the SimpleHTTPServer module to build a REST server. It has some GET routes - `submit`, which takes the `comment` param and stores it in `posts.json`; `steal`, which takes the `comment` param and stores it in `senhas.json`; the rest is just for serving statics files (`script.js` and `posts.json`).

## OK, what's so flawed about it?
A user can type HTML and it would run normally on other people's browsers.

## OK, so a hacker can make some text appear bold or in red font. Big deal.
Yes. And it can also run JavaScript on other clients. Have you heard of the `img` tag?

## Yes, what about it?
Have you heard of the `onload` attribute?

## Yes, what about... OK, so he can console.log something. Big deal.
Yes. And it can also have control over any variable stored in your script. And since it's on client side, he can see the same JavaScript that the server sent to every user.

## OK, once it's "inside" other people's browsers, how can it "get out"?
It can send a request to a spoof server that he owns with your information.

## What information?
That beautiful `password` you have stored there.

## Oh no.
Yeah. But don't worry. [Most browsers are prepared](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) to deal with something like this. For instance, it is very unlikely that he could send some request to a server that has not be whitelisted by the developers.<b>
Also, this is a very well-known vulnerability. Most developers are ready to deal with something like this. They just need to convert anything that is user submitted to a string before displaying it.

## Has this ever happened before?
[Yes, with Twitter.](https://www.youtube.com/watch?v=zv0kZKC6GAM)

## OK. What can I do with this?
Go wild! I have left a piece of code that you can send on `mock.html`. Just copy it, paste it on the textarea and send! All the logged users passwords will be stored in `senhas.js`.