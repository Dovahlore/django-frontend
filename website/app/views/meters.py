from django.shortcuts import render, HttpResponse, redirect
from django import forms

from app.utils.encrypt import md5
import app.models as models
from app.utils.checkcode import check_code
from django.urls import reverse

def  meter(request):


    return render(request, "meter.html" )