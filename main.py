import interface as ui
import database as db
import util
from time import sleep as s

users = 'users.txt'
if not db.User.file_exist(users):
    db.User.create_file(users)
while True:
    opcao = ui.menu(['Registered Users',
                     'Sign up',
                     'Sign in',
                     'Exit'])
    s(0.8)
    if opcao == 1:
        ui.title('REGISTERED USERS')
        db.read_file(users)
    if opcao == 2:
        ui.title('NEW REGISTRATION')
        nome = str(input('Name: '))
        age = util.read_int('Age: ')
        db.sign_up(users, nome, age)
    if opcao == 3:
        pass  # Sign in
    if opcao == 4:
        exit(ui.title('Closing system... See you later!'))
