# Login e senha
#
# Dificuldade: ☆☆☆
#
# Enunciado:
# Faça um sistema de Cadastro e Login. Primeiro, no cadastro, deve-se guardar o Usuário e a Senha. Depois, repita a
# leitura do usuário e senha até que ambos sejam válidos. Para cada leitura de senha incorreta informada, deve aparecer
# a mensagem "Usuário ou Senha inválidos!". Quando o usuário e senha forem informados corretamente deve ser impressa
# a mensagem "Login completo" e o algoritmo encerrado.
#
# +-----------------------------+
# |  Exemplo de entrada e saída |
# +-----------------------------+
# | --------                    |
# | Cadastro                    |
# | Usuário: Joaozinho          |
# | Senha: 12345                |
# | --------                    |
# | Login                       |
# | Qual Usuário?Mateus         |
# | Qual Senha?12345            |
# | Usuário ou Senha inválidos! |
# |                             |
# | Qual Usuário?Joaozinho      |
# | Qual Senha?54321            |
# | Usuário ou Senha inválidos! |
# |                             |
# | Qual Usuário?joãozinho      |
# | Qual Senha?12345            |
# | Usuário ou Senha inválidos! |
# |                             |
# | Qual Usuário?Joaozinho      |
# | Qual Senha?12345            |
# | Login completo              |
# +-----------------------------+
#
# DICA: while pode ser mais apropriado neste caso.
#

print('--------')
print('Cadastro')
user = input('Usuário: ')
senha = input('Senha: ')

print('--------')
print('Login')

login_user = input('Qual Usuário?')
login_senha = input('Qual Senha?')

while user != login_user or senha != login_senha:
    print('Usuário ou Senha inválidos!\n')
    login_user = input('Qual Usuário?')
    login_senha = input('Qual Senha?')

print('Login completo')