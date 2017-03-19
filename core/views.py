from django.shortcuts import render
from django.utils import timezone
from .models import Palestrantes, Palestras, Minicursos, Restaurantes, Patrocinio, Hoteis, Evento

def index(request):
	posts = Evento.objects.all()
	return render(request, 'core/index.html', {'posts': posts})

def palestrantes(request):
	posts = Palestrantes.objects.all()
	return render(request, 'core/palestrantes.html', {'posts': posts})

def palestras(request):
	posts = Palestras.objects.all()
	return render(request, 'core/palestras.html', {'posts': posts})

def minicursos(request):
	posts = Minicursos.objects.all()
	return render(request, 'core/minicursos.html', {'posts': posts})

def restaurantes(request):
	posts = Restaurantes.objects.all()
	return render(request, 'core/restaurantes.html', {'posts': posts})

def patrocinio(request):
	posts = Patrocinio.objects.all()
	return render(request, 'core/patrocinio.html', {'posts': posts})

def hoteis(request):
	posts = Hoteis.objects.all()
	return render(request, 'core/hoteis.html', {'posts': posts})