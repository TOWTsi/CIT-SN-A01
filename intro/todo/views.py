from django.http import HttpResponseRedirect, HttpResponse
#from django.template import loader #Nicht mehr benötigt wegen render
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse_lazy
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Task


def index(request): 
	task_list = Task.objects.order_by('-deadline')
	context = {'task_list': task_list}
	return render(request, 'todo/index.html', context) #drittes Argument (dictonary) ist optional

#def newtodo(request):
#    return render(request, 'todo/newtodo.html')
    
def testsite(request):
	return render(request, 'todo/test.html')
    
def newtodo(request):
	if request.method == 'POST':
		text = request.POST['text']
		deadline = timezone.now() #Das hier noch ändern!
		percent = request.POST['percent']
		
		t = Task(text = text, deadline = deadline, percent = percent)
		t.save()
		
		return index(request)
		#return render(request, 'todo/newtodo.html')
	else:
		return render(request, 'todo/newtodo.html')
		
		
def delete(request, pk):
	t = Task.objects.get(pk = pk)
	context = {'t':t}
	t.delete()
	
	if(request.method == 'POST'):
		t.delete()
	
	#return render(request, 'todo/test.html')
	return index(request)
	
def edit(request, pk):
	t = Task.objects.get(pk = pk)
	context = {'t' : t}
	
	if request.method == 'POST':
		t.text = request.POST['text']
		t.deadline = timezone.now() #Das hier noch ändern!
		t.percent = request.POST['percent']
		
		todo.save()
		return index(request)
	
	return render(request, 'todo.edit.html', context)	
		
