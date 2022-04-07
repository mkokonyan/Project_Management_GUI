from view.root_view import RootView
from view.welcome_view import WelcomeView


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
    root = RootView()
    welcome_view = WelcomeView(root)
    welcome_view.pack()
    print_hierarchy(root)
    root.mainloop()
