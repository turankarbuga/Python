print("""
********************

USER LOGIN

********************
""")

sys_username="Gritty"
sys_password="123456"

username=input("Username:")
password=input("Password:")

if(username == sys_username and password != sys_password):
    print("incorrect password")
elif(username != sys_username and password == sys_password):
    print("incorrect username")
elif(username != sys_username and password!=sys_password):
    print("incorrect username and incorrect password")
else:
    print("Loging into the system...")
