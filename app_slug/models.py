from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify

class Palavra(models.Model):
    '''
    Tabela Palavra
    '''
    palavra = models.CharField('Palavra', max_length=40, unique=True)
    slug = models.SlugField(max_length=40,  editable=False, unique=True)
 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.palavra)
        return super().save(*args, **kwargs)

    class Meta:
        '''
        Metamodelo
        '''
        db_table = 'palavras'

    def __str__(self):
        '''
        str
        '''
        return str(self.palavra)
