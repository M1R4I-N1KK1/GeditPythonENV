import os

os.system('git status')
commit = str(input('Nome do arquivo: '))
os.system('git add ' + commit)
os.system('git commit -m "Firs Commit"')
os.system('git push origin master')
os.system('git status')
