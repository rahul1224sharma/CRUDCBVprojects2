from django.shortcuts import render
from MyApps1.models import Employee
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView

# Create your views here.
class Create(CreateView):
    model = Employee
    #fields = ('empno','ename','job','sal')
    fields = '__all__'

class List(ListView):
    model = Employee

class Detail(DetailView):
    model = Employee

class Update(UpdateView):
    model = Employee
    fields = ('ename','job','sal')

from django.urls import reverse_lazy
class Delete(DeleteView):
    model = Employee
    success_url = reverse_lazy('list')

