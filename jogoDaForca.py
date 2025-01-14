from random import choice

print(" JOGO DA FORCA ".center(21, "="))

while True:
    opcaoJogar = int(input("Vamos jogar ?\n[1] - SIM\n[2] - Não\nRESPOSTA: "))
    
    while opcaoJogar != 1 and opcaoJogar != 2:
        print("="*10)
        print("Opção Inválida!")
        opcaoJogar = int(input("Vamos jogar ?\n[1] - SIM\n[2] - Não\nRESPOSTA: "))

    if opcaoJogar == 2:
        break
    else:
        palavraAleatoria = choice(["carro", "gato", "cachorro", "escola", "javascript", "cogumelo"])
        dicas = {
            "carro": "Meio de transporte com rodas.",
            "gato": "Animal de estimação que mia.",
            "cachorro": "Animal de estimação que late.",
            "escola": "Lugar onde se aprende.",
            "javascript": "Linguagem de programação usada na web.",
            "cogumelo": "Ser vivo com chapéu e haste, encontrado em florestas."
        }
        
        quantidadeLetras = len(palavraAleatoria)
        dica = dicas.get(palavraAleatoria, "Sem dicas disponíveis")
        contadorLetras = 0
        tentativas = 0
        letrasDescobertas = ["_" for _ in palavraAleatoria]

        print(f"Dica: {dica}")
        while contadorLetras < quantidadeLetras:
            letraJogador = str(input("Chute uma letra: ")).strip().lower()[0]

            if letraJogador in palavraAleatoria:
                print("="*20)
                print(f"A letra {letraJogador} tem na palavra!")

                for indice, letra in enumerate(palavraAleatoria):
                    if letra == letraJogador:
                        letrasDescobertas[indice] = letra
                        contadorLetras += 1

                
                print(f"Palavra: {''.join(letrasDescobertas)}")
            else:
                print("="*20)
                print(f"A letra {letraJogador} não tem na palavra!")
                tentativas += 1
                print(f"Você tem {6 - tentativas} tentaivas.")
            
            if tentativas == 6:
                print("="*20)
                print("Você perdeu!")
                break

        print("="*20)
        print("Você venceu!")