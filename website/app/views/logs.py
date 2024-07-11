from django.shortcuts import render, HttpResponse, redirect
from django import forms
import app.models as models


def logs(request):
    antennas = models.antenna.objects.all()
    servers = models.server.objects.all()

    return render(request, "logs.html", {"antennas": antennas, "servers": servers})
