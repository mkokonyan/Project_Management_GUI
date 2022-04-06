from view.main_view import MainView
from view.root import Root


def print_hierarchy(w, depth=0):
    w.update_idletasks()
    print(
        '  ' * depth + w.winfo_class()
        + ' w=' + str(w.winfo_width()) + " h=" + str(w.winfo_height())
        + ' x=' + str(w.winfo_x()) + ' y=' + str(w.winfo_y())
    )
    for chw in w.winfo_children():
        print_hierarchy(chw, depth + 1)


if __name__ == '__main__':
    root = Root()
    main_view = MainView(root)
    print_hierarchy(root)
    root.mainloop()



