============
billionfong
============

Introduction
***************
This is a package created by Billy Fong.

.. raw:: html
   <p>The package aims to create <strike>2</strike>4 Billy, and some mini games for time killing.</p>

billionfong
***************
This is the master class billionfong, with the followings:

:Subclass:   Child, IT Dog, Musician, Narcissist
:Methods:    create(personality = PERSONALITY), play(game = GAME), shout(), love()

Games
***************
There are 2 games created at this moment.

:Bingo:          Guess number between 1 to 100
:Mastermind: Guess 4 numbers between 1-6 with exact order.

Example
***************
::

  import billionfong
  
  #To show personalities and games included in the package.
  billionfong.info()
  
  #To create a class
  billy = billionfong.create(personality = "narcissist")
  billy.love()
  billy.shout()
  
  #Play mini-games
  billy.play(game = "mastermind")
