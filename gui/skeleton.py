import copy
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


import config
from load_save.load import load
from load_save.save import save
from gui.sum import show_sum
from gui.combine import show_combine
from gui.remove_duplicate import show_remove_duplicate
from gui.merge import show_merge
from gui.column import show_column


def set_table():
    config.table_lbl.config(text = config.curr_table)

    if config.gui_table != None:
        config.gui_table[0].pack_forget()
        config.gui_table[1].pack_forget()
        config.gui_table[2].pack_forget()

    table_data = config.get_data(config.curr_table)

    table_heads = ['SNo']
    table_heads.extend(table_data.columns)

    table = ttk.Treeview(config.table_frame,
                         columns = tuple(table_heads),
                         show = 'headings')

    table.heading('SNo', text = 'SNo')

    for i, col in enumerate(table_data.columns):
        table.heading(col, text = col + '|' + str(i))

    i = 0
    for _, row in table_data.iterrows():
        values = [i + 1]
        values.extend(row)
        table.insert(parent = '', index = i, values = values)
        i += 1

    v_scroll_bar = ttk.Scrollbar(config.table_frame,
                               orient = 'vertical',
                               command = table.yview)
    v_scroll_bar.pack(side = 'right',
                      fill = 'y')
    table.configure(yscrollcommand = v_scroll_bar.set)

    h_scroll_bar = ttk.Scrollbar(config.table_frame,
                               orient = 'horizontal',
                               command = table.xview)
    h_scroll_bar.pack(side = 'bottom',
                      fill = 'x')
    table.configure(xscrollcommand = h_scroll_bar.set)

    config.gui_table = [table, v_scroll_bar, h_scroll_bar]

    table.pack(padx = 20,
               pady = 20,
               expand = True,
               fill = 'both')


def load_file(frames):
    filetypes = (
        ('Comma Seperated Values', '*.csv'),
        ('Excel Spreadsheet', '*.xlsx'),
        ('JSON', '*.json')
    )

    location = filedialog.askopenfilename(title = 'Open file',
                                     filetypes = filetypes)

    load(location)

    frames[1].pack_forget()
    frames[2].pack_forget()
    left_skeleton(frames[0])


def save_file(frames):
    location = filedialog.askdirectory()

    if location == () or location == '':
        return

    save_window = tk.Tk()
    save_window.title('Save')

    formats = ('csv', 'json', 'xlsx')
    # file_name, format = '', formats[0]
    file_name = tk.StringVar()
    format = tk.StringVar()
    format.set(formats[0])

    save_lbl = tk.Label(save_window,
                        text = 'Save As:')
    save_lbl.pack(side = 'top',
                  padx = 10,
                  pady = 10,)

    name_frame = tk.Frame(save_window)
    name_frame.pack()
    name_lbl = tk.Label(name_frame,
                        text = 'File Name:')
    name_lbl.pack(side = 'left',
                  padx = 10)
    name_input = tk.Entry(name_frame,
                          textvariable = file_name)
    name_input.pack(side = 'left')

    format_frame = tk.Frame(save_window)
    format_frame.pack()
    format_lbl = tk.Label(format_frame,
                          text = 'Format:')
    format_lbl.pack(side = 'left',
                    padx = 10)
    format_input = tk.Entry(format_frame,
                            textvariable = format)
    format_input.pack(side = 'left')

    def save_():
        save(config.get_data(config.curr_table), file_name.get(), location, format.get())
        save_window.destroy()

    save_btn = tk.Button(save_window,
                         text = 'Save',
                         command = save_)
    save_btn.pack(padx = 10,
                  pady = 10)

    save_window.mainloop()


def left_skeleton(frame):
    upper = tk.Frame(frame)
    upper.pack(fill = 'y',
               padx = 10,
               pady = 10)

    lower = tk.Frame(frame)
    lower.pack(fill = 'both')

    load_btn = tk.Button(upper,
                         text = "Load File",
                         command = lambda: load_file([frame, lower, upper]))
    save_btn = tk.Button(upper,
                         text = "Save File",
                         command = lambda: save_file([frame, lower, upper]))

    load_btn.pack(fill = 'x')
    save_btn.pack(fill = 'x')

    loaded_lbl = tk.Label(lower,
                          text = 'Loaded Files',)
    loaded_lbl.pack(pady = 10,
                    padx = 10)

    files = config.file_name
    file_btns = [None] * config.file_loaded

    def set_curr_table(key):
        config.curr_table = key

        set_table()

    for i, file in enumerate(files):
        file_btns[i] = tk.Button(lower,
                                 text = file,
                                 command = lambda c = i: set_curr_table(file_btns[c].cget('text')))
        file_btns[i].pack(expand = True,
                          fill = 'both',
                          padx = 10)


def right_skeleton(frame):
    # label = tk.Label(frame, text = 'This is right label', bg = 'red')
    # label.pack(expand = True, fill = 'both')

    table_frame = tk.Frame(frame, bg = 'white')
    table_frame.pack(expand = True,
                     fill = 'both')

    config.table_frame = table_frame

    if config.curr_table != None:
        # table_data = config.get_data(config.curr_table)

        # cols = list(map(lambda i, x: x + '|' + i, enumerate(table_data.columns)))

        table = ttk.Treeview(table_frame,
                             # colunms = cols,
                             show = 'headings',
                             bg = 'white')
        table.pack(padx = 20,
                   pady = 20)

        config.gui_table = table

    else:
        table_lbl = tk.Label(table_frame,
                             text = 'No Table Selected!',
                             bg = 'white')
        table_lbl.pack(padx = 10,
                       pady = 10)
        config.table_lbl = table_lbl

    table_option = tk.Frame(frame)
    table_option.pack(side = 'bottom',
                      fill = 'y',
                      padx = 10,
                      pady = 10)

    # options = tk.StringVar('combine')
    # option_lbl = tk.Label(table_option,
    #                       textvariable = options
    #                       )
    # option_lbl.pack(side = 'left',
    #                 padx = 10,
    #                 expand = True
    #                 )

    options = config.processes
    process = tk.StringVar()
    option_menu = ttk.Combobox(table_option,
                               textvariable = process,
                               values = options,
                               state = 'readonly')
    option_menu.current(0)
    option_menu.pack(side = 'left',
                     padx = 10)

    def proceed():
        curr_proc = config.processes[option_menu.current()]

        if config.curr_table == None:
            return

        if curr_proc == 'sum':
            show_sum()

        elif curr_proc == 'combine':
            show_combine()

        elif curr_proc == 'remove duplicate':
            show_remove_duplicate()

        elif curr_proc == 'merge':
            if config.file_loaded > 2:
                show_merge()

        elif curr_proc == 'column':
            # show_column()
            pass

        try:
            config.gui_table[0].pack_forget()
            set_table()
        except:
            pass

    option_btn = tk.Button(table_option,
                           text = 'Apply',
                           command = proceed)
    option_btn.pack(side = 'right',
                    padx = 10)


def setup_skeleton(root):
    left_frame = tk.Frame(root)
    right_frame = tk.Frame(root)

    left_frame.pack(side = 'left', fill = 'both')
    right_frame.pack(side = 'left', fill = 'both', expand = True)

    left_skeleton(left_frame)
    right_skeleton(right_frame)