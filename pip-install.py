import os

class header:

	def __init__(self, name = 'TITLE'):
		self.cont = (34 - len(name)) / 2
		self.space = " " * int(self.cont)
		self.line = "#" * int(self.cont)
		self.line2 = '#' * len(name)
		self.name = name

	def title(self):
		print(f'#{self.space}{self.name}{self.space}#')
		
	def base(self):
		print(f'#{self.line}{self.line2}{self.line}#')


while True:
	pipins = "pip install "
	pipuni = "pip uninstall "
	what = 'Qual o nome do pacote a ser '
	
	a = header('PIP Modules')

	a.base()
	a.title()
	a.base()
		
	print("""
[ 1 ] Instalar Pacotes
[ 2 ] Remover Pacotes
[ 3 ] Lista de P. Instalado
-----------------------------------
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

