import tkinter as tk


def contar():
     
    valor = int(campo1.get())
    resultado = " "
    linha = ""
    print(valor)
   
    for i in range (valor,100+1):
        resultado += str(i) + " " 
        if i % 20 == 0:  # Quebra a linha a cada 20 números
                resultado += linha + "\n"
                linha = ""
    total.config(text=resultado)  
    
janela = tk.Tk()
janela.geometry("350x250")

janela.title("Contando")

campo1 =tk.Entry(janela)
campo1.pack(padx=5, pady=20)


botao = tk.Button( janela, text=" Contar ", command=contar)
botao.pack(padx=50)



total =tk.Label(janela, text="Total", justify="left") 
total.pack(pady=40)


janela.mainloop()
