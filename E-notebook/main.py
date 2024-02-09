#Modules used 
from tkinter.messagebox import *
import os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw #pip install
from time import sleep
import webbrowser as wb
from datetime import datetime
from pickle import load, dump
from pyautogui import *
from win32api import GetSystemMetrics
from math import *



bg, fg = '#FFE0D0', '#FFA374'

# For login and signup ######
global confirmed_varible
confirmed_varible = False

global log_confirm_varible
log_confirm_varible = False

# For notepad ##############
global open_status_name
open_status_name = False

global selected
selected = False

#############################

font = ('Times new',22,'bold')
font1 = ('Times new roman',18,'bold')
font2 = ('Times new roman',10,'bold')

def log_status():
    global log_confirm_varible
    return log_confirm_varible

def status():
    return confirmed_varible

def signup_screen(bg, fg):
    global confirmed_varible
    def save():
        global confirmed_varible
        name = nam_entry.get()
        name = name.title()
        username = username_entry.get()
        password = password_entry.get()
        confirmpassword = confirm_password_entry.get()

        email = email_entry.get()
        email = email.replace(' ','')
        email = email.lower()
        class_ = class_entry.get()
        
        subjects = []
        if english_var.get()==1:
            subjects.append('English')
        if hindi_var.get() ==1:
            subjects.append('Hindi')
        if cs_var.get() == 1:
            subjects.append('Computer Science')
        if ip_var.get() == 1:
            subjects.append('Informatics and Practises')
        if phy_var.get()==1:
            subjects.append('Physics')
        if chem_var.get() ==1:
            subjects.append('Chemistry')
        if busi_var.get() == 1:
            subjects.append('Business Studies')
        if accounts_var.get() ==1:
            subjects.append('Accountancy')
        if maths_var.get() == 1:
            subjects.append('Mathematics')
        if bio_var.get() ==1:
            subjects.append('Biology')
        if his_var.get() == 1:
            subjects.append('History')
        if geo_var.get()==1:
            subjects.append('Geography')
        if eco_var.get() ==1:
            subjects.append('Economics')
        if pol_sc_var.get() ==1:
            subjects.append('Political Science')
        
        else:
            pass   

        error = False # a flag variable

        ########### Conditions for a sucessful profile #############
        '''1. Checking if any entry is missing
        2. if email address is valid
        3. if password and confirm password are the same
        4. if there is atleast one subject
        5. if the given class is a valid one
        '''
        if len(name)==0 or len(class_)==0 or len(email) == 0:
            error = True
        if '@' not in email:
            error = True
        if confirmpassword != password:
            error = True
        
        # if len(subjects)==0:
        #     error = True
        if int(class_)>12:
            error = True



        if error:
            showerror('Error','Please Fill all the details correctly')
            nam_entry.delete(0,END)
            class_entry.delete(0,END)
            email_entry.delete(0,END)
            username_entry.delete(0,END)
            password_entry.delete(0,END)
            confirm_password_entry.delete(0,END)


        elif not error:
            path = f'{name}/Class {class_}'
            new_data = name, username, password, email, class_, subjects, path
            with open('profiles.dat','ab+') as file:
                for i in range(len(subjects)):
                    os.makedirs(f'{path}/{subjects[i]}/cw')
                    os.makedirs(f'{path}/{subjects[i]}/hw')

                dump(new_data, file)
                confirmed_varible = True
                sign_screen.destroy()
                return



    
    global open_status_name
    open_status_name = False

    global selected
    selected = False

    global confirmed_varible
    confirmed_varible = False

    global log_confirm_varible
    log_confirm_varible = False

    font = ('Playfair Dislplay',22,'bold')
    font1 = ('Times new roman',18,'bold')
    font2 = ('Times new roman',10,'bold')

    xx1 = GetSystemMetrics(0)
    yy1 = GetSystemMetrics(1)

    bg, fg =  '#FFE0D0', '#F86318'

    def sx1(num):
        ratio = num * xx1
        ratio = round(ratio/1280)
        return(ratio)

    def sy1(num):
        ratio = num * yy1
        ratio = round(ratio/720)
        return(ratio)

    def image_resize1(image_name, num = 'none'):
        if num == 'none':
            screen_w = GetSystemMetrics(0)
            screen_h = GetSystemMetrics(1)
        else:
            screen_w = sx1(num[0])
            screen_h = sy1(num[1])
        image = Image.open(image_name)
        # The (screen_h, screen_w) is (height, width)
        image_x = image.resize((screen_w, screen_h), Image.ANTIALIAS)
        return image_x

    # Main screen ###################################
    sign_screen = Tk()
    sign_screen.state('zoomed')
    sign_screen.title('Sign up Screen')
    sign_screen.config(bg=bg)

    ##########################################################

    ################ Screen width and height #################
    sign_x, sing_y = GetSystemMetrics(0), GetSystemMetrics(1)

    ##########################################################
    canvas = Canvas(sign_screen, width =sign_x // 2, height = sing_y)
    canvas.pack(fill = 'both', expand = True)

    img = ImageTk.PhotoImage(image_resize1('images/signupbg.png'))
    canvas.create_image(0, 0, anchor = 'nw',image=img)




    nam_entry = Entry(sign_screen,text ='', width = 20, font=font1, relief = FLAT)
    canvas.create_window(sx1(420), sy1(238), window = nam_entry)



    email_entry = Entry(sign_screen, text='',font=font1,  relief = FLAT, width = 23)
    canvas.create_window(sx1(445), sy1(312), window = email_entry)

    ############ Other details #######################


    username_entry = Entry(sign_screen, text='', width = 20, font=font1, relief = FLAT)
    canvas.create_window(sx1(420), sy1(419), window = username_entry)



    password_entry = Entry(sign_screen, text='', width = 20, font=font1, relief = FLAT, show ='*')
    canvas.create_window(sx1(421), sy1(485), window = password_entry)



    confirm_password_entry = Entry(sign_screen, text='', width = 20, font=font1, relief = FLAT, show ='*')
    canvas.create_window(sx1(421), sy1(545), window = confirm_password_entry)




    ############ Academic details ####################


    class_entry = Entry(sign_screen,text='', width= 2,font=font1, relief = FLAT)
    canvas.create_window(sx1(1059), sy1(237), window = class_entry)




    english_var, hindi_var, pol_sc_var, cs_var, ip_var, phy_var, chem_var, maths_var, bio_var, his_var, geo_var, eco_var, busi_var, accounts_var = IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()

    eng_entry = Checkbutton(sign_screen, text="English", bg = bg, fg = fg, relief = FLAT,font=font1, variable=english_var)
    canvas.create_window(sx1(700), sy1(305), window = eng_entry, anchor = 'nw')

    hin_entry = Checkbutton(sign_screen, text="Hindi", font=font1, bg = bg, fg = fg, variable=hindi_var)
    canvas.create_window(sx1(930), sy1(305), window = hin_entry, anchor = 'nw')

    cs_entry = Checkbutton(sign_screen, text="Computer Science", bg = bg, fg = fg, font=font1, variable=cs_var)
    canvas.create_window(sx1(700), sy1(344), window = cs_entry, anchor = 'nw')

    ip_entry = Checkbutton(sign_screen, text="Informatics Practises", bg = bg, fg = fg, font=font1, variable=ip_var)
    canvas.create_window(sx1(930), sy1(344), window = ip_entry, anchor = 'nw')

    phy_entry = Checkbutton(sign_screen, text="Physics", font=font1, bg = bg, fg = fg, variable=phy_var)
    canvas.create_window(sx1(700), sy1(383), window = phy_entry, anchor = 'nw')

    chem_entry = Checkbutton(sign_screen, text="Chemistry", font=font1, bg = bg, fg = fg, variable=chem_var)
    canvas.create_window(sx1(930), sy1(383), window = chem_entry, anchor = 'nw')

    math_entry = Checkbutton(sign_screen, text="Maths", font=font1, bg = bg, fg = fg, variable=maths_var)
    canvas.create_window(sx1(700), sy1(422), window = math_entry, anchor = 'nw')

    bio_entry = Checkbutton(sign_screen, text="Biology", font=font1, bg = bg, fg = fg, variable=bio_var)
    canvas.create_window(sx1(930), sy1(422), window = bio_entry, anchor = 'nw')

    his_entry = Checkbutton(sign_screen, text="History", font=font1, bg = bg, fg = fg, variable=his_var)
    canvas.create_window(sx1(700), sy1(461), window = his_entry, anchor = 'nw')

    geo_entry = Checkbutton(sign_screen, text="Geography", font=font1, bg = bg, fg = fg, variable=geo_var)
    canvas.create_window(sx1(930), sy1(461), window = geo_entry, anchor = 'nw')

    pol_entry = Checkbutton(sign_screen, text="Political Science", font=font1,bg = bg, fg = fg,  variable=pol_sc_var)
    canvas.create_window(sx1(700), sy1(500), window = pol_entry, anchor = 'nw')

    eco_entry = Checkbutton(sign_screen, text="Economics", font=font1, bg = bg, fg = fg, variable=eco_var)
    canvas.create_window(sx1(930), sy1(500), window = eco_entry, anchor = 'nw')

    busi_entry = Checkbutton(sign_screen, text="Business Studies", font=font1,bg = bg, fg = fg,  variable=busi_var)
    canvas.create_window(sx1(700), sy1(539), window = busi_entry, anchor = 'nw')

    accounts_entry = Checkbutton(sign_screen, text="Accountancy", font=font1, bg = bg, fg = fg, variable=accounts_var)
    canvas.create_window(sx1(930), sy1(539), window = accounts_entry, anchor = 'nw')

    sub_btn_img = ImageTk.PhotoImage(image_resize1('images\\submitbutton.png',(140,35)))
    sub_btn = Button(sign_screen, relief = FLAT,image = sub_btn_img, bg = bg, fg = fg, activebackground = '#FADFD1', command = save)
    canvas.create_window(sx1(1160), sy1(600), window = sub_btn, anchor = 'n')

    sign_screen.mainloop()

def login_screen(bg, fg):
    global log_confirm_varible


    def login():
        global log_confirm_varible

        with open('profiles.dat', 'rb') as file:
            try:
                while True:
                    record = load(file)
            except EOFError:
                req_username, req_password = record[1], record[2]
        given_username = name_entry.get()
        given_password = pass_entry.get()
        
        error = False
        if len(given_username)==0 or len(given_password)==0:
            error = True
        elif given_username != req_username or given_password!= req_password:
            error = True
        
        if error:
            showerror('Error','Username or Password is incorrect')
            name_entry.delete(0,END)
            pass_entry.delete(0,END)
        else:
            # showinfo('Log in sucess', f'Welcome {req_username}')
            log_confirm_varible = True
            log_screen.destroy()
            return

    def sx2(num):
        ratio = num * working_x
        ratio = round(ratio/980)
        return(ratio)

    def sy2(num):
        ratio = num * y2
        ratio = round(ratio/1080)
        return(ratio)
    log_screen = Tk()
    x2 =GetSystemMetrics(0)
    y2 =GetSystemMetrics(1)
    working_x = x2//2
    # log_screen.state('zoomed')
    log_screen.geometry(f'{int(x2)//2}x{y2}+{int(x2)//2}+0')
    log_screen.title('Login screen')
    log_screen.config(bg=bg)
    x = log_screen.winfo_screenwidth()
    y = log_screen.winfo_screenheight()
    

    frame = Frame(log_screen, highlightbackground = fg, highlightthickness = sx2(20), bg = bg)
    frame.pack(fill = 'both', expand = True)

    divider3 = Label(frame, text =' ',font = ('times new roman', sx2(60)), bg = fg)
    divider3.place(x=sx2(0), y= sy2(0), relwidth=1)

    # Homepage Label
    lbl = Label(frame, text = "LOGIN PAGE", font = ('Abadi MT Condensed Extra Bold',40),bg = bg, fg= fg)
    lbl.pack(side = TOP, pady = sy2(30))

    # Frame 2

    framex = Frame(frame)
    framex.pack( pady = sy2(20))

    frame2 = Frame(frame)
    frame2.pack( pady = sy2(15))

    # name label 
    name_label = Label(frame2, text="username".title(),bg = bg, fg = fg, font = font1)
    name_label.pack(side = LEFT, pady = 0)
    name_entry = Entry(frame2,width = sx2(20),font = font1 )
    name_entry.pack(side = LEFT, pady = 0)

    # Frame 3

    frame3 = Frame(frame)
    frame3.pack( pady = 15)

    pass_label = Label(frame3, text="password".title(),bg = bg, fg = fg, font = font1)
    pass_entry = Entry(frame3, text='',width = 20,font = font1, show='*' )
    pass_label.pack(side = LEFT, pady = 0)
    pass_entry.pack(side = LEFT, pady = 0)

    l_in_btn = Button(frame,text= "Log In", bg = fg, fg = bg, font=("Helvettica",sy2(20)), command = login)
    l_in_btn.pack(side = TOP, pady = sy2(20), ipady = sy2(10))
    
    divider3 = Label(frame, text =' ',font = ('times new roman', 60), bg = fg)
    divider3.place(x=0, y= sy2(y-60), relwidth=1, anchor = 'sw')
    divider3 = Label(frame, text =' ',font = ('times new roman', 60), bg = fg)
    divider3.place(x=0, y= sy2(y), relwidth=1, anchor = 'sw')

    log_screen.mainloop()

def homepage():
    def sx3(num):
        xx = GetSystemMetrics(0)
        working_x = xx//2
        ratio = num * working_x
        ratio = round(ratio/980)
        return(ratio)

    def sy3(num):
        yy = GetSystemMetrics(1)
        ratio = num * yy
        ratio = round(ratio/1080)
        return(ratio)
    


    def browser():
        wb.open('https://www.google.com')
        sleep(4)
        hotkey('win','left')
        sleep(1)
        press('enter')
    
    def calculator():
        def scientific_calc(): 
            textField.config(width = 30)
            sc_btn.place_forget()
            bc_btn.place(x = 4,y = 4)
            nullbtn.grid(row=0,column=0,padx=sx3(2),pady=sy3(2))
            pibtn.grid(row=0,column=1,padx=sx3(2),pady=sy3(2))
            sqrtbtn.grid(row=0,column=2,padx=sx3(2),pady=sy3(2))
            ebtn.grid(row=1,column=0,padx=sx3(2),pady=sy3(2))
            exbtn.grid(row=1,column=1,padx=sx3(2),pady=sy3(2))
            modbtn.grid(row=1,column=2,padx=sx3(2),pady=sy3(2))
            xybtn.grid(row=2,column=0,padx=sx3(2),pady=sy3(2))
            factbtn.grid(row=2,column=1,padx=sx3(2),pady=sy3(2))
            recbtn.grid(row=2,column=2,padx=sx3(2),pady=sy3(2))
            sinbtn.grid(row=3,column=0,padx=sx3(2),pady=sy3(2))
            cosbtn.grid(row=3,column=1,padx=sx3(2),pady=sy3(2))
            tanbtn.grid(row=3,column=2,padx=sx3(2),pady=sy3(2))
            plusminusbtn.grid(row=4,column=0,padx=sx3(2),pady=sy3(2))
            lnbtn.grid(row=4,column=1,padx=sx3(2),pady=sy3(2))
            log_btn.grid(row=4,column=2,padx=sx3(2),pady=sy3(2))
        def normal_calc():
            textField.config(width = 17)
            bc_btn.place_forget()
            sc_btn.place(x = 4, y= 4)
            nullbtn.grid_forget()
            pibtn.grid_forget()
            sqrtbtn.grid_forget()
            ebtn.grid_forget()
            exbtn.grid_forget()
            modbtn.grid_forget()
            xybtn.grid_forget()
            factbtn.grid_forget()
            recbtn.grid_forget()
            sinbtn.grid_forget()
            cosbtn.grid_forget()
            tanbtn.grid_forget()
            plusminusbtn.grid_forget()
            lnbtn.grid_forget()
            log_btn.grid_forget()
        def active_(event):
            b=event.widget
            b['background']='#ddc5a0'
        def deactive_(event):
            b=event.widget
            b['background']='#F4DCB7'
        def allclear():
            textField.delete(0,END)
        def clear(e):
            ex=textField.get()
            ex=ex[:-1:]
            textField.delete(0,END)
            textField.insert(0,ex)     
        def result(text):
            num = [str(k) for k in range(0,10)]
            op_ = ['+','-','÷','x']
            sp_ = [')', 'π', 'e','.']
            text = text.replace('x','*')
            text = text.replace('÷','/')
            text = text.replace('^','**')
            text = text.replace('π','pi')
            text = text.replace('√(','sqrt(')
            text= text.replace('ln(','log(')
            text = text.replace('log( ', 'log10(')
            if '!' in text:
                string = ''
                for i in range(text.index('!')):
                    if text[i] in num:
                        string+=text[i]
                    elif text[i] in op_ or i in sp_:
                        string=''
                text = text.replace(string+'!',f'factorial({string})')
            if 'sin(' in text :
                a1 = text.index('sin(')+4
                num_ = ''
                bo = 1
                bc = 0
                while bo>bc:
                    if text[a1]=='(':
                        bo+=1
                        num_+='('
                    elif text[a1]==')':
                        bc+=1
                        if num_.count('(')>num_.count(')'):
                            num_+=')'
                    elif text[a1] in num:
                        num_+=text[a1]
                    a1+=1
                text=text.replace(num_,f'radians({num_})')          
            if 'cos(' in text :
                a1 = text.index('cos(')+4
                num_ = ''
                bo = 1
                bc = 0
                while bo>bc:
                    if text[a1]=='(':
                        bo+=1
                        num_+='('
                    elif text[a1]==')':
                        bc+=1
                        if num_.count('(')>num_.count(')'):
                            num_+=')'
                    elif text[a1] in num:
                        num_+=text[a1]
                    a1+=1
                text=text.replace(num_,f'radians({num_})')     
            if 'tan(' in text :
                a1 = text.index('tan(')+4
                num_ = ''
                bo = 1
                bc = 0
                while bo>bc:
                    if text[a1]=='(':
                        bo+=1
                        num_+='('
                    elif text[a1]==')':
                        bc+=1
                        if num_.count('(')>num_.count(')'):
                            num_+=')'
                    elif text[a1] in num:
                        num_+=text[a1]
                    a1+=1
                # text.replace(num_,f'radians({num_})')
                ban = ['90','270', '90.0', '270.0']
                if eval(num_) in ban:
                    textField.delete(0,END)
                    showerror('Error', 'Unsupported Calculation')
                else:
                    text=text.replace(num_,f'radians({num_})')
            while text.count('(')> text.count(')'):
                text= text+')'
            textField.delete(0,END)
            res = str(round(float(eval(text)),10))
            if res[-1]=='0' and res[-2]=='.':
                res = res[:-2]
            textField.insert(END,res)
        def click_button_function(event):
            b=event.widget
            text=b['text']
            ex = textField.get() 
            num = [str(k) for k in range(0,10)]
            op_ = ['+','-','÷','x']
            sp_ = [')', 'π', 'e','.']
            if text in num:
                ex=textField.get()
                if len(ex)==0 and text!='0':
                    textField.insert(END, str(text))
                elif len(ex)>0:
                    if ex[-1] in sp_:
                        if ex[-1]=='.':
                            textField.insert(END,str(text))
                        else:
                            textField.insert(END,"x"+str(text))
                    else:
                        textField.insert(END, str(text))
            elif text in op_:
                if len(ex)==0:
                    pass
                elif ex[-1] in op_:
                    clear(e)
                    textField.insert(END, text)
                else:
                    textField.insert(END, text)
            elif text=="+/-":
                if len(ex)==0:
                    textField.insert(0,"(-")
                elif ex[-1] in num or ex[-1]=='.':
                    
                    textField.insert(0,"(-")
                elif ex[-1] in op_:
                    textField.insert(END,"(-")
                elif ex[-1] in sp_:
                    textField.insert(END,"x(-")
            elif text=="(":
                ex=ex=textField.get()
                if len(ex)==0:
                    textField.insert(END,"(")
                    return # forcefully ending the function
                else:
                    if ex[-1] in num:
                        textField.insert(END,"(")
                    elif ex[-1] in sp_:
                        textField.insert(END,"x(")
                    elif ex[-1] in op_:
                        textField.insert(END,'(')
                    return
            elif text ==')':
                if len(ex) == 0:
                    showerror('Error', 'Invalid Format')
                    return
                else:
                    if ex[-1] =='(':
                        showerror('Error', 'Invalid Format')
                        return
                    elif len(ex)>0 and '(' in ex and ex.count('(')>ex.count(')'):
                        textField.insert(END,')')
                        return        
                    elif ex[-1] in op_:
                        showerror('Error', 'Invalid Format')
                        return
            elif text==".":
                if len(ex)==0:
                    textField.insert(END,'0.')
                elif ex[-1] in num:
                    textField.insert(END,".")
                elif '.' in ex:
                    txt_ = ex[ex.index('.')::]
                    opx = False
                    for i in txt_:
                        if i in op_:
                            opx = True
                            break
                    if opx :
                        if ex[-1] in num:
                            textField.insert(END,'.')
                        elif ex[-1] in op_ or ex[-1] =='(':
                            textField.insert(END, '0.')
                        elif ex[-1] in sp_:
                            textField.insert(END, 'x0.')
                    else:
                        showerror('Error', "Invalid Format")
                elif ex[-1] in op_:
                    textField.insert(END, '0.')
                elif ex[-1]=='(':
                    textField.insert(END, '0.')
                elif ex[-1] in sp_:
                    textField.insert(END, 'x0.')
                else:
                    showerror('Error', "Invalid format")
            elif text=="√":
                if len(ex)==0:
                    textField.insert(END,'√(')
                elif ex[-1] in num or ex[-1] in sp_:
                    textField.insert(END,"x√(")
                elif ex[-1] in op_:
                    textField.insert(END, '√(')
                elif ex[-1]=='(':
                    textField.insert(END,'√(')
                else:
                    showerror('Error','Invalid Format')
            elif text=='π':
                if len(ex)==0:
                    textField.insert(END,'π')
                elif len(ex)>0 and ex[-1] in sp_:
                    textField.insert(END,'xπ')
                else:
                    textField.insert(END,'π')
            elif text == 'log': # log to base 10
                if len(ex)==0:
                    textField.insert(END, 'log( ')
                elif ex[-1] in num or ex[-1]==')':
                    textField.insert(END, 'xlog( ')
                elif ex[-1] in op_:
                    textField.insert(END, 'log( ')
                else:
                    showerror('Error', 'Invalid Format') 
            elif text == "ln": # log to the base e
                if len(ex)==0:
                    textField.insert(END, 'ln(')
                elif ex[-1] in num or ex[-1] in sp_:
                    textField.insert(END, 'xln(')
                elif ex[-1] in op_:
                    textField.insert(END, 'ln(')
                else:
                    showerror('Error', 'Invalid Format')
            elif text=='sin':
                if len(ex)==0:
                    textField.insert(END,"sin(")
                elif ex[-1] in num :
                    textField.insert(END,"xsin(")
                elif ex[-1] in sp_:
                    textField.insert(END,"xsin(")
                else:
                    textField.insert(END,"sin(")           
            elif text=='cos':
                if len(ex)==0:
                    textField.insert(END,"cos(")
                elif ex[-1] in num :
                    textField.insert(END,"xcos(")
                elif ex[-1] in sp_:
                    textField.insert(END,"xcos(")
                else:
                    textField.insert(END,"cos(")
            elif text=='tan':
                if len(ex)==0:
                    textField.insert(END,"tan(")
                elif ex[-1] in num :
                    textField.insert(END,"xtan(")
                elif ex[-1] in sp_:
                    textField.insert(END,"xtan(")
                else:
                    textField.insert(END,"tan(")         
            elif text=='e':
                if len(ex)==0:
                    textField.insert(END,'e')
                elif ex[-1] in num or ex[-1] in sp_:
                    textField.insert(END,"xe")
                else:
                    textField.insert(END,"e")
            elif text=='1/x':
                if len(ex)==0:
                    textField.insert(END,"1÷(")
                elif ex[-1] in op_:
                    textField.insert(END,"1÷(")
                else:
                    textField.insert(END,"x1÷(")
            elif text=='!':
                if len(ex) ==0:
                    showerror('Error', 'invalid format')
                    return
                elif ex[-1] in op_:
                    showerror('Error', 'invalid format')
                    return
                elif ex[-1] in sp_:
                    showerror('Error', 'invalid format')
                    return
                else:
                    textField.insert(END,"!")
            elif text == '|x|':
                if len(ex)==0:
                    textField.insert(END, 'abs(')
                elif ex[-1] in num or ex[-1] in sp_:
                    textField.insert(END, 'xabs(')
                else:
                    textField.insert(END, 'abs(')       
            elif text =="x^y": 
                if len(ex)>0:
                    if ex[-1] in num or ex[-1] in sp_:
                        textField.insert(END,'^(')
                else:
                    showerror('Error', 'Invalid format')
                    return # to end the funciton
            elif text =="e^x":          
                if len(ex)==0:
                    textField.insert(END,"e^(")
                    return
                elif len(ex)>0:
                    if ex[-1] in op_ or ex[-1]=='(':
                        textField.insert(END,"e^(")
                        return
                    else:
                        textField.insert(END,"xe^(")
                        return
            elif text=="=":
                text4 = str(textField.get())
                result(text4)
            else:
                textField.insert(END,text)

        # obtaining the height and width of the computer
        xx = GetSystemMetrics(0)
        yy = GetSystemMetrics(1)

        # important variables
        font=('Arial',19,"bold")
        ################################

        screen= Toplevel()
        screen.title("ABHRANEEL'S Calculator")
        
        screen.geometry(f'{xx//2}x{yy}+{xx//2}+0')
        screen.config(bg = '#ffffff')
        
        bg_btn='#F4DCB7'
        fg_btn = '#1f1510'
        relief_btn = 'flat'
        
        window= Frame(screen,bg="#ffa374", highlightbackground='#000000' , highlightthickness=5)
        window.place(x= int(xx//4), y= 40, anchor='n')

        text2 = ''' √  π 
e  = '''
        text3 = ''' +    
   ÷ '''

        sc_btn = Button(window, text = text2,font =('Arial', 14,'bold'), relief= relief_btn, bg = bg_btn, fg = fg_btn,activebackground = 'orange',width = 4, height = 2, command=scientific_calc)
        sc_btn.place(x = sx3(4),y = sy3(4))
        

        bc_btn = Button(window, text = text3,font =('Arial', 14,'bold'), relief= relief_btn, bg = bg_btn, fg = fg_btn,activebackground = 'orange',width = 4, height = 2, command=normal_calc)

        sc_btn.bind('<Enter>', active_)
        sc_btn.bind('<Leave>', deactive_)
        bc_btn.bind('<Enter>', active_)
        bc_btn.bind('<Leave>', deactive_)
        

        heading = Label(window, text="Calculator", font= font,bg ="#ffa374", fg=fg_btn)
        heading.pack(side = TOP, pady = sy3(15))



        textField= Entry(window,font=('Arial',23,"bold"),justify=RIGHT,width = sx3(17),bg='#EBE4D9')
        textField.pack(side = TOP, padx= sx3(5), pady=sy3(10), ipady = sy3(10))

        ###################################################################################################################
        ###################################################################################################################

        #button frame

        buttonFrame= Frame(window,bg="#ffa374")
        buttonFrame.pack(side =TOP, padx=0 , pady=0)

        #buttons

        # numbers
        btn1 = Button(buttonFrame, text='1',font=font, relief="flat",bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=4,height=2)
        btn1.grid(row=3,column=3,padx=sx3(2),pady=sy3(2))
        

        
        btn2 = Button(buttonFrame, text='2',font=font, relief="flat",bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=4,height=2)
        btn2.grid(row=3,column=4,padx=sx3(2),pady=sy3(2))


        
        btn3 = Button(buttonFrame, text='3',font=font, relief="flat",bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=4,height=2)
        btn3.grid(row=3,column=5,padx=sx3(2),pady=sy3(2))


        
        btn4 = Button(buttonFrame, text='4',font=font, relief="flat",bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=4,height=2)
        btn4.grid(row=2,column=3,padx=sx3(2),pady=sy3(2))


        
        btn5 = Button(buttonFrame, text='5',font=font, relief="flat",bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=4,height=2)
        btn5.grid(row=2,column=4,padx=sx3(2),pady=sy3(2))


        
        btn6 = Button(buttonFrame, text='6',font=font, relief="flat",bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=4,height=2)
        btn6.grid(row=2,column=5,padx=sx3(2),pady=sy3(2))


        
        btn7 = Button(buttonFrame, text='7',font=font, relief="flat",bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=4,height=2)
        btn7.grid(row=1,column=3,padx=sx3(2),pady=sy3(2))


        
        btn8 = Button(buttonFrame, text='8',font=font, relief="flat",bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=4,height=2)
        btn8.grid(row=1,column=4,padx=sx3(2),pady=sy3(2))


        
        btn9 = Button(buttonFrame, text='9',font=font, relief="flat",bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=4,height=2)
        btn9.grid(row=1,column=5,padx=sx3(2),pady=sy3(2))

        ###################################################################################################################
        ###################################################################################################################
        

        zerobtn=Button(buttonFrame, text="0",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=4,height=2)
        zerobtn.grid(row=4,column=4,padx=sx3(2),pady=sy3(2))
        
        dotbtn=Button(buttonFrame, text=".",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))
        dotbtn.grid(row=4,column=5,padx=sx3(2),pady=sy3(2))

        equalbtn=Button(buttonFrame, text="=",font=font, relief=relief_btn,bg=bg_btn,fg = fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))
        equalbtn.grid(row=4,column=6,padx=sx3(2),pady=sy3(2))

        addbtn=Button(buttonFrame, text="+",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))
        addbtn.grid(row=3,column=6,padx=sx3(2),pady=sy3(2))

        subbtn=Button(buttonFrame, text="-",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))
        subbtn.grid(row=2,column=6,padx=sx3(2),pady=sy3(2))

        mulbtn=Button(buttonFrame, text="x",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))
        mulbtn.grid(row=1,column=6,padx=sx3(2),pady=sy3(2))

        divbtn=Button(buttonFrame, text="÷",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))
        divbtn.grid(row=0,column=6,padx=sx3(2),pady=sy3(2))

        clearbtn=Button(buttonFrame, text='←',font=font, relief=relief_btn,activebackground= "Orange",bg=bg_btn, fg = fg_btn,activeforeground="white",width=sx3(4),height=sy3(2))
        clearbtn.grid(row=0,column=5,padx=sx3(2),pady=sy3(2))

        paranthesis1btn=Button(buttonFrame, text="(",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))
        paranthesis1btn.grid(row=0,column=3,padx=sx3(2),pady=sy3(2))

        paranthesis2btn=Button(buttonFrame, text=")",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))
        paranthesis2btn.grid(row=0,column=4,padx=sx3(2),pady=sy3(2))

        allclearbtn=Button(buttonFrame, text="AC",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2),command=allclear)
        allclearbtn.grid(row=4,column=3,padx=sx3(2),pady=sy3(2))

        #######################################################################################################
        #######################################################################################################

        nullbtn=Button(buttonFrame, text="--",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))
    

        pibtn=Button(buttonFrame, text="π",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))


        
        sqrtbtn=Button(buttonFrame, text="√",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))


        ebtn=Button(buttonFrame, text="e",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))


        exbtn=Button(buttonFrame, text="e^x",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))


        modbtn=Button(buttonFrame, text="|x|",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))

        xybtn=Button(buttonFrame, text="x^y",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))

        factbtn=Button(buttonFrame, text="!",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))

        recbtn=Button(buttonFrame, text="1/x",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))

        sinbtn=Button(buttonFrame, text="sin",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))

        cosbtn=Button(buttonFrame, text="cos",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))

        tanbtn=Button(buttonFrame, text="tan",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))

        plusminusbtn=Button(buttonFrame, text="+/-",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))
        lnbtn=Button(buttonFrame, text="ln",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))


        log_btn=Button(buttonFrame, text="log",font=font, relief=relief_btn,bg=bg_btn,fg=fg_btn,activebackground= "Orange", activeforeground="white",width=sx3(4),height=sy3(2))


        btn_list = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, addbtn,subbtn,mulbtn,divbtn,zerobtn,dotbtn,equalbtn,paranthesis1btn,paranthesis2btn, pibtn, sqrtbtn, log_btn, ebtn, lnbtn,allclearbtn, modbtn, xybtn, factbtn, exbtn, recbtn, sinbtn, cosbtn,
        tanbtn, plusminusbtn]

        nullbtn.bind('<Enter>', active_)
        nullbtn.bind('<Leave>', deactive_)

        clearbtn.bind('<Button-1>', clear)
        clearbtn.bind('<Enter>', active_)
        clearbtn.bind('<Leave>', deactive_)


        for i in btn_list:
            i.bind('<Enter>', active_)
            i.bind('<Leave>', deactive_)
            i.bind('<Button-1>',click_button_function)
        
        window.mainloop()
    
    def notepad():
        def new_file():
                # delete previous text
                my_text.delete('1.0', END)
                # update status bar
                root.title('New File - TextPad!')
                status_bar.config(text = "New File        ")

                global open_status_name
                open_status_name = False



            # Open files function
        def open_file():
            # delete previous text
            my_text.delete('1.0', END)

            # grab file name
            inintial_directory = 'D:\\python codes\\cs project class 12\\'
            text_file = filedialog.askopenfilename(initialdir = inintial_directory, title = 'Open File', filetypes = (("Text Files", "*.txt"), ('HTML Files', '*.html'), ('Python Files', "*.py"), ("All Files", '*.*')))
            try:
                # check to see if there is a file name
                if text_file:
                    # Make file name global so we can access the name throughout the program
                    global open_status_name
                    open_status_name = text_file
                # update status bar
                name = text_file
                
                name = name[len(inintial_directory):]
                status_bar.config(text = name)
                
                root.title(f'{name} -TextPad!')

                # open the file

                text_file = open(text_file, 'r')
                stuff = text_file.read()

                # Add file to textbox
                my_text.insert(END, stuff)

                #closing the opened file
                text_file.close()
            except:
                pass



        # Save as function
        def save_as():
            sub = var.get()
            get2 = var2.get()
            path = record[-1][6]
            work = get2
            main_path = os.getcwd()
            initial_directory = main_path+'\\'+path+'\\'+sub+'\\'+work
            now = datetime.datetime.now()
            name = now.strftime("%m-%d-%Y %H-%M-%S")
            file_name = f'{sub} - {work} - {name}'
            root.clipboard_append(file_name)

            text_file = filedialog.asksaveasfilename(defaultextension = '.*', initialdir= initial_directory, title = 'Save File', filetypes = (('Text Files', '*.txt'),("All Files", '*.*'), ('HTML Files','*.html'),('Python Files','*.py')))

            if text_file:
                # Update stauts bar
                name = text_file
                status_bar.config(text = f'Saved -{name}')
                name = name[len(initial_directory):]
                root.title(f'{name} -TextPad!')

                # Save the file
                text_file = open(text_file,'w')
                text_file.write(my_text.get(1.0,END))

                # Close the file
                text_file.close()



        # Save fundtion
        def save_file():

            global open_status_name
            if open_status_name:
                # Save the file
                text_file = open(open_status_name,'w')
                text_file.write(my_text.get(1.0,END))

                # Close the file
                text_file.close()
                status_bar.config(text = f'Saved: {open_status_name}        ')
            else:
                save_as()


        # Cut funciton
        def cut_file(e):
            global selected
            # check to see if used keyboard shortcut
            if e:
                selected = root.clipboard_get()

            if my_text.selection_get():

                # Grab selected text from textbox
                selected = my_text.selection_get()
                # delete selected text from text box
                my_text.delete('sel.first','sel.last')
                root.clipboard_clear()
                root.clipboard_append(selected)



        # Copy function
        def copy_file(e):
            global selected

            # check to see if used keyboard shortcut
            if e:
                selected = root.clipboard_get()
            if my_text.selection_get():
                # grab the selected text from textbox
                selected = my_text.selection_get()
                root.clipboard_clear()



        # Paste function
        def paste_file(e):
            global selected
            # check to see if used keyboard shortcut
            if e:
                selected = root.clipboard_get()
            else:
                if selected:
                    position = my_text.index(INSERT)
                    my_text.insert(position, selected)

            # Getting all the selected subjects


            

        x2 =GetSystemMetrics(0)
        y2 =GetSystemMetrics(1)


        root = Toplevel()
        root.title('Notes'.upper())
        root.geometry(f'{x2//2}x{y2}+{x2//2}+0')
        root.config(bg = '#b8cef2')

        bg = '#b8cef2'

        # Creating a save button for user comfort

        with open('profiles.dat','rb') as file:
            record = []
            try:
                while True :
                    records = load(file)
                    record.append(records)
            except EOFError:
                subject = record[-1][5]

        frame = Frame(root, bg = bg)
        frame.pack(fill=X, ipady = 0)

        lbl = Label(frame, text = 'Choose the subject', bg = bg, font = ('Poppins',20), fg = 'Blue')
        lbl.pack(side = LEFT, padx = 5)
        var = StringVar()
        var.set(subject[0])
        drop = OptionMenu(frame, var, *subject)
        drop.pack(side = LEFT, padx = 10)

        var2 = StringVar()
        work_ = ['cw','hw']
        var2.set(work_[0])
        drop2 = OptionMenu(frame, var2, *work_)
        drop2.pack(side = LEFT, padx = 5)

        save_btn = Button(frame, text = 'Save', font = ('Helvetica', 12), bg = 'sky blue',command = save_file)
        save_btn.pack(side = RIGHT , ipadx = 0, padx = 1.5)

        # Create main fram
        my_frame = Frame(root)
        my_frame.pack(pady = 5)


        #Create a scroll Bar

        text_scroll = Scrollbar(my_frame)
        text_scroll.pack(side = RIGHT, fill = Y)

        # Horizontal scroll bar


        hor_scroll = Scrollbar(my_frame, orient = 'horizontal')
        hor_scroll.pack(side = TOP, fill = X) 
        # create a TEXT Box

        my_text = Text(my_frame, width = 97, height =25, font = ('Helvetica',16), selectbackground = '#239FCF', selectforeground = 'White', undo = True, yscrollcommand = text_scroll.set, wrap = 'none' , xscrollcommand =hor_scroll.set )
        my_text.pack()

        text_scroll.config(command = my_text.yview)
        hor_scroll.config(command = my_text.xview)



        # Create Menu
        my_menu = Menu(root)
        root.config(menu = my_menu)



        # Add file menu
        file_menu = Menu(my_menu, tearoff = False)
        my_menu.add_cascade(label = 'File', menu = file_menu)
        file_menu.add_command(label = "New", command = lambda: new_file() )
        file_menu.add_command(label = "Open", command = lambda: open_file() )
        file_menu.add_command(label = "Save As", command = lambda: save_as())
        file_menu.add_command(label = "Save", command =lambda: save_file() )

        file_menu.add_separator()
        file_menu.add_command(label = "Exit", command = root.quit)

        # Add the edit menu
        edit_menu = Menu(my_menu, tearoff = False)
        my_menu.add_cascade(label = 'Edit', menu = edit_menu)
        edit_menu.add_command(label = "Cut      ", command = lambda: cut_file(False), accelerator = '(Ctrl+x)')
        edit_menu.add_command(label = "Copy     ", command = lambda: copy_file(False), accelerator = '(Ctrl+c)')
        edit_menu.add_command(label = "Paste    ", command = lambda: paste_file(False), accelerator = '(Ctrl+v)')

        edit_menu.add_separator()
        edit_menu.add_command(label = "Undo", command = my_text.edit_undo, accelerator = '(Ctrl+z)')
        edit_menu.add_command(label = "Redo", command = my_text.edit_redo, accelerator = '(Ctrl+y)')

        # Add Status bar to the bottomog App

        status_bar = Label(root, text = 'Ready      ', anchor= E)
        status_bar.pack(fill = X, side = BOTTOM, ipady = 5)


        # Edit bindings
        root.bind('Control-key-x', cut_file)
        root.bind('Control-key-c', copy_file)
        root.bind('Control-key-v', paste_file)
        root.bind('Control-key-s', save_file)
        root.bind('Control-key-o', open_file)
        root.bind('Control-key-n', new_file)
        root.bind('Control-key-shift-key-s', save_as)



        root.mainloop()

    
    font = ('Times new roman',22,'bold')
    font1 = ('Times new roman',18,'bold')
    font2 = ('Times new roman',16,'bold')

    bg, fg = '#ffffff', '#FFA374'

    xx = GetSystemMetrics(0)
    yy = GetSystemMetrics(1)
    
    working_x = xx//2

    def sx(num):
        ratio = num * working_x
        ratio = round(ratio/980)
        return(ratio)

    def sy(num):
        ratio = num * yy
        ratio = round(ratio/1080)
        return(ratio)

    # def image_resize(image_name, dim='none', num='none'):
    #     global screen_w, screen_h
    #     if dim == 'none':
    #         screen_w = GetSystemMetrics(0)
    #         screen_h = GetSystemMetrics(1)
    #     if dim == 'sq':
    #         screen_w = sy(num)
    #         screen_h = screen_w
    #     elif dim == 'rec':
    #         screen_w = sx(num[0])
    #         screen_h = sy(num[1])
    #     else:
    #         pass
    #     image = Image.open(image_name)
    #     # The (screen_h, screen_w) is (height, width)
    #     image_x = image.resize((screen_w, screen_h), Image.ANTIALIAS)
    #     return image_x

    def exit_():
        sys.exit()

    with open('profiles.dat','rb') as file:
        records = []
        try:
            while True:
                read = load(file)
                records.append(read)
        except:
            username = records[-1][0]


    homepage = Tk()
    homepage.title('Home Page')
    homepage.geometry(f'{xx//2}x{yy}+{xx//2}+0')
    homepage.config(bg = '#ffa374')
    
    def image_resize(image_name, dim='none', num='none'):
        global screen_w, screen_h
        if dim == 'none':
            screen_w = GetSystemMetrics(0)
            screen_h = GetSystemMetrics(1)
        if dim == 'sq':
            screen_w = sy(num)
            screen_h = screen_w
        elif dim == 'rec':
            screen_w = sx(num[0])
            screen_h = sy(num[1])
        else:
            pass
        image = Image.open(image_name)
        # The (screen_h, screen_w) is (height, width)
        image_x = image.resize((screen_w, screen_h), Image.ANTIALIAS)
        return image_x

    def hov_browser(e):
        image_ = ImageTk.PhotoImage(image_resize('images/3-1.png', 'sq',100))
        btn5.config(image = image_)
        btn5.image = image_

    def hov_calc(e):
        image_ = ImageTk.PhotoImage(image_resize('images/2-1.png', 'sq',100))
        btn4.config(image = image_)
        btn4.image = image_


    def hov_notepad(e):

        image_ = ImageTk.PhotoImage(image_resize('images/1-1.png', 'sq',100))
        btn3.config(image = image_)
        btn3.image = image_




    def hov_browser2(e):
        image_ = ImageTk.PhotoImage(image_resize('images/3.png', 'sq',100))
        btn5.config(image = image_)
        btn5.image = image_

    def hov_calc2(e):
        image_ = ImageTk.PhotoImage(image_resize('images/2.png', 'sq',100))
        btn4.config(image = image_)
        btn4.image = image_


    
    def hov_notepad2(e):
        image_ = ImageTk.PhotoImage(image_resize('images/1.png', 'sq',100))
        btn3.config(image = image_)
        btn3.image = image_




    canvas = Canvas(homepage, width = sx(xx//2), height = yy)
    canvas.pack()

    my_image = ImageTk.PhotoImage(image_resize('images/bgmain.png', 'rec',num = (xx//2, yy)))
    canvas.create_image(sx(xx//4), 0,anchor = 'n', image=my_image)

    # Creating different buttons
    # Exit button



    d_ = 80
    btn_bg = '#FAAB83'
    btn_bg2 = '#F6BB9D'

    #Notepad
    my_image3 = ImageTk.PhotoImage(image_resize('images/1.png', 'sq', 100))
    btn3 = Button(homepage, image = my_image3, height = d_, width =d_,bg = btn_bg, activebackground = btn_bg2, relief =FLAT, command = notepad)
    canvas.create_window(sx(490), sy(339), anchor = 'n', window = btn3)

    btn3.bind('<Enter>',hov_notepad)
    btn3.bind('<Leave>',hov_notepad2)
    

    # calculator
    my_image4 = ImageTk.PhotoImage(image_resize('images/2.png', 'sq', 100))
    btn4 = Button(homepage, image = my_image4, height = d_, width =d_, bg = btn_bg, activebackground = btn_bg2, relief =FLAT, command = calculator)
    canvas.create_window(sx(490), sy(490), anchor = 'n', window = btn4)
    btn4.bind('<Enter>',hov_calc)
    btn4.bind('<Leave>',hov_calc2)

    # Browser
    my_image5 = ImageTk.PhotoImage(image_resize('images/3.png', 'sq', 100))
    btn5 = Button(homepage, image = my_image5, height = d_, width =d_, bg = '#ffa374', activebackground = btn_bg2, relief =FLAT, command = browser)
    canvas.create_window(sx(490), sy(645), anchor = 'n', window = btn5)
    btn5.bind('<Enter>',hov_browser)
    btn5.bind('<Leave>',hov_browser2)

    # Profile button
    

    btn6 = Button(homepage, text = username , height = 0, font = font2, fg = '#ffffff', bg = "#ffa374", activebackground = btn_bg2, relief = FLAT,command = None)
    canvas.create_window(sx(90), sy(36),anchor = 'nw', window = btn6)

    homepage.mainloop()

#################### Main Functionings #####################################################################
def main1(): # for 
    with open('profiles.dat','rb') as file:
        record = []
        try:
            while True:
                data = load(file)
                record.append(data)
        except EOFError:
            pass
    log_confirm = False # Varible to check if someone can log in 
    if len(record)==0:
        war = 'yes'
        while war=='yes':
            sign = signup_screen(bg, fg)
            a = status() # This confirms the 
            if a:
                showinfo('Sign up Sucessful','Sign up Sucessful')
                log_confirm = True
                break
            else:
                war = askquestion('Sign up unseucessful', 'Failed to sign up. You have to sign up to use the app.\nDo you want to try again?')
                log_confirm = False
    else:
        log_confirm = True

    if log_confirm:
        login_screen(bg, fg)
        done = log_status()
        if done:
            return True

def main2():
    homepage()
if __name__ == '__main__':
    try:
        logx = main1()
        if logx:
            main2()
    except Exception as e:
        showerror('Error', str(e))
