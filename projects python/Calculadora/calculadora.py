from tkinter import *
from tkinter import ttk

cor_black = "#0a0a0a"
cor_white = "#f5f5f5"
cor_green = "#2cfa02"
cor_gray = "#999e98"
cor_yellow = "#f4fc03"
cor_purple = "#e703fc"

calculadora = Tk()
calculadora.title("Calculadora")
calculadora.geometry("235x310")
calculadora.config(bg=cor_black)

# Base Calculadora

visor = Frame(calculadora, width=235, height=50, bg=cor_black)
visor.grid(row=0, column=0)

corpo = Frame(calculadora, width=235, height=268)
corpo.grid(row=1, column=0)

valor_texto = StringVar()

todos_valores = ''

# Funções Calculadora


def entrada_valores(acao):
    global todos_valores
    todos_valores = todos_valores + str(acao)

    valor_texto.set(todos_valores)

# Função Calcula


def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))

# Limpa tela


def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# Leitor Tela


app_label = Label(visor, textvariable=valor_texto, width=16, height=2, padx=7,
                  relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor_black, fg=cor_white)
app_label.place(x=0, y=0)


# Botões / Parte 1

botao_C = Button(corpo, command=limpar_tela, text="C", width=11, height=2,
                 bg=cor_purple, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_C.place(x=0, y=0)

botao_resto = Button(corpo, command=lambda: entrada_valores('%'), text="%", width=5, height=2, bg=cor_yellow, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_resto.place(x=118, y=0)

botao_divisao = Button(corpo, command=lambda: entrada_valores('/'), text="/", width=5, height=2, bg=cor_yellow,
                       font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_divisao.place(x=177, y=0)

# Botôes / Parte 2

botao_9 = Button(corpo, command=lambda: entrada_valores('9'), text="9", width=5, height=2, bg=cor_green, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_9.place(x=118, y=52)

botao_multiplicacao = Button(corpo, command=lambda: entrada_valores('*'), text="x", width=5, height=2, bg=cor_yellow,
                             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_multiplicacao.place(x=177, y=52)

botao_7 = Button(corpo, command=lambda: entrada_valores('7'), text="7", width=5, height=2, bg=cor_green, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_7.place(x=0, y=52)

botao_8 = Button(corpo, command=lambda: entrada_valores('8'), text="8", width=5, height=2, bg=cor_green,
                 font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_8.place(x=59, y=52)

# Botões / Parte 3

botao_4 = Button(corpo, command=lambda: entrada_valores('4'), text="4", width=5, height=2, bg=cor_green, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_4.place(x=0, y=104)

botao_5 = Button(corpo, command=lambda: entrada_valores('5'), text="5", width=5, height=2, bg=cor_green,
                 font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_5.place(x=59, y=104)

botao_6 = Button(corpo, command=lambda: entrada_valores('6'), text="6", width=5, height=2, bg=cor_green, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_6.place(x=118, y=104)

botao_subtracao = Button(corpo, command=lambda: entrada_valores('-'), text="-", width=5, height=2, bg=cor_yellow,
                         font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_subtracao.place(x=177, y=104)

# Botões / Parte 4

botao_1 = Button(corpo, command=lambda: entrada_valores('1'), text="1", width=5, height=2, bg=cor_green, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_1.place(x=0, y=156)

botao_2 = Button(corpo, command=lambda: entrada_valores('2'), text="2", width=5, height=2, bg=cor_green,
                 font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_2.place(x=59, y=156)

botao_3 = Button(corpo, command=lambda: entrada_valores('3'), text="3", width=5, height=2, bg=cor_green, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_3.place(x=118, y=156)

botao_soma = Button(corpo, command=lambda: entrada_valores('+'), text="+", width=5, height=2, bg=cor_yellow,
                    font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_soma.place(x=177, y=156)

# Botões / Parte 5

botao_0 = Button(corpo, command=lambda: entrada_valores('0'), text="0", width=11, height=2, bg=cor_green,
                 font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_0.place(x=0, y=208)

botao_virgula = Button(corpo, command=lambda: entrada_valores(','), text=",", width=5, height=2, bg=cor_yellow, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_virgula.place(x=118, y=208)

botao_igual = Button(corpo, command=lambda: calcular(), text="=", width=5, height=2, bg=cor_yellow,
                     font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_igual.place(x=177, y=208)

calculadora.mainloop()
