from groq import Groq

client = Groq(api_key="SUA_CHAVE_GROQ_AQUI")

historico = [
    {
        "role": "system",
        "content": """Você é AutoBot, assistente virtual de seguro auto 
        de uma seguradora brasileira. Ajude com: cobertura, sinistro, franquia, 
        renovação de apólice, carro reserva e assistência 24h.
        Seja educado e objetivo. Responda em português brasileiro."""
    }
]

print("=" * 50)
print("   AutoBot - Assistente de Seguro Auto")
print("=" * 50)
print("Olá! Sou o AutoBot, seu assistente de seguro auto.")
print("Como posso te ajudar hoje?")
print("(Digite 'sair' para encerrar)\n")

while True:
    user_input = input("Você: ")
    
    if user_input.lower() == "sair":
        print("AutoBot: Obrigado! Até mais!")
        break
    
    if not user_input.strip():
        continue

    historico.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=historico
    )

    resposta = response.choices[0].message.content
    historico.append({"role": "assistant", "content": resposta})
    
    print(f"\nAutoBot: {resposta}\n")