from lexer import run

shell_on = True

print('Ease 1.0.0 (Jan 28 2021, 12:34:40) written with Python')
print('Type "quit" or "exit" t exit the shell, or "help" for more information.')

while shell_on:
    text = input('ease >>> ')
    
    if 'quit' in text.lower() or 'exit' in text.lower():
        shell_on = False
    
    else:
        run(text)