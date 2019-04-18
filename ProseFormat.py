# ----------------------------------------------------------------
# Program:  ProseFormat
# Function: Sublime Text plugin to be able for format prose text. 
#           Features include:
#            - Word wrap paragraphs
#            - Support list formatting
#            - Support different kinds of justification
# Author:   A. Schösser
# Date:     2019-17-04
#
# TODO List
# - Don't remove Empty New-Lines at the Beginning or the End
#   of selection
# - Single-Line Mode
# - Configurable Bullets
# - Configurable Numbers
# - Integration und Keyboard Shortcuts
# - Idempotent first_line indent
# - Block-Characters Editor?
# - Überschriften Erkennung?
# 
# -----------------------------------------------------------------

import sublime
import sublime_plugin
import re

# ----------------------------------------------
# Configuration
# ----------------------------------------------

# The width of the target text
width = 70

# First line indent of a paragraph. TODO: Make this idenopotent
paragraph_indent = 0

# Justification. Left: 0, Right: 1, Center: 2,  Block: 3
justify = 3

# Re-wrap. TODO. Special mode, do not collect words and paragraphs
# just work on each line separately
single_line_mode = False

# Renumber numbered lists automatically?
renumber_lists = True

# Supported bullets
# bullets = "^" + re.escape("- ")return val.startswith("- ") or val.startswith("* ") or val.startswith("o ")

# Tracing
traceOn = False

# ----------------------------------------------
# Main entry
# ----------------------------------------------
class ProseFormatCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        global justify

        load_settings()        

        # Get the configuration from the args
        # TODO: Move this to parse_args method
        if "justify" in args:
            justify = args["justify"]

        # Get the current selection and expand it to full lines
        if len(self.view.sel()[0]) == 0:
            return
        sel_region = self.view.sel()[0]
        sel_region = self.view.line(sel_region)
        self.view.sel().add(sel_region)

        # Get the currently selected text
        org_text = self.view.substr(sel_region)

        # Remove whitespaces from empty lines
        org_text = re.sub("\n\s+\n", "\n\n", org_text);

        # The result string
        formatted_text = ""

        # Iterate over each paragraph        
        paragraphs = org_text.split("\n\n")
        first_paragraph = True
        numbered_list_started = False
        numbered_list_counter = 1
        for paragraph in paragraphs:
            stripped_paragraph = paragraph.lstrip()

            # Care about paragraph separator new-line
            if not first_paragraph:
                formatted_text += "\n"
            else:
                first_paragraph = False

            trace("<P>")

            # Toggle the numbered list flag
            if not starts_with_number(stripped_paragraph):
                numbered_list_started = False

            # Determine type of paragraph
            if starts_with_bullet(stripped_paragraph):
                # Bulleted list
                first_indent = len(paragraph) - len(stripped_paragraph)
                first_indent_filler = "".rjust(first_indent, " ")

                indent = first_indent + 2;
                indent_filler = "".rjust(indent, " ")
            elif starts_with_number(stripped_paragraph):
                # Numbered list
                numbered_list_counter += 1

                first_indent = len(paragraph) - len(stripped_paragraph)
                first_indent_filler = "".rjust(first_indent, " ")

                # Check whether this is the first numbered paragraph
                # If so, save the number and increment it as long
                # as the list goes
                if renumber_lists:
                    if not numbered_list_started:
                        numbered_list_started = True
                        numbered_list_counter = num_val(stripped_paragraph)
                    else:
                        stripped_paragraph = replace_num(stripped_paragraph, numbered_list_counter)                                

                # Reserve space for digit number + separator + space
                indent = first_indent + num_len(stripped_paragraph) + 2;
                indent_filler = "".rjust(indent, " ")

            else:
                # Normal paragraph
                indent = len(paragraph) - len(stripped_paragraph)
                indent_filler = "".rjust(indent, " ")

                first_indent = indent + paragraph_indent
                first_indent_filler = "".rjust(first_indent, " ")

            # Render the paragraph
            words = stripped_paragraph.split()
            first_line = True
            line = ""
            for word in words:
                # Render a line when it's ready
                if len(line) + len(word) >= width and len(line) > 0:
                    if justify == 2:
                        line = line.center(width)

                    formatted_text += format_line(line, False) + "\n"
                    line = ""
                    first_line = False;

                # Keep feeding a line
                if len(line) == 0:
                    if first_line:
                        line += first_indent_filler + word                    
                    else:
                        line += indent_filler + word                    
                else:
                    line += " " + word

            # Print the "tail" line
            if len(line) > 0:
                formatted_text += format_line(line, True) + "\n"

        # Alter buffer, omit last \n as it wasn't included in the region
        self.view.replace(edit, sel_region, formatted_text[:-1])

# ----------------------------------------------
# Format a line according to the justification 
# settings
# ----------------------------------------------
def format_line(line, is_last):
    trace("Formatting line: " + line)
    if justify == 1:
        line = line.rjust(width)
    elif justify == 2:
        # TODO: This is rather a special case which should simply
        # center the selection line-by-line as is without word
        # wrapping
        line = line.center(width)
    elif justify == 3:
        if is_last:
            return line
        trace("Line to format: " + line)
        start_index = len(line) - len(line.lstrip())
        if starts_with_bullet(line.strip()):
            start_index += 2
        elif starts_with_number(line.strip()):
            start_index += 4
        current_index = start_index
        while len(line) < width:
            space_pos = line.find(" ", current_index)            
            if space_pos == -1:
                if current_index == start_index:
                    break
                current_index = start_index
                continue
            line = line[:space_pos] + " " + line[space_pos:]
            current_index = space_pos + 2
    return line

# ----------------------------------------------
# Returns True when a string starts witha list
# bullet.
# ----------------------------------------------
def starts_with_bullet(val):
    return val.startswith("- ") or val.startswith("* ") or val.startswith("o ")

# ----------------------------------------------
# Returns True when a string starts with a list
# number
# ----------------------------------------------
def starts_with_number(val):
    return re.match("^[0-9]+[.)]\s+", val) != None

# ----------------------------------------------
# Returns the length of the number of a list
# ----------------------------------------------
def num_len(val):
    match = re.match("^[0-9]", val)
    if match != None:
        return len(match.group(0))
    else:
        return -1

# ----------------------------------------------
# Replace a trailing number by a different one
# ----------------------------------------------
def replace_num(val, counter):
    return re.sub("^[0-9]+", str(counter), val)

# ----------------------------------------------
# Returns the value of the bulleted list number
# ----------------------------------------------
def num_val(val):
    match = re.match("^[0-9]+", val)
    if match != None:
        return int(match.group(0))
    else:
        return -1    

# ----------------------------------------------
# Reload settings from settings file
# TODO: Use all settings!
# ----------------------------------------------
def load_settings():
        global width
        settings = sublime.load_settings("ProseFormat.sublime-settings") 
        width = settings.get("width")

# Trace something to a string when traceOn flag is turned on
# TODO: Get rid of the return stuff...
def trace(msg):
    if traceOn:
        print(msg)
    