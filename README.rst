Roughcast
=========

We help you get the playtests you want, to make the game you envision.

Project managed at https://trello.com/b/7Zmo8d2w/roughcast

Setting up local development
----------------------------

You need:

- PostgreSQL
- virtualenv (preferably with virtualenvwrapper)
- Python 3.8

Clone the repo::

   git clone git@github.com:wlonk/roughcast.git
   cd roughcast

Set up your secrets ``.env`` file::

   cat << EOF > .env
   DJANGO_SECRET_KEY=$(pwgen 50 1 -ys)
   DJANGO_DEBUG=True
   HASHID_FIELD_SALT='samplesalt'
   EOF

(If you don't have ``pwgen`` on your system, and are running OS X with
Homebrew, you can run ``brew install pwgen``).

Set up a virtualenv, via something like::

   mkvirtualenv roughcast
   setvirtualenvproject .
   make install

Create a database and initialize it::

   createdb roughcast
   make migrate
   make loaddata

The sample data username is ``kit``, with password ``foobar``.

Run the local server::

   make

Running tests and lints
-----------------------

Once all the above is done, just::

   make lint test

An explanatory note on the makefile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We use a makefile to run the various Django admin commands, and related
commands like ``pip-compile`` and ``pip install``, because it allows us
to easily inject necessary environment variables from the untracked
``.env`` file into the running context, and because ``make`` is
available on most any developer's system. It may not seem like running
``make test`` gets you much over just running ``pytest`` directly, but
those environment variables are the reason.
