Markup: HTML Tags and Formatting
################################
:date: 2013-01-11 20:22
:author: themedemos
:category: Markup
:tags: content, css, formatting, html, markup
:slug: markup-html-tags-and-formatting
:status: published

Headings:
---------

Header one
----------

Header two
^^^^^^^^^^

Header three
~~~~~~~~~~~~

Header four
+++++++++++

Header five
===========

|

Blockquotes:
------------

Single line blockquote:

    Stay hungry. Stay foolish.

Multi line blockquote with a cite reference:

    People think focus means saying yes to the thing you've got to focus
    on. But that's not what it means at all. It means saying no to the
    hundred other good ideas that there are. You have to pick carefully.
    I'm actually as proud of the things we haven't done as the things I
    have done. Innovation is saying no to 1,000 things.

    *Steve Jobs - Apple Worldwide Developers' Conference, 1997*

|

Tables:
-------

+--------------------------+--------------------------+--------------------------+
| Employee                 | Salary                   |                          |
+==========================+==========================+==========================+
|  John Doe                | $1                       | Because that's all Steve |
|                          |                          | Jobs needed for a        |
|                          |                          | salary.                  |
+--------------------------+--------------------------+--------------------------+
|  Jane                    | $100K                    | For all the blogging she |
|                          |                          | does.                    |
|                          |                          |                          |
+--------------------------+--------------------------+--------------------------+
|  Fred                    | $100M                    | Pictures are worth a     |
|                          |                          | thousand words, right?   |
|                          |                          | So Jane x 1,000.         |
+--------------------------+--------------------------+--------------------------+
|  Jane                    | $100B                    | With hair like that?!    |
|                          |                          | Enough said...           |
|                          |                          |                          |
+--------------------------+--------------------------+--------------------------+

|

Definition Lists:
-----------------

|

Definition List Title
  Definition list division.

Startup
  A startup company or startup is a company or temporary organization
  designed to search for a repeatable and scalable business model.

#dowork
  Coined by Rob Dyrdek and his personal body guard Christopher "Big
  Black" Boykins, "Do Work" works as a self motivator, to motivating
  your friends.

Do It Live
  I'll let Bill O'Reilly will
  `explain <https://www.youtube.com/watch?v=O_HyZ5aW76c>`__ this one.

|

Unordered Lists (Nested):
-------------------------

-  List item one

   -  List item one

      -  List item one
      -  List item two
      -  List item three
      -  List item four

   -  List item two
   -  List item three
   -  List item four

-  List item two
-  List item three
-  List item four

|

Ordered List (Nested):
----------------------

#. List item one

   #. List item one

      #. List item one
      #. List item two
      #. List item three
      #. List item four

   #. List item two
   #. List item three
   #. List item four

#. List item two
#. List item three
#. List item four

|

HTML Tags:
----------

These supported tags come from the WordPress.com code
`FAQ <http://en.support.wordpress.com/code/>`__.

**Address Tag**

.. raw:: html

   <address>

| 1 Infinite Loop
|  Cupertino, CA 95014
|  United States

.. raw:: html

   </address>

**Anchor Tag (aka. Link)**

This is an example of a `link <http://apple.com>`__.

**Abbreviation Tag**

The abbreviation srsly stands for "seriously".

**Acronym Tag (deprecated in HTML5)**

The acronym ftw stands for "for the win".

**Big Tag (deprecated in HTML5)**

These tests are a big deal, but this tag is no longer supported in
HTML5.

**Cite Tag**

"Code is poetry." --Automattic

**Code Tag**

You will learn later on in these tests that ``word-wrap: break-word;``
will be your best friend.

**Delete Tag**

This tag will let you [STRIKEOUT:strikeout text], but this tag is no
longer supported in HTML5 (use the ``<strike>`` instead).

**Emphasize Tag**

The emphasize tag should *italicize* text.

**Insert Tag**

This tag should denote inserted text.

**Keyboard Tag**

This scarcely known tag emulates keyboard text, which is usually styled
like the ``<code>`` tag.

**Preformatted Tag**

This tag styles large blocks of code.

::

    .post-title {
        margin: 0 0 5px;
        font-weight: bold;
        font-size: 38px;
        line-height: 1.2;
        and here's a line of some really, really, really, really long text, just to see how the PRE tag handles it and to find out how it overflows;
    }

**Quote Tag**

“Developers, developers, developers...” --Steve Ballmer

**Strike Tag (deprecated in HTML5)**

This tag shows strike-through text

**Strong Tag**

This tag shows **bold** text.

**Subscript Tag**

Getting our science styling on with H\ :sub:`2`\ O, which should push
the "2" down.

**Superscript Tag**

Still sticking with science and Isaac Newton's E = MC\ :sup:`2`, which
should lift the 2 up.

**Teletype Tag (deprecated in HTML5)**

This rarely used tag emulates ``teletype text``, which is usually styled
like the ``<code>`` tag.

**Variable Tag**

This allows you to denote variables.
