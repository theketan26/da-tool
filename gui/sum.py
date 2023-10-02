import tkinter as tk

import config
from preprocess.modifiers.group_sum import group_sum


def show_sum():
    sum_win = tk.Toplevel(config.root)
    sum_win.grab_set()
    sum_win.title('Sum Options')

    group_col = tk.IntVar()
    sum_col = tk.IntVar()
    res_col = tk.StringVar()

    tk.Label(sum_win,
             text = 'Group Sum'
             ).pack(padx = 10,
                    pady = 10)
    tk.Label(sum_win,
             text = 'All entries must be Integer column ID'
             ).pack(padx = 10,
                    pady = 10)

    group_frame = tk.Frame(sum_win)
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

    sum_frame = tk.Frame(sum_win)
    sum_frame.pack(padx = 10,
                   pady = 10)
    tk.Label(sum_frame,
             text = 'Sum By:',
             justify = 'left'
             ).grid(row = 0,
                    column = 0)
    sum_ent = tk.Entry(sum_frame,
                       textvariable = sum_col)
    sum_ent.grid(row = 0,
                 column = 1)

    res_frame = tk.Frame(sum_win)
    res_frame.pack(padx = 10,
                 pady = 10)
    tk.Label(res_frame,
             text = 'Result Name:',
             justify = 'left'
             ).grid(row = 0,
                    column = 0)
    res_ent = tk.Entry(res_frame,
                       textvariable = res_col)
    res_ent.grid(row = 0,
                 column = 1)

    def perf():
        group, sum_, result = None, None, None
        while 1:
            try:
                group = int(group_ent.get())
                sum_ = int(sum_ent.get())
                result = res_ent.get()
                break
            except:
                continue

        report = group_sum(key = config.curr_table,
                           col_a = group,
                           col_b = sum_,
                           col_res_name = result)

        sum_win.grab_release()
        sum_win.quit()
        sum_win.destroy()

    tk.Button(sum_win,
              text = 'Sum',
              command = perf
              ).pack(padx = 10,
                     pady = 10)

    sum_win.mainloop()