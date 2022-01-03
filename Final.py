from tkinter import  *
import mysql.connector as sql
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import ImageTk, Image
import numpy as np
from base64 import b64encode, b64decode


class startpage :

    ''' This is a class in which the whole program is scripted, starting from creating tkinter window,
    with different entry boxes, labels, images, graphs using matplot library and database connections too.  '''

    def __init__(self, win) :

        ''' It is a reserved function in Python class which makes all the function initialize the attributes inside
        the class. It is also called as a constructor is object oriented terminology. '''

        self.win = win
        self.win.geometry("800x500+300+150")
        self.win.title("Salary Manager")
        # self.win.configure(bg = "#15350204f")

        st = StringVar()
        self.intt = IntVar()

        def main_table() :

            ''' The function main_table() is used for creating the table and the database in MySql. Here I have use
            Exceptional Handling for checking that the database is already created or not. Using different
            exceptions, I have created a database named salarymanagement and table name main in MySql server. Using
            the module mysql.connector, I have inserted columns in the table. '''

            self.cur.execute("create table main"
                        "("
                        "Name varchar(25), "
                        "Age mediumint, "
                        "Gender char(7), "
                        "Password varchar(100) NOT NULL, "
                        "Job char(5), "
                        "Job_Interval char(5), "
                        "Salary int, "
                        "Extra_Income "
                        "mediumint, "
                        "House_Rent mediumint, "
                        "Electric_Bill mediumint, "
                        "Food mediumint, "
                        "Cooking mediumint, "
                        "Health mediumint, "
                        "Education mediumint, "
                        "Water_Supply mediumint, "
                        "Shopping mediumint, "
                        "Travelling mediumint, "
                        "Internet mediumint,"
                        "Savings mediumint, "
                        "Loan mediumint, "
                        "Extra mediumint, "
                        "Donations mediumint"
                        ")"
                        "")

        self.db = sql.connect(host = "localhost", user = "root", passwd = "123456789")
        self.cur = self.db.cursor()

        try :

            self.cur.execute("create database salarymanagement")
            self.db = sql.connect(host = "localhost", user = "root", passwd = "123456789", database = "salarymanagement")
            self.cur = self.db.cursor()

        except sql.errors.DatabaseError :

            self.db = sql.connect(host = "localhost", user = "root", passwd = "123456789", database = "salarymanagement")
            self.cur = self.db.cursor()

            try :

                main_table()

            except sql.errors.ProgrammingError :
                pass

        finally :

            try :

                main_table()

            except sql.errors.ProgrammingError :

                pass

        self.home_frame = Frame(win, width = 800, height = 500, bg = "#fab308")
        self.home_frame.place(x = 0, y = 0)

        self.lab1 = Label(self.home_frame, text = "Name :", bg = "#fab308", fg = "white", font = "agencyfb")
        self.lab2 = Label(self.home_frame, text = "Age  :", bg = "#fab308", fg = "white", font = "agencyfb")
        self.labp = Label(self.home_frame, text = "Password :", bg = "#fab308")
        self.labp.configure(fg = "white", font = "agencyfb")
        self.labo = Label(self.home_frame, text = "Please Login / Sign Up to continue :")
        self.labo.configure(bg = "white", fg = "black", relief= "groove", font = "agencyfb")

        self.lab1.place(x = 300, y = 175)
        self.lab2.place(x = 300, y = 200)
        self.labp.place(x = 300, y = 225)
        self.labo.place(x = 294, y = 140)


        def coountdown(time, fab) : 

            ''' This function coountdown() is used for time interval. I have used this function several time for
            vanishing different frames. '''

            if time == -1 :
                fab.destroy()
            else :
                fab.after(500, coountdown, time-1, fab)

        fab = Frame(self.win, bg = "white", width = 800, height = 500)
        fab.place(x = 0, y = 0)
        coountdown(2, fab)

        basewidth = 300
        img = Image.open('Picture2.jpg')
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        im = img.resize((90,90), Image.ANTIALIAS)
        imgii = ImageTk.PhotoImage(im)
        imi = img.resize((150, 130), Image.ANTIALIAS)
        imgia = ImageTk.PhotoImage(imi)

        panel = Label(fab, image = imgii)
        panel.image = imgii
        panel.place(x = 355, y = 205)

        varm = IntVar()
        st = StringVar()
        st1 = StringVar()
        self.intt = IntVar()

        
        def mark():

            ''' The function mark() is used for hiding password in the first frame or login page. This function is
            embedded inside the Checkbutton widget so that if the button is checked then the password will bo shown
            or for any other case it will be replaced by a star(*). '''

            if varm.get() == 1 :

                self.password.configure(show = "")
                check.configure(text = "Hide")

            elif varm.get() == 0 :

                self.password.configure(show = "*")
                check.configure(text = "Show")

        self.name = Entry(self.home_frame, textvariable = st, font = "Arial", bg = "#FDFEFE", width = 16,
        fg = "black", bd = 0, selectbackground = "#B9AA8F")
        self.age = Entry(self.home_frame, textvariable = self.intt, font = "Arial", bg = "#FDFEFE", width = 16,
        fg = "black", bd = 0, selectbackground = "#B9AA8F")
        self.password = Entry(self.home_frame,textvariable = st1, show = "*", font = "Arial", bg = "#FDFEFE",
        width = 16, fg = "black", bd = 0, selectbackground = "#FDFEFE")
        check = Checkbutton(self.home_frame, text = "Show", command = mark, font = "Arial", bd = 0)
        check.configure(onvalue = 1, offvalue = 0, variable = varm, bg = "#fab308", fg = "white",
        activebackground = "#2A7888")

        self.name.place(x = 385, y = 175)
        self.age.place(x = 385, y = 200)
        self.password.place(x = 385, y = 225)
        check.place(x = 534, y = 225)

        self.messg = "Adita Ramesh \n Giri Prasanth \n Krithk Raju \n Venkat Ganesh  " 

        def like(event) :

            ''' The function like() is used to display the image in the login frame and it also display the about
            section of application by double clicking on the image. I have also packed a button named Out to exiting
            about frame displayed on the main frame. '''

            creator_info = Frame(self.home_frame, width = 600, height = 380)
            creator_info.place(x = 100, y = 60)

            messg_widget = Message(creator_info, text = self.messg, bg = "pink", fg = "black")
            messg_widget.place(x = 100, y = 100)

            def destrot() :

                ''' This small function destrot() is packed inside the Button named out for destroying the about
                frame or to clear the about section. '''

                creator_info.destroy()

            quite = Button(creator_info,text = "X", command = destrot, bd = 0, fg = "red")
            quite.place(x = 570, y = 0)

        top = Button(self.home_frame, image = imgia, bd = 0)
        top.bind('<Double-Button>', like)
        top.image = imgia
        top.place(x = 25, y = 25)

        # self.flag = ""
        # self.cart = ""
        self.constant = False

        #self.win.iconbitmap('management_ico.ico')

        def options() :

            ''' The function options() is used for displaying the different genders in the login page. I have used
            the OptionMenu widget for making the Option Button. This options are specified with the four different
            strings. '''

            self.lab3 = Label(self.home_frame, text = "Gender :", bg = "#fab308", fg = "white", font = "agencyfb")
            self.lab3.place(x = 300, y = 250)

            options = [
                "       Select         ",
    
                "         Male         ",
                "        Female        ",
                "        Perfer Not to Say        "
            ]

            st = StringVar()
            st.set(options[0])
            self.optnbtn = OptionMenu(self.home_frame, st, options[0], options[1], options[2],options[3])
            self.optnbtn.configure(bd = 0, height = 1, width = 12, font = "Arial", bg = "white", fg = "black",
            activebackground = "#B6C1C3")
            self.optnbtn.place(x = 385, y = 250)
            self.optnbtn1 = "gg"

        options()

        def service() :

            ''' This function service() is designed to store the Earnings of a person in a regular basis in the
            service sector. I have specified different entry box using the Entry widget to store the data of their
            expenses in our MySql server. '''
            self.service_frame = Frame(self.win, width = 800, height = 500, bg = "#6fc8c9")
            self.service_frame.place(x = 0, y = 0)

            self.var5 = IntVar()
            self.var6 = IntVar()

            self.var5.set(0)
            self.var6.set(0)

            self.flag = "servi"

            # self.day_1.place_forget()
            # self.week_1.place_forget()
            # self.month_1.place_forget()

            self.lab5 = Label(self.service_frame, text  = "EARNINGS")
            self.lab6 = Label(self.service_frame, text = "SALARY         :")
            self.lab7 = Label(self.service_frame, text = "EXTRA INCOME   :")

            self.lab5.configure(bd = 0, bg = "white", fg = "black", font=('Bahnschrift',15))
            self.lab6.configure(bd = 1, bg = "#6fc8c9", fg = "black", font = "arialroundedmtbold")
            self.lab7.configure(bd = 1, bg = "#6fc8c9", fg = "black", font = "arialroundedmtbold")


            self.lab5.place(x = 375, y = 155)
            self.lab6.place(x = 250, y = 250)
            self.lab7.place(x = 250, y = 325)

            self.salary_1 = Entry(self.service_frame, textvariable = self.var5)
            self.extra_1 = Entry(self.service_frame, textvariable = self.var6)
            self.salary_1.place(x = 390, y = 250)
            self.extra_1.place(x = 390, y = 325)

            ''' Here I have just extract the username and password from MySql server to check weather this account is 
            already registered or not. If registered, then it will extract the values of Earnings and Extra from MySql 
            server and placed it in the entry field as it was saved earlier by the owner of that account. It means 
            it will be recovered every time when it is logged in. '''

            user = str(self.name.get())
            passwd = b64encode(bytes(self.password.get(), "utf-16")).decode()

            self.cur.execute("select * from main where Name = '%s' and Password = '%s'" % (str(user), str(passwd)))
            rud = self.cur.fetchall()

            if rud :

                self.cur.execute("select Salary, Extra_Income from main where Name = '%s'and Job = 'servi'" %(user))
                nod = self.cur.fetchone()

                if nod :

                    rd = np.array(nod)

                    #self.var5.set(rd[0])
                    #self.var6.set(rd[1])

                    self.salary_1.configure(textvariable = self.var5)
                    self.extra_1.configure(textvariable = self.var6)

            submit = Button(self.service_frame, text = "SUBMIT", command = expenses)
            submit.configure(bd = 0, bg = "#e64e4e", fg = "white", font = "agencyfb", width = 10,relief= "groove")
            submit.place(x = 390, y = 375)

            self.acc = Button(self.win, text = ">", command = account, bd = 0)
            self.acc.place(x = 0, y = 240)

        def business() :

            ''' This function business() is designed to store the Earnings of a person in a regular basis in the
            business sector. I have specified different entry box using the Entry widget to store the data of their
            income in our MySql server. '''

            self.business_frame = Frame(self.win, width = 800, height = 500, bg = "#6fc8c9")
            self.business_frame.place(x = 0, y = 0)

            self.var5 = IntVar()
            self.var6 = IntVar()

            self.var5.set(0)
            self.var6.set(0)

            self.flag = "busin"

            # self.day_2.place_forget()
            # self.week_2.place_forget()
            # self.month_2.place_forget()

            self.lab8 = Label(self.business_frame, text = "EARNINGS")
            self.lab9 = Label(self.business_frame, text = "SALARY         :")
            self.lab10 = Label(self.business_frame, text = "EXTRA INCOME  :")

            self.lab8.configure(bd = 0, bg = "white", fg = "black", font=('Bahnschrift',15))
            self.lab9.configure(bd = 1, bg = "#6fc8c9", fg = "black", font = "arialroundedmtbold")
            self.lab10.configure(bd = 1, bg = "#6fc8c9", fg = "black", font = "arialroundedmtbold")

            self.lab8.place(x = 375, y = 155)
            self.lab9.place(x = 250, y = 250)
            self.lab10.place(x = 250, y = 325)

            self.salary_1 = Entry(self.business_frame, textvariable = self.var5)
            self.extra_1 = Entry(self.business_frame, textvariable = self.var6)
            self.salary_1.place(x = 390, y = 250)
            self.extra_1.place(x = 390, y = 325)

            ''' Here I have just extract the username and password from MySql server to check weather this account is 
            already registered or not. If registered, then it will extract the values of Earnings and Extra from MySql 
            server and placed it in the entry field as it was saved earlier by the owner of that account. It means 
            it will be recovered every time when it is logged in. '''

            user = str(self.name.get())
            passwd = b64encode(bytes(self.password.get(), "utf-16")).decode()

            self.cur.execute("select * from main where Name = '%s' and Password = '%s'" % (str(user), str(passwd)))
            rud = self.cur.fetchall()

            if rud:

                self.cur.execute("select Salary, Extra_Income from main where Name = '%s'and Job = 'busin'" % (user))
                nod = self.cur.fetchone()

                if nod :

                    rd = np.array(nod)

                    self.var5.set(rd[0])
                    self.var6.set(rd[1])

                self.salary_1.configure(textvariable = self.var5)
                self.extra_1.configure(textvariable = self.var6)

            submit = Button(self.business_frame, text = "SUBMIT", command = expenses)
            submit.configure(bd = 0, bg = "#e64e4e", fg = "white", font = "agencyfb", width = 10,relief= "groove")
            submit.place(x = 390, y = 375)

            self.acc = Button(self.win, text = ">", command = account, bd = 0)
            self.acc.place(x = 0, y = 240)

        def expenses() :

            ''' This function expenses() creates a frame that consists of different expenses of life. Here are
            different entry box with different labels for users convenient. I have specified different entry box using
            the Entry widget to store the data of their expenses in our MySql server. '''

            if self.salary_1.get() != "" or self.extra_1.get() != "" :

                self.frame2 = Frame(self.win, bg = "#6fc8c9", width = 800, height = 500)
                self.frame2.place(x = 0, y = 0)

                self.acc = Button(self.win, text = ">", command = account, bd = 0)
                self.acc.place(x = 0, y = 240)

                self.lab14 = Label(self.frame2, text = "EXPENSES", bd = 0)
                self.lab14.configure(fg = "black", bg = "white", font = ('Bahnschrift',15))
                self.lab14.place(x = 375, y = 50)

                self.var7 = IntVar()
                self.var8 = IntVar()
                self.var9 = IntVar()
                self.var10 = IntVar()
                self.var11 = IntVar()
                self.var12 = IntVar()
                self.var13 = IntVar()
                self.var14 = IntVar()
                self.var15 = IntVar()
                self.var16 = IntVar()
                self.var17 = IntVar()
                self.var18 = IntVar()
                self.var19 = IntVar()
                self.var20 = IntVar()

                self.var7.set(0)
                self.var8.set(0)
                self.var9.set(0)
                self.var10.set(0)
                self.var11.set(0)
                self.var12.set(0)
                self.var13.set(0)
                self.var14.set(0)
                self.var15.set(0)
                self.var16.set(0)
                self.var17.set(0)
                self.var18.set(0)
                self.var19.set(0)
                self.var20.set(0)

                lab15 = Label(self.frame2, text = "HOUSE RENT", bd = 1)
                lab16 = Label(self.frame2, text = "ELECTRIC BILLS", bd = 1)
                lab17 = Label(self.frame2, text = "FOOD", bd = 1)
                lab18 = Label(self.frame2, text = "COOKING EMENITIES", bd = 1)
                lab19 = Label(self.frame2, text = "HEALTH", bd = 1)
                lab20 = Label(self.frame2, text = "EDUCATION", bd = 1)
                lab21 = Label(self.frame2, text = "WATER SUPPLY", bd = 1)
                lab22 = Label(self.frame2, text = "SHOPPING", bd = 1)
                lab23 = Label(self.frame2, text = "TRAVELLING", bd = 1)
                lab24 = Label(self.frame2, text = "INTERNET &", bd = 1)
                lab24_a = Label(self.frame2, text = "COMMUNICATION BILLS", bd = 1)
                lab25 = Label(self.frame2, text = "SAVINGS", bd = 1)
                lab26 = Label(self.frame2, text = "LOAN REPAYMENT", bd = 1)
                lab27 = Label(self.frame2, text = "EXTRA", bd = 1)
                lab28 = Label(self.frame2, text = "DONATIONS", bd = 1)

                lab15.configure(fg = "#000000", bg = "#6fc8c9", font = "Arial")
                lab16.configure(fg = "#000000", bg = "#6fc8c9", font = "Arial")
                lab17.configure(fg = "#000000", bg = "#6fc8c9", font = "Arial")
                lab18.configure(fg = "#000000", bg = "#6fc8c9", font = "Arial")
                lab19.configure(fg = "#000000", bg = "#6fc8c9", font = "Arial")
                lab20.configure(fg = "#000000", bg = "#6fc8c9", font = "Arial")
                lab21.configure(fg = "#000000", bg = "#6fc8c9", font = "Arial")
                lab22.configure(fg = "#000000", bg = "#6fc8c9", font = "Arial")
                lab23.configure(fg = "#000000", bg = "#6fc8c9", font = "Arial")
                lab24.configure(fg = "#000000", bg = "#6fc8c9", font = "Arial")
                lab24_a.configure(fg = "#000000", bg = "#6fc8c9", font = "Arial")
                lab25.configure(fg = "#000000", bg = "#6fc8c9", font = "Arial")
                lab26.configure(fg = "#000000", bg = "#6fc8c9", font = "Arial")
                lab27.configure(fg = "#000000", bg = "#6fc8c9", font = "Arial")
                lab28.configure(fg = "#000000", bg = "#6fc8c9", font = "Arial")

                #intt = IntVar()
                self.intt .set(0)

                self.entry15 = Entry(self.frame2, textvariable = self.var7, bd = 0)
                self.entry16 = Entry(self.frame2, textvariable = self.var8, bd = 0)
                self.entry17 = Entry(self.frame2, textvariable = self.var9, bd = 0)
                self.entry18 = Entry(self.frame2, textvariable = self.var10, bd = 0)
                self.entry19 = Entry(self.frame2, textvariable = self.var11, bd = 0)
                self.entry20 = Entry(self.frame2, textvariable = self.var12, bd = 0)
                self.entry21 = Entry(self.frame2, textvariable = self.var13, bd = 0)
                self.entry22 = Entry(self.frame2, textvariable = self.var14, bd = 0)
                self.entry23 = Entry(self.frame2, textvariable = self.var15, bd = 0)
                self.entry24 = Entry(self.frame2, textvariable = self.var16, bd = 0)
                self.entry25 = Entry(self.frame2, textvariable = self.var17, bd = 0)
                self.entry26 = Entry(self.frame2, textvariable = self.var18, bd = 0)
                self.entry27 = Entry(self.frame2, textvariable = self.var19, bd = 0)
                self.entry28 = Entry(self.frame2, textvariable = self.var20, bd = 0)

                self.total_print = Label(self.frame2, text = 0, bd = 0)
                
                self.total = Label(self.frame2, text = ("TOTAL EXPENSES"), bd = 0)

                '''  Here again I have checked for account verification so that the data can be replaced with the 
                existing data stored in the MySql database for any similar username and password. So that it will be 
                easy for user to update their existing data in the frame. '''

                self.db = sql.connect(host = "localhost", user = "root", passwd = "123456789",database = "salarymanagement")
                                      
                self.cur = self.db.cursor()

                user = self.name.get()
                passwd = b64encode(bytes(self.password.get(), "utf-16")).decode()

                self.cur.execute("select * from main where Name = '%s' and Password = '%s'" % (str(user), str(passwd)))
                rud = self.cur.fetchall()

                if rud :

                    def if_login() :

                        ''' In this function if_login() we have extracted all the values of daily expenses
                        from database as stored by the user. I have also used a if structure before calling of this
                        function, that will help if the given username and password matched with the data stored
                        earlier in the database, otherwise it will create a new row for the new user. '''

                        rd = np.array(rud)

                        self.var1 = StringVar()
                        self.var2 = IntVar()
                        # self.var3 = StringVar()
                        self.var4 = StringVar()
                        self.var5 = IntVar()
                        self.var6 = IntVar()
                        self.var7 = IntVar()
                        self.var8 = IntVar()
                        self.var9 = IntVar()
                        self.var10 = IntVar()
                        self.var11 = IntVar()
                        self.var12 = IntVar()
                        self.var13 = IntVar()
                        self.var14 = IntVar()
                        self.var15 = IntVar()
                        self.var16 = IntVar()
                        self.var17 = IntVar()
                        self.var18 = IntVar()
                        self.var19 = IntVar()
                        self.var20 = IntVar()

                        self.var1.set(rd[0][0])
                        self.var2.set(rd[0][1])
                        # self.var3.set(rd[0][2])
                        self.var4.set(rd[0][3])
                        self.var5.set(rd[0][6])
                        self.var6.set(rd[0][7])
                        self.var7.set(rd[0][8])
                        self.var8.set(rd[0][9])
                        self.var9.set(rd[0][10])
                        self.var10.set(rd[0][11])
                        self.var11.set(rd[0][12])
                        self.var12.set(rd[0][13])
                        self.var13.set(rd[0][14])
                        self.var14.set(rd[0][15])
                        self.var15.set(rd[0][16])
                        self.var16.set(rd[0][17])
                        self.var17.set(rd[0][18])
                        self.var18.set(rd[0][19])
                        self.var19.set(rd[0][20])
                        self.var20.set(rd[0][21])

                        self.name.configure(textvariable = self.var1)
                        self.age.configure(textvariable = self.var2)
                        # self.optnbtn1.configure(textvariable = self.var3)
                        self.password.configure(textvariable = self.var4)
                        self.salary_1.configure(textvariable = self.var5)
                        self.extra_1.configure(textvariable = self.var6)
                        self.entry15.configure(textvariable = self.var7)
                        self.entry16.configure(textvariable = self.var8)
                        self.entry17.configure(textvariable = self.var9)
                        self.entry18.configure(textvariable = self.var10)
                        self.entry19.configure(textvariable = self.var11)
                        self.entry20.configure(textvariable = self.var12)
                        self.entry21.configure(textvariable = self.var13)
                        self.entry22.configure(textvariable = self.var14)
                        self.entry23.configure(textvariable = self.var15)
                        self.entry24.configure(textvariable = self.var16)
                        self.entry25.configure(textvariable = self.var17)
                        self.entry26.configure(textvariable = self.var18)
                        self.entry27.configure(textvariable = self.var19)
                        self.entry28.configure(textvariable = self.var20)

                    if_login()
                    self.db.commit()

                def click() :

                    ''' This function click() mainly used for collecting all the data from the entry boxes of
                    expenses an to check weather the total expenses is less that the total income including extra
                    income. If it is more that the income then it will show a error message, so that user can
                    understand the problem so that it can be changed into correct form. '''

                    self.lst_total = [
                        int(self.entry15.get()),
                        int(self.entry16.get()),
                        int(self.entry17.get()),
                        int(self.entry18.get()),
                        int(self.entry19.get()),
                        int(self.entry20.get()),
                        int(self.entry21.get()),
                        int(self.entry22.get()),
                        int(self.entry23.get()),
                        int(self.entry24.get()),
                        int(self.entry25.get()),
                        int(self.entry26.get()),
                        int(self.entry27.get()),
                        int(self.entry28.get())
                    ]

                    self.summ = 0
                    for i in range(0, len(self.lst_total)):
                        self.summ = self.summ + self.lst_total[i]

                    inc_1 = int(self.salary_1.get()) + int(self.extra_1.get())

                    if self.summ > inc_1 :

                        error = Frame(self.frame2, bd = 0, bg = "red", width = 800, height = 100)
                        error.place(x = 250, y = 245)
                        error_lab = Label(error, text = "YOUR INCOME IS LESS TO FULFILL YOUR EXPENSE")
                        error_lab.configure(bd = 0, fg = "black", bg = "red")
                        error_lab.pack()
                        self.total_print.configure(text = self.summ)

                        coountdown(6, error)

                        def error_ok() :

                            ''' The function error_ok() is used delete a error frame created due to a debug in the
                            program to make this simple and understandable. '''

                            error.place_forget()
                            #sleep(5)

                        error_btn = Button(error, text = "Ok", command = error_ok, bd = 0)
                        error_btn.pack()

                    else :

                        database()
                        self.total_print.configure(text = self.summ)

                        stat()

                click_btn = Button(self.frame2, text = "Enter", command = click, bd = 0)
                click_btn.configure()

                lab15.place(x = 50, y = 100)
                lab16.place(x = 50, y = 150)
                lab17.place(x = 50, y = 200)
                lab18.place(x = 50, y = 250)
                lab19.place(x = 50, y = 300)
                lab20.place(x = 50, y = 350)
                lab21.place(x = 50, y = 400)
                lab22.place(x = 450, y = 100)
                lab23.place(x = 450, y = 150)
                lab24.place(x = 450, y = 200)
                lab24_a.place(x = 450, y = 220)
                lab25.place(x = 450, y = 250)
                lab26.place(x = 450, y = 300)
                lab27.place(x = 450, y = 350)
                lab28.place(x = 450, y = 400)
                self.total.place(x = 280, y = 445)
                self.total_print.place(x = 480, y = 440)
                click_btn.place(x = 380, y = 475)

                self.entry15.place(x = 200, y = 100)
                self.entry16.place(x = 200, y = 150)
                self.entry17.place(x = 200, y = 200)
                self.entry18.place(x = 200, y = 250)
                self.entry19.place(x = 200, y = 300)
                self.entry20.place(x = 200, y = 350)
                self.entry21.place(x = 200, y = 400)
                self.entry22.place(x = 600, y = 100)
                self.entry23.place(x = 600, y = 150)
                self.entry24.place(x = 600, y = 200)
                self.entry25.place(x = 600, y = 250)
                self.entry26.place(x = 600, y = 300)
                self.entry27.place(x = 600, y = 350)
                self.entry28.place(x = 600, y = 400)

            else :

                fabu = Label(self.win, text = "Please enter your Name and Password")
                fabu.configure(bg = "#15350204f", fg = "black")
                fabu.place(x = 300, y = 345)
                coountdown(5, fabu)

        def stat() :

            ''' This function stat() will create a frame with three buttons for three types of graph. This was made
            so that user can get graphical or tabular view of his/her daily expenses. '''

            self.frame2.place_forget()
            self.statt = Frame(self.win, bg = "#6fc8c9", width = 800, height = 500)
            self.statt.place (x = 0, y = 0)

            ab = Label(self.statt, text = "STATISTICAL INTERPETATION",bg='black',fg='white',font=('Bahnschrift',15))
            ab.place(x = 340, y = 35)

            self.line_graph = Button(self.statt, text = "LINE GRAPH", command = line_graphical)
            self.bar_graph = Button(self.statt, text = "BAR GRAPH", command = bar_graphical)
            self.pie_graph = Button(self.statt, text = "PIE CHART", command = pie_graphical)

            self.line_graph.configure(bd = 0, width = 15, height = 6, bg = "white", activebackground =
            "#15350204f", font = "arialroundedmtbold", relief = SUNKEN)
            self.bar_graph.configure(bd = 0, width = 15, height = 6, bg = "white", activebackground =
            "#15350204f", font = "arialroundedmtbold", relief = SUNKEN)
            self.pie_graph.configure(bd = 0, width = 15, height = 6, bg = "white", activebackground =
            "#15350204f", font = "arialroundedmtbold", relief = SUNKEN)

            self.line_graph.place(x = 166, y = 160)
            self.bar_graph.place(x = 482, y = 160)
            self.pie_graph.place(x = 320, y = 330)

            self.acc = Button(self.statt, text = ">", command = account, bd = 0)
            self.acc.place(x = 0, y = 240)

        def line_graphical() :

            '''  The function line_graphical() is directed from the statt frame. Here using matplotlib and pyplot,
            I have plotted the data in format of line graph. For this I have used canvas and figure function from
            tkinter and matplotlib respectively. At first I have created a figure and then the data was plotted
            inside the line graph. After that the image was placed inside the canvas and then on main frame of the
            window. '''

            self.statt.place_forget()

            self.graph_frame = Frame(self.win, bg = "#a89e9e", width = 800, height = 500)
            self.graph_frame.place(x = 0, y = 0)

            fig = Figure(figsize = (8, 5), dpi = 100)
            fig.suptitle("Money Spent")

            b = []
            a = [
                "HOUSE RENT",
                "ELECTRIC BILLS",
                "FOOD",
                "COOKING EMENITIES",
                "HEALTH",
                "EDUCATION",
                "WATER SUPPLY",
                "SHOPPING",
                "TRAVELLING",
                "INTERNET & COMMUNICATION",
                "SAVINGS",
                "LOAN REPAYMENT",
                "EXTRA",
                "DONATIONS"
            ]

            for i in self.lst_total :
                b.append(i)

            graph = fig.add_subplot(122)
            graph.plot(b, a, marker = "o")
            graph.grid()

            canv = FigureCanvasTkAgg(fig, master = self.graph_frame)
            canv.draw()

            get_widz = canv.get_tk_widget()
            get_widz.pack()

            self.back = Button(self.graph_frame, text = "BACK", command = stat)
            self.back.configure(bd = 0, bg = "black", fg = "white", activebackground = "#15350204f",
            font = "arialroundedmtbold", relief = SUNKEN)
            self.back.place(x = 0, y = 0)

        def bar_graphical() :

            '''  The function bar_graphical() is directed from the statt frame. Here using matplotlib and pyplot,
            I have plotted the data in format of bar graph. For this I have used canvas and figure function from
            tkinter and matplotlib respectively. At first I have created a figure and then the data was plotted
            inside the line graph. After that the image was placed inside the canvas and then on main frame of the
            window. In the same way like the line graph. '''

            self.statt.place_forget()

            self.br_grph = Frame(self.win, bg = "#a89e9e", width = 800, height = 500)
            self.br_grph.place(x = 0, y = 0)

            fig = Figure(figsize = (8, 5), dpi = 100)
            fig.suptitle("Money Spent")

            b = []
            a = [
                "HOUSE RENT",
                "ELECTRIC BILLS",
                "FOOD",
                "COOKING EMENITIES",
                "HEALTH",
                "EDUCATION",
                "WATER SUPPLY",
                "SHOPPING",
                "TRAVELLING",
                "INTERNET & COMMUNICATION",
                "SAVINGS",
                "LOAN REPAYMENT",
                "EXTRA",
                "DONATIONS"
            ]

            for i in self.lst_total:
                b.append(i)

            graph = fig.add_subplot(122)
            graph.barh(a, b)
            graph.grid()

            canv = FigureCanvasTkAgg(fig, master = self.br_grph)
            canv.draw()

            get_widz = canv.get_tk_widget()
            get_widz.pack()

            self.back = Button(self.br_grph, text = "BACK", command = stat)
            self.back.configure(bd = 0, bg = "black", fg = "white", activebackground = "#15350204f",
            font = "arialroundedmtbold", relief = SUNKEN)
            self.back.place(x = 0, y = 0)

        def pie_graphical() :

            '''  The function pie_graphical() is directed from the statt frame. Here using matplotlib and pyplot,
            I have plotted the data in format of pie graph. For this I have used canvas and figure function from
            tkinter and matplotlib respectively. At first I have created a figure and then the data was plotted
            inside the line graph. After that the image was placed inside the canvas and then on main frame of the
            window. In the same way like the line graph & and bar graph. '''

            self.statt.place_forget()

            self.pie_grph = Frame(self.win, bg = "#a89e9e", width = 800, height = 500)
            self.pie_grph.place(x = 0, y = 0)

            fig = Figure(figsize = (8, 5), dpi = 100)
            fig.suptitle("Money Spent")

            b = []
            a = [
                "HOUSE RENT",
                "ELECTRIC BILLS",
                "FOOD",
                "COOKING EMENITIES",
                "HEALTH",
                "EDUCATION",
                "WATER SUPPLY",
                "SHOPPING",
                "TRAVELLING",
                "INTERNET & COMMUNICATION",
                "SAVINGS",
                "LOAN REPAYMENT",
                "EXTRA",
                "DONATIONS"
            ]

            for i in self.lst_total :
                b.append(i)

            graph = fig.add_subplot(111)
            graph.pie(b, labels = a)

            canv = FigureCanvasTkAgg(fig, master = self.pie_grph)
            canv.draw()

            get_widz = canv.get_tk_widget()
            get_widz.pack()

            self.back = Button(self.pie_grph, text = "BACK", command = stat)
            self.back.configure(bd = 0, bg = "black", fg = "white", activebackground = "#15350204f",
            font = "arialroundedmtbold", relief = SUNKEN)
            self.back.place(x = 0, y = 0)

        def database() :

            ''' This function database() once again checks for account verification so that the expenses can be
            stored in the MySql database. If the condition satisfied the it will restore the old data of thar user
            otherwise it will insert the new data of that new user. This thing will make the whole program more
            user-friendly, so there will be no need to remember the old data by user. '''

            user = self.name.get()
            passwd = b64encode(bytes(self.password.get(), "utf-16")).decode()

            self.cur.execute("select * from main where Name = '%s' and Password = '%s'" % (str(user), str(passwd)))
            rud = self.cur.fetchall()

            def inserting() :

                ''' The function inserting() is fully based on the module mysql.connector, because this function
                working on the department of inserting all the data of user starting from Name or username to daily
                expenses and total amount that have spent by user. Here I have extracted the all the data from the
                entry boxes using the syntax <entry>.get() function and put it into different columns of the table
                main main in MySql database. '''

                self.cur = self.db.cursor()
                self.cur.execute("insert into main values"
                                 "("
                                 "'{}', {}, '{}', '{}', '{}', '{}', {}, {}, {}, {}, {},"
                                 " {}, {}, {}, {}, {}, {}, {},{}, {}, {}, {})"
                                 .format
                    (
                    str(self.name.get()),
                                         self.age.get(),
                                         str(self.optnbtn1),
                    b64encode(bytes(self.password.get(), "utf-16")).decode(),
                                         str(self.flag),
                                         str(self.cart),
                                         int(self.salary_1.get()),
                                         int(self.extra_1.get()),
                                         self.entry15.get(),
                                         self.entry16.get(),
                                         self.entry17.get(),
                                         self.entry18.get(),
                                         self.entry19.get(),
                                         self.entry20.get(),
                                         self.entry21.get(),
                                         self.entry22.get(),
                                         self.entry23.get(),
                                         self.entry24.get(),
                                         self.entry25.get(),
                                         self.entry26.get(),
                                         self.entry27.get(),
                                         self.entry28.get()
                                         ))

            if rud :

                print("Welcome")
                inserting()
                self.db.commit()

            else :

                inserting()
                self.db.commit()
                print("Account Created")

            self.cur.close()
            self.db.close()

        def add_income_again() :

            ''' The function add_income_again() is called inside the settings tab Add Income. The function will
            redirect the user the service or business income page. Whenever user will press that button,
            the frame will be replaced by that frame. '''

            self.db = sql.connect(host = "localhost", user = "root", passwd = "123456789", database = "salarymanagement")
            self.cur = self.db.cursor()

            user = self.name.get()
            passwd = b64encode(bytes(self.password.get(), "utf-16")).decode()

            self.cur.execute("select Job from main where Name = '%s' and Password = '%s'" % (str(user), str(passwd)))
            rud = self.cur.fetchall()

            try :

                if rud[-1][0] == "servi" :

                    service()

                elif rud[-1][0] == "busin" :

                    business()

            except IndexError :

                if self.flag == "servi" :

                    service()

                elif self.flag == "busin" :

                    business()

        def account_setting() :

            ''' This function account_setting() is a part of settings where user can change their name as well their
            age too. Here one frame will be slided from left side of the window for settings options. The frame was
            a rectangle of dimension 250 x 500. '''

            self.frame.pack_forget()

            # intt = IntVar()
            varm = IntVar()
            st = StringVar()
            st1 = StringVar()
            self.intt.set(self.age.get())
            st.set(self.name.get())
            st1.set(self.password.get())
            self.constant = True

            self.frame1 = Frame(self.win, bg = "#ccf500", width = 250, height = 500)
            self.frame1.place(x = 0, y = 0)

            name_entry = Entry(self.frame1, textvariable = st)
            age_entry = Entry(self.frame1, textvariable = self.intt)
            password_entry = Entry(self.frame1, textvariable = st1, show = "*")
            name_entry.configure(bd = 1, width = 17)
            age_entry.configure(bd = 1, width = 17)

            def mark_2() :

                ''' The function mark_2() is same as the mark() at top level, used for hiding password in the first
                frame or login page. This function is embedded inside the Checkbutton widget so that if the button is
                checked then the password will bo shown or for any other case it will be replaced by a star(*). '''

                if varm.get() == 1 :

                    password_entry.configure(show = "")
                    check.configure(text = "Hide")

                elif varm.get() == 0 :

                    password_entry.configure(show = "*")
                    check.configure(text = "Show")

            def update_account() :

                ''' The function update_account() will change their name to the new name given by that user. Here I
                am just shifting the values name & age that we are getting from login page to the new name and age
                in the settings section. '''

                self.name = name_entry
                self.age = age_entry
                self.password = password_entry

            btn_name = Button(self.frame1, text = "Change Name", command = update_account)
            btn_age = Button(self.frame1, text = "Change Age", command = update_account)
            btn_password = Button(self.frame1, text = "Change Password", command = update_account)

            check = Checkbutton(self.frame1, text = "Show", command = mark_2, font = "Arial", bd = 0)
            check.configure(onvalue = 1, offvalue = 0, variable = varm, bg = "#ccf500", fg = "white",
                            activebackground = "pink")

            name_entry.place(x = 10, y = 150)
            age_entry.place(x = 10, y = 230)
            password_entry.place(x = 10, y = 310)

            btn_name.place(x = 140, y = 150)
            btn_age.place(x = 140, y = 230)
            btn_password.place(x = 140, y = 310)
            check.place(x = 10, y = 350)

        def account() :

            ''' The function account() is used to create a frame with several options like about, updating
            name & age, quit etc. for users benefits. This will also show your name at the top of the frame. The
            main work of this function is for account settings. '''

            # self.acc.place_forget()
            self.acc.configure(text = "<", command = account_update)
            self.acc.place_configure(x = 250, y = 240)
            # self.goback = Button(self.win, text = "21", command = account_update)
            # self.goback.place(x = 250, y = 240)
            self.frame = Frame(self.win, bg = "#e84f4f", width = 250, height = 500)
            self.frame.pack(side = LEFT)

            lab11 = Label(self.frame, text = "HELLO", font = "Bahnschrift", bd = 0)
            lab11.configure(bg = "#e84f4f", fg = "black")
            lab12  = Label(self.frame, text = self.name.get().capitalize(), font = "agencyfb", bd = 0)
            lab13 = Label(self.frame, text = "-"*50, bd = 0)
            lab13.configure(font = "agencyfb", bg = "#e84f4f", fg = "black")
            lab12.configure(bg = "#e84f4f", fg = "white",font=('Bahnschrift',15))

            lab11.place(x = 100, y = 40)
            lab12.place(x = 100, y = 65)
            lab13.place(x = 0, y = 90)

            def like() :

                ''' The function like() is used for showing the about section of the program. The work of the
                function is to place the about frame. '''

                creator_info = Frame(self.win, width = 600, height = 380)
                creator_info.place(x = 100, y = 60)

                messg_widget = Message(creator_info, text = self.messg, bg = "white", fg = "black")
                messg_widget.place(x = 100, y = 100)

                def destrot() :

                    ''' The function destrot() was used to destroy the about frame. Simply it is used as a cross
                    button which exit a window. '''

                    creator_info.destroy()

                quite = Button(creator_info, text = "X", command = destrot, bd = 0, fg = "red")
                quite.place(x = 570, y = 0)

            accsettings = Button(self.frame, text = "Account Settings", command = account_setting, font = "agencyfb")
            addincome = Button(self.frame, text = "Add Income", font = "agencyfb", command = add_income_again)
            about = Button(self.frame, text = "ABOUT", font = "agencyfb", command = like)
            quit = Button(self.frame, text = "Quit",font = "agencyfb", command = self.win.quit)
            accsettings.configure(bg = "white", fg = "black", bd = 2)
            addincome.configure(bg = "white", fg = "black", bd = 2)
            about.configure(bd = 2, bg = "white", fg = "black")
            quit.configure(bg = "white", fg = "black", bd = 2)

            accsettings.place(x = 70, y = 160)
            addincome.place(x = 70, y = 245)
            about.place(x = 70, y = 330)
            quit.place(x = 70, y = 415)

        def account_update() :

            ''' The function account_update() was just used for the sliding part of the account setting frame. This
            was responsible for the placing and vanishing part of the frame '''

            self.frame.pack_forget()

            if self.constant == True :

                self.frame1.place_forget()
                self.acc.configure(text = ">", command = account)
                self.acc.place_configure(x = 0, y = 240)
                # self.frame.pack_forget()

            # self.frame.place_forget()
            # self.goback.place_forget()
            self.acc.configure(text = ">", command = account)
            self.acc.place_configure(x = 0, y = 240)

        ''' Here all the function day1(), week1() etc. is responsible for storing the date of the period of interval 
        choose by the user. For different conditions it will store different strings in the MySql database. '''

        def day1() :

            self.cart = "Day"
            service()

        def week1() :

            self.cart = "Week"
            service()

        def month1() :

            self.cart = "Month"
            service()

        def day2():

            self.cart = "Day"
            business()

        def week2() :

            self.cart = "Week"
            business()

        def month2() :

            self.cart = "Month"
            business()

        def interval_service() :

            ''' This function interval_service() will create a frame with time of intervals for service sections.
            Every buttons will redirect you to different function specified for this. This is build so that user
            can store their income as per their options. '''

            #self.lab4.place_forget()
            self.service.place_forget()
            self.business.place_forget()

            self.day_1 = Button(self.win, text = "PER DAY", command = day1)
            self.week_1 = Button(self.win, text = "PER WEEK", command = week1)
            self.month_1 = Button(self.win, text  = "PER MONTH", command = month1)

            self.day_1.configure(bg = "white", bd =0 , width = 15, height = 6,font='Bahnschrift',relief= "groove")
            self.week_1.configure(bg = "white", bd = 0, width = 15, height = 6,font='Bahnschrift',relief= "groove")
            self.month_1.configure(bg = "white", bd = 0, width = 15, height = 6,font='Bahnschrift',relief= "groove")

            self.day_1.place(x = 350, y = 50)
            self.week_1.place(x = 350, y = 207)
            self.month_1.place(x = 350, y = 360)

            self.acc = Button(self.win, text = ">", command = account, bd = 0)
            self.acc.place(x = 0, y = 240)

        def interval_business() :

            ''' This function interval_business() will create a frame with time of intervals for business sections.
            Every buttons will redirect you to different function specified for this. This is build so that user
            can store their income as per their options. '''

            #self.lab4.place_forget()
            self.service.place_forget()
            self.business.place_forget()

            self.day_2 = Button(self.win, text = "PER DAY", command = day2)
            self.week_2 = Button(self.win, text = "PER WEEK", command = week2)
            self.month_2 = Button(self.win, text  = "PER MONTH", command = month2)

            self.day_2.configure(bg = "white", bd = 0, width = 15, height = 6,font='Bahnschrift',relief= "groove")
            self.week_2.configure(bg = "white", bd = 0, width = 15, height = 6,font='Bahnschrift',relief= "groove")
            self.month_2.configure(bg = "white", bd = 0, width = 15, height = 6,font='Bahnschrift',relief= "groove")

            self.day_2.place(x = 350, y = 50)
            self.week_2.place(x = 350, y = 207)
            self.month_2.place(x = 350, y =360)

            self.acc = Button(self.win, text = ">", command = account, bd = 0)
            self.acc.place(x = 0, y = 240)

        def afterenter() :

            ''' The function afterenter() is called after the enter button clicked in login page. This function will
            redirect you from login page to the job frame which will allow to select your job type. I have also
            specified a condition that if the entry box of name or username and password is blank then it will stop
            you from entering the job frame.'''

            if self.name.get() != "" and self.password.get() != "" :

                self.home_frame.place_forget()
                self.win.configure(bg = "#6fc8c9")

                #self.lab4 = Label(self.win, text = "/", fg = "red", bg ="dimgrey")
                #self.lab4.place(x = 400, y = 210)

                self.service = Button(self.win, text = "SERVICE", command = interval_service, bd = 2,relief= "groove")
                self.business = Button(self.win, text = "BUSINESS", command = interval_business, bd = 2,relief= "groove")

                self.service.configure(fg = "black", bg = "white", height = 3, width =13)
                self.service.configure(activebackground = "blue", activeforeground = "white")
                self.business.configure(fg = "black", bg = "white", height = 3, width =13)
                self.business.configure(activebackground = "blue", activeforeground = "white")

                self.service.place(x = 290, y  =200)
                self.business.place(x = 430, y = 200)

            else :

                fabu = Label(self.win, text = "Please enter your Name or Password")
                fabu.configure(bg = "#17616E", fg = "#A09995")
                fabu.place(x = 300, y = 360)
                coountdown(4, fabu)

        enter = Button(self.home_frame, text = "Enter", command = afterenter, bg = "#00b1d2")
        enter.configure(fg = "white", bd = 0, height = 2, activebackground = "#2A7888", width = 15, relief = SUNKEN)
        enter.configure(activeforeground = "black", highlightcolor = "pink", font = ("arialroundedmtbold"))
        enter.place(x = 340, y = 310)

if __name__ == "__main__" :

    ''' This thing is just checking that we are outside the class or function, if yes then it will call the 
    respected class startpage() with the parameter window as tkinter window as scripted below. '''

    window = Tk()
    startpage(window)

    window.mainloop()
