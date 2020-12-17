from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Item
from .forms import SearchForm
from django.db.models import Q

class Index(TemplateView):
    template_name = 'index.html'
        
    def get(self, request):
        data = Item.objects.all()
        self.params = {
            'data':data,
            }
        return render(request, 'books/index.html', self.params)
        