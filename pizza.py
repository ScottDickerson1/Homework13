import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('750x300')
        self.main_window.title('Add to your $5 pizza!')

        self.topframe = tkinter.Frame(self.main_window)
        self.midframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.name_prompt = tkinter.Label(self.topframe,text='Please enter your name in the prompt below:',fg='green',font=35)
        self.name_entry = tkinter.Entry(self.topframe,width=20)
        self.toppings_label = tkinter.Label(self.midframe,text='Please Select your Toppings',fg='green',font=35)
        self.spacer1 = tkinter.Label(self.midframe,text='')
        self.crust_label = tkinter.Label(self.bottomframe,text='Please select a crust',fg='green',font=35)
        self.spacer2 = tkinter.Label(self.bottomframe,text='')

        self.name_prompt.pack()
        self.name_entry.pack()
        self.spacer1.pack()
        self.toppings_label.pack()
        self.spacer2.pack()
        self.crust_label.pack()

        self.base_cost = tkinter.IntVar(value=5)
        self.total_cost = tkinter.IntVar()

        self.pep = tkinter.IntVar()
        self.sausage = tkinter.IntVar()
        self.olives = tkinter.IntVar()
        self.mush = tkinter.IntVar()
        self.toppings_cost = tkinter.IntVar()

        self.cb_pep = tkinter.Checkbutton(self.midframe,text='Pepperoni',variable=self.pep)
        self.cb_sausage = tkinter.Checkbutton(self.midframe,text='Sausage',variable=self.sausage)
        self.cb_olives = tkinter.Checkbutton(self.midframe,text='Olives',variable=self.olives)
        self.cb_mush = tkinter.Checkbutton(self.midframe,text='Mushrooms',variable=self.mush)

        self.cb_pep.pack(side='left')
        self.cb_sausage.pack(side='left')
        self.cb_olives.pack(side='left')
        self.cb_mush.pack(side='left')

        self.crust_cost = tkinter.IntVar()

        self.rb_stuffed = tkinter.Radiobutton(self.bottomframe,text='Stuffed Crust',variable=self.crust_cost,value=4)
        self.rb_thin = tkinter.Radiobutton(self.bottomframe,text='Thin Crust',variable=self.crust_cost,value=2)
        self.rb_reg = tkinter.Radiobutton(self.bottomframe,text='Regular Crust',variable=self.crust_cost,value=0)

        self.rb_reg.select()

        self.rb_reg.pack(side='left')
        self.rb_stuffed.pack(side='left')
        self.rb_thin.pack(side='left')

        self.topframe.pack()
        self.midframe.pack()
        self.bottomframe.pack()

        self.calcbutton = tkinter.Button(self.main_window,text='Calculate Cost',bg='green',fg='white',command=self.get_cost)
        self.quitbutton = tkinter.Button(self.main_window,text='Quit',bg='red',fg='white',command=self.main_window.destroy)

        self.calcbutton.pack(side='left')
        self.quitbutton.pack(side='right')


        tkinter.mainloop()

    def get_cost(self):
        name = self.name_entry.get()
        additional_cost = 0
        if self.pep.get() == 1:
            additional_cost += 3
        if self.sausage.get() == 1:
            additional_cost += 4
        if self.olives.get() == 1:
            additional_cost += 2
        if self.mush.get() == 1:
            additional_cost += 5
        self.toppings_cost.set(additional_cost)
        total_cost = self.crust_cost.get() + self.toppings_cost.get() + self.base_cost.get()
        self.total_cost.set(total_cost)
        tkinter.messagebox.showinfo('Pizza Cost', name + ', your pizza will cost ' + str(self.total_cost.get()))



MyGUI = MyGUI()
