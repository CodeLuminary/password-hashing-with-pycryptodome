from Crypto.Hash import SHA256
import fileinput

hash = SHA256.new()

should_continue = True #This determines wheather the loop should run or not
lines = [] #This holds each line of the passwd.a.txt file
hash_passwords = []

with open('passwd_a.txt', encoding='utf8') as f:
    lines = f.readlines()

count = 0

for line in lines:
    count += 1
    hash.update(bytes(line, 'utf-8'))
    password_dict = {
        "Index": str(count),
        "Usernames" : "UID" + str(count),
        "Hashed passwords": hash.hexdigest(),
        "plain text": line
    }
    
    hash_passwords.append(password_dict)
f.close()

def getPlainPassword(hashpassword):
    for passwds in hash_passwords:
        if hashpassword == passwds["Hashed passwords"]:
            return passwds["plain text"]

while(should_continue):
    option = input(''' Enter 1 to print PasswordTable for the passwd.a.txt file. \n
    Enter 2 to print hash password of a particular index.\n
    Enter 3 to recover a plaintext password.\n
    Enter c to cancel
    \n''')
    if option == 'c':
        should_continue = False
    elif option == '1':
        print("Index     Usernames     Hashed passwords")
        for passwds in hash_passwords:
            line_str = passwds["Index"]

            for i in range(0, (10 - len(passwds["Index"]))):
                line_str += " "
            line_str += passwds["Usernames"]

            for i in range(0, (14 - len(passwds["Usernames"]))):
                line_str += " "
            line_str += passwds["Hashed passwords"]
            print(line_str)

    elif option == '2':
        try:
            option2 = int(input("Enter password index position\n"))

            print("Index     Usernames     Hashed passwords")

            passwds = hash_passwords[option2 - 1]
            line_str = passwds["Index"]

            for i in range(0, (10 - len(passwds["Index"]))):
                line_str += " "
            line_str += passwds["Usernames"]

            for i in range(0, (14 - len(passwds["Usernames"]))):
                line_str += " "
            line_str += passwds["Hashed passwords"]
            print(line_str)
        except:
            print("Please put only an integer value")

    elif option == '3':
        hashpwd = input("Enter hash password\n")
        plainText = getPlainPassword(hashpwd)

        isAvailable = False
        #lines = []

        """for line in fileinput.input(['passwd_b.txt']):
            print(line)
        """

        lines = []
        with open('passwd_b.txt', encoding='utf8') as f:
            lines = f.readlines()

        for line in lines:
            if plainText == line:
                isAvailable = True
                break      
        
        f.close() 
        if isAvailable:
            print("PlainText password: " + plainText)
        else:
            print("Password not available.")    

    print("\n")

