from tkinter import *  #biblioteca para interfaces gráficas
from tkinter import ttk
#cores
cor1 = "#030303" #preto
cor2 = "#fcfcfc" #branco
cor3 = "#0e1030" #azul
cor4 = "#c1c2c7" #cinza
cor5 = "#f77102" #laranja




janela = Tk()
janela.config(bg=cor1)

janela.title("Calculadora")
janela.geometry("235x290")

#frames
frame_tela=Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0,column=0)

frame_corpo=Frame(janela, width=235, height=268, bg=cor3)
frame_corpo.grid(row=1,column=0)

#criando função

def calcular():
    result=eval('9/9')
    #passando valores para a tela
    app_label.set(result)


calcular()

#criando  label

app_label= Label(frame_tela, text='55555555555', width=16, height=2, padx=0, relief=FLAT, anchor="e", justify=CENTER, font='Ivy 17 ', fg=cor2, bg=cor3)
app_label.place(x=0, y=0)

#criado botões

b_1=Button(frame_corpo, text="C", width=11, height=2,bg=cor4, )
b_1.place(x=0, y=0)
b_2=Button(frame_corpo, text="%", width=4, height=2,bg=cor4)
b_2.place(x=115, y=0)
b_3=Button(frame_corpo, text="/", width=4, height=2, bg=cor5,fg=cor2)
b_3.place(x=174, y=0)

b_4=Button(frame_corpo, text="7", width=4, height=2,bg=cor4)
b_4.place(x=0, y=48)
b_5=Button(frame_corpo, text="8", width=4, height=2,bg=cor4)
b_5.place(x=58, y=48)
b_6=Button(frame_corpo, text="9", width=4, height=2, bg=cor4)
b_6.place(x=116, y=48)
b_7=Button(frame_corpo, text="*", width=4, height=2, bg=cor5,fg=cor2)
b_7.place(x=174, y=48)


b_8=Button(frame_corpo, text="4", width=4, height=2,bg=cor4)
b_8.place(x=0, y=96)
b_9=Button(frame_corpo, text="5", width=4, height=2,bg=cor4)
b_9.place(x=58, y=96)
b_10=Button(frame_corpo, text="6", width=4, height=2, bg=cor4)
b_10.place(x=116, y=96)
b_11=Button(frame_corpo, text="-", width=4, height=2, bg=cor5,fg=cor2)
b_11.place(x=174, y=96)


b_12=Button(frame_corpo, text="1", width=4, height=2,bg=cor4)
b_12.place(x=0, y=144)
b_13=Button(frame_corpo, text="2", width=4, height=2,bg=cor4)
b_13.place(x=58, y=144)
b_14=Button(frame_corpo, text="3", width=4, height=2, bg=cor4)
b_14.place(x=116, y=144)
b_15=Button(frame_corpo, text="+", width=4, height=2, bg=cor5,fg=cor2)
b_15.place(x=174, y=144)

b_16=Button(frame_corpo, text="0", width=11, height=2,bg=cor4, )
b_16.place(x=0, y=192)
b_17=Button(frame_corpo, text=".", width=4, height=2,bg=cor4)
b_17.place(x=115, y=192)
b_18=Button(frame_corpo, text="=", width=4, height=2, bg=cor5,fg=cor2)
b_18.place(x=174, y=192)


janela.mainloop()
