
print("Please signup")
sys_username = input("Username:")
sys_password = input("Password:")
sys_phone = input("Mobile Number:")
sys_mail= input("E-mail:")
right = 3

print('''
*****************************************
Successfully Registered {} Now you can login to server
*****************************************
'''.format(sys_username))

while True:
    username = input("Username:")
    password = input("Password:")

    if(username == sys_username and password != sys_password):
        print("Wrong password. Please Try Again.")
        right -= 1
        print("You can try {} more time.".format(right))
    elif(username!=sys_username and password == sys_password):
        print("Wrong username. Please Try Again.")
        right -= 1
        print("You can try {} more time.".format(right))
    elif(username != sys_username and password !=sys_password):
        print("Wrong password and username. Please Try Again.")
        right -= 1
        print("You can try {} more time.".format(right))
    else:
        print("Succesfully logged into the server {}.".format(sys_username))
        break
    if(right == 0):
        print("Too many input attempts. You have been banned from the server.")
        break
  
