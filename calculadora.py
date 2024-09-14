import tkinter as tk

def soma () :

    num1 = float(campo1.get())
    num2 = float(campo2.get())
    
    resultado = num1+num2
    total.config(text=f"O resultado é: {resultado}")
    
def sub () :

    num8 = float(campo1.get())
    num9 = float(campo2.get())
    
    resultado = num8-num9
    total.config(text=f"O resultado é: {resultado}")

def multi () :

    num4 = float(campo1.get())
    num5 = float(campo2.get())
    
    resultado = num4*num5
    total.config(text=f"O resultado é: {resultado}")

def div () :

    num6 = float(campo1.get())
    num7 = float(campo2.get())
    
    resultado = num6/num7
    total.config(text=f"O resultado é: {resultado}")
    
    

janela = tk.Tk()
janela.geometry("350x220")

janela.title("Tabela de Operacoes")

campo1 =tk.Entry(janela)
campo1.pack(padx=5, pady=20)

campo2 =tk.Entry(janela)
campo2.pack(padx=10, pady=20)


botaosoma = tk.Button( janela, text=" + ", command=soma)
botaosoma.pack(padx=50)
botaosoma.place(x=120, y=120)

botaosub =tk.Button(janela, text=" - ", command=sub)
botaosub.pack()
botaosub.place(x=150, y=120)

botaomulti =tk.Button(janela, text=" * ", command=multi)
botaomulti.pack()
botaomulti.place(x=180, y=120)
 
botaodiv =tk.Button(janela, text=" / ", command=div)
botaodiv.pack()
botaodiv.place(x=210, y=120)


total =tk.Label(janela, text="Total") 
total.pack(pady=40)


janela.mainloop()