from view.root import Root
from view.main_view import MainView

if __name__ == '__main__':
    root = Root()

    welcome_view = MainView(root)

    root.mainloop()
