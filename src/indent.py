from tkinter import Text, INSERT
import re


class Indent:

    text: Text
    indent: int

    def __init__(self, text):
        self.text = text

    def save_indent(self):
        self.indent = self.get_indent_level()

    def insert_indent(self):
        for i in range(self.indent):
            self.text.insert(INSERT, '\t')

    def get_indent_level(self):
        text = self.text
        line = text.get('insert linestart', 'insert lineend')
        match = re.match(r'^(\s+)', line)
        current_indent = len(match.group(0)) if match else 0
        return current_indent
