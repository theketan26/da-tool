import tkinter as tk

import config
from preprocess.modifiers.remove_duplicate import remove_duplicate


def show_remove_duplicate():
    rem_dup_win = tk.Toplevel(config.root)
    rem_dup_win.grab_set()
    rem_dup_win.title('Remove Duplicates Options')

    tk.Label(rem_dup_win,
             text = 'Remove Duplicates'
             ).pack(padx = 10,
                    pady = 10)

    tk.Label(rem_dup_win,
             text = 'For all columns set columns to -1'
             ).pack(padx = 10,
                    pady = 10)

    group_col = tk.IntVar(rem_dup_win)

    group_frame = tk.Frame(rem_dup_win)
    group_frame.pack(padx = 10,
                     pady = 10)
    tk.Label(group_frame,
             text = 'Group By:'
             ).pack(side = 'left')
    group_ent = tk.Entry(group_frame,
                         textvariable = group_col)
    group_ent.pack(side = 'left')

    def proceed():
        group_ = None
        while 1:
            try:
                group_ = int(group_col.get())
                break
            except:
                continue

        report = remove_duplicate(key = config.curr_table,
                                  column = group_)

        rem_dup_win.grab_release()
        rem_dup_win.quit()
        rem_dup_win.destroy()

    tk.Button(rem_dup_win,
              text = 'Remove',
              command = proceed
              ).pack(padx = 10,
                     pady = 10)

    rem_dup_win.mainloop()
