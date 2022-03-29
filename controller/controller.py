from model.model import Model
from view.window import WindowView
from view.view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        pass


if __name__ == '__main__':
    window = WindowView()
    controller = Controller()
    window.mainloop()
