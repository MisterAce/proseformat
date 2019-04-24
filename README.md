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

## Installation

Currently, there is no installation package. To install this plugin manually, simply clone this repository to your sublime text packages folder, for example:

```
cd ~/.config/sublime-text-3/Packages
git clone https://github.com/MisterAce/proseformat.git ProseFormat
```

## Usage

In order to format a range of text, select the text in Sublime Text. Then, use one of the following default key-bindings to format the selected text:

- `Ctrl+Alt+F, l`: Format the selected text left-justified
- `Ctrl+Alt+F, b`: Format the selected text block
- `Ctrl+Alt+F, c`: Format the selected text centered
- `Ctrl+Alt+F, r`: Format the selected text right-justified

In order to vary the width, open the ProseFormat user settings (Menu: Preferences -> Package Settings -> ProseFormat -> User Settings) and add the following line:

`"width": <custom width>`
