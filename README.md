# ProseFormat

ProseFormat is a Sublime Text 3 plugin that allows hard wrapping of prose text using a configurable width. The following features are supported:

- Supported alignment: left-aligned, centered, right-aligned, justified
- Variable indent
- Bulleted lists
- Numbered lists
- Automatic renumbering of numbered lists at level 1

Note, that ProseFormat is designed to work on plain text files, only. That is, it does not recoginize mark-down characters or the like.

## Example

The following example shows what ProseFormat can do for you. After editing, your prose text may look as fuzzy as this:

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

Currently, there is no installation package. To install this plugin manually, download the latest release from https://github.com/MisterAce/proseformat/releases/ and extract the contents to a temporary directory. Copy the contents of the proseformat-x.x directory to `~/.config/sublime-text-3/Packages`

Alternatively, simply clone this repository to the following directory:

```
cd ~/.config/sublime-text-3/Packages
git clone https://github.com/MisterAce/proseformat.git ProseFormat --depth=1
```

## Usage

In order to format a range of text, select the text in Sublime Text. Then, use one of the following default key-bindings to format the selected text:

- `Ctrl+Alt+F, l`: Format the selected text left aligned
- `Ctrl+Alt+F, j`: Format the selected text justified
- `Ctrl+Alt+F, c`: Format the selected text centered
- `Ctrl+Alt+F, r`: Format the selected text right aligned

In order to vary the width, open the ProseFormat user settings (Menu: Preferences -> Package Settings -> ProseFormat -> User Settings) and add the following line:

`"width": <custom width>`

## Paragraphs

ProseFormat formats each paragraph separately. It tries to fit as many words in a particular line not exceeding the width, possibly hoisting words from subsequent lines of a paragraph. Paragraphs are separated by an empty line. Thus, your source text should already be separated into paragraphs. The first line of a paragraph defines the indent all paragraph lines will have after formatting.

## Bulleted Lists

ProseFormat supports formatting bulleted lists. That is, it ensures that the text of each line of a bulleted list item is left-aligned equally. Also here, the first line of a bulleted list item defines the indent of all lines of the item. This enables you creating multi-level bulleted lists with different bullets:

```
    - Lorem  ipsum  dolor  sit  amet, consetetur sadipscing elitr, sed
      diam  nonumy  eirmod  tempor  invidunt ut labore et dolore magna
      aliquyam erat,

      * sed diam voluptua. At vero eos et accusam et justo duo dolores
        et ea rebum. Stet clita kasd gubergren,

        no  sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem
        ipsum  dolor  sit  amet, consetetur sadipscing elitr, sed diam
        nonumy eirmod tempor invidunt ut labore et dolore magna

    - aliquyam  erat,  sed  diam  voluptua.  At vero eos et accusam et
      justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea
      takimata sanctus est Lorem ipsum dolor sit amet.

```

Note, that bulleted list items are also separated by an empty line.

## Numbered Lists

ProseFormat also lays out numbered list items to be left-aligned equally when it detects that a paragraph starts with a list number. When during editing a re-ordering of the numberd list-items took place, ProseFormat can renumber the items to be in ascending order, starting with the number of the first item of a list.


