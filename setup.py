#! /usr/bin/env python

from distutils.core import setup

setup(name='papirus',
      version='0.0.1',
      description="PaPiRus API",
      author='starbuck93',
      author_email='me.starbuck@gmail.com',
      url='starbuckstech.com',
      packages=['papirus'],
      scripts=['bin/papirus-clear', 'bin/papirus-write', 'bin/papirus-set', 'bin/papirus-gol', 'bin/papirus-clock', 'bin/papirus-config', 'bin/papirus-setup', 'bin/papirus-draw']
     )
