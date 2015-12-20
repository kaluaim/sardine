Antidisestablishmentarianism
############################
:date: 2009-10-05 12:00
:author: themedemos
:category: Edge Case
:tags: content, css, edge case, html, layout, title
:slug: title-should-not-overflow-the-content-area
:status: published

Title should not overflow the content area
------------------------------------------

A few things to check for:

-  Non-breaking text in the title, content, and comments should have no
   adverse effects on layout or functionality.
-  Check the browser window / tab title.
-  If you are a plugin or widget developer, check that this text does
   not break anything.

The following CSS properties will help you support non-breaking text.

::

    -ms-word-wrap: break-word;
    word-wrap: break-word;

 
