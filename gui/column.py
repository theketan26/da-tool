import tkinter as tk


import config


def main_menu():
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

    btn_add = tk.Button(btns_frame,
                        text = 'Add',
                        command = lambda: print('add column'))
    btn_remove = tk.Button(btns_frame,
                          text = 'Remove',
                          command = lambda: print('remove column'))
    btn_operate = tk.Button(btns_frame,
                            text = 'Operate',
                            command = lambda: print('operate on column'))

    btn_add.pack(fill = 'x')
    btn_remove.pack(fill = 'x')
    btn_operate.pack(fill = 'x')

    col_win.mainloop()


def show_column():
    main_menu()