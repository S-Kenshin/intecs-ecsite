from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return HttpResponse('HelloWorld')

class Index(TemplateView):
    
    template_name = "index.html"
    
    def __init__(self):
        self.params = {
            'title':'INTECS BOOKs',
            'message':'待望のintecsのECサイトが、ついに出た！',
            }
        
    def get(self,request):
        return render(request, 'books/index.html', self.params)