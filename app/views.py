from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import *
from .models import *
from .forms import UserForm
# Create your views here.


def index(request):
 submitbutton = request.POST.get("submit")
 #form = LocationChoiceField(request.POST)
 text = ''

 form = UserForm(request.POST)
 if form.is_valid():
  text = form.cleaned_data.get("name")
 query_results = stock_params_full.objects.filter(a_25=text)
 stock_results = stock_price_full.objects.all()
 context = {
  'query_results': query_results,
  'form':form, 'text': text, 'submitbutton': submitbutton, 'stock_results': stock_results}
 return render(request, 'htmlcod.html', context)