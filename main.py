#janela => 500 x 500
#titulo
#campos para selecionar as moedas de origem e destino
#botão para converter 
#lista de exibição com os nomes das moedas
import customtkinter

#criar e configurar a janela 
customtkinter.set_appearance_mode("white")
customtkinter.set_default_color_theme("green")
janela = customtkinter.CTk ()
janela.geometry("600x600"),
#criar os botões, textos, e demais elementos 
titulo = customtkinter.CTkLabel(janela, text="Conversor de moedas", font=("forte", 30), text_color=("#FF087F"))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem",  font=("arial", 18), text_color=("#DB7093"))
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino",  font=("arial", 18))
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=["USD", "EUR", "BRL", "BTC"],  font=("arial black", 18), fg_color=("#FF1493"), button_color=("#FF1493"))

campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["USD", "EUR", "BRL", "BTC"],  font=("arial black", 18), text_color=("#DB7093"))
moedas_disponiveis = ["USB: dólar americano","EUR: euro","BRL: real brasileiro","BTC: Bitcoin"]


def converter_moeda():
    print("Converter moeda")
botao_converter = customtkinter.CTkButton(janela, text="Converter" , command=converter_moeda,  font=("arial black", 18))

lista_moedas = customtkinter.CTkScrollableFrame(janela)

for moeda in  moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda, font=("arial black",14))
    texto_moeda.pack(padx=10,pady=10)

#moeda1 = customtkinter.CTkLabel(lista_moedas, text="USB: dólar americano")
#moeda2 = customtkinter.CTkLabel(lista_moedas, text="EUR: euro")
#moeda3 = customtkinter.CTkLabel(lista_moedas, text="BRL: real brasileiro")
#moeda4 = customtkinter.CTkLabel(lista_moedas, text="BTC: Bitcoin")
#moeda1.pack()
#moeda2.pack()
#moeda3.pack()
#moeda4.pack()

#colocar os elementos criados na tela 
titulo.pack(padx=10,pady=10)
texto_moeda_origem.pack(padx=10,pady=10)
campo_moeda_origem.pack(padx=10,pady=10)
texto_moeda_destino.pack(padx=10,pady=10)
campo_moeda_destino.pack(padx=10,pady=10)
botao_converter.pack(padx=10,pady=10)
lista_moedas.pack(padx=10,pady=10)

#rodar a janela
janela.mainloop()