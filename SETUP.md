# Setup rápido

1. Crie um virtualenv e instale requirements:
   ```
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. No Render, configure a variável de ambiente DATABASE_URL com a URL do banco (ou deixe que o Render preencha automaticamente se você criou o Postgres lá).

3. Rode migrações e crie superuser:
   ```
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Faça upload de uma imagem de perfil e preencha SiteSettings no admin.

OBS: O projeto já vem configurado para usar PostgreSQL por meio de dj-database-url. A SECRET_KEY padrão está em settings.py; troque por uma segura em produção.
