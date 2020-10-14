# Login e senha

print('--------')
print('Cadastro')
user = input('Usuário: ')
senha = input('Senha: ')

print('--------')
print('Login')

login_user = 0
login_senha = 0

while user != login_user or senha != login_senha:
    print('Usuário ou Senha inválidos!')
    login_user = input('Qual Usuário?')
    login_senha = input('Qual Senha?')

print('Login completo')