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
    date = models.DateField(null=True,blank=True)

    class Meta:
        db_table = 'app_coverage'



class Execution(models.Model):
    category = models.CharField(max_length=30, blank=True)
    alpha1 = models.CharField(max_length=100, blank=True, verbose_name='Alpha1')
    alpha2 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Alpha2')
    alpha3 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Alpha3')
    app_name = models.CharField(max_length=100,blank=True,null=True,verbose_name='App name')

    date = models.DateField(null=True,blank=True)

    class Meta:
        db_table = 'app_execution'

class Failed(models.Model):
    c =  models.CharField(max_length=10,blank=True,null=True,verbose_name='C')
    link = models.URLField(max_length=500,blank=True,null=True,verbose_name='link')
    comment = models.CharField(max_length=100,blank=True,null=True,verbose_name='Comment')
    high_level_resone = models.CharField(max_length=200,blank=True,null=True,verbose_name='High Level Reasone')
    low_level_resone = models.CharField(max_length=200,blank=True,null=True,verbose_name='Low Level Reasone')
    issue_description = models.CharField(max_length=500,blank=True,null=True, verbose_name='Issue Desciption')
    frequency = models.CharField(max_length=100,blank=True,null=True,verbose_name='Frequency')
    analysis = models.CharField(max_length=1000,blank=True,null=True, verbose_name='Analysis')
    rca = models.CharField(max_length=200,blank=True,null=True,verbose_name='Rca')
    action =models.CharField(max_length=100, blank=True, null=True,verbose_name='Action')

    class Meta:
        db_table='app_failed'


class Disabled(models.Model):
    c =  models.CharField(max_length=10,blank=True,null=True,verbose_name='C')
    link = models.URLField(max_length=500,blank=True,null=True,verbose_name='link')
    comment = models.CharField(max_length=1000,blank=True,null=True,verbose_name='Comment')
    high_level_resone = models.CharField(max_length=200,blank=True,null=True,verbose_name='High Level Reasone')
    low_level_resone = models.CharField(max_length=200,blank=True,null=True,verbose_name='Low Level Reasone')
    issue_description = models.CharField(max_length=500,blank=True,null=True, verbose_name='Issue Desciption')
    frequency = models.CharField(max_length=100,blank=True,null=True,verbose_name='Frequency')
    analysis = models.CharField(max_length=1000,blank=True,null=True, verbose_name='Analysis')
    rca = models.CharField(max_length=200,blank=True,null=True,verbose_name='Rca')
    action =models.CharField(max_length=100, blank=True, null=True,verbose_name='Action')

    class Meta:
        db_table='app_disabled'
