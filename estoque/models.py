from django.db import models


class Categoria(models.Model):

	nome		= models.CharField(max_length=40,null=False)

class Local(models.Model):

	nome		= models.CharField(max_length=40,null=False)

class Estoque(models.Model):

	nome		= models.CharField(max_length=40,null=False)
	custo		= models.DecimalField(max_digits=10,decimal_places=2,default='0.00')
	quantidade 	= models.IntegerField(default='0')
	reposicao 	= models.IntegerField(default='0')
	categoria	= models.ForeignKey('Categoria')
	local  		= models.ForeignKey('Local')