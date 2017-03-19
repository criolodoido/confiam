from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^palestrantes$', views.palestrantes, name='palestrantes'),
	url(r'^palestras$', views.palestras, name='palestras'),
	url(r'^minicursos$', views.minicursos, name='minicursos'),
	url(r'^restaurantes$', views.restaurantes, name='restaurantes'),
	url(r'^patrocinio$', views.patrocinio, name='patrocinio'),
	url(r'^hoteis$', views.hoteis, name='hoteis'),
]