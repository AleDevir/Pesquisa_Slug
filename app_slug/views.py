from django.shortcuts import render
from django.views.generic import   ListView
from django.template.defaultfilters import slugify
from .models import Palavra


class HomeListView(ListView):
    '''
    Exibi as Palavras pesquisadas
    '''
    model = Palavra
    palavra = ''
    template_name = 'home.html'

    def post(self, request, *args, **kwargs):
        self.palavra = ''
        if self.request.method == 'POST':
            self.palavra = self.request.POST['palavra']
        
        return render(request, self.template_name, {
            "palavra": self.palavra,
            "object_list": self.get_queryset(),
        })

    def get_queryset(self):
        if self.palavra:
            slug = slugify(self.palavra)
            return Palavra.objects.filter(slug__contains=slug).order_by('slug')
        return Palavra.objects.all().order_by('slug')
