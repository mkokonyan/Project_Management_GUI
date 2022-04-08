class GoMainMenuCommand:
    def __init__(self, project_controller):
        self.project_controller = project_controller

    def __call__(self):
        self.project_controller.go_main_menu()
