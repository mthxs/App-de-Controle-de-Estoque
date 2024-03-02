import tkinter
#from view import *
from tkinter import messagebox
import customtkinter
import customtkinter as ctk
import os
from PIL import ImageTk,Image
from tkinter.filedialog import askopenfilenames

def verification():
    with open('E:\Documentos\pythonProject\INDEFINIDO\ORGANIZADOR DE PRODUTOS\empresa.txt', "r", encoding="utf-8") as a:
        nomedaempresa = a.read()
        if nomedaempresa == "":
            return firstentry()
        else:
            return menu(nomedaempresa)

#def estoque():




def menu(nomedaempresa):

    nomedessaempresa = nomedaempresa
    texto_informativo = ctk.CTkLabel(janela, text=nomedessaempresa,width=60,height=10,font=("Times New Roman", 50))
    texto_informativo.pack(side="top",padx=1, pady=150)
    texto_informativo.configure(fg_color="black",text_color="white",compound="top")
    botao_adicionar = ctk.CTkButton(janela, text="Adicionar Venda", command=janela_adicionar,width=60,height=10,font=("Times New Roman", 30))
    botao_adicionar.pack(side="right",padx=200, pady=0)
    botao_adicionar.configure( corner_radius=32 )
    botao_historico = ctk.CTkButton(janela, text="Histórico da Empresa",width=60,height=10,font=("Times New Roman", 30))
    botao_historico.pack(side="left",padx=200,pady=0)
    botao_historico.configure( corner_radius=32 )
    botao_produtos = ctk.CTkButton(janela, text="Produtos",command=janela_produtos,width=60,height=10,font=("Times New Roman", 30))
    botao_produtos.pack(pady=150,padx=0)
    botao_produtos.place(relx=0.5, rely=0.81, anchor=tkinter.CENTER)
    botao_produtos.configure(corner_radius=32)



def novo_produto():
    global entradavalor, entradaquantidade
    novoproduto = ctk.CTkToplevel()
    novoproduto.geometry("600x700")
    novoproduto.title('Adiocionar Novo Produto')
    labelnome = ctk.CTkLabel(novoproduto, text="Informe o nome do produto que você deseja adicionar: ")
    labelnome.pack(padx=10, pady=10)
    labelnomedoproduto = ctk.CTkEntry(novoproduto)
    labelnomedoproduto.pack(padx=10, pady=10)
    labelvalor= ctk.CTkLabel(novoproduto,text="Informe o Valor do Produto  R$: ")
    labelvalor.pack(padx=5,pady=5)
    entradavalor= ctk.CTkEntry(novoproduto)
    entradavalor.pack(padx=10,pady=10)
    labelquantidade= ctk.CTkLabel(novoproduto,text="Informe a Quantidade:")
    labelquantidade.pack(padx=5,pady=5)
    entradaquantidade = ctk.CTkEntry(novoproduto)
    entradaquantidade.pack(padx=10,pady=10)
    labelimagem= ctk.CTkLabel(novoproduto, text="Adicione uma imagem do produto: ")
    labelimagem.pack(padx=10,pady=10)
    imagempadrao = ImageTk.PhotoImage(file="newimage.png")
    img_label = ctk.CTkLabel(novoproduto,text="",image=imagempadrao)
    img_label.pack(padx=10,pady=10)
    img_label.configure(width=200,height=200)
    def adicionar_imagem():
        global image_data, img

        path = askopenfilenames()
        if path:
            path = path[0]
            lerimagem = open(path, 'rb')
            image_data = lerimagem.read()
            lerimagem.close()

            img = ImageTk.PhotoImage(Image.open(path))
            img_label.configure(image=img)
    botaonovafoto= ctk.CTkButton(novoproduto,text="Adicionar Foto do Produto (300X300)",command=adicionar_imagem,font=("Times New Roman", 20))
    botaonovafoto.pack(padx=10,pady=10)
    botaonovafoto.configure(corner_radius=32)
    botaoconfirm = ctk.CTkButton(novoproduto, text="Confirmar",command=lambda:validação(labelnomedoproduto.get(),entradavalor.get(),entradaquantidade.get(),img_path),  font=("Times New Roman", 20),fg_color="green")
    botaoconfirm.pack(padx=10, pady=10)
    botaoconfirm.configure(corner_radius=32)
    botaovoltar = ctk.CTkButton(novoproduto, text="Fechar essa janela",fg_color="red", command=novoproduto.destroy)
    botaovoltar.pack(padx=10, pady=10)



def janela_produtos():
    janelaprodutos = ctk.CTkToplevel()
    janelaprodutos.geometry("1000x500")
    janelaprodutos.title("Produtos da Loja")
    labelnome = ctk.CTkLabel(janelaprodutos, text="Informe o nome do produto: ")
    labelnome.pack(padx=10, pady=10)
    labelnomedoproduto = ctk.CTkEntry(janelaprodutos)
    labelnomedoproduto.pack(padx=10,pady=10)
    botaoconfirm= ctk.CTkButton(janelaprodutos,text= "Adicionar um novo Produto",command=novo_produto)
    botaoconfirm.pack(padx=10, pady=10)
    botaovoltar = ctk.CTkButton(janelaprodutos,text="Fechar essa janela",fg_color="red", command=janelaprodutos.destroy)
    botaovoltar.pack(padx=10, pady=10)

def janela_adicionar():
    janela2 = ctk.CTkToplevel()
    janela2.geometry("1000x500")
    janela2.title('Adicionar Produto')
    labelnome = ctk.CTkLabel(janela2, text="Informe o nome do produto: ")
    labelnome.pack(padx=10, pady=10)
    labelnomedoproduto = ctk.CTkEntry(janela2)
    labelnomedoproduto.pack(padx=10,pady=10)
    botaoconfirm= ctk.CTkButton(janela2,text= "Confirmar Venda")
    botaoconfirm.pack(padx=10, pady=10)
    botaovoltar = ctk.CTkButton(janela2,text="Fechar essa janela",fg_color="red", command=janela2.destroy)
    botaovoltar.pack(padx=10, pady=10)
def salvar(nomedaloja):
    nomedessalojinha = nomedaloja
    with open('E:\Documentos\pythonProject\INDEFINIDO\ORGANIZADOR DE PRODUTOS\empresa.txt', "a", encoding="utf-8") as save:
        save.write(nomedessalojinha)
    frame_firstentry.destroy()
    verification()


def firstentry():
    global frame_firstentry
    frame_firstentry=ctk.CTkFrame(janela)
    frame_firstentry.pack(padx=100, pady=100)
    frame_firstentry.configure(width=700,height=500)
    nomeda_loja = ctk.CTkLabel(frame_firstentry,text="Qual o Nome da Sua Loja?")
    nomeda_loja.pack(padx=10, pady=10)
    nomedaloja = ctk.CTkEntry(frame_firstentry,width=20 )
    nomedaloja.pack(padx=10, pady=10)
    nomedaloja.configure(width=300, height=50, font=("Arial", 20))
    botaoconfirm = ctk.CTkButton(frame_firstentry, text="Confirmar",fg_color="green",command=lambda: salvar(nomedaloja.get()))
    botaoconfirm.pack(padx=10, pady=10)

image_data = b''
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela= ctk.CTk()
janela.title("Organizador de produtos")
janela.geometry("1920x1080")
imagem_fundo=ImageTk.PhotoImage(Image.open("fundomaior.png"))
frameprincipal=ctk.CTkFrame(master=janela)
frameprincipal.pack()
fundo = ctk.CTkLabel(janela,text="",image=imagem_fundo)
fundo.place(relheigh=1,relwidth=1)

janela.configure(background=imagem_fundo)

if not os.path.exists('E:\Documentos\pythonProject\INDEFINIDO\ORGANIZADOR DE PRODUTOS\empresa.txt'):
    with open('E:\Documentos\pythonProject\INDEFINIDO\ORGANIZADOR DE PRODUTOS\empresa.txt', 'w', encoding='utf-8'):
        pass
verification()




janela.mainloop()
#frame_nome=ctk.CTkFrame(master=fundo,width=1000,height=500,corner_radius=15)
   # frame_nome.place(x=750, y=10, )
    #framemenu=ctk.CTkFrame(master=fundo,width=320,height=360,corner_radius=15)
   # framemenu.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)