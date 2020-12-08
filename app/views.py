# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from datetime import date, timedelta
from django.views.generic import ListView
from .models import Coverage, Execution
from django.views.generic import View, TemplateView
from django.http import JsonResponse
from django.db.models import Count, Q
from .forms import *
from django.contrib import messages



@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('error-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('error-500.html')
        return HttpResponse(html_template.render(context, request))


class CrudView(ListView):
    model = Coverage
    template_name = 'layouts/coverage.html'
    context_object_name = 'users'


class CreateCrudUser(View):
    def get(self, request):
        date1 = request.GET.get('date', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)
        alpha1 = request.GET.get('alpha', None)
        appname1 = request.GET.get('app', None)

        obj = Coverage.objects.create(
            date=date1,
            category=name1,
            alpha1=address1,
            alpha2=age1,
            alpha3=alpha1,
            app_name=appname1

        )

        user = {'id': obj.id,'date':obj.date,'name': obj.category, 'address': obj.alpha1, 'age': obj.alpha2, 'alpha': obj.alpha3,'app_name': obj.app_name}

        data = {
            'user': user
        }
        #print(JsonResponse(data))
        return JsonResponse(data)


class UpdateCrudUser(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)
        alpha1 = request.GET.get('alpha', None)

        obj = Coverage.objects.get(id=id1)
        obj.category = name1
        obj.alpha1 = address1
        obj.alpha2 = age1
        obj.alpha3 = alpha1

        obj.save()

        user = {'id': obj.id, 'name': obj.category, 'address': obj.alpha1, 'age': obj.alpha2, 'alpha': obj.alpha3}

        data = {
            'user': user
        }
        return JsonResponse(data)


class DeleteCrudUser(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Coverage.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


################################################## Execution Input ######################################

class ExecutionView(ListView):
    model = Execution
    template_name = 'layouts/execution.html'
    context_object_name = 'users'


class ExecutionCreate(View):

    def get(self, request):
        date1 = request.GET.get('date', None)
        category1 = request.GET.get('category', None)
        alpha1 = request.GET.get('alpha1', None)
        alpha2 = request.GET.get('alpha2', None)
        alpha3 = request.GET.get('alpha3', None)
        app1 = request.GET.get('app', None)

        obj = Execution.objects.create(
            date=date1,
            category=category1,
            alpha1=alpha1,
            alpha2=alpha2,
            alpha3=alpha3,
            app_name=app1

        )

        user = {'id': obj.id,'date': obj.date,'category': obj.category, 'alpha1': obj.alpha1, 'alpha2': obj.alpha2,
                'alpha3': obj.alpha3, 'app_name' : obj.app_name}

        data = {
            'user': user
        }
        # print(JsonResponse(data))
        return JsonResponse(data)


class ExecutionUpdate(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        category1 = request.GET.get('category', None)
        alpha1 = request.GET.get('alpha1', None)
        alpha2 = request.GET.get('alpha2', None)
        alpha3 = request.GET.get('alpha3', None)

        obj = Execution.objects.get(id=id1)
        obj.category = category1
        obj.alpha1 = alpha1
        obj.alpha2 = alpha2
        obj.alpha3 = alpha3

        obj.save()

        user = {'id': obj.id, 'category': obj.category, 'alpha1': obj.alpha1, 'alpha2': obj.alpha2,
                'alpha3': obj.alpha3}

        data = {
            'user': user
        }
        return JsonResponse(data)


class DeleteExecution(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Execution.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


############################################## Coverage Report ######################################################33


class CoverageReportView(ListView):
    model = Coverage
    template_name = 'layouts/coverage_report.html'
    context_object_name = 'users'


class CreateCoverageReport(View):

    def get(self, request, **kwargs):
        # import pdb
        # pdb.set_trace()
        retrive_data=request.GET
        fromdate1 = retrive_data['fromdate']
        todate1 = retrive_data['todate']
        cat1 = retrive_data['category']
        app1 = retrive_data['app']
        
        temp = {'alpha1': [], 'alpha2': [], 'alpha3': [], 'date': []}

        temp1={'date':[]}
        if cat1 == "Coverage":
            lis=["Automatable","Automated","Not Automated"]
            for key in lis:
                if key not in temp1.keys():
                    temp1[key]=[]
                result = Coverage.objects.filter(date__range=[fromdate1, todate1],app_name=app1,category=key)
                for unit in result:
                    if (int(unit.alpha1) & int(unit.alpha2) & int(unit.alpha3) == None):
                        temp1[key]=0
                    #calculation
                    else: 
                        calculation=int(unit.alpha1)+int(unit.alpha2)+int(unit.alpha3)
                        temp1[key].append(calculation)




            
        elif cat1 == "Execution":
            lis=["Pass","Failed","Not Executed"]
            for key in lis:
                if key not in temp1.keys():
                    temp1[key]=[]
                result = Execution.objects.filter(date__range=[fromdate1, todate1],app_name=app1,category=key)
                for unit in result:
                    if (int(unit.alpha1) & int(unit.alpha2) & int(unit.alpha3) == None):
                        temp1[key]=0
                    #calculation
                    else: 
                        calculation=int(unit.alpha1)+int(unit.alpha2)+int(unit.alpha3)
                        temp1[key].append(calculation)


        

        delta = datetime.datetime.strptime(todate1, '%Y-%m-%d') - datetime.datetime.strptime(fromdate1, '%Y-%m-%d')
        for i in range(delta.days + 1):
            day = datetime.datetime.strptime(fromdate1, '%Y-%m-%d') + timedelta(days=i)
            temp1['date'].append(day.strftime("%x"))

        data = {
            'user': temp1
        }
        print(data)
        return JsonResponse(data)


############################################ Failed ###############################################################

class CreateFailedDataEntry(View):
    template_name = 'layouts/failed_form.html'


    def get(self, request, id=None):
        form = FailedDataEntryForm()
        context={
            'form': form
        }

        return render(request,self.template_name,context)

    def post(self, request,id=None):
        form = FailedDataEntryForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Data is Save SuccessFully.")
                return redirect('failed_input')
            else:
                messages.add_message(request, messages.SUCCESS, "Something went wrong.")
                return redirect('failed_input')



####################################### Disabled ############################################################3

class CreateDisabledDataEntry(View):
    template_name = 'layouts/disabled_input.html'


    def get(self, request, id=None):
        form = DisabledDataEntryForm()
        context={
            'form': form
        }

        return render(request,self.template_name,context)

    def post(self, request,id=None):
        form = DisabledDataEntryForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Data is Save SuccessFully.")
                return redirect('disabled_input')
            else:
                messages.add_message(request, messages.SUCCESS, "Something went wrong.")
                return redirect('disabled_input')

