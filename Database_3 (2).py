#import modules

from tkinter import *
from tkinter import messagebox
import sqlite3
from tkcalendar import *
from tkinter import ttk


# create a window
root = Tk()

# set a title for the window
root.title("book_student")

root.geometry("980x420")
root.configure(pady = 20 , padx = 20)

frame = LabelFrame( root  , bg ="#f0ca0c" , text = "   ..... Book Form .....   ",width= 940, height = 360 , bd = 5 , fg = "#4a4948" , font = "Helvetica").place(x = 0 , y = 0 )
# connect to database if exist or if doesnt exit create one
conn= sqlite3.connect("Books_table.bd")
conn1 =  conn = sqlite3.connect('library.bd')


#create cursors
Cursor = conn.cursor()
Cursor1 = conn1.cursor()

#seelect all the items of table
Cursor1.execute("SELECT * , oid FROM student")
records = Cursor1.fetchall()

Subject_list = ["Select the subject" , "Scientific" , "Story" , "Study Course" , "Art" , "Sport" , "Funny" , "Adventuries"]
option = [" none"]


for record in records :
	option.append(record[0]+" "+record[1])




#create a table and comment it after you run the program becuse it often try to make another table 
'''
Cursor.execute(""" CREATE TABLE books (

			book_name text ,
			book_number integer ,
			book_writer text ,
			book_subject text ,
			available_num integer ,
			availablity text ,
			barrower text ,
			return_date text
			)""") '''



def show():
	global print_reord
	print_reord = ''


	# connect to database if exist or if doesnt exit create one
	conn= sqlite3.connect("Books_table.bd")


	#create cursors
	Cursor = conn.cursor()

	Cursor.execute("SELECT * , oid FROM books")
	records = Cursor.fetchall()

	Query_window = Toplevel()
	Query_window.title("Show Table ...")
	Frm = Frame(Query_window)
	Frm.pack()

	Table = ttk.Treeview(Frm , column = (1,2,3,4,5,6,7,8) , show = "headings" , height = 5 )
	Table.pack(side =LEFT , padx=20 , pady =20 )

	Table.heading(1 , text = "Book name")
	Table.column(1 , width =130)
	Table.heading(2 , text = "Book number")
	Table.column(2 , width =130)
	Table.heading(3 , text = "Book writer")
	Table.column(3 , width =130)
	Table.heading(4 , text = "Book subject")
	Table.column(4 , width =130)
	Table.heading(5 , text = "Quantity")
	Table.column(5 , width =130)
	Table.heading(6 , text = "Borrower")
	Table.column(6 , width =130)
	Table.heading(7 , text = "Return date")
	Table.column(7 , width =130)
	Table.heading(8 , text = "Availability")
	Table.column(8 , width =130)

	
	# insert values to the table 
	for record in records:
		Table.insert("", "end" , value =record )


	#Commit changes
	conn.commit()
	#close database
	conn.close()



def add():
	# connect to database if exist or if doesnt exit create one
	conn= sqlite3.connect("Books_table.bd")
	#create cursors
	Cursor = conn.cursor()

	if b_name.get() != "" and b_num.get() != "":
		# Insert value to table 
		Cursor.execute("INSERT INTO books VALUES ( :b_name , :b_num , :b_writer , :b_subjet , :available_num  , :borrower , :returndate, :Availablity)",
			{
				'b_name': b_name.get() ,
				'b_num' : b_num.get() ,
				'b_writer' : b_writer.get(),
				'b_subjet' : Subject.get(),
				'available_num' : available_num.get(),
				'borrower' : borrower.get(),
				'returndate' : Returndate.get(),
				'Availablity': var.get() 
			})
	else :
		response = messagebox.showerror("Fill the Form ..." , "Please Fill the Form !")

	#Commit changes
	conn.commit()
	#close database
	conn.close()

	#Clear text boxes
	b_name.delete( 0 , END)
	b_num.delete( 0, END)
	b_writer.delete( 0 , END)
	available_num.delete(0 , END)
	Returndate.delete( 0 , END)
	Returndate.insert(0 ," Available ")


def Delete_ID():
	if Select_DELETE.Book_ID_editor.get() == "Select an Item " :
		response = messagebox.showerror("Select an item ... " , "Please select an item from the menu ! ")
		Select_DELETE.select.destroy()

	else :	

		# connect to database if exist or if doesnt exit create one
		conn= sqlite3.connect("Books_table.bd")


		#create cursors
		Cursor = conn.cursor()

		Cursor.execute("DELETE FROM books WHERE oid = " + Select_DELETE.Book_ID_editor.get())

		#Commit changes
		conn.commit()
		#close database
		conn.close()
		Select_DELETE.select.destroy()


def Delete_NAME():
	if Select_DELETE.Book_name_editor.get() == "Select an Item " :
		response = messagebox.showerror("Select an item ... " , "Please select an item from the menu ! ")
		Select_DELETE.select.destroy()

	else :	


		# connect to database if exist or if doesnt exit create one
		conn= sqlite3.connect("Books_table.bd")


		#create cursors
		Cursor = conn.cursor()

		Cursor.execute( 'DELETE FROM books WHERE book_name = ? ' , (Select_DELETE.Book_name_editor.get() ,))
		#Commit changes
		conn.commit()
		#close database
		conn.close()
		Select_DELETE.select.destroy()

	
def Update_ID ():
	# connect to database if exist or if doesnt exit create one
	conn= sqlite3.connect("Books_table.bd")
	#create cursors
	Cursor = conn.cursor()

	#Insert new value instead of old one in the table 
	Cursor.execute("""UPDATE books SET 
		book_name =(?) ,
		book_number =(?),
		book_writer =(?),
		book_subject =(?),
		available_num =(?),
		barrower = (?),
		return_date = (?),
		available= (?)
		WHERE oid = (?) """ , 
		(b_name_editor1.get(),
		b_num_editor1.get() ,
		b_writer_editor1.get(),
		Subject_editor1.get(),
		available_num_editor1.get(),
		borrower.get(),
		Returndate_editor_1.get(),
		var.get(),
		Select_EDIT.Book_ID_editor.get()
		 ))


	#Commit changes
	conn.commit()
	#close database
	conn.close()

	editor1.destroy()




def open_calender_ID(Returndate_editor1):
	window = Toplevel()
	window.title("Calender")
	open_calender_ID.cal = Calendar( window , selectmode = "day" , year = 2020 , month = 8 )
	open_calender_ID.cal.grid(row = 0 , column = 0 )

	def get_date(cal ,Returndate_editor1):
		date = cal.get_date()
		Returndate_editor1.delete(0 , END)
		Returndate_editor1.insert(0 , date)
		window.destroy()
	date_button = Button(window , text = "Select the date" , width = 35 , bg = "#403f3c" , fg = "#ffffff" , command =lambda : get_date(open_calender_ID.cal , Returndate_editor1) ).grid(row = 1 , column = 0)
		

def ID_FIND():

	if Select_EDIT.Book_ID_editor.get() == "Select an Item " :
		response = messagebox.showerror("Select an item ... " , "Please select an item from the menu ! ")
		Select_EDIT.select.destroy()

	else :	
		selected  = int(Select_EDIT.Book_ID_editor.get())

		if selected in  Select_EDIT.ID :

			Select_EDIT.select.destroy()

			global option
			global b_name_editor1
			global b_num_editor1
			global b_writer_editor1
			global available_num_editor1
			global Subject_editor1
			global borrower
			global Returndate_editor_1
			global editor1

			editor1 = Toplevel()

			editor1.title("Edit")

			editor1.configure(bg = "#f0ca0c")

			editor1.geometry("875x430")

			# connect to database if exist or if doesnt exit create one
			conn= sqlite3.connect("Books_table.bd")

			#create cursors
			Cursor = conn.cursor()

			Cursor.execute( 'SELECT * FROM books WHERE oid = ? ' , (Select_EDIT.Book_ID_editor.get() ,))
			records1 = Cursor.fetchall()	




			borrower = StringVar()
			Subject_editor1 = StringVar()

			#create text boxes
			b_name_editor1= Entry( editor1 , width = 30 , bd = 5)
			b_name_editor1.grid( row = 0 , column = 1 , pady = (30 , 30) )


			b_num_editor1 = Entry( editor1 , width = 30 , bd = 5)
			b_num_editor1.grid( row =0, column = 3 , pady = (30 ,30), columnspan = 2 )


			b_writer_editor1= Entry( editor1 , width = 30 , bd = 5)
			b_writer_editor1.grid( row = 1 , column = 1 , pady = (30 , 30))

			available_num_editor1 = Entry( editor1 , width = 30 , bd = 5)
			available_num_editor1.grid(row = 1 , column = 3 ,  pady = (30 ,30) , columnspan = 2 )

			b_subjet_editor1 = OptionMenu(editor1 , Subject_editor1 , *Subject_list )
			b_subjet_editor1.grid(row = 2 , column = 1 ,pady = (30 ,30),  padx =5 )
			b_subjet_editor1.config(bg = "#f0ca0c" , fg= "#080226" , font ="Arial 8 bold " , width = 30 )


			ID_FIND.Returndate_editor1 = Entry( editor1 , width = 30 , bd = 5)
			ID_FIND.Returndate_editor1.grid( row = 2, column = 3 , pady = (30 ,30), columnspan = 2 )
			ID_FIND.Returndate_editor1.insert(0 ," Available ")

			Returndate_editor_1 = ID_FIND.Returndate_editor1
			cal_button_editor1 =Button(editor1 , text = "v" , command = lambda : open_calender(Returndate_editor_1), state =NORMAL ,bg ="#09011c" , fg = "#f0ca0c"  ).grid(row = 2 , column =4 , padx = (100 ,0))


			Borrow_editor1 = OptionMenu(editor1 , borrower, *option )
			Borrow_editor1.grid(row = 3 , column = 1 )
			Borrow_editor1.config(bg = "#f0ca0c" , fg= "#080226" , font ="Arial 8 bold " , width = 30)


					
			available_editor1 = Checkbutton(editor1 , text = "Available" , variable=var , onvalue = "Available" ,offvalue = "Unavailable", bg = "#f0ca0c" , fg= "#080226" , font ="Arial 8 bold " )
			available_editor1.grid(row = 3 ,column = 3)

			Unavailable_editor1 = Checkbutton(editor1 , text = "Unavailable" , variable=var , onvalue = "Unavailable" ,offvalue = "Available", bg = "#f0ca0c" , fg= "#080226" , font ="Arial 8 bold " )
			Unavailable_editor1.grid(row = 3 ,column = 4)

			# create text labels

			b_name_lab_editor1 = Label( editor1 , text = "      Book name :" , font = "Arial 12 bold " , bg ="#f0ca0c" , fg = "#080226")
			b_name_lab_editor1.grid(row = 0 , column = 0 , pady = (30 , 30) , padx = 5)


			b_num_lab_editor1 = Label( editor1 , text = "Book number :" , font = "Arial 12 bold" , bg ="#f0ca0c", fg = "#080226")
			b_num_lab_editor1.grid(row = 0 , column = 2 , pady = (30 , 30) , padx = 5)

			b_writer_lab_editor1 = Label( editor1 , text = "     Book Writer :" , font = "Arial 12 bold" , bg ="#f0ca0c", fg = "#080226")
			b_writer_lab_editor1.grid(row = 1 , column = 0 , pady = (30 , 30) , padx = 5)

				 
			b_subject_lab_editor1 = Label( editor1 , text = "Subject  :" , font = "Arial 12 bold" , bg ="#f0ca0c", fg = "#080226")
			b_subject_lab_editor1.grid(row = 2 , column =0 , pady = (30 , 30) , padx = 5)


			b_quantity_lab_editor1 = Label( editor1 , text = "quantity :" , font = "Arial 12 bold" , bg ="#f0ca0c", fg = "#080226")
			b_quantity_lab_editor1.grid(row = 1 , column = 2 , pady = (30 , 30) , padx = 5)


			return_date_lab_editor1 = Label(editor1 , text = "Return date : " , font = "Arial 12 bold" , bg = "#f0ca0c", fg = "#080226")
			return_date_lab_editor1.grid(row = 2 , column = 2 , pady = (30 , 30) , padx = 5)



			borrower_lab_editor1 = Label(editor1 , text = "Borrower : " , font = "Arial 12 bold" , bg = "#f0ca0c", fg = "#080226")
			borrower_lab_editor1.grid(row = 3 , column = 0 , pady = (30 , 30) , padx = 5)


			availablity_lab_editor1 = Label(editor1 , text = "availability : " , font = "Arial 12 bold" , bg = "#f0ca0c", fg = "#080226")
			availablity_lab_editor1.grid(row = 3 , column = 2 , pady = (30 , 30) , padx = (5,20))

			# Create a Save button 
			Save_button_editor1  = Button(editor1 , text = "Save a record" , font = "Arial 14 bold" ,bd = 6,bg = "#080226", fg = "#f0ca0c" , command = Update_ID)
			Save_button_editor1.grid(row  = 4 , column = 0 , ipadx = 360 ,ipady = 15 , columnspan = 6)

			#Commit changes
			conn.commit()

			#close database
			conn.close()

			for record in records1:
				b_name_editor1.insert( 0 , record[0])
				b_num_editor1.insert( 0, record[1])
				b_writer_editor1.insert( 0 , record[2])
				Subject_editor1.set(record[3])
				available_num_editor1.insert( 0 , record[4])
				if record[7] == "Available" :
					available_editor1.select()
				else : 
					Unavailable_editor1.select()
				borrower.set(record[5])
				ID_FIND.Returndate_editor1.delete(0 , END)
				ID_FIND.Returndate_editor1.insert(0 , record[6])
			


def Update_Name ():
	# connect to database if exist or if doesnt exit create one
	conn= sqlite3.connect("Books_table.bd")
	#create cursors
	Cursor = conn.cursor()

	#Insert new value instead of old one in the table 
	Cursor.execute("""UPDATE books SET 
		book_name =(?) ,
		book_number =(?),
		book_writer =(?),
		book_subject =(?),
		available_num =(?),
		barrower = (?),
		return_date = (?),
		available= (?)
		WHERE book_name = (?) """ , 
		(b_name_editor2.get(),
		b_num_editor2.get() ,
		b_writer_editor2.get(),
		Subject_editor2.get(),
		available_num_editor2.get(),
		borrower.get(),
		Returndate_editor_2.get(),
		var.get(),
		Select_EDIT.Book_name_editor.get()
		 ))


	#Commit changes
	conn.commit()
	#close database
	conn.close()

	editor2.destroy()
	window.destroy()


# Opening calender and selecting the date


def open_calender_name(Returndate_editor2):
	global window 
	window = Toplevel()
	window.title("Calender")
	open_calender_name.cal = Calendar( window , selectmode = "day" , year = 2020 , month = 8 )
	open_calender_name.cal.grid(row = 0 , column = 0 )

	def get_date(cal ,Returndate_editor2):
		date = cal.get_date()
		Returndate_editor2.delete(0 , END)
		Returndate_editor2.insert(0 , date)
		window.destroy()
	date_button = Button(window , text = "Select the date" , width = 35 , bg = "#403f3c" , fg = "#ffffff" , command =lambda : get_date(open_calender_name.cal , Returndate_editor2) ).grid(row = 1 , column = 0)
	


def NAME_FIND():
	if Select_EDIT.Book_name_editor.get() in Select_EDIT.Book_name :
		global option
		global b_name_editor2
		global b_num_editor2
		global b_writer_editor2
		global available_num_editor2
		global Subject_editor2
		global borrower
		global Returndate_editor_2
		global editor2


		editor2 = Toplevel()

		editor2.title("Edit")

		editor2.configure(bg = "#f0ca0c")

		editor2.geometry("875x430")

		

		borrower = StringVar()

		Subject_editor2 = StringVar()


		# connect to database if exist or if doesnt exit create one
		conn= sqlite3.connect("Books_table.bd")

		#create cursors
		Cursor = conn.cursor()
		
		Cursor.execute( 'SELECT * FROM books WHERE book_name = ? ' , (Select_EDIT.Book_name_editor.get() ,))
		records = Cursor.fetchall()	




		#create text boxes
		b_name_editor2= Entry( editor2 , width = 30 , bd = 5)
		b_name_editor2.grid( row = 0 , column = 1 , pady = (30 , 30) )


		b_num_editor2 = Entry( editor2 , width = 30 , bd = 5)
		b_num_editor2.grid( row =0, column = 3 , pady = (30 ,30), columnspan = 2 )


		b_writer_editor2= Entry( editor2 , width = 30 , bd = 5)
		b_writer_editor2.grid( row = 1 , column = 1 , pady = (30 , 30))

		available_num_editor2 = Entry( editor2 , width = 30 , bd = 5)
		available_num_editor2.grid(row = 1 , column = 3 ,  pady = (30 ,30) , columnspan = 2 )

		b_subjet_editor2 = OptionMenu(editor2 , Subject_editor2 , *Subject_list )
		b_subjet_editor2.grid(row = 2 , column = 1 ,pady = (30 ,30),  padx =5 )
		b_subjet_editor2.config(bg = "#f0ca0c" , fg= "#080226" , font ="Arial 8 bold " , width = 30 )


		NAME_FIND.Returndate_editor2 = Entry( editor2 , width = 30 , bd = 5)
		NAME_FIND.Returndate_editor2.grid( row = 2, column = 3 , pady = (30 ,30), columnspan = 2 )
		NAME_FIND.Returndate_editor2.insert(0 ," Available ")

		Returndate_editor_2=NAME_FIND.Returndate_editor2
		cal_button_editor2 =Button(editor2 , text = "v" , command = lambda : open_calender_name(Returndate_editor_2), state =NORMAL ,bg ="#09011c" , fg = "#f0ca0c"  ).grid(row = 2 ,column =4 , padx = (100 ,0))


		Borrow_editor2 = OptionMenu(editor2 , borrower, *option )
		Borrow_editor2.grid(row = 3 , column = 1 )
		Borrow_editor2.config(bg = "#f0ca0c" , fg= "#080226" , font ="Arial 8 bold " , width = 30)


			
		available_editor2 = Checkbutton(editor2 , text = "Available" , variable=var , onvalue = "Available" ,offvalue = "Unavailable", bg = "#f0ca0c" , fg= "#080226" , font ="Arial 8 bold " )
		available_editor2.grid(row = 3 ,column = 3)

		Unavailable_editor2 = Checkbutton(editor2 , text = "Unavailable" , variable=var , onvalue = "Unavailable" ,offvalue = "Available", bg = "#f0ca0c" , fg= "#080226" , font ="Arial 8 bold " )
		Unavailable_editor2.grid(row = 3 ,column = 4)

		# create text labels

		b_name_lab_editor2 = Label( editor2 , text = "      Book name :" , font = "Arial 12 bold " , bg ="#f0ca0c" , fg = "#080226")
		b_name_lab_editor2.grid(row = 0 , column = 0 , pady = (30 , 30) , padx = 5)


		b_num_lab_editor2 = Label( editor2 , text = "Book number :" , font = "Arial 12 bold" , bg ="#f0ca0c", fg = "#080226")
		b_num_lab_editor2.grid(row = 0 , column = 2 , pady = (30 , 30) , padx = 5)

		b_writer_lab_editor2 = Label( editor2, text = "     Book Writer :" , font = "Arial 12 bold" , bg ="#f0ca0c", fg = "#080226")
		b_writer_lab_editor2.grid(row = 1 , column = 0 , pady = (30 , 30) , padx = 5)

		 
		b_subject_lab_editor2 = Label( editor2 , text = "Subject  :" , font = "Arial 12 bold" , bg ="#f0ca0c", fg = "#080226")
		b_subject_lab_editor2.grid(row = 2 , column =0 , pady = (30 , 30) , padx = 5)


		b_quantity_lab_editor2 = Label( editor2 , text = "quantity :" , font = "Arial 12 bold" , bg ="#f0ca0c", fg = "#080226")
		b_quantity_lab_editor2.grid(row = 1 , column = 2 , pady = (30 , 30) , padx = 5)


		return_date_lab_editor2 = Label(editor2 , text = "Return date : " , font = "Arial 12 bold" , bg = "#f0ca0c", fg = "#080226")
		return_date_lab_editor2.grid(row = 2 , column = 2 , pady = (30 , 30) , padx = 5)



		borrower_lab_editor2 = Label(editor2 , text = "Borrower : " , font = "Arial 12 bold" , bg = "#f0ca0c", fg = "#080226")
		borrower_lab_editor2.grid(row = 3 , column = 0 , pady = (30 , 30) , padx = 5)


		availablity_lab_editor2 = Label(editor2 , text = "availability : " , font = "Arial 12 bold" , bg = "#f0ca0c", fg = "#080226")
		availablity_lab_editor2.grid(row = 3 , column = 2 , pady = (30 , 30) , padx = (5,20))

		# Create a Save button 
		Save_button_editor2  = Button(editor2 , text = "Save a record" , font = "Arial 14 bold" ,bd = 6,bg = "#080226", fg = "#f0ca0c" , command = Update_Name)
		Save_button_editor2.grid(row  = 4 , column = 0 , ipadx = 360 ,ipady = 15 , columnspan = 6)

		#Commit changes
		conn.commit()

		#close database
		conn.close()



		for record in records:
			b_name_editor2.insert( 0 , record[0])
			b_num_editor2.insert( 0, record[1])
			b_writer_editor2.insert( 0 , record[2])
			Subject_editor2.set(record[3])
			available_num_editor2.insert( 0 , record[4])
			if record[7] == "Available" :
				available_editor2.select()
			else : 
				Unavailable_editor2.select()
			borrower.set(record[5])
			NAME_FIND.Returndate_editor2.delete(0 , END)
			NAME_FIND.Returndate_editor2.insert(0 , record[6])
	else : 
		response = messagebox.showerror("Select an item ... " , "Please select an item from the menu ! ")
		Select_EDIT.select.destroy()


def Select_EDIT() :
	Select_EDIT.select = Toplevel()

	Select_EDIT.select.title("Search ...")

	Select_EDIT.select.configure(pady = 30 , padx = 30 , bg ="#09011c"  )

	# connect to database if exist or if doesnt exit create one
	conn= sqlite3.connect("Books_table.bd")

	#create cursors
	Cursor = conn.cursor()

	

	Select_EDIT.Book_name_editor = StringVar()
	Select_EDIT.Book_name_editor.set("Select an Item ")


	Select_EDIT.Book_ID_editor = StringVar()
	Select_EDIT.Book_ID_editor.set("Select an Item ")

	Select_EDIT.Book_name = []

	Select_EDIT.ID = []

	Cursor.execute("SELECT * , oid FROM books")
	records2= Cursor.fetchall()

	for row in records2:
		Select_EDIT.Book_name.append(row[0])
		Select_EDIT.ID.append(row[8])


	#Create a text boxes
	Select_EDIT.BOOK_ID = OptionMenu(Select_EDIT.select , Select_EDIT.Book_ID_editor , *Select_EDIT.ID )
	Select_EDIT.BOOK_ID.grid(row = 0 , column =1 , padx = (18, 0) ,ipadx = 12 , pady =(0 , 10) )
	Select_EDIT.BOOK_ID.configure(bg ="#09011c" , fg = "#f0ca0c" ,  width=  21 )

	
	Select_EDIT.BOOK_NAME = OptionMenu(Select_EDIT.select , Select_EDIT.Book_name_editor , *Select_EDIT.Book_name )
	Select_EDIT.BOOK_NAME.grid(row = 1 , column =1 , padx = (18, 0),ipadx = 12 )
	Select_EDIT.BOOK_NAME.configure(bg ="#09011c" , fg = "#f0ca0c" ,  width=  21 )

	#Create labels for text boxes
	Search_id_lab = Label(Select_EDIT.select , text = "Search Book By ID :", font = "Arial 10 bold" , fg ="#f0ca0c" , bg = "#09011c")
	Search_id_lab.grid(row = 0 , column = 0, pady =(0 , 10) )

	Search_name_lab = Label(Select_EDIT.select , text = "Search Book By Name :" , font = "Arial 10 bold" , fg ="#f0ca0c" , bg = "#09011c")
	Search_name_lab.grid(row = 1 , column = 0)




	#Create Buttons
	ID_find = Button(Select_EDIT.select , text = "EDIT" , bd = 3  , fg ="#09011c" , bg = "#f0ca0c", font = "Arial 8 bold" , command = ID_FIND)
	ID_find.grid(row = 0 , column = 2, padx=(10 ,0), pady =(0 , 10) )

	Name_find = Button(Select_EDIT.select , text = "EDIT" , bd = 3, fg ="#09011c" , bg = "#f0ca0c", font = "Arial 8 bold", command = NAME_FIND)
	Name_find.grid(row = 1 , column = 2  , padx=(10 ,0))


	#Commit changes
	conn.commit()

	#close database
	conn.close()


def Select_DELETE() :
	Select_DELETE.select = Toplevel()

	Select_DELETE.select.title("Search ...")

	Select_DELETE.select.configure(pady = 30 , padx = 30 , bg ="#09011c"  )

	# connect to database if exist or if doesnt exit create one
	conn= sqlite3.connect("Books_table.bd")

	#create cursors
	Cursor = conn.cursor()

	

	Select_DELETE.Book_name_editor = StringVar()
	Select_DELETE.Book_name_editor.set("Select an Item ")


	Select_DELETE.Book_ID_editor = StringVar()
	Select_DELETE.Book_ID_editor.set("Select an Item ")

	Select_DELETE.Book_name = []

	Select_DELETE.ID = []

	Cursor.execute("SELECT * , oid FROM books")
	records2= Cursor.fetchall()

	for row in records2:
		Select_DELETE.Book_name.append(row[0])
		Select_DELETE.ID.append(row[8])


	#Create a text boxes
	Select_DELETE.BOOK_ID = OptionMenu(Select_DELETE.select , Select_DELETE.Book_ID_editor , *Select_DELETE.ID )
	Select_DELETE.BOOK_ID.grid(row = 0 , column =1 , padx = (18, 0) ,ipadx = 12 , pady =(0 , 10) )
	Select_DELETE.BOOK_ID.configure(bg ="#09011c" , fg = "#f0ca0c" ,  width=  21 )

	
	Select_DELETE.BOOK_NAME = OptionMenu(Select_DELETE.select , Select_DELETE.Book_name_editor , *Select_DELETE.Book_name )
	Select_DELETE.BOOK_NAME.grid(row = 1 , column =1 , padx = (18, 0),ipadx = 12 )
	Select_DELETE.BOOK_NAME.configure(bg ="#09011c" , fg = "#f0ca0c" ,  width=  21 )

	#Create labels for text boxes
	Search_id_lab = Label(Select_DELETE.select , text = "Search Book By ID :", font = "Arial 10 bold" , fg ="#f0ca0c" , bg = "#09011c")
	Search_id_lab.grid(row = 0 , column = 0, pady =(0 , 10) )

	Search_name_lab = Label(Select_DELETE.select , text = "Search Book By Name :" , font = "Arial 10 bold" , fg ="#f0ca0c" , bg = "#09011c")
	Search_name_lab.grid(row = 1 , column = 0)




	#Create Buttons
	ID_find = Button(Select_DELETE.select , text = "Delete" , bd = 3  , fg ="#09011c" , bg = "#f0ca0c", font = "Arial 8 bold" , command = Delete_ID)
	ID_find.grid(row = 0 , column = 2, padx=(10 ,0), pady =(0 , 10) )

	Name_find = Button(Select_DELETE.select , text = "Delete" , bd = 3, fg ="#09011c" , bg = "#f0ca0c", font = "Arial 8 bold", command = Delete_NAME)
	Name_find.grid(row = 1 , column = 2  , padx=(10 ,0))


	#Commit changes
	conn.commit()

	#close database
	conn.close()



# Opening calender and selecting the date

def open_calender(Returndate):
	window = Toplevel()
	window.title("Calender")
	open_calender.cal = Calendar( window , selectmode = "day" , year = 2020 , month = 8 )
	open_calender.cal.grid(row = 0 , column = 0 )

	def get_date(cal ,Returndate):
		date = cal.get_date()
		Returndate.delete(0 , END)
		Returndate.insert(0 , date)
		window.destroy()
	date_button = Button(window , text = "Select the date" , width = 35 , bg = "#403f3c" , fg = "#ffffff" , command =lambda : get_date(open_calender.cal , Returndate) ).grid(row = 1 , column = 0)
	

var =StringVar()
borrower = StringVar()
borrower.set(option[0])



Subject = StringVar()
Subject.set(Subject_list[0])
#create text boxes
b_name = Entry( frame , width = 30 , bd = 5)
b_name.grid( row = 0 , column = 1 , pady = (30 , 30) )


b_num = Entry( frame , width = 30 , bd = 5)
b_num.grid( row =0, column = 3 , pady = (30 ,30))


b_writer= Entry( frame , width = 30 , bd = 5)
b_writer.grid( row = 1 , column = 1 , pady = (30 , 30))

available_num = Entry( frame , width = 30 , bd = 5)
available_num.grid(row = 1 , column = 3 ,  pady = (30 ,30) )

b_subjet = OptionMenu(frame , Subject , *Subject_list )
b_subjet.grid(row = 2 , column = 1 ,pady = (30 ,30),  padx =5 )
b_subjet.config(bg = "#f0ca0c" , fg= "#080226" , font ="Arial 8 bold " , width = 30 )


Returndate = Entry( frame , width = 30 , bd = 5)
Returndate.grid( row = 2, column = 3 , pady = (30 ,30) )
Returndate.insert(0 ," Available ")

cal_button =Button(frame , text = "v" , command = lambda : open_calender(Returndate), state =NORMAL ,bg ="#09011c" , fg = "#f0ca0c"  ).place(x =870 , y =205 )





Borrower = OptionMenu(frame , borrower , *option )
Borrower.grid(row = 3 , column = 1 )
Borrower.config(bg = "#f0ca0c" , fg= "#080226" , font ="Arial 8 bold " , width = 30)

available = Checkbutton(frame , text = "Available" , variable=var , onvalue = "Available" ,offvalue = "Unavailable", bg = "#f0ca0c" , fg= "#080226" , font ="Arial 8 bold " )
available.place(x =685 , y =295 )

Unavailable = Checkbutton(frame , text = "Unavailable" , variable=var , onvalue = "Unavailable" , offvalue = "Available", bg = "#f0ca0c" , fg= "#080226" , font ="Arial 8 bold " )
Unavailable.place(x =785 , y =295 )
Unavailable.deselect()

# create text labels

b_name_lab = Label( frame , text = "      Book name :" , font = "Arial 12 bold " , bg ="#f0ca0c" , fg = "#080226")
b_name_lab.grid(row = 0 , column = 0 , pady = (30 , 30) , padx = 5)


b_num_lab = Label( frame , text = "Book number :" , font = "Arial 12 bold" , bg ="#f0ca0c", fg = "#080226")
b_num_lab.grid(row = 0 , column = 2 , pady = (30 , 30) , padx = 5)

b_writer_lab = Label( frame , text = "     Book Writer :" , font = "Arial 12 bold" , bg ="#f0ca0c", fg = "#080226")
b_writer_lab.grid(row = 1 , column = 0 , pady = (30 , 30) , padx = 5)

 
b_subject_lab = Label( frame , text = "Subject  :" , font = "Arial 12 bold" , bg ="#f0ca0c", fg = "#080226")
b_subject_lab.grid(row = 2 , column =0 , pady = (30 , 30) , padx = 5)


b_quantity_lab = Label( frame , text = "quantity :" , font = "Arial 12 bold" , bg ="#f0ca0c", fg = "#080226")
b_quantity_lab.grid(row = 1 , column = 2 , pady = (30 , 30) , padx = 5)


return_date_lab = Label(frame , text = "Return date : " , font = "Arial 12 bold" , bg = "#f0ca0c", fg = "#080226")
return_date_lab.grid(row = 2 , column = 2 , pady = (30 , 30) , padx = 5)



borrower_lab = Label(frame , text = "Borrower : " , font = "Arial 12 bold" , bg = "#f0ca0c", fg = "#080226")
borrower_lab.grid(row = 3 , column = 0 , pady = (30 , 30) , padx = 5)


availablity_lab = Label(frame , text = "availability : " , font = "Arial 12 bold" , bg = "#f0ca0c", fg = "#080226")
availablity_lab.grid(row = 3 , column = 2 , pady = (30 , 30) , padx = (5,20))



#Buttons

#Create a button to add a record to database
add_button = Button(root , text = "Add record"  , width = 25, bg = "#09011c" , fg = "#ffffff", font = "Arial 10 bold" , command = add)
add_button.grid( row = 4, column =0 , pady = (11 , 0 ) ,padx = (0 , 26)  )

#Create a button to Edit a record
Edit_button = Button(root , text = "Edit a record"  , width = 25 , bg = "#09011c" , fg = "#ffffff", font = "Arial 10 bold",command = Select_EDIT)
Edit_button.grid( row = 4, column =1 , pady = (11 , 0 )   ,padx = (0 , 13))

#Create a button to delete a record from the database
delete_button = Button(root , text = "Delete a record"  , width = 25, bg = "#09011c" , fg = "#ffffff", font = "Arial 10 bold" , command = Select_DELETE)
delete_button.grid( row = 4, column =2 , pady = (11 , 0 ) ,padx = (13, 0)  )


#Create a button to add a record to database
show_button = Button(root , text = "Show record"  , width = 25, bg = "#09011c" , fg = "#ffffff", font = "Arial 10 bold", command = show)
show_button.place(x = 724 , y = 360 )



# commit changes
conn.commit()
conn1.commit()


#close the databases
conn.close()
conn1.close()

root.mainloop()
