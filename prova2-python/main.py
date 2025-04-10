nome = input("Digite seu nome: ")
email = input("Digite o seu email: ")
telefone = input("Digite o seu telefone: ") #85 92535 - 3245
dicionario = dict({

			"nome": nome,
			"email": email,
 			"telefone": telefone
				})
print(f"""
 			 Nome: {dicionario['nome']}
				 Telefone: {dicionario['telefone']}
				E-mail: {dicionario['email']}
					""")
