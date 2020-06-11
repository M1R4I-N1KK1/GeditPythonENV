import os
while True:
	pipins = "pip install "
	pipuni = "pip uninstall "
	what = 'Qual o nome do pacote a ser '
	print("""
[ 1 ] Instalar Pacotes
[ 2 ] Remover Pacotes
[ 3 ] Lista de Pacotes
[ 0 ] Sair do Progama
	""")
	option = int(input('Qual a opção: '))
	if option == 1:
		packeage = input(str(what + 'instalado? '))
		os.system(pipins + packeage)
	elif option == 2:
		packeage = input(str(what + 'desinstalado? '))
		os.system(pipuni + packeage)
	elif option == 3:
		os.system('pip freeze')
		backup = str(input('Deseja salvar a lista em um arquivo "TXT" ? ')).upper()
		if backup == 'S':
			os.system('pip freeze > ~/requirements.txt')
			print('Arquivos salvo em /home')
	elif option == 0:
		print('Enter para sair')
		break
