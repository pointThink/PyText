from tkinter import *


class Insert:

    text: Text

    def __init__(self, text_box):
        self.text = text_box

    def insert(self, symbol):
        index = self.text.index('insert')
        self.text.insert(INSERT, symbol)
        self.text.mark_set(INSERT, index)

    # Braces
    def round_brace(self, event):
        self.insert(')')

    def square_brace(self, event):
        self.insert(']')

    def curly_brace(self, event):
        self.insert(']')

    # Quotes
    def quote_double(self, event):
        self.insert('\"')

    def quote_single(self, event):
        self.insert('\'')
