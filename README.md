[![Slack Status](http://slack.animaapp.com/badge.svg)](http://slack.animaapp.com)
[![apm](https://img.shields.io/apm/l/vim-mode.svg?maxAge=2592000)]()
[![GitHub stars](https://img.shields.io/github/stars/animaapp/cocoabutter.svg?style=social&label=Star&maxAge=2592000)]()
[![Twitter Follow](https://img.shields.io/twitter/follow/animaapp.svg?style=social&label=Follow&maxAge=2592000)]()

# CocoaButter
Crash Reporting for Sketch Plugins.

<kbd>![](https://cl.ly/0I1r0k3l013M/ezgif-1369415000.gif)</kbd>

<kbd>![](https://cl.ly/2j471S1I1m2n/Screen%20Shot%202016-10-01%20at%201.12.20%20PM.png)</kbd>

Demo: https://cocoabutter.herokuapp.com

## Motivation

An easy way to collect and view crash reports from real users with Sketch related details such as the current page artboards and exception message.

## Integration

1. Drop [CocoaButter.js](https://raw.githubusercontent.com/AnimaApp/CocoaButter/master/CocoaButter.js) in your Plugin folder.
2. ```@import 'CocoaButter.js'``` into your `.cocoascript` files.
3. Wrap your plugin code with `try` `catch`
4. Initialize `CocoaButter` instance and `report()`
```
@import 'CocoaButter.js'

var onRun = function(context) {
  try {
    ...<your plugin code>...
  }
  catch (e) {
    var cocoabutter = new CocoaButter()
    cocoabutter.baseURL = "<your cocoabutter server url (i.e http://cocoabutter.herokuapp.com)"
    cocoabutter.username = "<your cocoabutter username>"
    cocoabutter.password = "<your cocoabutter password>"
    cocoabutter.report(e, context)
  }
}
```

## Deployment
You can deploy your own CocoaButter server for free on Heroku with a single click, no coding required.

1. [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
2. Optionally pick a name for your server:  
<kbd>![](https://cl.ly/452x3b1z193G/Screen%20Shot%202016-10-01%20at%209.06.38%20AM.png)</kbd>
3. Pick a username and a password for your instance:  
<kbd>![](https://cl.ly/2F2K2b2f3e1Y/Screen%20Shot%202016-10-01%20at%209.06.30%20AM.png)</kbd>
4. Click  
<kbd>![](https://cl.ly/1U2d0V2p2g2q/Screen%20Shot%202016-10-01%20at%209.59.05%20AM.png)</kbd>

## CocoaButter as a Service

If you want CococButter as a Service rather than deploying your own upvote this issue:  
https://github.com/AnimaApp/CocoaButter/issues/1

## Contributing

Contributions are welcome 🎉

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull request** so that we can review your changes

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
