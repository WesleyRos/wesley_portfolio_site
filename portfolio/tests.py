from django.test import TestCase
from .models import Profile,Case,Tool
class PortfolioTests(TestCase):
 def test_preview_and_editable_profile(self):
  self.assertContains(self.client.get('/'),'Seu nome')
  Profile.objects.create(name='Nome de teste',headline='Minha chamada',email='teste@example.com')
  page=self.client.get('/')
  self.assertContains(page,'Minha chamada');self.assertContains(page,'mailto:teste@example.com')
 def test_drafts_are_private_and_content_escaped(self):
  case=Case.objects.create(title='Case de teste',slug='teste',category='Teste',summary='<script>alert(1)</script>',problem='Desafio',methodology='Método')
  self.assertEqual(self.client.get('/cases/teste/').status_code,404)
  self.assertNotContains(self.client.get('/'),'Case de teste')
  case.published=True;case.save()
  page=self.client.get('/cases/teste/')
  self.assertEqual(page.status_code,200);self.assertContains(page,'&lt;script&gt;');self.assertNotContains(page,'<script>alert(1)</script>')
 def test_tool_categories(self):
  Tool.objects.create(name='Ferramenta de teste',category='bi')
  self.assertContains(self.client.get('/'),'data-category="bi"')
