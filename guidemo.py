from tkinter import *
#1. Login/Registration
#2. User can see his own profile
#3. user can see other's profile
#4. user can propose other users
#5. user can see who proposed
#6. user can see all the matches
#7. Edit profile
#8. Logout

def check_login():
    #print(email.get())
    #print(password.get())

    if email.get() == 'admin@mywbut.com' and password.get() == '1234':
        result.config(text = "Login Success! Redirecting...", font=("Arial",10))
    else:
        result.config(text="Wrong email or password!", font=("Arial",10))

root=Tk()

root.title("Tinder Login")
root.minsize(400,600)

heading=Label(root, text="Tinder")
heading.config(font=("Times",30))
heading.pack(pady=(30,30))

email_label = Label(root, text="Enter Email:")
email_label.config(font=("Arial",16))
email_label.pack(pady=(10,10))

email=Entry(root)
email.pack(pady=(5,20))

password_label = Label(root, text="Enter Password:")
password_label.config(font=("Arial",16))
password_label.pack(pady=(5,10))

password=Entry(root)
password.pack(pady=(5,10))

login=Button(root, text="Login", command=lambda : check_login())
login.pack(pady=(5,30))

result = Label(root)
result.pack()


root.mainloop()