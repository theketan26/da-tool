import tkinter as tk
from tkinter import ttk
from matplotlib import pyplot as plt


import config


def show_graph():
    plt.show()


def plot(type = 'Line'):
    columns = list(config.curr_data.columns)

    win = tk.Toplevel(config.root)
    win.title(f'{type} Plot Options')
    win.grab_set()

    tk.Label(win,
             text = f'{type} PLot'
             ).pack(padx = 10,
                    pady = 10)

    ent_win = tk.Frame(win)
    ent_win.pack(padx = 10,
                 pady = 10)
    tk.Label(ent_win,
             text = 'X:'
             ).grid(row = 0,
                    column = 0)
    x_ent = ttk.Combobox(ent_win,
                         values = columns,
                         state = 'readonly')
    x_ent.current(0)
    x_ent.grid(row = 0,
               column = 1)

    if type != 'Histogram':
        tk.Label(ent_win,
                 text = 'Y:'
                 ).grid(row = 1,
                        column = 0)
        y_ent = ttk.Combobox(ent_win,
                             values = columns,
                             state = 'readonly')
        y_ent.current(0)
        y_ent.grid(row = 1,
                   column = 1)

    def proceed():
        x, y = x_ent.get(), y_ent.get()

        x_id = list(config.curr_data.columns).index(x)
        y_id = list(config.curr_data.columns).index(y)

        x_data = list(config.curr_data.iloc[:, x_id])
        y_data = list(config.curr_data.iloc[:, y_id])

        if type == 'Line':
            plt.plot(x_data, y_data)

        elif type == 'Bar':
            plt.bar(x_data, y_data)

        elif type == 'Scatter':
            plt.bar(x_data, y_data)

        elif type == 'Histogram':
            plt.hist(x_data)

        win.grab_release()
        win.destroy()

        show_graph()

    ent_btn = tk.Button(win,
                        text = 'Visualize',
                        command = proceed)
    ent_btn.pack(padx = 10,
                 pady = 10)

    win.mainloop()


def visualize():
    visual_win = tk.Toplevel(config.root)
    visual_win.title('Visualize')
    visual_win.grab_set()

    tk.Label(visual_win,
             text = 'Visualize'
             ).pack(padx = 10,
                    pady = 10)

    options = config.visuals
    graph_options = ttk.Combobox(visual_win,
                                 values = options,
                                 state = 'readonly')
    graph_options.current(0)
    graph_options.pack(padx = 10)

    def proceed():
        option = graph_options.get()

        visual_win.grab_release()
        visual_win.destroy()

        if option == 'Line Plot':
            plot()

        elif option == 'Bar Plot':
            plot('Bar')

        elif option == 'Bar Plot':
            plot('Histogram')

        elif option == 'Scatter Plot':
            plot('Scatter')

    tk.Button(visual_win,
              text = 'Visual',
              command = proceed
              ).pack(padx = 10,
                     pady = 10)

    visual_win.mainloop()
