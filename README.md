# CocoaButter
Crash Reporting for Sketch Plugins.

![](https://cl.ly/1b0H2i3z163D/ezgif-1564281746.gif)

## Motivation

An easy way to collect and view crashes from real users that has the information from Sketch plugins such as the current page artboards and exception message.

## Deployment
You can deploy your own CocoaButter instance for free on Heroku with a single click, no coding required.

1. [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
2. Optionally pick a name for your server:  
<kbd>![](https://cl.ly/452x3b1z193G/Screen%20Shot%202016-10-01%20at%209.06.38%20AM.png)</kbd>
3. Pick a username and a password for your instance:  
<kbd>![](https://cl.ly/2F2K2b2f3e1Y/Screen%20Shot%202016-10-01%20at%209.06.30%20AM.png)</kbd>
4. Click  
<kbd>![](https://cl.ly/1U2d0V2p2g2q/Screen%20Shot%202016-10-01%20at%209.59.05%20AM.png)</kbd>

## Integration

1. Drop `CocoaButter.js` in your Plugin folder.
2. ```@import 'CocoaButter.js'``` into your `.cocoascript` files.
4. Initialize a `CocoaButter` instance:
3. Wrap your main function with `try` `catch`:
```
var onRun = function(context) {
  try {
    ...<your code>...
  }
  catch (e) {
    var cocoabutter = CocoaButter()
    cocoabutter.report(e, context)
  }
}
```

## License

The MIT License (MIT)

Copyright (c) 2016 Anima App

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
