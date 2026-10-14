# Perfil profissional

Projeto independente em Django e Python, inspirado na organização do portfólio https://aayushbharti.in/. Design próprio voltado a inteligência de mercado e análise sênior de dados.

## Abrir

No PowerShell:

```powershell
cd "C:\Users\user4\Documents\Perfil Profissional"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\Iniciar-Portfolio.ps1"
```

Acesse http://localhost:8001. Esta é uma versão local para avaliação.

## Editar o conteúdo

Para criar seu acesso ao painel, execute `.\.venv\Scripts\python.exe manage.py createsuperuser` e escolha usuário e senha. Acesse http://localhost:8001/admin/ para cadastrar perfil, ferramentas, experiências e cases. Os cases ficam como rascunhos até marcar Publicar no site. Não foi criado nenhum usuário ou senha por padrão.

O nome e os conteúdos de apresentação ainda estão em preparação. Os espaços de cases não representam trabalhos realizados. O gráfico inicial é apenas ilustrativo. A versão inicial não envia mensagens; o contato abre o e-mail ou LinkedIn que você cadastrar.

Banco local: db.sqlite3. Preserve esse arquivo e .secret-key ao atualizar. A interface está em templates/ e static/; conteúdo e painel em portfolio/. Para reinstalar em outro computador, crie um ambiente virtual Python e instale requirements.txt. Para publicar na internet será preciso configurar domínio, servidor de produção e variáveis de ambiente.

## Qualidade do JavaScript

Vitest testa as categorias do agronegócio, a validade das conexões e a identificação dos contextos demonstrativos. oxlint verifica static/ e tests/. Com Node.js e npm instalados, use `npm ci`, `npm test` e `npm run lint`. O site continua em Django; estas ferramentas são usadas apenas no desenvolvimento e não são necessárias para abrir o portfólio.

## Rede do agronegócio

O projeto inclui somente a rede 3D do agronegócio.

Grafo 3D: biblioteca 3d-force-graph, distribuída localmente em static/vendor, licença MIT. Dados demonstrativos: 1.200 nós. Arraste para girar; Ampliar abre tela cheia com zoom. Fundo sem reação ao cursor.

Mapa do agronegócio: nove categorias, temas identificáveis e relações qualitativas curadas. Não representa um modelo de previsão ou séries ao vivo. Roda do mouse: zoom; arraste o fundo: órbita; arraste um ponto: reposicionar; clique em ponto ou selecione tema: explicações; Reorganizar rede: remove posições fixadas e reenquadra. Fontes de referência: https://portaldeinformacoes.conab.gov.br/ e https://www.bcb.gov.br/estabilidadefinanceira/creditorural

Interação: +/− e roda do mouse ajustam zoom; arraste o fundo com botão esquerdo para girar, direito para deslocar; arraste um ponto para reposicionar. O tema selecionado ganha um destaque para facilitar o arraste. Correção local da biblioteca documentada em static/vendor/PATCHES.md.
