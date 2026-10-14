from django.db import models
class Profile(models.Model):
 name=models.CharField('Nome profissional',max_length=100,default='Seu nome')
 role=models.CharField('Cargo',max_length=150,default='Analista sênior de inteligência de mercado')
 headline=models.CharField('Chamada principal',max_length=220,default='Dados que ampliam a visão. Análises que orientam decisões.')
 bio=models.TextField('Apresentação',blank=True)
 email=models.EmailField('E-mail de contato',blank=True)
 linkedin=models.URLField('LinkedIn',blank=True)
 photo_url=models.URLField('URL da foto',blank=True)
 location=models.CharField('Localização',max_length=100,blank=True)
 def __str__(self):return self.name
 class Meta:verbose_name='Perfil';verbose_name_plural='Perfil'
class Tool(models.Model):
 CATEGORY=[('analise','Análise de dados'),('bi','Business intelligence'),('dados','Bancos de dados'),('automacao','Automação'),('pesquisa','Pesquisa de mercado')]
 name=models.CharField('Ferramenta',max_length=80)
 category=models.CharField('Categoria',max_length=20,choices=CATEGORY)
 description=models.CharField('Como utilizo',max_length=240,blank=True)
 order=models.PositiveIntegerField('Ordem',default=0)
 class Meta:ordering=['order','name'];verbose_name='Ferramenta'
 def __str__(self):return self.name
class Case(models.Model):
 title=models.CharField('Título',max_length=160)
 slug=models.SlugField(unique=True)
 category=models.CharField('Área',max_length=100)
 summary=models.TextField('Resumo')
 problem=models.TextField('Desafio de negócio')
 data_sources=models.TextField('Dados e fontes',blank=True)
 methodology=models.TextField('Metodologia')
 insights=models.TextField('Principais descobertas',blank=True)
 impact=models.TextField('Impacto e resultados',blank=True)
 tools=models.ManyToManyField(Tool,blank=True,verbose_name='Ferramentas')
 published=models.BooleanField('Publicar no site',default=False)
 order=models.PositiveIntegerField('Ordem',default=0)
 class Meta:ordering=['order','title'];verbose_name='Case';verbose_name_plural='Cases'
 def __str__(self):return self.title
class Experience(models.Model):
 title=models.CharField('Cargo',max_length=150)
 company=models.CharField('Empresa',max_length=150)
 period=models.CharField('Período',max_length=80)
 description=models.TextField('Responsabilidades e entregas')
 order=models.PositiveIntegerField('Ordem',default=0)
 class Meta:ordering=['order'];verbose_name='Experiência'
 def __str__(self):return f'{self.title} — {self.company}'

class Education(models.Model):
 title=models.CharField('Formação',max_length=180)
 institution=models.CharField('Instituição',max_length=180)
 period=models.CharField('Período',max_length=80)
 description=models.TextField('Detalhes',blank=True)
 order=models.PositiveIntegerField('Ordem',default=0)
 class Meta:ordering=['order'];verbose_name='Formação';verbose_name_plural='Formações'
 def __str__(self):return self.title
class Certificate(models.Model):
 title=models.CharField('Certificado',max_length=180)
 issuer=models.CharField('Instituição',max_length=180)
 date=models.CharField('Data ou período',max_length=80,blank=True)
 url=models.URLField('Link de verificação',blank=True)
 order=models.PositiveIntegerField('Ordem',default=0)
 class Meta:ordering=['order'];verbose_name='Certificado'
 def __str__(self):return self.title
