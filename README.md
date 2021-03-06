# Project-1
Movie microsite project complete with movie trailers.
# Fresh Tomatoes project
A microsite generated by python that presents some of my favorite movies.

## Installation and usage

Built and tested on Ubuntu Linux with Python 2.7.6.

Place all three files in the same directory (or folder).
In this example the directory is named `project` but you are welcome to name it anything.

```
project/
+-- fresh_tomatoes.py
+-- media.py
+-- entertainment_center.py
```

### Execute
On the Linux command shell (AKA command terminal) change to the directory
containing the three files.

Then execute the python code like this:

`python entertainment_center.py`

This will generate an html file in the currect directory named `fresh_tomatoes.html`.

If the microsite does not automatically open in your default browser,
the html file can be opened manually with any modern webbrowser.

## Known Issues
When I execute this command on Ubuntu Linux using Firefox the html file is 
properly generated and automatically opens in Firefox.
My terminal reports an error when running this code:

`(process:27039): GLib-CRITICAL **: g_slice_set_config: assertion 'sys_page_size == 0' failed`

According to the top answer for 
[this](http://superuser.com/questions/855835/checking-firefox-version-using-cmd-and-gives-error) 
superuser.com question this error message is due to a display configuration 
issue related to Linux and Mozilla.

In any case the website works flawlessly despite the error message. 
The error may not appear on other systems.
