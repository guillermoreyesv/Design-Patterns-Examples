"""
Este patrón se utiliza para separar la lógica de presentación de la lógica de
negocio en una aplicación web o servicio web. En el patrón MVC, el Modelo
representa los datos y la lógica de negocio, la Vista representa la
interfaz de usuario y el Controlador actúa como intermediario entre el Modelo
y la Vista.
"""


# Modelo
class UserModel:
    def __init__(self, name, email):
        self.name = name
        self.email = email


# Vista
class UserView:
    def show_user(self, user):
        print(f"Name: {user.name}")
        print(f"Email: {user.email}")


# Controlador
class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_user(self, name, email):
        self.model.name = name
        self.model.email = email

    def show_user(self):
        self.view.show_user(self.model)


# Uso del patrón MVC
user_model = UserModel("John Doe", "john.doe@example.com")
user_view = UserView()
user_controller = UserController(user_model, user_view)

user_controller.show_user()
# Output: Name: John Doe, Email: john.doe@example.com

user_controller.update_user("Jane Doe", "jane.doe@example.com")
user_controller.show_user()
# Output: Name: Jane Doe, Email: jane.doe@example.com
