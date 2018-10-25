from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(self, email, password, name, age):
        self.email = email
        self.name = name
        self.age = age
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return f'User {self.name}'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
