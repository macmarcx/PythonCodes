@echo off

:: Diretório do repositório Git
set REPO_DIR=C:\Users\marco\Documents\Python Scripts\data visualizer\src

:: Mensagem de commit
set COMMIT_MESSAGE="Commit automático - %date% %time%"

:: Navegar até o diretório do repositório
cd %REPO_DIR%

:: Adicionar arquivos ao estágio
git add .

:: Fazer o commit
git commit -m %COMMIT_MESSAGE%

:: Opcional: enviar os commits para o repositório remoto
git push origin master

:: Finaliza o script
exit
