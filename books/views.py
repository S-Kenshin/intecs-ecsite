from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Item
from .forms import SearchForm
from django.db.models import Q

class Find(TemplateView):
    def  __init__(self):
        self.params = {
            'msg': '',
            'form': '',
            'data': '',
            }

    def post(self, request):
        msg = request.POST['find']
        form = SearchForm(request.POST)
        sql =
        'select * from hello_friend'
        if msg != '':
            sql += 'where ' + msg
        data = Friend.objects.raw(sql)
        msg = sql
        self.params['msg'] = msg
        self.params['form'] = form
        self.params['data'] = data
        
        return render(request, 'hello/find.html', self.params)
    
    
    def get(self, request):
        self.params['msg'] = 'search words'
        self.params['form'] = FindForm()
        self.params['data'] = Friend.objects.all()
        return render(request, 'hello/find.html', self.params)