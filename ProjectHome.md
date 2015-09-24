# The project is moved to "[Net-Fish](http://code.google.com/p/net-fish)". #

## Goals: ##
_This project try to provide a web framework with highly pluggable and components and applications which running on google appengine to benefit from the power of cloud computing._

## About web framework: ##
Some ideas have been taken from the popular python project [Django](http://www.djangoproject.com/). Django has done very good job which provides almost everything as a web framework, but sadly it does not support non-relational database like google appengine datastore. Fortunately I found two projects which try to make it work on appengine:

  1. [Google App Engine Helper for Django](http://code.google.com/p/google-app-engine-django/) (by google), somehow it supports only small part of django (a lot of modules which require db operations will fail), and the project was updated in a very low frequency.
  1. [app-engine-patch](http://code.google.com/p/app-engine-patch) (unofficial) support most functions of django, however, in my eyes, it changed the django-like structure which make it very hard to reuse apps. And it was already switched to a new  [project](http://www.allbuttonspressed.com/projects/django-nonrel), which can not called stable.

## Infrastructure: ##
Because none of the above are good enough, I decided to write something by myself. Instead of starting everything from scratch, I include google-app-engine-django as well, thus you can use some components of django like:
  * auth
  * template
  * markup
  * sitemaps
  * ...
Besides that, this project currently provides many other web components:
    * HTTP and XMLRPC request dispatcher
    * Entity Models including [Many-to-Many relationship](http://www.niubi.de/post/671/)
    * Account
    * Feeds handling
    * Google account & OpenID login
And all these components are also applications at the same time, which means, you can easily install/uninstall them like apps in the settings.py.

## Features: ##
  * Pluggable and reusable Applications(django like)
  * MVC(django template engine)
  * ORM(use GAE datastore)
  * OpenID support
  * YAML CSS Framewrok
  * Skinable Layout
  * Free to use!!

## Demo: ##

As example, I wrote a simple [blog](http://www.niubi.de) application, more apps can be easily added.

## Download: ##
To try the framework, simply check out the latest code from [svn](http://niubi.googlecode.com/svn/trunk/) or [github](http://github.com/lvbeck/niubi).

## Documentation: ##
to-do