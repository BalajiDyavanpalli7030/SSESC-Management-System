import tkinter as tk
from tkinter import ttk
import time
import random
from PIL import Image,ImageTk
from tkinter import Toplevel
from tkinter import messagebox as m_box
from tkinter.ttk import Treeview
import pymysql

win=tk.Tk()
win.title('Sarathi Sunday English Speakers\' Club')
win.config(bg='light yellow')
win.geometry('800x600+100+50')
win.iconbitmap('icon.ico')
win.resizable(False,False)
######################################
def edit():
    edit_body=Toplevel()
    edit_body.title('edit_body')
    edit_body.geometry('500x150+250+300')
    edit_body.grab_set()
    edit_body_name=tk.Label(edit_body,text="Enter Body name below : ",font=('helvetica',20),fg='red')
    edit_body_name.pack()
    edit_body_entry=tk.Entry(edit_body,width=40,font=('times new roman',20),fg='blue')
    edit_body_entry.focus()
    edit_body_entry.pack()

    edit_bg_colour=tk.Label(edit_body,text="Enter Background Colour : ",font=('helvetica',15),fg='red')
    edit_bg_colour.place(x=0,y=70)
    edit_bg=tk.Entry(edit_body,width=12,font=('times new roman',12),fg='blue')
    edit_bg.place(x=240,y=75)
    
    def on(event):
        try:
            if edit_bg.get() != '':
                if edit_bg.get() == 'red':
                    clock_logo.config(fg='blue')
                    edit_body_label.config(fg='blue')
                    founder.config(fg='blue')
            edit_body_label.config(bg=edit_bg.get())
            founder.config(bg=edit_bg.get())        
            clock_logo.config(bg=edit_bg.get())
            win.config(bg=edit_bg.get())
        except:
            pass
        edit_body_label['text']=edit_body_entry.get()+' Executive \n Body'
        edit_body_entry.delete(0,'end')
        edit_body.destroy()
    edit_body_entry.bind("<Return>",on)
    def submit():
        try:
            if edit_bg.get() != '':
                if edit_bg.get() == 'red':
                    clock_logo.config(fg='blue')
                    founder.config(fg='blue')
                    edit_body_label.config(fg='blue')
                clock_logo.config(bg=edit_bg.get())
                founder.config(bg=edit_bg.get())
                edit_body_label.config(bg=edit_bg.get())
                win.config(bg=edit_bg.get())
        except:
            pass
        edit_body_label['text']=edit_body_entry.get()+' Executive \n Body'
        edit_body.destroy()

    submit=tk.Button(edit_body,width=6,text='Submit',command=submit,fg='red',bg='sky blue',
                     font=('calibry',15))
    submit.place(x=220,y=100)
    
edit_body_label=tk.Button(win,text='Executive'+'\n'+'Body',bg='light yellow',fg='red',borderwidth=0,
                     command=edit,font=('times new roman',25))
edit_body_label.place(x=0,y=0)

theme_label=tk.Label(win,text='Sarathi Sunday English Speakers\' Club',bg='light green',
                     fg='blue',font=('times new roman',30))
theme_label.place(x=405
                  ,y=130,anchor="center")

theme_label=tk.Label(win,text='Theme',bg='light green',fg='blue',font=('times new roman',30))
theme_label.place(x=420,y=190,anchor="center")
#######################################################################
theme_label=tk.Label(win,text='Anchors',bg='light green',fg='blue',font=('times new roman',20))
theme_label.place(x=650,y=300,anchor="center")

first_anchor=tk.Label(win,text='First Anchor',bg='light green',fg='blue',font=('times new roman',20))
first_anchor.place(x=650,y=350,anchor="center")

second_anchor=tk.Label(win,text='Second Anchor',bg='light green',fg='blue',
                       font=('times new roman',20))
second_anchor.place(x=650,y=400,anchor="center")
##########################################
colours=['red','green','pink','gold2','red2','yellow' ]
def intro_label_colour():
    fg=random.choice(colours)
    main_logo.config(fg=fg)
    main_logo.after(30,intro_label_colour)

def intro_label_trick():
    global count,text
    if (count>=len(s)):
        count=0
        text= ""
        main_logo.config(text=text)
    else:
        text=text+s[count]
        
        main_logo.config(text=text)
        count+=1
    main_logo.after(500,intro_label_trick)
s='SSESC'
count=0
text=''
#main logo
main_logo=tk.Label(win,text="SSESC",relief='ridge',bg='blue',borderwidth=10,width=6,
                   font=('times new roman',50))
main_logo.place(x=290,y=0)
intro_label_trick()
intro_label_colour()
################################################################
def tick():
    time_str=time.strftime('%H:%M:%S')
    date_str=time.strftime('%d/%m/%y')
    clock_logo.config(text='Date : '+date_str+' \n'+'Time: '+time_str)
    clock_logo.after(200,tick)
clock_logo=tk.Label(win,relief='ridge',bg='light yellow',borderwidth=0,width=12,fg='red',
                    font=('times new roman',16))
clock_logo.place(x=656,y=0)
tick()
######################################################################
def theme():
    theme=Toplevel()
    theme.title('theme')
    theme.geometry('500x250+250+300')
    theme.grab_set()
    theme_name=tk.Label(theme,text="Enter theme name below : ",font=('helvetica',20),fg='red')
    theme_name.pack()
    theme_entry=tk.Entry(theme,width=40,font=('times new roman',20),fg='blue')
    theme_entry.focus()
    theme_entry.pack()

    anchor1_label=tk.Label(theme,text='Enter First Anchor : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=18,borderwidth=5,anchor='w',relief='groove')
    anchor1_label.place(x=10,y=80)

    anchor2_label=tk.Label(theme,text='Enter Second Anchor : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=18,borderwidth=5,anchor='w',relief='groove')
    anchor2_label.place(x=10,y=130)
    
    anchor1_var=tk.StringVar()
    anchor2_var=tk.StringVar()
    anchor1_entry=tk.Entry(theme,textvariable=anchor1_var,fg='blue',font=('times new roman',18),
                      width=18,borderwidth=5,relief='groove')
    anchor1_entry.place(x=260,y=80)

    anchor2_entry=tk.Entry(theme,textvariable=anchor2_var,fg='blue',font=('times new roman',18),
                      width=18,borderwidth=5,relief='groove')
    anchor2_entry.place(x=260,y=130)

    def on(event):
        first_anchor['text']=anchor1_var.get()
        second_anchor['text']=anchor2_var.get()
        value=theme_entry.get()
        theme_label['text']=value
        theme_entry.delete(0,'end')
        theme.destroy()
    theme_entry.bind("<Return>",on)
    def submit():
        first_anchor['text']=anchor1_var.get()
        second_anchor['text']=anchor2_var.get()
        theme_label['text']=theme_entry.get()
        theme.destroy()
        
    submit=tk.Button(theme,width=6,text='Submit',command=submit,fg='red',bg='sky blue',
                     font=('calibry',15))
    submit.place(x=200,y=190)

theme_label=tk.Label(win,text='Sarathi Sunday English Speakers\' Club',bg='light green',
                     fg='red',font=('times new roman',30))
theme_label.place(x=405,y=250,anchor="center")

entry_box=tk.Button(win,width=15,text='Edit Todays Theme',command=theme,bg='light green',
                    fg='blue',font=('times new roman',15))
entry_box.place(x=200,y=500)

###########################################################################    
load = Image.open("images.jpg")
render = ImageTk.PhotoImage(load)
img = tk.Label(win, image=render)
img.image = render
img.place(x=640,y=490)
###########################################################################
founder=tk.Label(win,width=15,text='Founder President'+'\n'+"Prof.Vitthal Vanga",bg='light yellow',fg='red',
                    font=('times new roman',20))
founder.place(x=0,y=300)
#################################
def add_sarathian():
    def add():
        id=id_var.get()
        name=name_var.get()
        dob=dob_var.get()
        mob=mob_var.get()
        gender=gender_var.get()
        address=address_var.get()
        try:
            strr =  "INSERT INTO membersdata (id,name, mobile ,address,gender,dob) VALUES (%s, %s,%s, %s,%s, %s)"
            my_cursor.execute(strr,(id,name, mob ,address,gender,dob))
            con.commit()
            res = m_box.askyesnocancel('Notification',f'Id {id} Name "\ {name} "\ Added successfully . and want to clean the form',parent=add_root)
            if res:
                id_var.set('')
                name_var.set('')
                dob_var.set('')
                mob_var.set('')
                address_var.set('')
        except NameError:
            m_box.showerror('Notification','Please connect to database',parent=add_root)
            add_root.destroy()
        except:
            m_box.showerror('Notification','Id already Exist try another one',parent=add_root)
    add_root=Toplevel()
    add_root.grab_set()
    add_root.focus()
    add_root.title('Add New Sarathian')
    add_root.geometry('400x350+300+300')
    add_root.config(bg='gold2')
    id_label=tk.Label(add_root,text='Enter Id : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=5,anchor='w',relief='groove')
    id_label.place(x=10,y=10)

    name_label=tk.Label(add_root,text='Enter Name : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=3,anchor='w',relief='groove')
    name_label.place(x=10,y=60)

    dob_label=tk.Label(add_root,text='Enter DOB : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=3,anchor='w',relief='groove')
    dob_label.place(x=10,y=110)

    gender_label=tk.Label(add_root,text='Select Gender : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=3,anchor='w',relief='groove')
    gender_label.place(x=10,y=160)

    mob_label=tk.Label(add_root,text='Enter Mobile : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=3,anchor='w',relief='groove')
    mob_label.place(x=10,y=210)

    address_label=tk.Label(add_root,text='Enter Address : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=3,anchor='w',relief='groove')
    address_label.place(x=10,y=260)

    id_var=tk.StringVar()   
    name_var=tk.StringVar()
    dob_var=tk.StringVar()
    mob_var=tk.StringVar()
    address_var=tk.StringVar()
    id_entry=tk.Entry(add_root,fg='blue',textvariable=id_var,font=('times new roman',18),
                      width=16,borderwidth=5,relief='groove')
    id_entry.place(x=190,y=10)
    id_entry.focus()

    name_entry=tk.Entry(add_root,textvariable=name_var,fg='blue',font=('times new roman',18),
                      width=16,borderwidth=5,relief='groove')
    name_entry.place(x=190,y=60)

    dob_entry=tk.Entry(add_root,textvariable=dob_var,fg='blue',font=('times new roman',18),
                      width=16,borderwidth=5,relief='groove')
    dob_entry.place(x=190,y=110)

    gender_var=tk.StringVar()
    gender_combobox=ttk.Combobox(add_root,width=15,font=('times new roman',18),textvariable=gender_var,state='readonly')
    gender_combobox['values']=('Male','Female','Other')
    gender_combobox.current(0)
    gender_combobox.place(x=190,y=160)

    mob_entry=tk.Entry(add_root,textvariable=mob_var,fg='blue',font=('times new roman',18),
                      width=16,borderwidth=5,relief='groove')
    mob_entry.place(x=190,y=210)
    
    adress_entry=tk.Entry(add_root,textvariable=address_var,fg='blue',font=('times new roman',18),
                      width=16,borderwidth=5,relief='groove')
    adress_entry.place(x=190,y=260)

    submit_btn=tk.Button(add_root,width=6,text='Submit',command=add,bg='light green',fg='blue',
                        activebackground='gold2',activeforeground='blue',font=('times new roman',18))
    submit_btn.place(x=140,y=305)

    add_root.mainloop()

entry_box=tk.Button(win,width=15,text='Add Sarthian',command=add_sarathian,bg='light green',fg='blue',
                    activebackground='gold2',activeforeground='blue',font=('times new roman',15))
entry_box.place(x=0,y=450)
############################################################################
def search_sarathian():
    def search ():
        id=id_var.get()
        name=name_var.get()
        dob=dob_var.get()
        mob=mob_var.get()
        gender=gender_var.get()
        if id !=( ''):
            search_by='id'
            m=id
        if name != (''):
            search_by='name'
            m=name
        if dob != '':
            search_by='dob'
            m=dob
        if mob != '':
            search_by='mobile'
            m=mob
        if gender != '':
            search_by='gender'
            m=gender
            
        show_root=Toplevel()
        show_root.grab_set()
        show_root.focus()
        show_root.geometry('795x500+100+150')
        show_root.resizable(False,False)
        show_root.config(bg='firebrick1')
        frame=tk.Frame(show_root,bg='gold2',relief='groove',borderwidth=5)
        frame.place(x=0,y=0,width=795,height=500)

        scroll_x=tk.Scrollbar(frame,orient='horizontal')
        scroll_x.pack(side='bottom',fill='x')
        
        scroll_y=tk.Scrollbar(frame,orient='vertical')
        scroll_y.pack(side='right',fill='y')

        members_table=ttk.Treeview(frame,columns=('Id','Name','Mobile No','Address','Gender','D.O.B'),
                                  yscrollcommand=scroll_y,xscrollcommand=scroll_x)

        members_table.pack(fill='both',expand=1)
        scroll_x.config(command=members_table.xview)
        scroll_y.config(command=members_table.yview)
        
        style =ttk.Style()
        style.configure('Treeview.Heading',foreground='blue',font=('helvetica',16))
        style.configure('Treeview',foreground='green',font=('times new roman',15),background='cyan',fg='green')

        members_table.heading('Id',text='Id')
        members_table.heading('Name',text='Name')
        members_table.heading('Mobile No',text='Mobile No')
        members_table.heading('Address',text='Address')
        members_table.heading('Gender',text='Gender')
        members_table.heading('D.O.B',text='D.O.B')
        members_table['show']='headings'
        
        members_table.column('Id',width=50)
        members_table.column('Name',width=300)
        members_table.column('Mobile No',width=140)
        members_table.column('Address',width=260)
        members_table.column('Gender',width=100)
        members_table.column('D.O.B',width=110)
        try:
            strr =f'select * from membersdata where {search_by} = %s'
            my_cursor.execute(strr,m)
            datas = my_cursor.fetchall()
            members_table.delete(*members_table.get_children())
            for i in datas:
                val = [i[0],i[1],i[2],i[3],i[4],i[5]]
                members_table.insert('', 'end',
                     values=(val))
        except  UnboundLocalError:
            search_root.destroy()
            m_box.showerror('Error','Please Connect to Database First',parent=show_root)
            show_root.destroy()
        show_root.mainloop()
        
    
    entry_box=tk.Button(win,width=15,text='All Members',command=show_all,bg='light green',
                        activebackground='yellow',activeforeground='red',fg='blue',font=('times new roman',15))
    entry_box.place(x=0,y=400)
    
    search_root=Toplevel()
    search_root.grab_set()
    search_root.focus()
    search_root.geometry('400x310+300+300')
    search_root.config(bg='red')
    id_label=tk.Label(search_root,text='Enter Id : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=5,anchor='w',relief='groove')
    id_label.place(x=10,y=10)

    name_label=tk.Label(search_root,text='Enter Name : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=3,anchor='w',relief='groove')
    name_label.place(x=10,y=60)

    dob_label=tk.Label(search_root,text='Enter DOB : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=3,anchor='w',relief='groove')
    dob_label.place(x=10,y=110)

    gender_label=tk.Label(search_root,text='Select Gender : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=3,anchor='w',relief='groove')
    gender_label.place(x=10,y=160)

    mob_label=tk.Label(search_root,text='Enter Mobile : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=3,anchor='w',relief='groove')
    mob_label.place(x=10,y=210)

    id_var=tk.StringVar()   
    name_var=tk.StringVar()
    dob_var=tk.StringVar()
    mob_var=tk.StringVar()
    id_entry=tk.Entry(search_root,fg='blue',textvariable=id_var,font=('times new roman',18),
                      width=16,borderwidth=5,relief='groove')
    id_entry.place(x=190,y=10)
    id_entry.focus()

    name_entry=tk.Entry(search_root,textvariable=name_var,fg='blue',font=('times new roman',18),
                      width=16,borderwidth=5,relief='groove')
    name_entry.place(x=190,y=60)

    dob_entry=tk.Entry(search_root,textvariable=dob_var,fg='blue',font=('times new roman',18),
                      width=16,borderwidth=5,relief='groove')
    dob_entry.place(x=190,y=110)

    gender_var=tk.StringVar()
    gender_combobox=ttk.Combobox(search_root,width=15,font=('times new roman',18),textvariable=gender_var,state='readonly')
    gender_combobox['values']=('Male','Female','Other',"")
    gender_combobox.place(x=190,y=160)

    mob_entry=tk.Entry(search_root,textvariable=mob_var,fg='blue',font=('times new roman',18),
                      width=16,borderwidth=5,relief='groove')
    mob_entry.place(x=190,y=210)

    submit_btn=tk.Button(search_root,width=6,text='Search',command=search,bg='light green',fg='blue',
                        activebackground='gold2',activeforeground='blue',font=('times new roman',18))
    submit_btn.place(x=140,y=260)
    
    search_root.mainloop()
entry_box=tk.Button(win,width=15,text='Search Sarthian',command=search_sarathian,bg='light green',fg='blue',
                    activebackground='red',activeforeground='gold2',font=('times new roman',15))
entry_box.place(x=0,y=500)

############################################################################
def update():
    def updated():
        id=id_var.get()
        name=name_var.get()
        dob=dob_var.get()
        mob=mob_var.get()
        gender=gender_var.get()
        address=address_var.get()
        try:
            strr='update membersdata set name =%s ,dob=%s,mobile=%s,gender=%s,address=%s where id =%s'
            my_cursor.execute(strr,(name,dob,mob,gender,address,id))
            con.commit()
            res = m_box.askyesnocancel('Notification',f'Updated Successfully! \n Do you want to exit')
            if res:update_root.destroy()
        except NameError:
            m_box.showerror('Error','Please connect to Database First')
    enter_id_root.destroy()
    global update_root
    update_root=Toplevel()
    update_root.grab_set()
    update_root.focus()
    update_root.geometry('400x350+300+300')
    update_root.config(bg='firebrick1')
    id_label=tk.Label(update_root,text='Update Id : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=5,anchor='w',relief='groove')
    id_label.place(x=10,y=10)

    name_label=tk.Label(update_root,text='Update Name : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=3,anchor='w',relief='groove')
    name_label.place(x=10,y=60)

    dob_label=tk.Label(update_root,text='Update DOB : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=3,anchor='w',relief='groove')
    dob_label.place(x=10,y=110)

    gender_label=tk.Label(update_root,text='Select Gender : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=3,anchor='w',relief='groove')
    gender_label.place(x=10,y=160)

    mob_label=tk.Label(update_root,text='Update Mobile : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=3,anchor='w',relief='groove')
    mob_label.place(x=10,y=210)
    address_label=tk.Label(update_root,text='Update Address : ',bg='light green',fg='blue',font=('times new roman',18),
                  width=12,borderwidth=3,anchor='w',relief='groove')
    address_label.place(x=10,y=260)

    id_var=tk.StringVar()   
    name_var=tk.StringVar()
    dob_var=tk.StringVar()
    mob_var=tk.StringVar()
    address_var=tk.StringVar()

    id_entry=tk.Entry(update_root,fg='blue',textvariable=id_var,font=('times new roman',18),
                      width=16,borderwidth=5,relief='groove')
    id_entry.place(x=190,y=10)
    id_entry.focus()

    name_entry=tk.Entry(update_root,textvariable=name_var,fg='blue',font=('times new roman',18),
                      width=16,borderwidth=5,relief='groove')
    name_entry.place(x=190,y=60)

    dob_entry=tk.Entry(update_root,textvariable=dob_var,fg='blue',font=('times new roman',18),
                      width=16,borderwidth=5,relief='groove')
    dob_entry.place(x=190,y=110)

    gender_var=tk.StringVar()
    gender_combobox=ttk.Combobox(update_root,width=15,font=('times new roman',18),textvariable=gender_var,state='readonly')
    gender_combobox['values']=('Male','Female','Other')
    gender_combobox.current(0)
    gender_combobox.place(x=190,y=160)

    mob_entry=tk.Entry(update_root,textvariable=mob_var,fg='blue',font=('times new roman',18),
                      width=16,borderwidth=5,relief='groove')
    mob_entry.place(x=190,y=210)
    address_entry=tk.Entry(update_root,textvariable=address_var,fg='blue',font=('times new roman',18),
                      width=16,borderwidth=5,relief='groove')
    address_entry.place(x=190,y=260)

    submit_btn=tk.Button(update_root,width=6,text='Update',command=updated,bg='light green',fg='blue',
                        activebackground='gold2',activeforeground='blue',font=('times new roman',18))
    submit_btn.place(x=140,y=305)
    
    v=enter_id_var.get()
    try:
        strr =f'select * from membersdata where id = %s'
        my_cursor.execute(strr,v)
        d = my_cursor.fetchall()
        id_var.set(d[0][0])
        name_var.set(d[0][1])
        address_var.set(d[0][3])
        dob_var.set(d[0][5])
        gender_var.set(d[0][4])
        mob_var.set(d[0][2])
    except NameError:
        update_root.destroy()
        m_box.showerror('Error','Please connect to Database First')
    update_root.mainloop()
def update_sarathian():
    global enter_id_root
    enter_id_root=Toplevel()
    enter_id_root.grab_set()
    enter_id_root.focus()
    enter_id_root.geometry('400x110+300+300')
    enter_id_root.config(bg='red')
    
    id_label=tk.Label(enter_id_root,text='Enter Id to update : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=15,borderwidth=5,anchor='w',relief='groove')
    id_label.place(x=10,y=10)

    global enter_id_var
    enter_id_var=tk.StringVar()
    id_entry=tk.Entry(enter_id_root,fg='blue',textvariable=enter_id_var,font=('times new roman',18),
                      width=12,borderwidth=5,relief='groove')
    id_entry.place(x=230,y=10)
    id_entry.focus()
    
    submit_btn=tk.Button(enter_id_root,width=6,text='Upadate',command=update,bg='light green',fg='blue',
                        activebackground='gold2',activeforeground='blue',font=('times new roman',18))
    submit_btn.place(x=130,y=60)

entry_box=tk.Button(win,width=15,text='Update Sarthian',command=update_sarathian,bg='light green',fg='blue',
                    activebackground='red',activeforeground='yellow',font=('times new roman',15))
entry_box.place(x=0,y=550)
############################################################################
def delete_sarathian():
        delete=Toplevel()
        delete.title('Delete')
        delete.geometry('500x100+250+300')
        delete.grab_set()
        delete_name=tk.Label(delete,text="Enter member id  below : ",font=('helvetica',20),fg='red')
        delete_name.pack()
        delete_entry=tk.Entry(delete,width=40,font=('times new roman',20),fg='blue')
        delete_entry.focus()
        delete_entry.pack()
        def on(event):
            value=delete_entry.get()
            delete_label['text']=value
            delete_entry.delete(0,'end')
            delete.destroy()
            delete_entry.bind("<Return>",on)
        def submit():
            id=delete_entry.get()
            try:
                strr = 'delete from membersdata where id = %s'
                my_cursor.execute(strr,(id))
                con.commit()
                m_box.showinfo('Notification',f'id {id} deleted successfull...')
            except NameError:
                delete.destroy()
                m_box.showerror('Error','Please connect to Database First')
        submit=tk.Button(delete,width=6,text='Delete',command=submit,fg='black',bg='sky blue',
                         font=('calibry',20))
        submit.pack()
entry_box=tk.Button(win,width=15,text='Delete Sarathian',command=delete_sarathian,bg='light green',
                    activebackground='yellow',activeforeground='red',fg='blue',font=('times new roman',15))
entry_box.place(x=200,y=550)
############################################################################
def todays_members():
    m_box.showinfo('Notification','First click on \"Enter Date\"Button \n Then Enter Id')
    def new_sunday():
        def new_sun():
            try:
                global new_table
                new_table='sarathi'+date_entry.get()
                rr = f'create table {new_table} (user_id int primary key,foreign key(user_id) references membersdata(id ))'
                my_cursor.execute(rr)
                m_box.showinfo('Notification','Fresh Sunday',parent=date)
                all_mem()
                date.destroy()
            except NameError:
                todays_mem_root.destroy()
                date.destroy()
                m_box.showerror('Error','Please connect to Database First')
            except:
                res = m_box.askyesnocancel('Confirmation','Is it todays Date?',parent=date)
                if res:
                    all_mem()
                    date.destroy()
        date=Toplevel()
        date.grab_set()
        date.focus()
        date.geometry('490x180+300+300')
        date.resizable(False,False)
        date.config(bg='black')
        theme_name=tk.Label(date,text='Date should be like this:10May2020 ',bg='light green',fg='blue',font=('times new roman',18),
                      width=30,borderwidth=5,anchor='center',relief='groove')
        theme_name.pack()
        
        date_name=tk.Label(date,text='Add Todays Date : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=15,borderwidth=5,anchor='w',relief='groove')
        date_name.place(x=0,y=50)
        
        date_entry=tk.Entry(date,fg='blue',font=('times new roman',18),
                          width=20,borderwidth=5,relief='groove')
        date_entry.place(x=240,y=50)
        
        submit_date=tk.Button(date,text='Submit',command=new_sun,bg='light green',fg='blue',font=('times new roman',18),
                      width=5,borderwidth=5,anchor='center',relief='groove')
        submit_date.place(x=190,y=110)
    def del_sar():
        try:
            now_del=new_table
            added_mem=add_member_entry_var.get()
            strr = f'delete from {now_del} where user_id = %s'
            my_cursor.execute(strr,(added_mem))
            con.commit()
            all_mems()
            m_box.showinfo('Notification',f'id {added_mem} deleted successfull...',parent=todays_mem_root)
        except:
            m_box.showinfo('Notification','Id Doesnt exist',parent=todays_mem_root)
            
    def add_members():
        try:
            now_insert=new_table
            added_mem=add_member_entry_var.get()
            strr =  f"INSERT INTO  {now_insert} (user_id) VALUES (%s)"
            my_cursor.execute(strr,(added_mem))
            all_mem()
            con.commit()
            add_member_entry_var.set('')
        except NameError:
            m_box.showerror('Notification','Enter Id number',parent=todays_mem_root)
            add_member_entry_var.set('')
            return
        except:
            m_box.showerror('Notification','Already Addded',parent=todays_mem_root)
            add_member_entry_var.set('')

    global all_mem
    def all_mem():
        try:
            now_insert=new_table
            strr =f'select * from membersdata inner join {now_insert} on membersdata.id={now_insert}.user_id '
            my_cursor.execute(strr)
            datas = my_cursor.fetchall()
            members_table.delete(*members_table.get_children())
            for i in datas:
                val = [i[0],i[1],i[2],i[3],i[4],i[5]]
                print(val)
                members_table.insert('', 'end',
                values=(val))
        except:
            pass
    todays_mem_root=Toplevel()
    todays_mem_root.grab_set()
    todays_mem_root.focus()
    todays_mem_root.geometry('795x550+100+100')
    todays_mem_root.resizable(False,False)
    todays_mem_root.config(bg='black')

    frame=tk.Frame(todays_mem_root,bg='gold2',relief='groove',borderwidth=5)
    frame.place(x=0,y=40,width=795,height=460)

    scroll_x=tk.Scrollbar(frame,orient='horizontal')
    scroll_x.pack(side='bottom',fill='x')
    
    scroll_y=tk.Scrollbar(frame,orient='vertical')
    scroll_y.pack(side='right',fill='y')

    members_table=ttk.Treeview(frame,columns=('Id','Name','Mobile No','Address','Gender','D.O.B'),
                              yscrollcommand=scroll_y,xscrollcommand=scroll_x)
    members_table.pack(fill='both',expand=1)
    scroll_x.config(command=members_table.xview)
    scroll_y.config(command=members_table.yview)
    
    style =ttk.Style()
    style.configure('Treeview.Heading',foreground='blue',font=('helvetica',16))
    style.configure('Treeview',foreground='green',font=('times new roman',15),background='cyan',fg='green',bg='red')

    members=tk.Label(todays_mem_root,text=': Todays Sarthians : ',bg='light yellow',fg='red',font=('times new roman',18),
                      width=16,borderwidth=5,anchor='center',relief='groove')
    members.place(x=320,y=0)
    
    add_member=tk.Button(todays_mem_root,text='Add Sarthian : ',command=add_members,bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=5,anchor='w',relief='groove')
    add_member.place(x=0,y=500)

    add_member=tk.Button(todays_mem_root,text='Remove Sarthian : ',command=del_sar,bg='light green',fg='blue',font=('times new roman',18),
                      width=14,borderwidth=5,anchor='w',relief='groove')
    add_member.place(x=270,y=500)

    add_member_entry_var=tk.StringVar()
    add_member_entry=tk.Entry(todays_mem_root,textvariable=add_member_entry_var,fg='blue',font=('times new roman',18),
                      width=5,borderwidth=10,relief='groove')
    add_member_entry.place(x=180,y=500)
    add_member_entry.focus()
    
    new_sun=tk.Button(todays_mem_root,text='Enter Date : ',command=new_sunday,bg='light green',fg='blue',font=('times new roman',18),
                      width=10,borderwidth=5,anchor='w',relief='groove')
    new_sun.place(x=650,y=500)
    new_sun=tk.Button(todays_mem_root,text=':Show All : ',command=all_mem,bg='light green',fg='blue',font=('times new roman',18),
                      width=8,borderwidth=5,anchor='w',relief='groove')
    new_sun.place(x=500,y=500)

    members_table.heading('Id',text='Id')
    members_table.heading('Name',text='Name')
    members_table.heading('Mobile No',text='Mobile No')
    members_table.heading('Address',text='Address')
    members_table.heading('Gender',text='Gender')
    members_table.heading('D.O.B',text='D.O.B')
    members_table['show']='headings'

    members_table.column('Id',width=50)
    members_table.column('Name',width=300)
    members_table.column('Mobile No',width=140)
    members_table.column('Address',width=260)
    members_table.column('Gender',width=100)
    members_table.column('D.O.B',width=100)

    todays_mem_root.mainloop()
    
entry_box=tk.Button(win,width=15,text='Todays Members',command=todays_members,bg='light green',
                    activebackground='yellow',activeforeground='red',fg='blue',font=('times new roman',15))
entry_box.place(x=200,y=450)
###########################################################################
def body_members():
    m_box.showinfo('Notification','First click on \"Enter Body\"Button')
    def new_body_mem():
        def new_mem():
            try:
                global new_body_db
                new_body_db='ExecutiveBody'+exe_entry.get()
                rr = f'create table {new_body_db} (body_id int primary key,foreign key(body_id) references membersdata(id ),mem_post varchar(50))'
                my_cursor.execute(rr)
                m_box.showinfo('Notification','Fresh Executive Body',parent=ex)
                all_mems()
                ex.destroy()
            except NameError:
                m_box.showerror('Error','Please connect to Database First',parent=ex)
                ex.destroy()
                Exe_body_root.destroy()
            except:
                res = m_box.askyesnocancel('Confirmation',f'Is it {exe_entry.get()} Executive body?',parent=ex)
                if res:
                    all_mems()
                    ex.destroy()

        ex=Toplevel()
        ex.grab_set()
        ex.title('Executive Body')
        ex.focus()
        ex.geometry('490x180+300+300')
        ex.resizable(False,False)
        ex.config(bg='black')
        
        exe_label=tk.Label(ex,text='Add Executive Body Number Below',bg='light green',fg='blue',font=('times new roman',18),
                      width=40,borderwidth=5,anchor='center',relief='groove')
        exe_label.place(x=0,y=0)
        
        exe_entry=tk.Entry(ex,fg='blue',font=('times new roman',18),
                          width=6,borderwidth=5,relief='groove')
        exe_entry.place(x=190,y=60)
        exe_entry.focus()
        submit_exe=tk.Button(ex,text='Submit',command=new_mem,bg='light green',fg='blue',font=('times new roman',18),
                      width=5,borderwidth=5,anchor='center',relief='groove')
        submit_exe.place(x=190,y=110)

    def add_body_members():
        def del_body_mem():
            try:
                now_del=new_body_db
                added_mem_id=exe_id_entry_var.get()
                strr = f'delete from {now_del} where body_id = %s'
                my_cursor.execute(strr,(added_mem_id))
                con.commit()
                all_mems()
                m_box.showinfo('Notification',f'id {added_mem_id} deleted successfull...',parent=exe)
                exe_id_entry_var.set('')
            except NameError:
                m_box.showerror('Error','Please connect to Database First',parent=exe)
                Exe_body_root.destroy()
                exe.destroy()
            except:
                m_box.showinfo('Notification','Id Doesnt exist',parent=exe)
                exe_id_entry_var.set('')
                
        def all_mem():
            try:
                now_insert=new_body_db
                added_mem_id=exe_id_entry_var.get()
                added_mem_post=mem_post_entry_var.get()
                strr =  f"INSERT INTO  {now_insert} (body_id,mem_post) VALUES (%s,%s)"
                my_cursor.execute(strr,(added_mem_id,added_mem_post))
                con.commit()
                m_box.showinfo('Notification','Added Successfull',parent=exe)
                all_mems()
                exe_id_entry_var.set('')
                mem_post_entry_var.set('')
            except NameError:
                m_box.showerror('Error','First enter Body Number Into \n Enter Body',parent=exe)
                exe.destroy()
            except NameError:
                m_box.showerror('Notification','Enter Id number',parent=exe)
                return
            except pymysql.err.IntegrityError:
                m_box.showerror('New Sarathian','First add into Add Sarthian ',parent=exe)
            except:
                m_box.showerror('Notification','Already Addded',parent=exe)
                exe_id_entry_var.set('')
                mem_post_entry_var.set('')

        exe=Toplevel()
        exe.grab_set()
        exe.title('Add Or Delete')
        exe.focus()
        exe.geometry('490x180+300+300')
        exe.resizable(False,False)
        exe.config(bg='black')

        exe_id_entry_var=tk.StringVar()
        mem_post_entry_var=tk.StringVar()
        exe_id_label=tk.Label(exe,text='Add Member Id :',bg='light green',fg='blue',font=('times new roman',18),
                      width=15,borderwidth=5,anchor='center',relief='groove')
        exe_id_label.place(x=0,y=0)
        

        exe_id_entry=tk.Entry(exe,fg='blue',textvariable=exe_id_entry_var,font=('times new roman',18),
                          width=20,borderwidth=5,relief='groove')
        exe_id_entry.place(x=240,y=0)
        exe_id_entry.focus()

        
        mem_post=tk.Label(exe,text='Add Member Post : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=15,borderwidth=5,anchor='w',relief='groove')
        mem_post.place(x=0,y=50)
        
        mem_post_entry=tk.Entry(exe,fg='blue',textvariable=mem_post_entry_var,font=('times new roman',18),
                          width=20,borderwidth=5,relief='groove')
        mem_post_entry.place(x=240,y=50)
        
        del_exe=tk.Button(exe,text='Delete Member',command=del_body_mem,bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=5,anchor='center',relief='groove')
        del_exe.place(x=300,y=110)
        
        
        submit_exe=tk.Button(exe,text='Submit',command=all_mem,bg='light green',fg='blue',font=('times new roman',18),
                      width=5,borderwidth=5,anchor='center',relief='groove')
        submit_exe.place(x=190,y=110)
            
    global all_mems
    def all_mems():
        try:
            now_insert=new_body_db
            strr =f'select * from membersdata inner join {now_insert} on membersdata.id={now_insert}.body_id '
            my_cursor.execute(strr)
            datas = my_cursor.fetchall()
            members_table.delete(*members_table.get_children())
            for i in datas:
                val = [i[0],i[1],i[7],i[2],i[3],i[4],i[5]]
                members_table.insert('', 'end',
                values=(val))
        except:
            pass
    
    Exe_body_root=Toplevel()
    Exe_body_root.grab_set()
    Exe_body_root.title('Executive Body Members')
    Exe_body_root.focus()
    Exe_body_root.geometry('795x550+100+100')
    Exe_body_root.resizable(False,False)
    Exe_body_root.config(bg='black')

    frame=tk.Frame(Exe_body_root,bg='gold2',relief='groove',borderwidth=5)
    frame.place(x=0,y=40,width=795,height=460)

    scroll_x=tk.Scrollbar(frame,orient='horizontal')
    scroll_x.pack(side='bottom',fill='x')
    
    scroll_y=tk.Scrollbar(frame,orient='vertical')
    scroll_y.pack(side='right',fill='y')

    members_table=ttk.Treeview(frame,columns=('Id','Name','Member Post','Mobile','Address','Gender','D.O.B'),
                              yscrollcommand=scroll_y,xscrollcommand=scroll_x)
    members_table.pack(fill='both',expand=1)
    
    scroll_x.config(command=members_table.xview)
    scroll_y.config(command=members_table.yview)
    
    style =ttk.Style()
    style.configure('Treeview.Heading',foreground='blue',font=('helvetica',16))
    style.configure('Treeview',foreground='green',font=('times new roman',15),background='cyan',fg='green',bg='red')

    members=tk.Label(Exe_body_root,text=': Executive Body Members : ',bg='light yellow',fg='red',font=('times new roman',18),
                      width=20,borderwidth=5,anchor='center',relief='groove')
    members.place(x=280,y=0)
    
    add_member=tk.Button(Exe_body_root,text='Add Member : ',command=add_body_members,fg='blue',font=('times new roman',18),
                      width=12,borderwidth=5,anchor='w',relief='groove')
    add_member.place(x=0,y=500)

    new_sun=tk.Button(Exe_body_root,text='Enter Body: ',command=new_body_mem,fg='blue',font=('times new roman',18),
                      width=10,borderwidth=5,anchor='w',relief='groove')
    new_sun.place(x=650,y=500)
    new_sun=tk.Button(Exe_body_root,text=':Show All : ',command=all_mems,fg='blue',font=('times new roman',18),
                      width=8,borderwidth=5,anchor='w',relief='groove')
    new_sun.place(x=400,y=500)

    members_table.heading('Id',text='Id')
    members_table.heading('Name',text='Name')
    members_table.heading('Member Post',text='Member Post')
    members_table.heading('Mobile',text='Mobile No')
    members_table.heading('Address',text='Address')
    members_table.heading('Gender',text='Gender')
    members_table.heading('D.O.B',text='D.O.B')
    members_table['show']='headings'

    members_table.column('Id',width=50)
    members_table.column('Name',width=260)
    members_table.column('Member Post',width=150)
    members_table.column('Mobile',width=140)
    members_table.column('Address',width=260)
    members_table.column('Gender',width=100)
    members_table.column('D.O.B',width=100)
    
    Exe_body_root.mainloop()

entry_box=tk.Button(win,width=15,text='Executive Body',command=body_members,bg='light green',fg='blue',
                    activebackground='red',activeforeground='gold2',font=('times new roman',15))
entry_box.place(x=200,y=400)
############################################################################
def show_all():
    show_root=Toplevel()
    show_root.grab_set()
    show_root.focus()
    show_root.geometry('795x500+100+150')
    show_root.resizable(False,False)
    show_root.config(bg='firebrick1')

    frame=tk.Frame(show_root,bg='gold2',relief='groove',borderwidth=5)
    frame.place(x=0,y=0,width=795,height=500)

    scroll_x=tk.Scrollbar(frame,orient='horizontal')
    scroll_x.pack(side='bottom',fill='x')
    
    scroll_y=tk.Scrollbar(frame,orient='vertical')
    scroll_y.pack(side='right',fill='y')

    members_table=ttk.Treeview(frame,columns=('Id','Name','Mobile No','Address','Gender','D.O.B'),
                              yscrollcommand=scroll_y,xscrollcommand=scroll_x)

    members_table.pack(fill='both',expand=1)
    scroll_x.config(command=members_table.xview)
    scroll_y.config(command=members_table.yview)
    
    style =ttk.Style()
    style.configure('Treeview.Heading',foreground='blue',font=('helvetica',16))
    style.configure('Treeview',foreground='green',font=('times new roman',15),background='cyan',fg='green',bg='red')

    members_table.heading('Id',text='Id')
    members_table.heading('Name',text='Name')
    members_table.heading('Mobile No',text='Mobile No')
    members_table.heading('Address',text='Address')
    members_table.heading('Gender',text='Gender')
    members_table.heading('D.O.B',text='D.O.B')
    members_table['show']='headings'

    members_table.column('Id',width=50)
    members_table.column('Name',width=300)
    members_table.column('Mobile No',width=140)
    members_table.column('Address',width=260)
    members_table.column('Gender',width=100)
    members_table.column('D.O.B',width=100)
    try:
        strr ='select * from membersdata'
        my_cursor.execute(strr)
        datas = my_cursor.fetchall()
        members_table.delete(*members_table.get_children())
        for i in datas:
            val = [i[0],i[1],i[2],i[3],i[4],i[5]]
            members_table.insert('', 'end',
                 values=(val))
    except:
        show_root.destroy()
        m_box.showerror('Notification','Please connect to Database first')
    show_root.mainloop()
    
entry_box=tk.Button(win,width=15,text='All Members',command=show_all,bg='light green',
                    activebackground='yellow',activeforeground='red',fg='blue',font=('times new roman',15))
entry_box.place(x=0,y=400)
#############################################################################
def end():
    ask = m_box.askyesnocancel('Notification','Do you want to exit')
    if ask:win.destroy()

ex_box=tk.Button(win,width=8,text='Exit',command=end,bg='light green',
                    activebackground='yellow',activeforeground='red',fg='blue',font=('times new roman',15))
ex_box.place(x=380,y=550)

################################################################################
def connectdb():
    def submitdb():
        global con,my_cursor
        host = host_var.get()
        user = user_var.get()
        password = password_var.get()
        try:
            con = pymysql.connect(host=host ,user=user,password=password)
            my_cursor = con.cursor()
            m_box.showinfo("Notification",'successfully connected')
            dbroot.destroy()
        except:
            m_box.showerror("Notification",'Data is incorrect please try again',parent=dbroot)
            return

        try:
            strr = 'create database sarathimanagementsystem'
            my_cursor.execute(strr)
            strr = 'use sarathimanagementsystem'
            my_cursor.execute(strr)
            strr = 'create table membersdata (id int ,name varchar(30),mobile varchar(12),address varchar(100),gender varchar(10),dob varchar(20))'
            my_cursor.execute(strr)
            strr = 'alter table membersdata modify column id int not null'
            my_cursor.execute(strr)
            strr = 'alter table membersdata modify column id int primary key'
            my_cursor.execute(strr)
        except:
            strr ='use sarathimanagementsystem'
            my_cursor.execute(strr)
    dbroot =Toplevel()
    dbroot.grab_set()
    dbroot.geometry('400x205+320+180')
    dbroot.focus()
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')

    host_label=tk.Label(dbroot,text='Enter Host : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=5,anchor='w',relief='groove')
    host_label.place(x=10,y=10)

    user_label=tk.Label(dbroot,text='Enter User : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=5,anchor='w',relief='groove')
    user_label.place(x=10,y=60)

    password_label=tk.Label(dbroot,text='Enter Password : ',bg='light green',fg='blue',font=('times new roman',18),
                      width=12,borderwidth=5,anchor='w',relief='groove')
    password_label.place(x=10,y=110)

    host_var=tk.StringVar()
    user_var=tk.StringVar()
    password_var=tk.StringVar()
    
    host_entry=tk.Entry(dbroot,textvariable=host_var,fg='blue',font=('times new roman',18),
                      width=14,borderwidth=5,relief='groove')
    host_entry.place(x=200,y=10)
    host_entry.focus()

    user_entry=tk.Entry(dbroot,textvariable=user_var,fg='blue',font=('times new roman',18),
                      width=14,borderwidth=5,relief='groove')
    user_entry.place(x=200,y=60)

    password_entry=tk.Entry(dbroot,textvariable=password_var,fg='blue',font=('times new roman',18),
                      width=14,borderwidth=5,relief='groove')
    password_entry.place(x=200,y=110)

    submit_btn=tk.Button(dbroot,width=5,text='Submit',command=submitdb,bg='light green',fg='blue',
                        activebackground='gold2',activeforeground='blue',font=('times new roman',18))
    submit_btn.place(x=144,y=155)

    dbroot.mainloop()

entry_box=tk.Button(win,width=18,text='Connect to Database',bg='light green',command=connectdb
                    ,activebackground='yellow',activeforeground='red',fg='blue',font=('times new roman',10))
entry_box.place(x=660,y=60)

win.mainloop()



