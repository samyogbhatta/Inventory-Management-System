from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.font import Font
import datetime
import sqlite3
import os
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from billing import billClass

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+110+80")
        self.root.title("Inventory Management System")
        self.root.resizable(False, False)
        self.root.config(bg="#f0f0f0")

        #------------- title --------------
        self.icon_title = PhotoImage(file=r"C:/Users/N I T R O 5/Desktop/Inventory-Management-System/images/logo1.png")
        title = Label(self.root, text=" Inventory Management System", image=self.icon_title, compound=LEFT, font=("Helvetica", 30, "bold"), bg="#1e3c72", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=85)

        #------------ logout button -----------
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="#ff4757", fg="white", cursor="hand2", command=self.logout)
        btn_logout.place(x=1150, y=10, height=50, width=150)

        #---------------- calendar -----------------
        self.calendar_frame = Frame(self.root, bd=2, relief=FLAT, bg="#1e3c72")
        self.calendar_frame.place(x=950, y=300, width=350, height=300)
        self.update_calendar()

        #---------------- current time -----------------
        self.lbl_time = Label(self.root, text="", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#1e3c72")
        self.lbl_time.place(x=950, y=610, width=350, height=50)
        self.update_time()

        #---------------- left menu ---------------
        self.MenuLogo = Image.open(r"C:/Users/N I T R O 5/Desktop/Inventory-Management-System/images/menu_im3.png")
        self.MenuLogo = self.MenuLogo.resize((180, 180))
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu = Frame(self.root, bd=2, relief=FLAT, bg="#1e3c72")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo, bg="#1e3c72")
        lbl_menuLogo.pack(side=TOP, fill=X, pady=10)

        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20, "bold"), bg="#1e3c72", fg="white")
        lbl_menu.pack(side=TOP, fill=X)

        self.icon_side = PhotoImage(file=r"C:/Users/N I T R O 5/Desktop/Inventory-Management-System/images/side.png")

        btn_employee = Button(LeftMenu, text="Employee", command=self.employee, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 18, "bold"), bg="#1e3c72", fg="white", bd=0, cursor="hand2")
        btn_employee.pack(side=TOP, fill=X, pady=5)
        btn_supplier = Button(LeftMenu, text="Supplier", command=self.supplier, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 18, "bold"), bg="#1e3c72", fg="white", bd=0, cursor="hand2")
        btn_supplier.pack(side=TOP, fill=X, pady=5)
        btn_category = Button(LeftMenu, text="Category", command=self.category, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 18, "bold"), bg="#1e3c72", fg="white", bd=0, cursor="hand2")
        btn_category.pack(side=TOP, fill=X, pady=5)
        btn_product = Button(LeftMenu, text="Products", command=self.product, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 18, "bold"), bg="#1e3c72", fg="white", bd=0, cursor="hand2")
        btn_product.pack(side=TOP, fill=X, pady=5)
        btn_sales = Button(LeftMenu, text="Sales", command=self.sales, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 18, "bold"), bg="#1e3c72", fg="white", bd=0, cursor="hand2")
        btn_sales.pack(side=TOP, fill=X, pady=5)
        btn_billing = Button(LeftMenu, text="Billing", command=self.billing, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 18, "bold"), bg="#1e3c72", fg="white", bd=0, cursor="hand2")
        btn_billing.pack(side=TOP, fill=X, pady=5)

        #----------- content ----------------
        custom_font = Font(family="Helvetica", size=18, weight="bold")

        self.lbl_employee = self.create_card(x=250, y=120, color="#3498db", icon="👨‍💼", text="Total Employee\n{ 0 }", font=custom_font)
        self.lbl_supplier = self.create_card(x=600, y=120, color="#e67e22", icon="🚚", text="Total Supplier\n{ 0 }", font=custom_font)
        self.lbl_category = self.create_card(x=950, y=120, color="#2ecc71", icon="📦", text="Total Category\n{ 0 }", font=custom_font)
        self.lbl_product = self.create_card(x=250, y=300, color="#9b59b6", icon="🛒", text="Total Product\n{ 0 }", font=custom_font)
        self.lbl_sales = self.create_card(x=600, y=300, color="#f1c40f", icon="💰", text="Total Sales\n{ 0 }", font=custom_font)

        #------------ footer -----------------
        lbl_footer = Label(self.root, text="IMS-Inventory Management System | Developed by .......\nFor any Technical Issues Contact:.........", font=("times new roman", 12), bg="#1e3c72", fg="white")
        lbl_footer.pack(side=BOTTOM, fill=X)

        self.update_content()

    def create_card(self, x, y, color, icon, text, font):
        card = Frame(self.root, bd=2, relief=FLAT, bg=color, highlightthickness=0, highlightbackground="#000")
        card.place(x=x, y=y, height=150, width=300)

        icon_label = Label(card, text=icon, bg=color, fg="white", font=("Helvetica", 40))
        icon_label.place(x=10, y=30)

        text_label = Label(card, text=text, bg=color, fg="white", font=font)
        text_label.place(x=80, y=50)
        
        return text_label

    def update_time(self):
        now_local = datetime.datetime.now().strftime('%H:%M:%S')
        self.lbl_time.config(text=f"Current Time: {now_local}")
        self.lbl_time.after(1000, self.update_time)

    def update_calendar(self):
        today = datetime.date.today()
        cal = Calendar(self.calendar_frame, selectmode='day', year=today.year, month=today.month, day=today.day)
        cal.pack(expand=YES, fill=BOTH)

    #-------------- functions ----------------
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def update_content(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            product = cur.fetchall()
            self.lbl_product.config(text=f"Total Product\n[ {str(len(product))} ]")

            cur.execute("select * from category")
            category = cur.fetchall()
            self.lbl_category.config(text=f"Total Category\n[ {str(len(category))} ]")

            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(text=f"Total Employee\n[ {str(len(employee))} ]")

            cur.execute("select * from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.config(text=f"Total Supplier\n[ {str(len(supplier))} ]")

            bill_path = r'C:/Users/N I T R O 5/Desktop/Inventory-Management-System/bill'
            bill = len(os.listdir(bill_path))
            self.lbl_sales.config(text=f"Total Sales\n[ {str(bill)} ]")

            self.root.after(1000, self.update_content)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    
    def billing(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = billClass(self.new_win)  # Open billing window

    def logout(self):
        self.root.destroy()
        from login import Login  # Import placed here to avoid circular import
        self.login_win = Tk()
        self.new_login = Login(self.login_win)
        self.login_win.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()