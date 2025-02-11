from tkinter import *
from tkinter import messagebox
from dashboard import IMS  # Import IMS class from ims.py file
from PIL import Image, ImageTk  # Importing PIL for image handling

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700+400+50")
        self.root.title("Login | Inventory Management System")
        self.root.resizable(False, False)

        # Add a background image
        self.bg_image = Image.open(r"C:\Users\N I T R O 5\Desktop\Inventory-Management-System\images\background.jpg")
        self.bg_image = self.bg_image.resize((1000, 600), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Add a portrait-style image on the left side
        self.portrait_image = Image.open(r"C:\Users\N I T R O 5\Desktop\Inventory-Management-System\images\portrait.jpg")
        self.portrait_image = self.portrait_image.resize((300, 800), Image.LANCZOS)  # Resize to portrait dimensions
        self.portrait_photo = ImageTk.PhotoImage(self.portrait_image)
        self.portrait_label = Label(self.root, image=self.portrait_photo, bg="#f4f4f4")
        self.portrait_label.place(x=15, y=30)  # Position it on the left side

        # Add login form frame
        self.frame = Frame(self.root, width=350, height=350, bg="white")
        self.frame.place(x=480, y=70)

        heading = Label(self.frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        # Define on_enter and on_leave for username
        def on_enter_user(e):
            self.username_entry.delete(0, 'end')

        def on_leave_user(e):
            name = self.username_entry.get()
            if name == '':
                self.username_entry.insert(0, 'Username')

        # Define on_enter and on_leave for password
        def on_enter_code(e):
            self.password_entry.delete(0, 'end')

        def on_leave_code(e):
            name = self.password_entry.get()
            if name == '':
                self.password_entry.insert(0, 'Password')

        self.username_entry = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        self.username_entry.place(x=30, y=80)
        self.username_entry.insert(0, 'Username')
        self.username_entry.bind('<FocusIn>', on_enter_user)
        self.username_entry.bind('<FocusOut>', on_leave_user)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

        self.password_entry = Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        self.password_entry.place(x=30, y=150)
        self.password_entry.insert(0, 'Password')
        self.password_entry.bind('<FocusIn>', on_enter_code)
        self.password_entry.bind('<FocusOut>', on_leave_code)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=178)

        self.login_button = Button(self.frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=self.login)
        self.login_button.place(x=35, y=204)

        Label(self.frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9)).place(x=75, y=270)

        self.sign_up = Button(self.frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
        self.sign_up.place(x=215, y=270)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # For demonstration purposes, using hardcoded credentials
        if username == "admin" and password == "password123":
            self.root.destroy()  # Close the login window
            self.open_ims_window()  # Open IMS window
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def open_ims_window(self):
        ims_root = Tk()  # Create a new root for the IMS window
        ims_obj = IMS(ims_root)  # Initialize IMS class with the root window
        ims_root.mainloop()  # Start the IMS window's main loop

if __name__ == "__main__":
    root = Tk()
    login_obj = Login(root)
    root.mainloop()