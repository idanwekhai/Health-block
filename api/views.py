from django.shortcuts import render

# Create your views here.
from .models import Patient
from django.views.generic import ListView
from rest_framework import viewsets

from . import serializers


class PatientListView(ListView):
	model = Patient
	template_name = 'patient_list.html'
	context_object_name = 'patient_list'


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = serializers.PatientSerializer