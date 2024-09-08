# to encrypt and decrypt the text; the fernet module generate the key
from cryptography.fernet import Fernet

'''def write_key():
    key= Fernet.generate_key()
    with open('key.key',"wb") as key_file:
        key_file.write(key)'''

def load_key():
    file=open('key.key',"rb")
    key= file.read()
    file.close()
    return key



key= load_key()
fer=Fernet(key)

def view():
    with open('passwords.txt','r') as file:
        for line in file.readlines():
            data= line.rstrip()
            user,passw= data.split("|")
            print("Username: ",user,"Password: ",
                  fer.decrypt(passw.encode()).decode())


def add():
    name= input("Account name: ")
    password= input("Password: ")
    with open('passwords.txt','a') as file:
        file.write(name+" | "+fer.encrypt(password.encode()).decode() + "\n")

while True:
    mode= input("Would you like to add a new password or view existing ones (view,add)?,press q to quit ")
    if mode=="q".lower():
        break
    if mode== "add".lower():
        add()
    elif mode=="view".lower():
        view()
    else:
        print("Wrong mode")
        continue