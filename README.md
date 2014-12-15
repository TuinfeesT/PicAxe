PicAxe
======

In the cold dreariness of December 2014, a couple of [TuinfeesTers](http://www.github.com/TuinfeesT) were searching for the perfect Gallery application... and found none. So, in good old [n+1](http://xkcd.com/927/) fashion, we decided to build our own!

Requirements
============

Uploading photos
----------------

- Support uploading photos
    - ...through the website...
        - ...one at a time
        - ...all at once
        - ...all at once using an archive format
    - ...through a local application...
        - ...one at a time
        - ...all at once
        - ...all at once using an archive format
    - ...with proper support for symlinks

User support
------------
- Support user registration
- Support groups
- Support user permissions
    - Support permissions per album
    - Support permissions per photo
        
Security
--------

- Be properly secure by...
    - ...implementing CSP headers
    - ...using the proper CSRF protections already embedded in Django
    - ...using Django ORM **exclusively**
    
Design
------

- Have a design that is...
    - ...simple to start with (Bootstrap maybe?)
    - ...customizable
