# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Coverage(models.Model):
    category = models.CharField(max_length=30, blank=True,null=True)
    alpha1 = models.CharField(max_length=100, blank=True,null=True ,verbose_name='Alpha1')
    alpha2 = models.CharField(max_length=100,blank=True, null=True,verbose_name='Alpha2')
    alpha3 = models.CharField(max_length=100,blank=True, null=True,verbose_name='Alpha3')
    app_name = models.CharField(max_length=100,blank=True,null=True,verbose_name='App name')
    date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'app_coverage'



class Execution(models.Model):
    category = models.CharField(max_length=30, blank=True)
    alpha1 = models.CharField(max_length=100, blank=True, verbose_name='Alpha1')
    alpha2 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Alpha2')
    alpha3 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Alpha3')
    app_name = models.CharField(max_length=100,blank=True,null=True,verbose_name='App name')

    date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'app_execution'

