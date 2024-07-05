from django.shortcuts import render, HttpResponse, redirect
from django import forms
import app.models as models


def  meter(request):
    antennas=models.antenna.objects.all()
    print(antennas)

    return render(request, "meter.html",{"antennas":antennas} )