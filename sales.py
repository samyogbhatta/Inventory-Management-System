from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os

class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+120")
        self.root.title("Inventory Management System")
        self.root.config(bg="#f0f0f0")
        self.root.resizable(False, False)
        self.root.focus_force()

        self.blll_list = []
        self.var_invoice = StringVar()
        
        # Title
        lbl_title = Label(self.root, text="View Customer Bills", font=("times new roman", 30, "bold"), bg="#1e3c72", fg="white", bd=3, relief=RIDGE)
        lbl_title.pack(side=TOP, fill=X, padx=10, pady=20)
        
        lbl_invoice = Label(self.root, text="Invoice No.", font=("times new roman", 15), bg="#f0f0f0")
        lbl_invoice.place(x=50, y=100)
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("times new roman", 15), bg="lightyellow")
        txt_invoice.place(x=160, y=100, width=180, height=28)

        btn_search = Button(self.root, text="Search", command=self.search, font=("times new roman", 15, "bold"), bg="#3498db", fg="white", cursor="hand2")
        btn_search.place(x=360, y=100, width=120, height=28)
        btn_clear = Button(self.root, text="Refresh", command=self.clear, font=("times new roman", 15, "bold"), bg="#95a5a6", fg="white", cursor="hand2")
        btn_clear.place(x=490, y=100, width=120, height=28)

        # Bill List
        sales_Frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_Frame.place(x=50, y=140, width=200, height=330)

        scrolly = Scrollbar(sales_Frame, orient=VERTICAL)
        self.Sales_List = Listbox(sales_Frame, font=("times new roman", 15), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH, expand=1)
        self.Sales_List.bind("<ButtonRelease-1>", self.get_data)

        # Bill Area
        bill_Frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_Frame.place(x=280, y=140, width=410, height=330)
        
        lbl_title2 = Label(bill_Frame, text="Customer Bill Area", font=("times new roman", 20, "bold"), bg="#f39c12", fg="white")
        lbl_title2.pack(side=TOP, fill=X)
        
        scrolly2 = Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_area = Text(bill_Frame, bg="lightyellow", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)

        # Statistics Panel
        stats_Frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        stats_Frame.place(x=700, y=140, width=380, height=330)

        lbl_stats_title = Label(stats_Frame, text="Sales Statistics", font=("times new roman", 20, "bold"), bg="#1e3c72", fg="white")
        lbl_stats_title.pack(side=TOP, fill=X)

        self.lbl_num_bills = Label(stats_Frame, text="Number of Bills: 0", font=("times new roman", 30, "bold"), fg="#3498db", bg="white")
        self.lbl_num_bills.pack(pady=100)

        self.show_statistics()

    # ----------------------------------------------------------------------------------------------------
    def show(self):
        del self.blll_list[:]
        self.Sales_List.delete(0, END)
        
        bill_path = r'C:\Users\N I T R O 5\Desktop\Inventory-Management-System\bill'
        
        for i in os.listdir(bill_path):
            if i.split('.')[-1] == 'txt':
                self.Sales_List.insert(END, i)
                self.blll_list.append(i.split('.')[0])
        self.show_statistics()

    def get_data(self, ev):
        index_ = self.Sales_List.curselection()
        file_name = self.Sales_List.get(index_)
        
        bill_path = r'C:\Users\N I T R O 5\Desktop\Inventory-Management-System\bill'
        
        self.bill_area.delete('1.0', END)
        
        with open(os.path.join(bill_path, file_name), 'r') as fp:
            for i in fp:
                self.bill_area.insert(END, i)

    def search(self):
        if self.var_invoice.get() == "":
            messagebox.showerror("Error", "Invoice no. should be required", parent=self.root)
        else:
            if self.var_invoice.get() in self.blll_list:
                bill_path = r'C:\Users\N I T R O 5\Desktop\Inventory-Management-System\bill'
                
                with open(os.path.join(bill_path, f'{self.var_invoice.get()}.txt'), 'r') as fp:
                    self.bill_area.delete('1.0', END)
                    for i in fp:
                        self.bill_area.insert(END, i)
            else:
                messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0', END)

    def show_statistics(self):
        num_bills = len(self.blll_list)
        self.lbl_num_bills.config(text=f"Number of Bills: {num_bills}")

if __name__ == "__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()
