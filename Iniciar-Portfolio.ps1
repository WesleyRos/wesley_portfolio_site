param([int]$Porta=8001)
$ErrorActionPreference='Stop'
Set-Location -LiteralPath $PSScriptRoot
$pythonPath=Join-Path $PSScriptRoot '.venv/Scripts/python.exe'
if(!(Test-Path -LiteralPath $pythonPath)){throw 'O ambiente Python não foi encontrado nesta pasta.'}
& $pythonPath manage.py migrate --noinput
if($LASTEXITCODE -ne 0){throw 'Não foi possível preparar o banco.'}
Write-Host "Seu portfólio: http://localhost:$Porta"
Write-Host 'Mantenha a janela aberta; Ctrl+C encerra.'
& $pythonPath manage.py runserver "127.0.0.1:$Porta"
