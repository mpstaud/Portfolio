userName = 'mpstauds'
passWord = 'Chel$e@D@gg3r1988'


# Checks to make sure the credentials are correct
def checkPassword():
    enteredUser = input('Enter your username: ')
    enteredPass = input('Enter you password: ')

    if enteredUser == userName and enteredPass == passWord:
        print('Password Correct. Logging you in...')
        return True

    else:
        print('Username or Password is incorrect')
        return False


# authenticate calls the check password function and repeats until credentials are entered in properly
def authenticate():
    loginResult = checkPassword()

    while not loginResult:
        loginResult = checkPassword()

    return


authenticate()

print('*****        *****             *******       ****************  ****************')
print('******      ******            **** ****      ****************  ****************')
print('*******    *******           ****   ****           ****              ****      ')
print('********  ********          ****     ****          ****              ****      ')
print('**** ******** ****         ***************         ****              ****      ')
print('****  ******  ****        *****************        ****              ****      ')
print('****          ****       ****           ****       ****              ****      ')
print('****          ****      ****             ****      ****              ****      ')
print('****          ****     ****               ****     ****              ****      ')



