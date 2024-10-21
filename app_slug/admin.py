from django.contrib import admin
from .models import Palavra

class PalavraAdmin(admin.ModelAdmin):
    '''
    Foto Admin
    '''
    list_display = [
        'palavra',
        'slug',    
    ]
    search_fields = ['palavra']


admin.site.register(Palavra, PalavraAdmin)
