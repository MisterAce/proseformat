# ProseFormat

ProseFormat is a Sublime Text plugin that allows hard wrapping of prose text using a configurable width. The following features are supported:

- Different justifications: left-aligned, centered, right-aligned, block text
- Support bulleted lists
- Support numbered lists
- Support automatic renumbering of level 1 numbered lists

## Example

The following example shows what ProseFormat can do for you. Suppose after editing, your prose text looks like this:

```
Prose Paragraphs
----------------

	Lorem ipsum dolor sit amet, consetetur sadipscing 
	elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
	aliquyam erat, 
	sed diam voluptua. At vero eos et 
	accusam et justo duo dolores et ea rebum. Stet 
	clita kasd gubergren, no sea 
	takimata sanctus est Lorem ipsum dolor sit amet. 

Bulleted Lists
--------------

	- Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 

	- sed diam voluptua. At vero eos et accusam et 
	justo duo dolores et ea rebum. Stet clita 
	kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. 
	Lorem ipsum dolor sit amet, 
	consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 

	- aliquyam erat, sed diam voluptua. 
	At vero eos et accusam et justo duo dolores 
	et ea rebum. Stet clita kasd gubergren, no 
	sea takimata sanctus est Lorem ipsum dolor sit amet.   

Numbered Lists
--------------

	1. Duis autem vel eum iriure dolor in 
	hendrerit in vulputate velit 
	esse molestie consequat, vel illum dolore eu feugiat nulla facilisis 

	1. at vero eros et accumsan et iusto odio 
	dignissim qui blandit praesent 
	luptatum zzril delenit augue duis dolore te feugait 

	3. nulla facilisi. Lorem ipsum dolor sit amet,
```

This is what the text looks like after formatting it with ProseFormat:

```
Prose Paragraphs
----------------

    Lorem  ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
    nonumy  eirmod  tempor invidunt ut labore et dolore magna aliquyam
    erat,  sed  diam  voluptua.  At  vero  eos et accusam et justo duo
    dolores  et  ea  rebum. Stet clita kasd gubergren, no sea takimata
    sanctus est Lorem ipsum dolor sit amet.

Bulleted Lists
--------------

    - Lorem  ipsum  dolor  sit  amet, consetetur sadipscing elitr, sed
      diam  nonumy  eirmod  tempor  invidunt ut labore et dolore magna
      aliquyam erat,

    - sed  diam  voluptua. At vero eos et accusam et justo duo dolores
      et ea rebum. Stet clita kasd gubergren,

      no  sea  takimata  sanctus est Lorem ipsum dolor sit amet. Lorem
      ipsum  dolor  sit  amet,  consetetur  sadipscing elitr, sed diam
      nonumy eirmod tempor invidunt ut labore et dolore magna

    - aliquyam  erat,  sed  diam  voluptua.  At vero eos et accusam et
      justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea
      takimata sanctus est Lorem ipsum dolor sit amet.

Numbered Lists
--------------

    1. Duis autem vel eum iriure dolor in hendrerit in vulputate velit
       esse  molestie  consequat,  vel  illum  dolore eu feugiat nulla
       facilisis

    2. at  vero  eros  et accumsan et iusto odio dignissim qui blandit
       praesent luptatum zzril delenit augue duis dolore te feugait

    3. nulla facilisi. Lorem ipsum dolor sit amet,
```

