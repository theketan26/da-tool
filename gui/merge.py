import tkinter as tk

import config
from preprocess.modifiers.look_up import look_up


def show_merge():
    merge_win = tk.Toplevel(config.root)
    merge_win.grab_set()
    merge_win.title('Merge Options')

    this_merge_by = tk.StringVar()
    this_selected = tk.StringVar()
    that_file_name = tk.StringVar()
    that_merge_by = tk.StringVar()
    that_selected = tk.StringVar()

    tk.Label(merge_win,
             text = 'Merge'
             ).pack(padx = 10,
                    pady = 10)

    this_frame = tk.Frame(merge_win)
    this_frame.pack(padx = 10,
                    pady = 10)

    tk.Label(this_frame,
             text = 'This table:'
             ).grid(row = 0,
                    column = 0,
                    columnspan = 2)

    tk.Label(this_frame,
             text = 'Merge By:',
             justify = 'left'
             ).grid(row = 1,
                    column = 0)
    this_merge_by_ent = tk.Entry(this_frame,
                                 textvariable = this_merge_by
                                 )
    this_merge_by_ent.grid(row = 1,
                           column = 1)

    # tk.Label(this_frame,
    #          text = 'Selected columns:'
    #          ).grid(row = 2,
    #                 column = 0)
    # this_selected_ent = tk.Entry(this_frame,
    #                              textvariable = this_selected
    #                              )
    # this_selected_ent.grid(row = 2,
    #                        column = 1)


    that_frame = tk.Frame(merge_win)
    that_frame.pack(padx = 10,
                    pady = 10)

    tk.Label(that_frame,
             text = "Second File:"
             ).grid(row = 0,
                    column = 0,
                    columnspan = 2)

    tk.Label(that_frame,
             text = 'File name:',
             justify = 'left'
             ).grid(row = 1,
                    column = 0)
    that_file_name_ent = tk.Entry(that_frame,
                                  textvariable = that_file_name)
    that_file_name_ent.grid(row = 1,
                            column = 1)

    tk.Label(that_frame,
             text = 'Merge by:',
             justify = 'left'
             ).grid(row = 2,
                    column = 0)
    that_merge_by_ent = tk.Entry(that_frame,
                                 textvariable = that_merge_by)
    that_merge_by_ent.grid(row = 2,
                           column = 1)

    # tk.Label(that_frame,
    #          text = 'Selected columns:'
    #          ).grid(row = 3,
    #                 column = 0)
    # that_selected_ent = tk.Entry(that_frame,
    #                              textvariable = that_selected)
    # that_selected_ent.grid(row = 3,
    #                        column = 1)

    def proceed():
        this_merge_by_, this_selected_, that_file_name_, that_merge_by_, that_selected_ = [None] * 5

        while 1:
            try:
                this_merge_by_ = int(this_merge_by_ent.get())
                # this_selected_ = list(map(int, this_selected_ent.get().split()))
                that_file_name_ = that_file_name_ent.get()
                that_merge_by_ = int(that_merge_by_ent.get())
                # that_selected_ = list(map(int, that_selected_ent.get().split()))
                break
            except:
                return

        report = look_up(key_a = config.curr_table,
                         key_b = that_file_name_,
                         col_a = this_merge_by_,
                         col_b = that_merge_by_,)
                         # a_cols = this_selected_,
                         # b_cols = that_selected_)

        merge_win.grab_release()
        merge_win.quit()
        merge_win.destroy()

    tk.Button(merge_win,
              text = 'Merge',
              command = proceed
              ).pack(padx = 10,
                     pady = 10)

    merge_win.mainloop()
