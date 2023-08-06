import json
import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from PIL import Image, ImageTk, ImageDraw
import random

def definir_numero_certo():
    return random.randint(1, 100)

def verificar_palpite(palpite, numero_secreto):
    if palpite < numero_secreto:
        return "errado - abaixo"
    elif palpite > numero_secreto:
        return "errado - acima"
    else:
        return "certo"

def fazer_palpite():
    try:
        palpite = int(entry_palpite.get())
    except ValueError:
        resultado_var.set("Palpite inválido")
        return

    horario_tentativa = datetime.now().strftime("%H:%M:%S")
    resultado = verificar_palpite(palpite, numero_secreto)

    tentativa = {
        "Palpite": palpite,
        "Horario": horario_tentativa,
        "Resultado": resultado
    }

    tentativas.append(tentativa)

    salvar_tentativas(tentativas)

    if resultado == "certo":
        resultado_var.set(f"Finalmente acertou, seu sortudo! O número secreto era {numero_secreto}.")
    else:
        resultado_var.set(f"Você errou, seu imbecil! Tente novamente.")

    entry_palpite.delete(0, tk.END)

def salvar_tentativas(tentativas):
    arquivo_json = os.path.join(os.path.expanduser("~"), "Desktop", "tentativas.json")
    with open(arquivo_json, "w") as file:
        json.dump(tentativas, file, indent=2)

def criar_botao_arredondado(width, height, radius, color):
    button_image = Image.new("RGBA", (width, height))
    draw = ImageDraw.Draw(button_image)
    draw.rounded_rectangle((0, 0, width, height), radius, fill=color)
    return ImageTk.PhotoImage(button_image)

def mostrar_numero_certo():
    messagebox.showinfo("Número Certo", f"O número correto é: {numero_secreto}")

numero_secreto = definir_numero_certo()
tentativas = []

app = tk.Tk()
app.title("Jogo de Adivinhação")
app.geometry("300x250")

label_instrucao = tk.Label(app, text="Digite seu palpite entre 1 e 100:")
label_instrucao.pack(pady=10)

entry_palpite = tk.Entry(app)
entry_palpite.pack(pady=5)

botao_imagem = criar_botao_arredondado(100, 40, 20, "blue")
botao_palpitar = tk.Button(app, image=botao_imagem, text="Palpitar", compound="center",
                           command=fazer_palpite, bd=0, relief=tk.RAISED, fg="white", font=("Arial", 10, "bold"))
botao_palpitar.pack(pady=10)

resultado_var = tk.StringVar()
resultado_label = tk.Label(app, textvariable=resultado_var)
resultado_label.pack()

botao_imagem_mostrar_certo = criar_botao_arredondado(200, 40, 20, "green")
botao_mostrar_certo = tk.Button(app, image=botao_imagem_mostrar_certo, text="Mostrar Número Certo", compound="center",
                                command=mostrar_numero_certo, bd=0, relief=tk.RAISED, fg="white", font=("Arial", 12, "bold"))
botao_mostrar_certo.pack(pady=10)

app.mainloop()
