from email.utils import collapse_rfc2231_value
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

co0 = "#f0f3f5"
co1 = "#feffff"
co2 = "#3fb5a3"
co3 = "#38576b"
co4 = "#403d3d"

#criando janela
janela = Tk()
janela.title("Tela Login")
janela.geometry("310x300")
janela.config(background=co1)
janela.resizable(width=FALSE, height=FALSE)

#Dividindo a janela
frame_cima = Frame(janela, width=310, height=50, background=co1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela,width=310, height=250, bg=co0, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#Configurando o frame cima---------
l_nome = Label(frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
l_linha.place(x=10, y=45)

credenciais = ['joao', '12345678']

def verificar_senha():
    nome = e_nome.get()
    senha = e_pass.get()
    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin')
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta ' + credenciais[0] + '!')
    else:
        messagebox.showwarning('Erro', 'Verifique o nome e a senha!!!')

#Donfigurando frame baixo
I_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
I_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=14, y = 50)

I_pass = Label(frame_baixo, text='Palavra passe *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
I_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
e_pass.place(x=14, y = 130)

b_confirmar = Button(frame_baixo, command=verificar_senha, text='Entrar', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=180)

janela.mainloop()