from view.root_view import RootView
from view.welcome_view import WelcomeView

if __name__ == '__main__':
    root = RootView()
    welcome_view = WelcomeView(root)
    welcome_view.pack()
    root.mainloop()
