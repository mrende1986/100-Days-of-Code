from cgitb import text


text_input = input("Enter a sentence to be converted to Morse Code: ")

morse = ''
for char in str(text_input).lower():
    if char == ' ':
        morse += '    '
    else:
        if char == 'a':
            morse += '* ---   '
        elif char == 'b':
            morse += '--- * * *   '
        elif char == 'c':
            morse += '--- * --- *   '
        elif char == 'd':
            morse += '--- * *   '
        elif char == 'e':
            morse += '*   '
        elif char == 'f':
            morse += '* * --- *   '
        elif char == 'g':
            morse += '* * --- *   '
        elif char == 'h':
            morse += '* * * *   '
        elif char == 'i':
            morse += '* *   '
        elif char == 'j':
            morse += '* --- --- ---   '
        elif char == 'k':
            morse += '--- * ---   '
        elif char == 'l':
            morse += '* --- * *   '
        elif char == 'm':
            morse += '--- ---   '
        elif char == 'n':
            morse += '--- *   '
        elif char == 'o':
            morse += '--- --- ---   '
        elif char == 'p':
            morse += '* --- --- *   '
        elif char == 'q':
            morse += '--- --- * ---   '
        elif char == 'r':
            morse += '* --- *   '
        elif char == 's':
            morse += '* * *   '
        elif char == 't':
            morse += '---   '
        elif char == 'u':
            morse += '* * ---   '
        elif char == 'v':
            morse += '* * * ---   '
        elif char == 'w':
            morse += '* --- ---   '
        elif char == 'x':
            morse += '--- * * ---   '
        elif char == 'y':
            morse += '--- * --- ---   '
        elif char == 'z':
            morse += '--- --- * *   '
        elif char == '1':
            morse += '* --- --- --- ---   '
        elif char == '2':
            morse += '* * --- --- ---   '
        elif char == '3':
            morse += '* * * --- ---   '
        elif char == '4':
            morse += '* * * * --- ---   '
        elif char == '5':
            morse += '* * * * *   '
        elif char == '6':
            morse += '--- * * * *   '
        elif char == '7':
            morse += '--- --- * * *   '
        elif char == '8':
            morse += '--- --- --- * *   '
        elif char == '9':
            morse += '--- --- --- --- *   '
        elif char == '0':
            morse += '--- --- --- --- ---   '
        else:
            pass


    

print(morse)