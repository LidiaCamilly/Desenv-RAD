import tkinter as tk
from tkinter import ttk
import CRUD as CRUD

class PrincipalBD:
    def __init__(self, win):
        self.objBD = CRUD.dtbase()
        self.lbNome = tk.Label(win, text= 'Nome:')
        self.lbTel = tk.Label(win, text='Telefone:')

        self.txtNome = tk.Entry()
        self.txtTel = tk.Entry()
        self.btAdicionar = tk.Button(win, text = 'Adicionar', command=self.fCadastrar)
        self.btExcluir = tk.Button(win, text= 'Excluir', command=self.fExcluir)
        self.btAtualizar = tk.Button(win, text='Atualizar', command= self.fAtualizar)
        self.btLimpar = tk.Button(win, text='Limpar', command=self.fLimparTela)

        self.dadosColunas = ('Nome', 'Telefone')
        self.treeProdutos = ttk.Treeview(win,
                                         columns=self.dadosColunas,
                                         selectmode='browse')
        self.verscrlbar = ttk.Scrollbar(win, orient='vertical',
                                        command= self.treeProdutos.yview)
        self.verscrlbar.pack(side='right', fill = 'x')

        self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)

        self.treeProdutos.heading('Nome', text='Nome')
        self.treeProdutos.heading('Telefone', text='Telefone')

        self.treeProdutos.column('Nome',minwidth=0,width=50)
        self.treeProdutos.column('Telefone',minwidth=0, width=50)

        self.treeProdutos.pack(padx=10, pady=10)

        self.treeProdutos.bind('<<TreeviewSelect>>',
                               self.apresentarAgenda)

        self.lbNome.place(x=100, y=50)
        self.txtNome.place(x=250, y=50)
        self.lbTel.place(x=100,y=100)
        self.txtTel.place(x=250,y=100)

        self.btAdicionar.place(x=100, y=200)
        self.btAtualizar.place(x=200, y=200)
        self.btExcluir.place(x=300,y=200)
        self.btLimpar.place(x=400, y=200)

        self.treeProdutos.place(x=100,y=300)
        self.verscrlbar.place(x=805, y=300, height=225)
        self.carregarDados()

    def apresentarAgenda(self, event):
        self.fLimparTela()
        for selection in self.treeProdutos.selection():
            item = self.treeProdutos.item(selection)
            nome, telefone = item['values'][0:3]
            self.txtNome.insert(0, nome)
            self.txtTel.insert(0, telefone)

    def carregarDados(self):
        try:
            self.id = 0
            self.iid = 0
            registros = self.objBD.selecionar()
            for item in registros:
                nome = item[0]
                telefone = item[1]
                print('Nome:', nome)
                print('Telefone:', telefone)

                self.treeProdutos.insert('', 'end',
                                         iid=self.iid,
                                         values=(nome,telefone))
                self.iid = self.iid + 1
                self.id= self.id + 1
        except:
            print('Ainda não existem dados para carregar')

    def fLerCampos(self):
        try:
            nome = self.txtNome.get()
            print('Nome', nome)
            telefone = int(self.txtTel.get())
            print('Telefone', telefone)
        except:
            print('Não foi possível ler os dados')
        return nome, telefone
    def fCadastrar(self):
        try:
            print('******** dados disponíveis *********')
            nome, telefone = self.fLerCampos()
            self.objBD.inserir(nome,telefone)
            self.treeProdutos.insert('','End',
                                     iid = self.iid,
                                     values=(nome, telefone))
            self.iid= self.iid + 1
            self.id = self.id + 1
            self.fLimparTela()
            print('Pessoa Cadastrada com sucesso!')
        except:
            print('Não foi possível criar o contato.')

    def fAtualizar(self):
        try:
            print('******** dados disponíveis *********')
            nome, telefone = self.fLerCampos()
            self.objBD.atualizar(nome,telefone)
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDados()
            self.fLimparTela()
        except:
            print('Não foi possível atualizar o contato')
    def fExcluir(self):
        try:
            print('******** dados disponíveis *********')
            nome, telefone = self.fLerCampos()
            self.objBD.exluir(nome, telefone)
            self.carregarDados()
            self.fLimparTela()
        except:
            print('Não foi possível excluir o contato.')

    def fLimparTela(self):
        try:
            print('******** dados disponíveis *********')
            self.txtNome.delete(0, tk.END)
            self.txtTel.delete(0, tk.END)
            print('Campos limpos')
        except:
            print('Não foi possível limpar os campos')


janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title('Agenda telefônica')
janela.geometry('620x620')
janela.mainloop()