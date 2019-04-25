# ----------------------------------------------------------------
# Program:  ProseFormat
# Function: Sublime Text plugin to be able for format prose text. 
#           Features include:
#            - Word wrap paragraphs
#            - Support list formatting
#            - Support different kinds of alignment
# Author:   MisterAce
# Date:     2019-17-04
#
# TODO List
# - Idempotent first_line indent
# - Table formatting
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
        if "text-align" in args:
            alignment = args["text-align"]

        # And save some settings locally
        width = settings.get("width")
        paragraph_indent = settings.get("paragraph_indent")

        # Get the current selection and expand it to full lines
        if len(self.view.sel()[0]) == 0:
            return
        sel_region = self.view.sel()[0]
        if self.view.classify(sel_region.end()) & sublime.CLASS_LINE_START != 0:
            sel_region = sublime.Region(sel_region.begin(), sel_region.end() - 1)
        sel_region = self.view.full_line(sel_region)
        self.view.sel().add(sel_region)

        # Get the currently selected text
        org_text = self.view.substr(sel_region)

        # The result string
        formatted_text = ""

        # Iterate over each paragraph        
        paragraphs = re.split(settings.get("paragraphSeparator"), org_text)
        numbered_list_started = False
        numbered_list_counter = 1
        for paragraph in paragraphs:
            stripped_paragraph = paragraph.lstrip()

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
                if settings.get("renumber_lists"):
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
                    formatted_text += format_line(line, alignment, width, False)
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
                formatted_text += format_line(line, alignment, width, True)

            # The paragraph separator
            formatted_text += "\n"

        # Alter buffer, omit last \n as it wasn't included in the region
        self.view.replace(edit, sel_region, formatted_text[:-1])


# ----------------------------------------------
# Format a line according to the alignment 
# settings
# ----------------------------------------------
def format_line(line, alignment, width, is_last):
    if alignment == 1:
        # right
        line = line.rjust(width)
    elif alignment == 2:
        # center
        # TODO: This is rather a special case which should simply
        # center the selection line-by-line as is without word
        # wrapping
        line = line.center(width).rstrip()
    elif alignment == 3:
        # justify
        if is_last:
            return line + "\n"
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
    return line + "\n"


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
    