import time, sys

frase = '\t\t\t\t\t| \033[1;32mH\033[1;31me\033[1;33ml\033[1;34ml\033[1;32mo \033[1;31mW\033[1;33mo\033[1;34mr\033[1;32ml\033[1;31md\033[m |\n'

print('\t\t\t\t\t', end='')
print('_' * 15)

for c in list(frase):
    print(c, end='')
    sys.stdout.flush()
    time.sleep(0.03)

print('\t\t\t\t\t', end='')
print('-' * 15)

print("olá mundo")
