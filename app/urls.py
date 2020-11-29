# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from django.conf.urls import url


urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The Coverage
    path('', views.index, name='home'),
    path('coverage/', views.CrudView.as_view(), name='coverage_view'),
    path('create/coverage/', views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('update/coverage/', views.UpdateCrudUser.as_view(), name='crud_ajax_update'),
    path('delete/coverage/', views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),

    # The Execution
    path('execution/', views.ExecutionView.as_view(), name='execution_view'),
    path('create/execution/', views.ExecutionCreate.as_view(), name='execution_create'),
    path('update/execution/', views.ExecutionUpdate.as_view(), name='execution_update'),
    path('delete/execution/', views.DeleteExecution.as_view(), name='execution_delete'),

    #The Coverage Report
    path('coverage/report/', views.CoverageReportView.as_view(), name='coverage_report_view'),
    path('coverage/report/plot/', views.CreateCoverageReport.as_view(), name='coverage_report_plot'),








]
