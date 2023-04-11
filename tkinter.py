#MAIN
from tkinterx import aplication

jan = aplication()



from tkinter import *
from tkinter import ttk
from create import inserir_filmes, inserir_usuarios

janela = Tk()



#uma class necessariamente não precisa de um construtur, caso não seja objeto
class aplication():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.inputs()
        self.lista_frame2()
        janela.mainloop()

    def tela(self):
        self.janela.title('NETFLIX')
        self.janela.configure(background='#ee82ee')
        self.janela.geometry('700x500')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=500)
    def frames(self):
        self.frame0 = Frame(self.janela, bg='#bfddf3')
        self.frame0.place(relx = 0.03, rely=0.03,
                         relwidth=0.94, relheight=0.11)

        self.frame1 = Frame(self.janela, bg='#bfddf3')
        self.frame1.place(relx= 0.03, rely=0.20,
                         relwidth=0.94, relheight=0.25)

        self.frame2 = Frame(self.janela, bg='#bfddf3')
        self.frame2.place(relx= 0.03, rely=0.50,
                         relwidth=0.94, relheight=0.45)

    def botoes(self):
        self.btBuscar = Button(self.frame0, text='Buscar')
        self.btBuscar.place(relx=0.15, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btLimpar = Button(self.frame0, text='Limpar')
        self.btLimpar.place(relx=0.27, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btCreate = Button(self.frame0, text='Create', command=self.insert_user)
        self.btCreate.place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btRead = Button(self.frame0, text='Read')
        self.btRead.place(relx=0.57, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btUpdate = Button(self.frame0, text='Update')
        self.btUpdate.place(relx=0.69, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btDelete = Button(self.frame0, text='Delete')
        self.btDelete.place(relx=0.81, rely=0.40, relwidth=0.1, relheight=0.50)

    def labels(self):
        self.lbIDUsuario = Label(self.frame0, text='ID', bg='#bfddf3')
        self.lbIDUsuario.place(relx=0.005, rely=0.01,
                               relwidth=0.1, relheight=0.3)

        self.lbNome = Label(self.frame1, text='Nome', bg='#bfddf3')
        self.lbNome.place(relx=0.005, rely=0.06,
                               relwidth=0.1, relheight=0.15)

        self.lbEmail = Label(self.frame1, text='Email', bg='#bfddf3')
        self.lbEmail.place(relx=0.005, rely=0.37,
                          relwidth=0.1, relheight=0.15)

        self.lbPlano = Label(self.frame1, text='Plano', bg='#bfddf3')
        self.lbPlano.place(relx=0.005, rely=0.69,
                          relwidth=0.1, relheight=0.15)

        self.lbTipo = Label(self.frame1, text='Tipo', bg='#bfddf3')
        self.lbTipo.place(relx=0.32, rely=0.69,
                           relwidth=0.1, relheight=0.15)

        self.lbIdade = Label(self.frame1, text='Idade', bg='#bfddf3')
        self.lbIdade.place(relx=0.62, rely=0.69,
                          relwidth=0.1, relheight=0.15)

    def inputs(self):
        self.inpIUDsuario = Entry(self.frame0)
        self.inpIUDsuario.place(relx=0.005, rely=0.37,
                                relwidth=0.1, relheight=0.50)

        self.inpNome = Entry(self.frame1)
        self.inpNome.place(relx=0.12, rely=0.05,
                            relwidth=0.8, relheight=0.25)

        self.inpEmail = Entry(self.frame1)
        self.inpEmail.place(relx=0.12, rely=0.35,
                           relwidth=0.8, relheight=0.25)

        self.inpPlano = Entry(self.frame1)
        self.inpPlano.place(relx=0.12, rely=0.65,
                            relwidth=0.2, relheight=0.25)

        self.inpTipo = Entry(self.frame1)
        self.inpTipo.place(relx=0.425, rely=0.65,
                            relwidth=0.2, relheight=0.25)

        self.inpIdade = Entry(self.frame1)
        self.inpIdade.place(relx=0.72, rely=0.65,
                            relwidth=0.2, relheight=0.25)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame2, height=3,
                                     columns=('col1',
                                              'col2',
                                              'col3',
                                              'col4',
                                              'col5',
                                              'col6',))
        self.listaCli.heading('#0', text='ID')
        self.listaCli.heading('#1', text='Nome')
        self.listaCli.heading('#2', text='Email')
        self.listaCli.heading('#3', text='Plano')
        self.listaCli.heading('#4', text='Tipo')
        self.listaCli.heading('#5', text='Idade')

        self.listaCli.column('#0', width=35)
        self.listaCli.column('#1', width=188)
        self.listaCli.column('#2', width=188)
        self.listaCli.column('#3', width=70)
        self.listaCli.column('#4', width=70)
        self.listaCli.column('#5', width=70)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrollista=Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scrollista.set)
        self.scrollista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

    def insert_user(self):
        inserir_usuarios(self.inpNome.get(), self.inpEmail.get(), self.inpPlano.get(),
                         self.inpTipo.get(), self.inpIdade.get())
