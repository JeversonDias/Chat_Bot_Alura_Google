import tkinter as tk
import google.generativeai as genai
#Escrito por @JeversonDias + Luri
GOOGLE_API_KEY = "COLE SUA CHAVE API AQUI"
genai.configure(api_key=GOOGLE_API_KEY)

# Função para obter a resposta gradualmente
def obter_resposta():
    pergunta = entrada_pergunta.get()
    entrada_pergunta.delete(0, tk.END)  # Limpar o prompt
    resposta = model.generate_content(pergunta)
    texto_resposta.config(state=tk.NORMAL)
    texto_resposta.insert(tk.END, resposta.text + "\n")
    texto_resposta.config(state=tk.DISABLED)

# Função para resetar o texto
def resetar_texto():
    texto_resposta.config(state=tk.NORMAL)
    texto_resposta.delete(1.0, tk.END)  # Limpar o texto
    texto_resposta.config(state=tk.DISABLED)

# Configurar a janela
janela = tk.Tk()
janela.title("Chatbot IA")
janela.configure(bg="#FFD700")  # Cor de fundo Alura

# Configurar a janela para abrir em fullscreen
largura = janela.winfo_screenwidth()
altura = janela.winfo_screenheight()
janela.geometry(f"{largura}x{altura}")

# Entrada para a pergunta
entrada_pergunta = tk.Entry(janela, width=50, font=("Arial", 14))
entrada_pergunta.pack(pady=10)

# Botão para enviar a pergunta
botao_enviar = tk.Button(janela, text="Enviar", command=obter_resposta, bg="#008B8B", fg="white")  # Cores Alura
botao_enviar.pack()

# Área de texto para exibir a resposta gradualmente
texto_resposta = tk.Text(janela, wrap="word", font=("Arial", 14, "bold"))
texto_resposta.pack(expand=True, fill="both")

# Botão para resetar o texto
botao_resetar = tk.Button(janela, text="Resetar", command=resetar_texto, bg="#008B8B", fg="white")  # Cores Alura
botao_resetar.pack()

# Configurações de geração
generation_config = {
    "candidate_count": 1,
    "temperature": 0.5
}

# Configurações de segurança
safety_settings = {
    "harassment": "BLOCK_NONE",
    "hate": "BLOCK_NONE",
    "sexual": "BLOCK_NONE",
    "dangerous": "BLOCK_NONE"
}

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                             generation_config=generation_config,
                             safety_settings=safety_settings)

# Iniciar a interface gráfica
janela.mainloop()