# ----------------------------------------------------------------
# Program:  ProseFormat
# Function: Sublime Text plugin to be able for format prose text. 
#           Features include:
#            - Word wrap paragraphs
#            - Support list formatting
#            - Support different kinds of justification
# Author:   MisterAce
# Date:     2019-17-04
#
# TODO List
# - Command to open default and user settings side-by-side
# - Table formatting
# - Idempotent first_line indent
# - Don't remove empty new-lines at the beginning or the end
#   of selection
# - Single-line Mode
# - Block-Characters Editor?
# 
# -----------------------------------------------------------------

import sublime
import sublime_plugin
import re

# ----------------------------------------------
# Configuration
# ----------------------------------------------

settings = ""

# ----------------------------------------------
# Main entry
# ----------------------------------------------
class ProseFormatCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
 
        load_settings()        

        # Get the configuration from the args
        if "justify" in args:
            justification = args["justify"]
        width = settings.get("width")

        # Get the current selection and expand it to full lines
        if len(self.view.sel()[0]) == 0:
            return
        sel_region = self.view.sel()[0]
        sel_region = self.view.line(sel_region)
        self.view.sel().add(sel_region)

        # Get the currently selected text
        org_text = self.view.substr(sel_region)

        # The result string
        formatted_text = ""

        # Iterate over each paragraph        
        paragraphs = re.split(settings.get("paragraphSeparator"), org_text)
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

                    formatted_text += format_line(line, justification, width, False) + "\n"
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
                formatted_text += format_line(line, justification, width, True) + "\n"

        # Alter buffer, omit last \n as it wasn't included in the region
        self.view.replace(edit, sel_region, formatted_text[:-1])


# ----------------------------------------------
# Format a line according to the justification 
# settings
# ----------------------------------------------
def format_line(line, justification, width, is_last):
    if justification == 1:
        line = line.rjust(width)
    elif justification == 2:
        # TODO: This is rather a special case which should simply
        # center the selection line-by-line as is without word
        # wrapping
        line = line.center(width)
    elif justification == 3:
        if is_last:
            return line
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
    return re.match(settings.get("bullets"), val) != None


# ----------------------------------------------
# Returns True when a string starts with a list
# number
# ----------------------------------------------
def starts_with_number(val):
    return re.match(settings.get("listNumber"), val) != None


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
# Returns the value of the list number
# ----------------------------------------------
def num_val(val):
    match = re.match("^[0-9]+", val)
    if match != None:
        return int(match.group(0))
    else:
        return -1    


# ----------------------------------------------
# Reload settings from settings file
# ----------------------------------------------
def load_settings():
        global settings
        settings = sublime.load_settings("ProseFormat.sublime-settings") 
       

# ----------------------------------------------
# Trace something to a string when traceOn flag 
# is turned on
# ----------------------------------------------
def trace(msg):
    if settings.get("traceOn"):
        print(msg)
    