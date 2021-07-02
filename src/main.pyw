from tkinter import *
import tkinter.font as tkfont
import tkinter.filedialog as filedialog
import tkinter.messagebox as msgbox

from syntax import Syntax
from indent import Indent
from insert import Insert
import files


class PyEdit:

    def __init__(self, master: Tk):
        self.version = '0.1.0'

        self.file = None
        self.master = master

        master.title('PyEdit - Untitled')
        master.geometry('600x600')

        # Widgets
        self.text = Text(master, undo=True)

        self.text.config(font=('Cascadia Code', 10, 'normal'))
        self.text.config(background='#1a1a1a', foreground='white')
        self.text.config(insertbackground='white')
        self.text.pack(expand=True, fill=BOTH)

        # setting tab size
        font = tkfont.Font(font=self.text['font'])
        tab_size = font.measure('    ')
        self.text.config(tabs=tab_size)

        # Menu
        self.menu = Menu(master)

        # file menu
        self.file_menu = Menu(self.menu, tearoff=False)

        self.file_menu.add_command(label='New', command=self.new)
        self.file_menu.add_command(label='Open', command=self.open)
        self.file_menu.add_command(label='Save', command=self.save)
        self.file_menu.add_command(label='Save as', command=self.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=exit)

        # edit menu
        self.edit_menu = Menu(self.menu, tearoff=False)

        self.edit_menu.add_command(label='Undo', command=self.text.edit_undo)
        self.edit_menu.add_command(label='Redo', command=self.text.edit_redo)

        # adding menus
        self.menu.add_cascade(label='File', menu=self.file_menu)
        self.menu.add_cascade(label='Edit', menu=self.edit_menu)

        self.menu.add_command(label='About', command=self.about)

        master.config(menu=self.menu)

        self.insert = Insert(self.text)  # Insert setup
        self.indent = Indent(self.text)  # indent setup
        self.syntax = Syntax(self.text, self.text.get('1.0', END))  # Syntax setup

        # Binding insert functions
        master.bind('(', self.insert.round_brace)
        master.bind('[', self.insert.square_brace)
        master.bind('{', self.insert.curly_brace)
        master.bind('\'', self.insert.quote_single)
        master.bind('\"', self.insert.quote_double)

        # binding file functions
        master.bind('<Control-s>', lambda event: self.save())
        master.bind('<Control-S>', lambda event: self.save_as())
        master.bind('<Control-o>', lambda event: self.open())
        master.bind('<Control-n>', lambda event: self.new())

        # Binding highlighter function
        self.text.bind('<KeyRelease>', lambda event: self.highlight_syntax())

        # Binding indent function
        self.text.bind('<Return>', lambda event: self.indent.save_indent())
        master.bind('<Return>', lambda event: self.indent.insert_indent())

        """
        The reason there are 2 bindings
        is that the text binding is executed and then
        the character is inserted
        
        master binding is executed after insert
        
        The indentation is saved while on previous line
        """

    def open(self):
        open_file = filedialog.askopenfilename()
        self.file = open_file
        self.master.title('PyEdit - ' + open_file)

        data = files.read(open_file)

        self.text.delete('1.0', END)
        self.text.insert('1.0', data)

        self.first_higlight()

    def save(self):
        if self.file is None:
            self.save_as()

        else:
            files.write(self.file, self.text.get('1.0', END))

    def save_as(self):
        save_file = filedialog.asksaveasfilename()
        self.file = save_file
        self.master.title('PyEdit - ' + save_file)

        self.first_higlight()

        files.write(self.file, self.text.get('1.0', END))

    def new(self):
        self.text.delete('1.0', END)
        self.file = None

    def highlight_syntax(self):
        if self.file is not None:
            ext = self.file.split('.')[-1]

            if ext == 'py' or ext == 'pyw':
                self.syntax.default_highlight()

    def first_higlight(self):
        if self.file is not None:
            ext = self.file.split('.')[-1]

            if ext == 'py' or ext == 'pyw':
                self.syntax.initial_highlight()

    def about(self):
        msgbox.showinfo('About', f'Text editor PyText version {self.version} by pointThink')


if __name__ == '__main__':
    root = Tk()
    window = PyEdit(root)
    root.mainloop()
