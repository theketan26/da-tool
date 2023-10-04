import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


from preprocess.modifiers.add_remove import add, remove
import config


def add_column():
    win = tk.Toplevel(config.root)
    win.grab_set()
    win.title('Add Column')

    tk.Label(win,
             text = 'Add Column'
             ).pack(padx = 10,
                    pady = 10)

    frame = tk.Frame(win)
    frame.pack(padx = 10,
               pady = 10)

    tk.Label(frame,
             text = 'Column Name:'
             ).grid(row = 0,
                    column = 0)
    name_ent = tk.Entry(frame)
    name_ent.grid(row = 0,
                  column = 1)

    tk.Label(frame,
             text = 'Default Values:'
             ).grid(row = 1,
                    column = 0)
    def_ent = tk.Entry(frame)
    def_ent.grid(row = 1,
                 column = 1)

    def proceed():
        name = name_ent.get()
        default = def_ent.get()

        try:
            default = float(default)
        except:
            pass

        add(config.curr_table, name, default)

        win.grab_release()
        win.quit()
        win.destroy()

    tk.Button(win,
              text = 'Add',
              command = proceed
              ).pack(padx = 10,
                     pady = 10)

    win.mainloop()


def remove_column(col_id):
    ans = messagebox.askquestion('Confirm',
                                 f'Do you want to delete column {list(config.curr_data.columns)[col_id]}?')
    if ans == 'yes':
        remove(config.curr_table, col_id)


def main_menu(col_id):
    col_win = tk.Toplevel(config.root)
    col_win.grab_set()
    col_win.title('Column Options')

    tk.Label(col_win,
             text = 'Column Options'
             ).pack(padx = 10,
                    pady = 10)

    btns_frame = tk.Frame(col_win)
    btns_frame.pack(padx = 10,
                    pady = 10)

    options = config.column_process
    option_ent = ttk.Combobox(col_win,
                              values = options,
                              state = 'readonly')
    option_ent.current(0)
    option_ent.pack(padx = 10,
                     pady = 10)

    def proceed():
        option = option_ent.get()

        col_win.grab_release()
        col_win.destroy()

        if option == 'Add':
            add_column()

        elif option == 'Remove':
            remove_column(col_id)

    tk.Button(col_win,
              text = 'Next',
              command = proceed
              ).pack(padx = 10,
                     pady = 10)

    # btn_add = tk.Button(btns_frame,
    #                     text = 'Add new',
    #                     command = lambda: print('add column'))
    # btn_remove = tk.Button(btns_frame,
    #                       text = f'Remove column {col_id}',
    #                       command = lambda: print('remove column'))
    # btn_operate = tk.Button(btns_frame,
    #                         text = f'Operate on {col_id}',
    #                         command = lambda: print('operate on column'))
    #
    # btn_add.pack(fill = 'x')
    # btn_remove.pack(fill = 'x')
    # btn_operate.pack(fill = 'x')

    col_win.mainloop()


def show_column(col_id):
    main_menu(col_id)