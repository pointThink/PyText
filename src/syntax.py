from tkinter import *

from pygments import lex
from pygments.lexers.python import Python3Lexer


class Syntax:

    def __init__(self, text: Text, initial_content: str):
        self.lexer = Python3Lexer()

        self.text: Text = text
        self.previous_content = initial_content

        self.comment_color = '#546e7a'
        self.string_color = '#c3e88d'
        self.number_color = '#f78c6c'
        self.type_color = '#f07178'
        self.keyword_color = '#c792ea'
        self.operator_color = '#89ddff'
        self.bultin_function_color = '#c792ea'
        self.class_color = '#f07178'
        self.namespace_color = '#89ddff'
        self.class_name_color = '#82aaff'
        self.function_name_color = '#82aaff'
        self.font_color = '#FFFFFF'
        self.bg_color = '#212121'
        self.menu_fg_active = '#80cbc4'
        self.menu_bg_active = '#323232'
        self.selection_color = '#353535'

    def default_highlight(self):
        row, _ = self.text.index(INSERT).split('.')
        location = f'{row}.0'
        content = self.text.get("1.0", "end-1c")
        lines = content.split("\n")
        if self.previous_content != content:
            self.text.mark_set("range_start", location)
            word = str(len(lines[int(row) - 1]))
            if int(word) < 10:
                data = self.text.get(location, row + ".0" + word)
            else:
                data = self.text.get(location, row + "." + word)
            for token, content in lex(data, self.lexer):
                self.text.mark_set("range_end", "range_start + %dc" % len(content))
                self.text.tag_add(str(token), "range_start", "range_end")
                self.text.mark_set("range_start", "range_end")
        self.previous_content = self.text.get("1.0", "end-1c")

    def initial_highlight(self):
        self.clear_existing_tags()

        self.text.mark_set("range_start", "1.0")
        data = self.text.get("1.0", "end-1c")
        for token, content in lex(data, self.lexer):
            self.text.mark_set("range_end", "range_start + %dc" % len(content))
            self.text.tag_add(str(token), "range_start", "range_end")
            self.text.mark_set("range_start", "range_end")
        self.text.tag_configure('Token.Comment.Single', foreground=self.comment_color)
        self.text.tag_configure('Token.Comment.Multiline', foreground=self.comment_color)
        self.text.tag_configure('Token.Literal.String', foreground=self.string_color)
        self.text.tag_configure('Token.Literal.String.Char', foreground=self.string_color)
        self.text.tag_configure('Token.Literal.Number.Integer', foreground=self.number_color)
        self.text.tag_configure('Token.Literal.Number.Float', foreground=self.number_color)
        self.text.tag_configure('Token.Keyword', foreground=self.keyword_color)
        self.text.tag_configure('Token.Operator', foreground=self.operator_color)
        self.text.tag_configure('Token.Keyword.Type', foreground=self.type_color)
        self.text.tag_configure('Token.Keyword.Declaration', foreground=self.bultin_function_color)
        self.text.tag_configure('Token.Name.Class', foreground=self.class_name_color)
        # self.text.tag_configure('Token.Text.Whitespace')
        self.text.tag_configure('Token.Name.Function', foreground=self.function_name_color)
        self.text.tag_configure('Token.Keyword.Namespace', foreground=self.namespace_color)
        self.text.tag_configure('Token.Name.Builtin.Pseudo', foreground=self.class_color)
        self.text.tag_configure('Token.Name.Builtin', foreground=self.bultin_function_color)
        self.text.tag_configure('Token.Punctuation.Indicator', foreground=self.bultin_function_color)
        self.text.tag_configure('Token.Literal.Scalar.Plain', foreground=self.number_color)
        self.text.tag_configure('Token.Literal.String.Single', foreground=self.string_color)
        self.text.tag_configure('Token.Literal.String.Double', foreground=self.string_color)
        self.text.tag_configure('Token.Keyword.Constant', foreground=self.number_color)
        self.text.tag_configure('Token.Literal.String.Interpol', foreground=self.string_color)
        self.text.tag_configure('Token.Name.Decorator', foreground=self.number_color)
        self.text.tag_configure('Token.Operator.Word', foreground=self.operator_color)
        self.text.tag_configure('Token.Literal.String.Affix', foreground=self.bultin_function_color)
        self.text.tag_configure('Token.Name.Function.Magic', foreground=self.bultin_function_color)
        self.text.tag_configure('Token.Literal.Number.Oct', foreground=self.number_color)
        self.text.tag_configure('Token.Keyword.Reserved', foreground=self.keyword_color)
        self.text.tag_configure('Token.Name.Attribute', foreground=self.bultin_function_color)
        self.text.tag_configure('Token.Name.Tag', foreground=self.namespace_color)
        self.text.tag_configure('Token.Comment.PreprocFile', foreground=self.namespace_color)
        self.text.tag_configure('Token.Name.Label', foreground=self.class_color)
        self.text.tag_configure('Token.Literal.String.Escape', foreground=self.number_color)

    def clear_existing_tags(self):
        for tag in self.text.tag_names():
            self.text.tag_delete(tag)