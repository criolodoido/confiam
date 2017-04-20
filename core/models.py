# -*- coding: utf 8 -*-
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Sobre(models.Model):
	nome = models.CharField(max_length=200, null=False, blank=False)
	apresentacao = models.TextField(null=False, blank=False)
	foto = CloudinaryField('foto', null=True, blank=True)
	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(
            blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.nome

class Palestras(models.Model):
	nome_palestrante = models.CharField(max_length=200, null=False, blank=False)
	sua_palestra = models.TextField(null=False, blank=False)
	foto_palestrante = CloudinaryField('foto_palestra', null=True, blank=True)
	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(
            blank=True, null=True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.nome_palestrante

class Minicursos(models.Model):
	nome_minicurso = models.CharField(max_length=200, null=False, blank=False)
	apresentacao_minicurso = models.TextField(null=False, blank=False)
	foto_minicurso = CloudinaryField('foto_palestra', null=True, blank=True)
	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(
            blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.nome_minicurso

class Restaurantes(models.Model):
	nome_restaurante = models.CharField(max_length=200, null=False, blank=False)
	apresentacao_restaurante = models.TextField(null=False, blank=False)
	foto_restaurante = CloudinaryField('foto_restaurante', null=True, blank=True)
	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(
            blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.nome_restaurante

class Patrocinio(models.Model):
	nome_patrocinio = models.CharField(max_length=200, null=False, blank=False)
	apresentacao_patrocinio = models.TextField(null=False, blank=False)
	foto_patrocinio = CloudinaryField('foto_patrocinio', null=False, blank=False)
	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(
            blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.nome_patrocinio

class Hoteis(models.Model):
	nome_hotel = models.CharField(max_length=200, null=False, blank=False)
	apresentacao_hotel = models.TextField(null=False, blank=False)
	foto_hotel = CloudinaryField('foto', null=True, blank=True)
	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(
            blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.nome_hotel

class Evento(models.Model):
	nome_evento = models.CharField(max_length=200, null=False, blank=False)
	apresentacao_evento = models.TextField(null=False, blank=False)
	foto_evento = CloudinaryField('foto', null=True, blank=True)
	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(
            blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.nome_evento