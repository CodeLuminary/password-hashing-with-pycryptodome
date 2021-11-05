

should_continue = True #This determines wheather the loop should run or not
passwordlines = [] #This holds each line of the passwd.a.txt file


while(should_continue):
    option = input(''' Enter 1 to print PasswordTable for the passwd.a.txt file. \n
    Enter 2 to print hash password of a particular index.\n
    Enter 3 to recover a plaintext password.\n
    Enter c to cancel\n
    \n''')
    if option == 'c':
        should_continue = False
    elif option == '1':
        pass
    elif option == '2':
        pass
    elif option == '3':
        pass