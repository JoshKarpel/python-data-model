START_SEQUENCES = {
    'red': '\u001b[31m',
    'green': '\u001b[32m',
    'blue': '\u001b[34m',
}
RESET_SEQUENCE = '\u001b[0m'

print(START_SEQUENCES['green'], end = '')
print('Hello world, but green!')
print(RESET_SEQUENCE, end = '')
print("Not green!")
