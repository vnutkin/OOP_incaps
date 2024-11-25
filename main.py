class User():
    def __init__(self, id, name):
        self.id =  id
        self.name = name
        self.level = 'user'
    def get_info(self):
        print(f'User Id {self.id}, name {self.name}, level {self.level}')
class Admin(User):
    def __init__(self):
        self.users = []
    def _add_user(self, user):
        self.users.append(user)
    def _del_user(self, user):
        self.users.remove(user)
    def set_admin(self, user):
        user.level = 'admin'
    def get_info(self, id):
        for user in self.users:
            if user.id == id:
                print(f'User Id {user.id}, name {user.name}, level {user.level}')
                return
        print(f'no user with Id {id}')
    def list_users(self):
        for user in self.users:
            user.get_info()

u = User
user1 = u(1,'Peter')
user2 = u(2, 'Anna')
user3 = u(3, 'Bob')
ad = Admin()
user3.get_info()
ad.set_admin(user3)
user3.get_info()
ad._add_user(user1)
ad._add_user(user2)
ad._add_user(user3)
user1.get_info()
user2.get_info()
ad.list_users()
ad._del_user(user2)
user2.get_info()
ad.get_info(2)
ad.list_users()


