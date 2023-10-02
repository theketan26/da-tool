import tkinter as tk

import config
from preprocess.modifiers.group_combine import group_combine


def show_combine():
    comb_win = tk.Toplevel(config.root)
    comb_win.grab_set()
    comb_win.title('Combine Options')

    tk.Label(comb_win,
             text = 'Combine'
             ).pack(padx = 10,
                    pady = 10)

    group_col = tk.IntVar(comb_win)
    combiner = tk.StringVar(comb_win)
    combiner.set(',')

    group_frame = tk.Frame(comb_win)
    group_frame.pack(padx = 10,
                     pady = 10)
    tk.Label(group_frame,
             text = 'Group By:',
             justify = 'left'
             ).grid(row = 0,
                    column = 0)
    group_ent = tk.Entry(group_frame,
                         textvariable = group_col)
    group_ent.grid(row = 0,
                   column = 1)

    combiner_frame = tk.Frame(comb_win)
    combiner_frame.pack(padx = 10,
                        pady = 10)
    tk.Label(combiner_frame,
             text = 'Combiner:',
             justify = 'left'
             ).grid(row = 0,
                    column = 0)
    combiner_ent = tk.Entry(combiner_frame,
                            textvariable = combiner)
    combiner_ent.grid(row = 0,
                      column = 1)

    def proceed():
        group_, combiner_ = None, None
        while 1:
            try:
                group_ = int(group_col.get())
                combiner_ = combiner.get()
                break
            except:
                continue

        report = group_combine(key = config.curr_table,
                               col_a = group_,
                               combiner = combiner_)

        comb_win.grab_release()
        comb_win.quit()
        comb_win.destroy()

    tk.Button(comb_win,
              text = 'Combine',
              command = proceed
              ).pack(padx = 10,
                     pady = 10)

    comb_win.mainloop()
