Edge Case: Nested And Mixed Lists
#################################
:date: 2009-05-15 14:48
:author: themedemos
:category: Edge Case
:tags: content, css, edge case, lists, markup
:slug: edge-case-nested-and-mixed-lists
:status: published

Nested and mixed lists are an interesting beast. It's a corner case to
make sure that

-  Lists within lists do not break the ordered list numbering order
-  Your list styles go deep enough.

Ordered - Unordered - Ordered
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. ordered item
#. ordered item

   -  **unordered**
   -  **unordered**

      #. ordered item
      #. ordered item

#. ordered item
#. ordered item

Ordered - Unordered - Unordered
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. ordered item
#. ordered item

   -  **unordered**
   -  **unordered**

      -  unordered item
      -  unordered item

#. ordered item
#. ordered item

Unordered - Ordered - Unordered
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  unordered item
-  unordered item

   #. ordered
   #. ordered

      -  unordered item
      -  unordered item

-  unordered item
-  unordered item

Unordered - Unordered - Ordered
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  unordered item
-  unordered item

   -  unordered
   -  unordered

      #. **ordered item**
      #. **ordered item**

-  unordered item
-  unordered item
