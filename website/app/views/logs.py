from django.shortcuts import render, HttpResponse, redirect
from django import forms
import app.models as models


def logs(request):


    return render(request, "logs.html", {})
